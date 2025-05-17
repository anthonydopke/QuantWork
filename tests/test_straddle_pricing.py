from MarketDataLoader.MarketFromExcel import Market
from utils.paths import data_path
import datetime
from Priceable.CustomEuropeanPriceable import CustomEuropeanPriceable
from Models.BlackModel import BlackModel
from Products.Straddle import Straddle
from Products.Option import VanillaOption
from Products.Enums import OptionType

def test_price_straddle():
    xl_file = data_path('spx_1_nov_24.xlsx')
    pricingdate = datetime.datetime(2024, 11,1)
    market = Market(xl_file, pricingdate)
    black_model = BlackModel(market)
    straddle_option = Straddle(market.spot, T = 1)
    priceable = CustomEuropeanPriceable(black_model, straddle_option)
    price = priceable.price()
    assert price>0

def test_consistency_straddle():
    xl_file = data_path('spx_1_nov_24.xlsx')
    pricingdate = datetime.datetime(2024, 11,1)
    market = Market(xl_file, pricingdate)
    black_model = BlackModel(market)
    straddle_option = Straddle(market.spot, T = 1)
    priceable = CustomEuropeanPriceable(black_model, straddle_option)
    straddle_price = priceable.price()
    call_option, put_option = VanillaOption(K = market.spot, T = 1,option_type= OptionType.CALL), VanillaOption(K = market.spot, T = 1, option_type=OptionType.PUT)
    call_price = black_model.PriceVanillaOption(call_option)
    put_price = black_model.PriceVanillaOption(put_option)
    assert straddle_price == (call_price+put_price)
