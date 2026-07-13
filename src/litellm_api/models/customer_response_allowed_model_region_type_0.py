from enum import Enum

class CustomerResponseAllowedModelRegionType0(str, Enum):
    EU = "eu"
    US = "us"

    def __str__(self) -> str:
        return str(self.value)
