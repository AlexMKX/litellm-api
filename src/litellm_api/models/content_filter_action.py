from enum import Enum

class ContentFilterAction(str, Enum):
    BLOCK = "BLOCK"
    MASK = "MASK"

    def __str__(self) -> str:
        return str(self.value)
