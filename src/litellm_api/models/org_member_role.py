from enum import Enum

class OrgMemberRole(str, Enum):
    INTERNAL_USER = "internal_user"
    INTERNAL_USER_VIEWER = "internal_user_viewer"
    ORG_ADMIN = "org_admin"

    def __str__(self) -> str:
        return str(self.value)
