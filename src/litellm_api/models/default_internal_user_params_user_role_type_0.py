from enum import Enum

class DefaultInternalUserParamsUserRoleType0(str, Enum):
    INTERNAL_USER = "internal_user"
    INTERNAL_USER_VIEWER = "internal_user_viewer"
    PROXY_ADMIN = "proxy_admin"
    PROXY_ADMIN_VIEWER = "proxy_admin_viewer"

    def __str__(self) -> str:
        return str(self.value)
