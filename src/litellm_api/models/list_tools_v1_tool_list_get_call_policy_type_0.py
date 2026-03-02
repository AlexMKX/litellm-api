from enum import Enum

class ListToolsV1ToolListGetCallPolicyType0(str, Enum):
    BLOCKED = "blocked"
    DUAL_LLM = "dual_llm"
    TRUSTED = "trusted"
    UNTRUSTED = "untrusted"

    def __str__(self) -> str:
        return str(self.value)
