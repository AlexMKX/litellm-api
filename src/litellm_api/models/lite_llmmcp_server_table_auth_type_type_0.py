from enum import Enum

class LiteLLMMCPServerTableAuthTypeType0(str, Enum):
    API_KEY = "api_key"
    AUTHORIZATION = "authorization"
    BASIC = "basic"
    BEARER_TOKEN = "bearer_token"
    NONE = "none"
    OAUTH2 = "oauth2"

    def __str__(self) -> str:
        return str(self.value)
