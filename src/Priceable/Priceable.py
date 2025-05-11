from Products.EuropeanCustom import EuropeanCustomOption
from Models.PricingModel import PricingModel
from Models.BlackModel import BlackModel

class PriceableCustomEuropean:
    def __init__(self, pricing_model: BlackModel, european_custom_option: EuropeanCustomOption):
        self.model = pricing_model
        self.custom_option = european_custom_option

    def price(self) -> float:
        total_price = 0.0
        for vanilla_option, weight in self.custom_option.list_calls:
            total_price += self.model.PriceVanillaOption(vanilla_option) * weight
        for vanilla_option, weight in self.custom_option.list_puts:
            total_price += self.model.PriceVanillaOption(vanilla_option) * weight
        return total_price

