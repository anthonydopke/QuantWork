from MarketDataLoader.MarketFromExcel import Market
from utils.paths import data_path
import datetime

def test_MarketBuilder():
    xl_file = data_path('spx_1_nov_24.xlsx')
    pricingdate = datetime.datetime(2024, 11,1)
    mkt = Market(xl_file, pricingdate)
    assert mkt.spot > 0, "Spot price should be positive"
    assert len(mkt.maturities) == len(mkt.maturities_as_dates), "Mismatch in maturity arrays"
    assert all(t >= 0 for t in mkt.maturities), "All maturities should be non-negative"
    T_test = 0.5  # 6 months
    fwd = mkt.get_forward(T_test)
    assert isinstance(fwd, float) and fwd > 0, "Forward price interpolation failed"

# def test_VolatilityMatrixShape():
#     xl_file = data_path('spx_1_nov_24.xlsx')
#     pricingdate = datetime.datetime(2024, 11, 1)
#     mkt = Market(xl_file, pricingdate)

#     vol_matrix = mkt.vol_surface 
#     n_strikes = len(mkt.strikes)
#     n_maturities = len(mkt.maturities)

#     assert len(vol_matrix) == n_maturities, f"Expected {n_maturities} rows (maturities), got {len(vol_matrix)}"
#     for row in vol_matrix:
#         assert len(row) == n_strikes, f"Each row should have {n_strikes} columns (strikes)"

# def test_VolatilityInterpolation():
#     xl_file = data_path('spx_1_nov_24.xlsx')
#     pricingdate = datetime.datetime(2024, 11, 1)
#     mkt = Market(xl_file, pricingdate)

#     # 1. Volatility exactly on the grid
#     known_T = mkt.maturities[1]  # not the first one (which may be spot)
#     known_K = mkt.strikes[2]
#     vol_exact = mkt.vol_surface[1,2]
#     vol_exact_interp = mkt.get_volatility(known_K, known_T)
#     assert isinstance(vol_exact_interp, float)
#     assert vol_exact == vol_exact_interp

#     # 2. Interpolated volatility (in between strikes and maturities)
#     mid_T = (mkt.maturities[1] + mkt.maturities[2]) / 2
#     mid_K = (mkt.strikes[1] + mkt.strikes[2]) / 2
#     vol_interp = mkt.get_volatility(mid_K, mid_T)
#     assert isinstance(vol_interp, float)
#     assert vol_interp > 0, "Interpolated volatility should be positive"
#     assert abs(vol_interp - vol_exact) / vol_exact < 0.5, "Interpolation too far off"

#     # 3. Extrapolation for short maturity (T < min T)
#     short_T = -0.01  # 1 day before pricing, should be treated as spot
#     vol_short = mkt.get_volatility(mid_K, short_T)
#     assert vol_short > 0, "Short maturity extrapolation failed"

#     # 4. Extrapolation for long maturity (T > max T)
#     long_T = mkt.maturities[-1] + 1.0  # 1Y beyond
#     vol_long = mkt.get_volatility(mid_K, long_T)
#     assert vol_long > 0, "Long maturity extrapolation failed"

#     # 5. Extrapolation for small strike
#     small_K = mkt.strikes[0] * 0.9
#     vol_lowK = mkt.get_volatility(small_K, mid_T)
#     assert vol_lowK > 0, "Low strike extrapolation failed"

#     # 6. Extrapolation for large strike
#     large_K = mkt.strikes[-1] * 1.1
#     vol_highK = mkt.get_volatility(large_K, mid_T)
#     assert vol_highK > 0, "High strike extrapolation failed"







