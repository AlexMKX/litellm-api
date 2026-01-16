from enum import Enum

class ListFineTuningJobsV1FineTuningJobsGetCustomLlmProviderType0(str, Enum):
    AZURE = "azure"
    OPENAI = "openai"

    def __str__(self) -> str:
        return str(self.value)
