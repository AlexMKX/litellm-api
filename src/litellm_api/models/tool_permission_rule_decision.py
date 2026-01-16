from enum import Enum

class ToolPermissionRuleDecision(str, Enum):
    ALLOW = "allow"
    DENY = "deny"

    def __str__(self) -> str:
        return str(self.value)
