from Products.Enums import OptionType
from Products.EuropeanCustom import EuropeanCustomOption

class Straddle(EuropeanCustomOption):
    def __init__(self, K, T, quantity=1):
        booked = {
            OptionType.CALL: {
                (K, T): quantity
            },
            OptionType.PUT: {
                (K, T): quantity
            }
        }

        super().__init__(booked)

        
    