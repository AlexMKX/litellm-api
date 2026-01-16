from enum import Enum

class APIKeySecuritySchemeIn(str, Enum):
    COOKIE = "cookie"
    HEADER = "header"
    QUERY = "query"

    def __str__(self) -> str:
        return str(self.value)
