from enum import Enum

class LitellmParamsPresidioFilterScopeType0(str, Enum):
    BOTH = "both"
    INPUT = "input"
    OUTPUT = "output"

    def __str__(self) -> str:
        return str(self.value)
