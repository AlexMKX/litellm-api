from enum import Enum

class LiteLLMKeyType(str, Enum):
    DEFAULT = "default"
    LLM_API = "llm_api"
    MANAGEMENT = "management"
    READ_ONLY = "read_only"

    def __str__(self) -> str:
        return str(self.value)
