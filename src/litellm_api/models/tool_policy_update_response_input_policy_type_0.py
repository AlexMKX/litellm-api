from enum import Enum

class ToolPolicyUpdateResponseInputPolicyType0(str, Enum):
    BLOCKED = "blocked"
    TRUSTED = "trusted"
    UNTRUSTED = "untrusted"

    def __str__(self) -> str:
        return str(self.value)
