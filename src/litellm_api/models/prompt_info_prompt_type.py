from enum import Enum

class PromptInfoPromptType(str, Enum):
    CONFIG = "config"
    DB = "db"

    def __str__(self) -> str:
        return str(self.value)
