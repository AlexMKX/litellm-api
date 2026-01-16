from enum import Enum

class LiteLLMFineTuningJobCreateCustomLlmProviderType0(str, Enum):
    AZURE = "azure"
    OPENAI = "openai"
    VERTEX_AI = "vertex_ai"

    def __str__(self) -> str:
        return str(self.value)
