from enum import Enum

class CoordinationRedisSettingsFieldSection(str, Enum):
    CLUSTER = "cluster"
    CONNECTION = "connection"
    SENTINEL = "sentinel"

    def __str__(self) -> str:
        return str(self.value)
