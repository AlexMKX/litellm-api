from enum import Enum

class MCPPublicServerAuthTypeType0(str, Enum):
    API_KEY = "api_key"
    AUTHORIZATION = "authorization"
    AWS_SIGV4 = "aws_sigv4"
    BASIC = "basic"
    BEARER_TOKEN = "bearer_token"
    NONE = "none"
    OAUTH2 = "oauth2"
    TOKEN = "token"

    def __str__(self) -> str:
        return str(self.value)
