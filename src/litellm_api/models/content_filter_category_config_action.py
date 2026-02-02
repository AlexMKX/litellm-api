from enum import Enum

class ContentFilterCategoryConfigAction(str, Enum):
    BLOCK = "BLOCK"
    MASK = "MASK"

    def __str__(self) -> str:
        return str(self.value)
