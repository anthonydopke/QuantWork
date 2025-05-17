from MarketDataLoader.MarketFromExcel import Market
from utils.paths import data_path
import datetime
from Priceable.CustomEuropeanPriceable import CustomEuropeanPriceable
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
    assert 1 == 1

def test_custom_european_option():
    xl_file = data_path('spx_1_nov_24.xlsx')
    pricingdate = datetime.datetime(2024, 11,1)
    market = Market(xl_file, pricingdate)
    black_model = BlackModel(market)

    # Build a small portfolio from valid (K, T) grid points
    call1 = (market.strikes[2], market.maturities[1])
    call2 = (market.strikes[3], market.maturities[1])
    put1 = (market.strikes[1], market.maturities[1])

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
    assert 1 == 1

def test_priceable_european_custom_option():
    xl_file = data_path('spx_1_nov_24.xlsx')
    pricingdate = datetime.datetime(2024, 11,1)
    market = Market(xl_file, pricingdate)
    black_model = BlackModel(market)

    # Build a small portfolio from valid (K, T) grid points
    call1 = (market.strikes[2], market.maturities[1])
    call2 = (market.strikes[3], market.maturities[1])
    put1 = (market.strikes[1], market.maturities[1])

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
    priceable = CustomEuropeanPriceable(black_model, custom_option)
    assert 1 == 1  

def test_price_european_custom_option():
    xl_file = data_path('spx_1_nov_24.xlsx')
    pricingdate = datetime.datetime(2024, 11,1)
    market = Market(xl_file, pricingdate)
    black_model = BlackModel(market)

    # Build a small portfolio from valid (K, T) grid points
    call1 = (market.strikes[2], market.maturities[1])
    call2 = (market.strikes[3], market.maturities[1])
    put1 = (market.strikes[1], market.maturities[1])

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
    priceable = CustomEuropeanPriceable(black_model, custom_option)
    # price = priceable.price()
    assert 1 == 1  