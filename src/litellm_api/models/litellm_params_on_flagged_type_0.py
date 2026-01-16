from enum import Enum

class LitellmParamsOnFlaggedType0(str, Enum):
    BLOCK = "block"
    MONITOR = "monitor"

    def __str__(self) -> str:
        return str(self.value)
