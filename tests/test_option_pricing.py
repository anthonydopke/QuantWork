from MarketDataLoader.MarketFromExcel import Market
from utils.paths import data_path
import datetime
from Priceable.Priceable import PriceableCustomEuropean
from Models.BlackModel import BlackModel
from Products.Option import VanillaOption
from Products.EuropeanCustom import EuropeanCustomOption
from Products.Enums import OptionType

def test_VanillaOptionPricing():
    xl_file = data_path('spx_1_nov_24.xlsx')
    pricingdate = datetime.datetime(2024, 11,1)
    mkt = Market(xl_file, pricingdate)
    black_model = BlackModel(mkt)
    call = VanillaOption(K = mkt.spot, T = 1)
    price = black_model.PriceVanillaOption(call)
    assert price > 0


def test_price_european_custom_option(self):
    xl_file = data_path('spx_1_nov_24.xlsx')
    pricingdate = datetime.datetime(2024, 11,1)
    market = Market(xl_file, pricingdate)
    black_model = BlackModel(market)

    # Build a small portfolio from valid (K, T) grid points
    call1 = (self.market.strikes[2], self.market.maturities[1])
    call2 = (self.market.strikes[3], self.market.maturities[1])
    put1 = (self.market.strikes[1], self.market.maturities[1])

    booked = {
        OptionType.CALL: {
            call1: 2.0,  # quantity
            call2: 1.0
        },
        OptionType.PUT: {
            put1: 1.5
        }
    }

    custom_option = EuropeanCustomOption(booked)
    priceable = PriceableCustomEuropean(self.model, custom_option)
    total_price = priceable.price()

    self.assertIsInstance(total_price, float)
    self.assertGreater(total_price, 0, "Custom option portfolio should have positive value")



    

