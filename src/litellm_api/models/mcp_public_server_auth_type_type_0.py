from enum import Enum

class MCPPublicServerAuthTypeType0(str, Enum):
    API_KEY = "api_key"
    AUTHORIZATION = "authorization"
    AWS_SIGV4 = "aws_sigv4"
    BASIC = "basic"
    BEARER_TOKEN = "bearer_token"
    NONE = "none"
    OAUTH2 = "oauth2"
    OAUTH2_TOKEN_EXCHANGE = "oauth2_token_exchange"
    OAUTH_DELEGATE = "oauth_delegate"
    TOKEN = "token"
    TRUE_PASSTHROUGH = "true_passthrough"

    def __str__(self) -> str:
        return str(self.value)
