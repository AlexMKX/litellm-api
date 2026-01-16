from enum import Enum

class EmailEvent(str, Enum):
    MAX_BUDGET_ALERT = "Max Budget Alert"
    NEW_USER_INVITATION = "New User Invitation"
    SOFT_BUDGET_CROSSED = "Soft Budget Crossed"
    VIRTUAL_KEY_CREATED = "Virtual Key Created"
    VIRTUAL_KEY_ROTATED = "Virtual Key Rotated"

    def __str__(self) -> str:
        return str(self.value)
