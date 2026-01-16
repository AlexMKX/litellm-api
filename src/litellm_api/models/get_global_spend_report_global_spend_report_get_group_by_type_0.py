from enum import Enum

class GetGlobalSpendReportGlobalSpendReportGetGroupByType0(str, Enum):
    API_KEY = "api_key"
    CUSTOMER = "customer"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
