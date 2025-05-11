from abc import ABC, abstractmethod
from .Enums import OptionType, ModelType

# === Abstract Option class ===

class Option(ABC):
    def __init__(self, K, T, sigma = None, option_type=OptionType.CALL):
        self.K = K
        self.T = T
        self.sigma = sigma
        self.option_type = option_type

    @abstractmethod
    def price(self, model = ModelType.MODELFREE):
        pass

    @abstractmethod
    def greeks(self, model = ModelType.BLACK):
        pass

# === Vanilla Option class ===

class VanillaOption(Option):
    def __init__(self, K, T, sigma = None, option_type=OptionType.CALL):
        super().__init__(K, T, sigma, option_type)

class Straddle(Option):
    def __init__(self, K, T, sigma=None, option_type=OptionType.CALL):
        super().__init__(K, T, sigma, option_type)
    
    def price(self, model = ModelType.MODELFREE):
        call = VanillaOption(self.K, self.T, self.sigma, OptionType.CALL)
        put = VanillaOption(self.K, self.T, self.sigma, OptionType.PUT)
        return call.price(model=model) + put.price(model=model)

    
