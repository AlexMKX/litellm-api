from enum import Enum

class KeyManagementRoutes(str, Enum):
    VALUE_0 = "/key/generate"
    VALUE_1 = "/key/update"
    VALUE_10 = "/key/{key_id}/reset_spend"
    VALUE_11 = "/key/access_group_assignment"
    VALUE_12 = "/key/info"
    VALUE_13 = "/key/health"
    VALUE_14 = "/key/list"
    VALUE_15 = "/key/aliases"
    VALUE_16 = "/team/daily/activity"
    VALUE_17 = "/spend/logs"
    VALUE_18 = "/spend/logs/v2"
    VALUE_2 = "/key/delete"
    VALUE_3 = "/key/regenerate"
    VALUE_4 = "/key/service-account/generate"
    VALUE_5 = "/key/{key_id}/regenerate"
    VALUE_6 = "/key/block"
    VALUE_7 = "/key/unblock"
    VALUE_8 = "/key/bulk_update"
    VALUE_9 = "/team/key/bulk_update"

    def __str__(self) -> str:
        return str(self.value)
