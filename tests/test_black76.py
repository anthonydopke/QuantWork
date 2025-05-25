from Models.Numericals.Black76 import Black76
from Products.Enums import OptionType

def test_CallPrice():
    model = Black76(F=100, T=1, discount_rate=0.05)
    price = model.call_price(K=100, sigma=0.2)
    assert isinstance(price, float)
    assert price > 0

def test_PutPrice():
    model = Black76(F=100, T=1, discount_rate=0.05)
    price = model.put_price(K=100, sigma=0.2)
    assert isinstance(price, float)
    assert price > 0

def test_DeltaCall():
    model = Black76(F=100, T=1, discount_rate=0.05)
    delta = model.delta(K=100, sigma=0.2, option=OptionType.CALL)
    assert 0 < delta < 1

def test_DeltaPut():
    model = Black76(F=100, T=1, discount_rate=0.05)
    delta = model.delta(K=100, sigma=0.2, option=OptionType.PUT)
    assert -1 < delta < 0
