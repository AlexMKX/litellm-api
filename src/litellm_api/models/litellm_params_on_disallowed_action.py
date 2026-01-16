from enum import Enum

class LitellmParamsOnDisallowedAction(str, Enum):
    BLOCK = "block"
    REWRITE = "rewrite"

    def __str__(self) -> str:
        return str(self.value)
