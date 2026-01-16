from enum import Enum

class ContentFilterPatternPatternType(str, Enum):
    PREBUILT = "prebuilt"
    REGEX = "regex"

    def __str__(self) -> str:
        return str(self.value)
