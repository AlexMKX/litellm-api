from enum import Enum

class KeyManagementRoutes(str, Enum):
    VALUE_0 = "/key/generate"
    VALUE_1 = "/key/update"
    VALUE_10 = "/key/info"
    VALUE_11 = "/key/health"
    VALUE_12 = "/key/list"
    VALUE_13 = "/key/aliases"
    VALUE_14 = "/team/daily/activity"
    VALUE_2 = "/key/delete"
    VALUE_3 = "/key/regenerate"
    VALUE_4 = "/key/service-account/generate"
    VALUE_5 = "/key/{key_id}/regenerate"
    VALUE_6 = "/key/block"
    VALUE_7 = "/key/unblock"
    VALUE_8 = "/key/bulk_update"
    VALUE_9 = "/key/{key_id}/reset_spend"

    def __str__(self) -> str:
        return str(self.value)
