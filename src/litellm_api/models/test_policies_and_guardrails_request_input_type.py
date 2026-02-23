from enum import Enum

class TestPoliciesAndGuardrailsRequestInputType(str, Enum):
    REQUEST = "request"
    RESPONSE = "response"

    def __str__(self) -> str:
        return str(self.value)
