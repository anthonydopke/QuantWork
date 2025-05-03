import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d


class OptionDataFetcher:
    def __init__(self, ticker):
        self.ticker = ticker
        self.option_maturities = {}
        self.spot_price = None
        self.forward_curve = None
    
    def build_market(self):
        """
        Fetch option data from Yahoo Finance and build the forward curve in one step.
        """
        self.fetch_options()
        self.build_forward_curve()

    def fetch_options(self):
        stock = yf.Ticker(self.ticker)
        self.spot_price = stock.history(period='1d')['Close'].iloc[-1]  # Latest close price
        expirations = stock.options

        for expiry in expirations:
            opt_chain = stock.option_chain(expiry)
            maturity = OptionMaturity(expiry, opt_chain.calls, opt_chain.puts, self.spot_price)
            self.option_maturities[expiry] = maturity

    def build_forward_curve(self):
        """
        Build and interpolate the forward curve. 
        Also sets self.forward_interpolator.

        Returns:
            set: A set of (expiry, forward) tuples
        """
        forward_set = set()
        expiries = []
        forwards = []

        for expiry, maturity in self.option_maturities.items():
            try:
                forward = maturity.estimate_forward()
                expiry_date = pd.to_datetime(expiry)
                forward_set.add((expiry_date, forward))
                expiries.append(expiry_date)
                forwards.append(forward)
            except Exception as e:
                print(f"Could not estimate forward for {expiry}: {e}")

        if expiries and forwards:
            # Sort by expiry
            expiries, forwards = zip(*sorted(zip(expiries, forwards)))

            # Convert dates to numerical values (days to expiry)
            expiry_days = [(exp - pd.Timestamp.today()).days for exp in expiries]

            # Build interpolator
            self.forward_interpolator = interp1d(expiry_days, forwards, kind='linear', fill_value="extrapolate")

    def get_forward(self, expiry):
        """
        Get interpolated forward price for a given expiry.

        Args:
            expiry (datetime.datetime, str, int, or float): 
                - if datetime or str: expiry date
                - if int/float: maturity in years

        Returns:
            float: interpolated forward price
        """
        if self.forward_interpolator is None:
            raise ValueError("Forward curve has not been built. Please call build_forward_curve() first.")

        # Handle depending on input type
        if isinstance(expiry, (pd.Timestamp, str)):
            expiry_date = pd.to_datetime(expiry)
            expiry_day = (expiry_date - pd.Timestamp.today()).days
        elif isinstance(expiry, (int, float)):
            expiry_day = int(expiry * 365.25)
  # Assuming 365.25 days in a year
        else:
            raise TypeError(f"Unsupported expiry type: {type(expiry)}. Must be datetime, str, int or float.")
        
        return float(self.forward_interpolator(expiry_day))



    def get_maturities(self):
        return list(self.option_maturities.keys())

    def get_maturity_data(self, expiry):
        return self.option_maturities.get(expiry, None)
    
## Plotting 

    def plot_forward_curve(self):
        """
        Plots the forward curve based on the interpolated data.

        Returns:
            None
        """
        if self.forward_interpolator is None:
            raise ValueError("Forward curve has not been built. Please call build_forward_curve() first.")
        
        # Get the current list of expiries and forward values
        expiries = list(self.option_maturities.keys())
        expiry_dates = [pd.to_datetime(exp) for exp in expiries]
        expiry_days = [(exp - pd.Timestamp.today()).days for exp in expiry_dates]

        # Get the interpolated forward values for plotting
        forward_values = self.forward_interpolator(expiry_days)

        # Plotting the forward curve
        plt.figure(figsize=(10, 6))
        plt.plot(expiry_days, forward_values, label="Forward Curve", color='b', marker='o')

        # Plot the actual data points
        actual_forwards = [maturity.estimate_forward() for maturity in self.option_maturities.values()]
        plt.scatter(expiry_days, actual_forwards, color='r', label="Actual Forwards", zorder=5)

        plt.xlabel('Days to Expiry')
        plt.ylabel('Forward Price')
        plt.title(f"Forward Curve for {self.ticker}")
        plt.legend()
        plt.grid(True)
        plt.show()



class OptionMaturity:
    def __init__(self, expiry, calls, puts, spot_price):
        self.expiry = expiry
        self.calls = calls
        self.puts = puts
        self.spot_price = spot_price
        """
        Option data for a single maturity : smiles, prices of call/puts, forward.
        In development : Bid/Ask Spread
        """

    def get_strikes(self):
        return self.calls['strike'].tolist(), self.puts['strike'].tolist()
    
    def estimate_forward(self):
        """
        Estimate the forward price using Put-Call Parity around ATM strikes.

        Returns:
            float: estimated forward price
        """
        # Merge calls and puts on strike
        merged = pd.merge(self.calls[['strike', 'lastPrice']], 
                        self.puts[['strike', 'lastPrice']], 
                        on='strike', 
                        suffixes=('_call', '_put'))
        
        # Find strike closest to spot
        merged['abs_diff'] = (merged['strike'] - self.spot_price).abs()
        atm_row = merged.loc[merged['abs_diff'].idxmin()]

        K = atm_row['strike']
        C = atm_row['lastPrice_call']
        P = atm_row['lastPrice_put']

        # Put-call parity approximation
        forward = K + (C - P)

        return forward


## Plotting 
    def plot_smile(self, option_type='call', x_axis='strike'):
        """
        Plot the implied volatility smile.

        Args:
            option_type (str): 'call', 'put', or 'OTM' (for smoother curve)
            x_axis (str): 'strike' or 'moneyness'
        """
        if option_type == 'call':
            data = self.calls
        elif option_type == 'put':
            data = self.puts
        elif option_type == 'OTM':
            otm_calls = self.calls[self.calls['strike'] > self.spot_price]
            otm_puts = self.puts[self.puts['strike'] < self.spot_price]
            data = pd.concat([otm_puts, otm_calls])
        else:
            raise ValueError("option_type must be 'call', 'put', or 'OTM'")

        strikes = data['strike']
        iv = data['impliedVolatility']

        if x_axis == 'strike':
            x_values = strikes
            x_label = 'Strike Price'
        elif x_axis == 'moneyness':
            x_values = strikes / self.spot_price
            x_label = 'Moneyness (K/S₀)'
        else:
            raise ValueError("x_axis must be 'strike' or 'moneyness'")

        plt.figure(figsize=(10, 6))
        plt.plot(x_values, iv, marker='o', linestyle='-', label=f'{option_type} IV')

        # Spot/ATM marker
        if x_axis == 'moneyness':
            plt.axvline(1.0, color='red', linestyle='--', label='ATM (K/S₀=1)')
        else:
            plt.axvline(self.spot_price, color='red', linestyle='--', label='Spot Price')

        plt.title(f'{option_type} Volatility Smile - Expiry {self.expiry}')
        plt.xlabel(x_label)
        plt.ylabel('Implied Volatility')
        plt.legend()
        plt.grid(True)
        plt.show()
