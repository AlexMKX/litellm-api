from enum import Enum

class LitellmParamsAction(str, Enum):
    BLOCK = "block"
    MASK = "mask"

    def __str__(self) -> str:
        return str(self.value)
