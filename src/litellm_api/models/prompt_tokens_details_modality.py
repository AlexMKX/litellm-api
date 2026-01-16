from enum import Enum

class PromptTokensDetailsModality(str, Enum):
    AUDIO = "AUDIO"
    IMAGE = "IMAGE"
    TEXT = "TEXT"
    VIDEO = "VIDEO"

    def __str__(self) -> str:
        return str(self.value)
