from enum import Enum

class ToolPolicyUpdateRequestOutputPolicyType0(str, Enum):
    TRUSTED = "trusted"
    UNTRUSTED = "untrusted"

    def __str__(self) -> str:
        return str(self.value)
