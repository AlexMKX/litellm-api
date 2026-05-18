from enum import Enum

class LitellmParamsGroundingStrictnessType0(str, Enum):
    BALANCED = "BALANCED"
    STRICT = "STRICT"

    def __str__(self) -> str:
        return str(self.value)
