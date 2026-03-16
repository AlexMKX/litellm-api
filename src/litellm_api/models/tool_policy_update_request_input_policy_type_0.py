from enum import Enum

class ToolPolicyUpdateRequestInputPolicyType0(str, Enum):
    BLOCKED = "blocked"
    TRUSTED = "trusted"
    UNTRUSTED = "untrusted"

    def __str__(self) -> str:
        return str(self.value)
