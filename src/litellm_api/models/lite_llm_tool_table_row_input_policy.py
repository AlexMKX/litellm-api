from enum import Enum

class LiteLLMToolTableRowInputPolicy(str, Enum):
    BLOCKED = "blocked"
    TRUSTED = "trusted"
    UNTRUSTED = "untrusted"

    def __str__(self) -> str:
        return str(self.value)
