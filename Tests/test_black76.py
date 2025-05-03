import math
from src.Models.Numericals.Black76 import Black76
from src.Models.Numericals.OptionType import OptionType

def test_call_price():
    model = Black76(F=100, T=1, discount_rate=0.05)
    price = model.call_price(K=100, sigma=0.2)
    assert isinstance(price, float)
    assert price > 0

def test_put_price():
    model = Black76(F=100, T=1, discount_rate=0.05)
    price = model.put_price(K=100, sigma=0.2)
    assert isinstance(price, float)
    assert price > 0

def test_delta_call():
    model = Black76(F=100, T=1, discount_rate=0.05)
    delta = model.delta(K=100, sigma=0.2, option=OptionType.CALL)
    assert 0 < delta < 1

def test_delta_put():
    model = Black76(F=100, T=1, discount_rate=0.05)
    delta = model.delta(K=100, sigma=0.2, option=OptionType.PUT)
    assert -1 < delta < 0
