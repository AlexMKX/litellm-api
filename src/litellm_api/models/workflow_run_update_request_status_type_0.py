from enum import Enum

class WorkflowRunUpdateRequestStatusType0(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    PAUSED = "paused"
    PENDING = "pending"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
