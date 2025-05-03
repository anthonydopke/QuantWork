from abc import ABC, abstractmethod
from OptionType import OptionType

# === Abstract Option class ===

class Option(ABC):
    def __init__(self, K, T, sigma, option_type=OptionType.CALL):
        self.K = K
        self.T = T
        self.sigma = sigma
        self.option_type = option_type

    @abstractmethod
    def price(self, model):
        pass

    @abstractmethod
    def greeks(self, model):
        pass

# === Vanilla Option class ===

class VanillaOption(Option):
    def __init__(self, K, T, sigma, option_type=OptionType.CALL):
        super().__init__(K, T, sigma, option_type)

