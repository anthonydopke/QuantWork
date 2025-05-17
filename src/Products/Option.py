from abc import ABC, abstractmethod
from .Enums import OptionType
from Models.ModelType import ModelType
# === Abstract Option class ===

class Option(ABC):
    def __init__(self, K, T, sigma = None, option_type=OptionType.CALL):
        self.K = K
        self.T = T
        self.sigma = sigma
        self.option_type = option_type

# === Vanilla Option class ===

class VanillaOption(Option):
    def __init__(self, K, T, sigma = None, option_type=OptionType.CALL):
        super().__init__(K, T, sigma, option_type)

class Straddle(Option):
    def __init__(self, K, T, sigma=None, option_type=OptionType.STRADDLE):
        super().__init__(K, T, sigma, option_type)
    

    
