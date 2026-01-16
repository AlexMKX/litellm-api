from enum import Enum

class KeyHealthResponseKey(str, Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"

    def __str__(self) -> str:
        return str(self.value)
