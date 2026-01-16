from enum import Enum

class ProviderCredentialFieldFieldType(str, Enum):
    PASSWORD = "password"
    SELECT = "select"
    TEXT = "text"
    TEXTAREA = "textarea"
    UPLOAD = "upload"

    def __str__(self) -> str:
        return str(self.value)
