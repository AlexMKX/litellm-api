from enum import Enum

class PiiAction(str, Enum):
    BLOCK = "BLOCK"
    MASK = "MASK"

    def __str__(self) -> str:
        return str(self.value)
