import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from datetime import datetime
import os


class Market:
    def __init__(self, excel_path: str, pricing_date: datetime):
        """
        Initialize market data from an Excel file.

        Excel format:
        - First column: Expiry dates (as string or datetime)
        - Second column: Forward prices
        - From third column onward:
            * First row: Absolute strikes
            * Headers: Moneyness (e.g. '100.0%')
            * Values: Implied volatilities
        """
        self._pricing_date = pricing_date
        self._xl_path = excel_path

        self._spot = None
        self._forward_curve = None
        self._forward_curve_interpolated = None
        self._vol_KT = None
        self._strikes = None
        self._maturities = None
        self._maturitiesAsDates = None

        self._load_market_data()

    def _load_market_data(self):
        df = pd.read_excel(self._xl_path, index_col=0)

        # Set pricing date as the first maturity row
        df.index = pd.to_datetime(df.index)
        df.index = df.index.where(df.index != df.index[0], self._pricing_date)

        self._maturitiesAsDates = df.index
        self._maturities = [(d - self._pricing_date).days / 365.25 for d in df.index]
        self._maturities[0] = 0

        forwards = df.iloc[:, 0].astype(float).values

        # Fill missing forward at pricing date with ATM forward (from 100% moneyness column)
        if pd.isna(forwards[0]):
            forwards[0] = df['100.0%'].iloc[0]

        self._forward_curve = forwards
        self._forward_curve_interpolated = interp1d(
            self._maturities, forwards, kind="linear", fill_value="extrapolate"
        )

        # Extract vol surface
        vol_data = df.iloc[:, 1:].copy()
        moneyness = np.array([float(col.strip('%')) / 100 for col in vol_data.columns])
        strikes_row = moneyness * forwards[0]
        vol_matrix = vol_data.iloc[1:].astype(float).values

        self._strikes = strikes_row
        self._vol_KT = vol_matrix / 100

        # Compute spot from strike and moneyness
        self._spot = forwards[0]  # Assuming consistent moneyness-strike structure

    # Properties
    @property
    def spot(self):
        return self._spot

    @property
    def pricing_date(self):
        return self._pricing_date

    @property
    def maturities(self):
        return self._maturities

    @property
    def maturities_as_dates(self):
        return self._maturitiesAsDates

    @property
    def forward_curve(self):
        return self._forward_curve

    @property
    def strikes(self):
        return self._strikes

    @property
    def vol_surface(self):
        return self._vol_KT

    def get_forward(self, T: float) -> float:
        """
        Get interpolated forward price for a given maturity (in years).
        """
        return float(self._forward_curve_interpolated(T))
