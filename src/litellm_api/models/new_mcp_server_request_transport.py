from enum import Enum

class NewMCPServerRequestTransport(str, Enum):
    HTTP = "http"
    SSE = "sse"
    STDIO = "stdio"

    def __str__(self) -> str:
        return str(self.value)
