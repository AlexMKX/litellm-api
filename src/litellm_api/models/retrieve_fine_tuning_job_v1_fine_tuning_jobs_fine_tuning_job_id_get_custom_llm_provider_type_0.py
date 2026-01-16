from enum import Enum

class RetrieveFineTuningJobV1FineTuningJobsFineTuningJobIdGetCustomLlmProviderType0(str, Enum):
    AZURE = "azure"
    OPENAI = "openai"

    def __str__(self) -> str:
        return str(self.value)
