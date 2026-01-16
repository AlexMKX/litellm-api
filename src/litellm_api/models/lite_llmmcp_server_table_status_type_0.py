from enum import Enum

class LiteLLMMCPServerTableStatusType0(str, Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
