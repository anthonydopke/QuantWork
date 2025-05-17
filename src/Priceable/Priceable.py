from Models.PricingModel import PricingModel
from Products.Option import Option
from abc import ABC,abstractmethod

class Priceable(ABC):
    """
    A priceable is a virtual object reprenting how pricing is handled,
    PRICEABLE = MODEL + PRODUCT
    """
    def __init__(self, model: PricingModel, option: Option):
        self._model = model
        self._option = option
    
    @abstractmethod
    def price(self)-> float:
        """ Handles the pricing"""
        pass

    @property
    def model(self) -> PricingModel:
        """Returns the pricing model."""
        return self._model

    @property
    def option(self) -> Option:
        """Returns the financial option."""
        return self._option
    
