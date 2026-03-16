from enum import Enum

class ToolPolicyUpdateResponseOutputPolicyType0(str, Enum):
    TRUSTED = "trusted"
    UNTRUSTED = "untrusted"

    def __str__(self) -> str:
        return str(self.value)
