from enum import Enum

class AgentCredentialFieldFieldType(str, Enum):
    PASSWORD = "password"
    SELECT = "select"
    TEXT = "text"
    TEXTAREA = "textarea"
    UPLOAD = "upload"

    def __str__(self) -> str:
        return str(self.value)
