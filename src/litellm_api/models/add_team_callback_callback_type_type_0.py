from enum import Enum

class AddTeamCallbackCallbackTypeType0(str, Enum):
    FAILURE = "failure"
    SUCCESS = "success"
    SUCCESS_AND_FAILURE = "success_and_failure"

    def __str__(self) -> str:
        return str(self.value)
