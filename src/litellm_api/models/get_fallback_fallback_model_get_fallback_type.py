from enum import Enum

class GetFallbackFallbackModelGetFallbackType(str, Enum):
    CONTENT_POLICY = "content_policy"
    CONTEXT_WINDOW = "context_window"
    GENERAL = "general"

    def __str__(self) -> str:
        return str(self.value)
