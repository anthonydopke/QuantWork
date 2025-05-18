from MarketDataLoader.MarketFromExcel import Market
from utils.paths import data_path
import datetime
from Priceable.CustomEuropeanPriceable import CustomEuropeanPriceable
from Models.BlackModel import BlackModel
from Products.CommonOption import Straddle, Butterfly, Digital
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

def test_price_butterfly():
    xl_file = data_path('spx_1_nov_24.xlsx')
    pricingdate = datetime.datetime(2024, 11,1)
    market = Market(xl_file, pricingdate)
    black_model = BlackModel(market)
    butterfly_option = Butterfly(market.spot, T = 1)
    priceable = CustomEuropeanPriceable(black_model, butterfly_option)
    price = priceable.price()
    assert price>0

def test_price_digital():
    xl_file = data_path('spx_1_nov_24.xlsx')
    pricingdate = datetime.datetime(2024, 11,1)
    market = Market(xl_file, pricingdate)
    black_model = BlackModel(market)
    digital_call = Digital(market.spot, T = 1)
    digital_put = Digital(market.spot, T = 1, optiontype = OptionType.PUT)
    priceable_call = CustomEuropeanPriceable(black_model, digital_call)
    priceable_put = CustomEuropeanPriceable(black_model, digital_put)
    price_call = priceable_call.price()
    price_put = priceable_put.price()
    assert price_call>0
    assert price_put>0
    assert (price_call + price_put -1) < 1e-10