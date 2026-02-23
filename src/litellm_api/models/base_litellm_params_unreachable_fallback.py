from enum import Enum

class BaseLitellmParamsUnreachableFallback(str, Enum):
    FAIL_CLOSED = "fail_closed"
    FAIL_OPEN = "fail_open"

    def __str__(self) -> str:
        return str(self.value)
