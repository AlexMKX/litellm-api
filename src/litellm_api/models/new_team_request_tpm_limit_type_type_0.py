from enum import Enum

class NewTeamRequestTpmLimitTypeType0(str, Enum):
    BEST_EFFORT_THROUGHPUT = "best_effort_throughput"
    GUARANTEED_THROUGHPUT = "guaranteed_throughput"

    def __str__(self) -> str:
        return str(self.value)
