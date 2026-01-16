from enum import Enum

class ModelInfoTierType0(str, Enum):
    FREE = "free"
    PAID = "paid"

    def __str__(self) -> str:
        return str(self.value)
