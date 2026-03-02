from enum import Enum

class LitellmParamsOnViolationType0(str, Enum):
    END_SESSION = "end_session"
    WARN = "warn"

    def __str__(self) -> str:
        return str(self.value)
