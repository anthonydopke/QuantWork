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







