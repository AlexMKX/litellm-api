from enum import Enum

class PolicyValidationErrorType(str, Enum):
    CIRCULAR_INHERITANCE = "circular_inheritance"
    INVALID_GUARDRAIL = "invalid_guardrail"
    INVALID_INHERITANCE = "invalid_inheritance"
    INVALID_KEY = "invalid_key"
    INVALID_MODEL = "invalid_model"
    INVALID_SCOPE = "invalid_scope"
    INVALID_SYNTAX = "invalid_syntax"
    INVALID_TEAM = "invalid_team"

    def __str__(self) -> str:
        return str(self.value)
