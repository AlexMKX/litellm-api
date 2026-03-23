from enum import Enum

class NewMCPServerRequestOauth2FlowType0(str, Enum):
    AUTHORIZATION_CODE = "authorization_code"
    CLIENT_CREDENTIALS = "client_credentials"

    def __str__(self) -> str:
        return str(self.value)
