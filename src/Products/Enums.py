from enum import Enum, auto

# === Enum pour les types d'options ===

class OptionType(Enum):
    CALL = auto()
    PUT = auto()
    DIGITAL_CALL = auto()
    DIGITAL_PUT = auto()
    STRADDLE = auto()
    

    