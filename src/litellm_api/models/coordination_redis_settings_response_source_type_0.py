from enum import Enum

class CoordinationRedisSettingsResponseSourceType0(str, Enum):
    CACHE_BACKEND = "cache_backend"
    COORDINATION_REDIS = "coordination_redis"
    ENVIRONMENT = "environment"

    def __str__(self) -> str:
        return str(self.value)
