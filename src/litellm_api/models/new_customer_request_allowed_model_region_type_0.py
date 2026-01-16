from enum import Enum

class NewCustomerRequestAllowedModelRegionType0(str, Enum):
    EU = "eu"
    US = "us"

    def __str__(self) -> str:
        return str(self.value)
