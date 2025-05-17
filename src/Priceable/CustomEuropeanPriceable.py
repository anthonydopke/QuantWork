from Products.EuropeanCustom import EuropeanCustomOption
from Models.BlackModel import BlackModel
from Priceable.Priceable import Priceable  


class CustomEuropeanPriceable(Priceable):
    def __init__(self, pricing_model: BlackModel, european_custom_option: EuropeanCustomOption):
        super().__init__(pricing_model, european_custom_option)

    def price(self) -> float:
        total_price = 0.0
        for vanilla_option, weight in self.option.list_calls:
            total_price += self.model.PriceVanillaOption(vanilla_option) * weight
        for vanilla_option, weight in self.option.list_puts:
            total_price += self.model.PriceVanillaOption(vanilla_option) * weight
        return total_price

