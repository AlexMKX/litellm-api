from enum import Enum

class LoggingCallbackStatusStatus(str, Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"

    def __str__(self) -> str:
        return str(self.value)
