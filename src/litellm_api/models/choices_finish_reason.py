from enum import Enum

class ChoicesFinishReason(str, Enum):
    CONTENT_FILTER = "content_filter"
    EOS = "eos"
    FINISH_REASON_UNSPECIFIED = "finish_reason_unspecified"
    FUNCTION_CALL = "function_call"
    GUARDRAIL_INTERVENED = "guardrail_intervened"
    LENGTH = "length"
    MALFORMED_FUNCTION_CALL = "malformed_function_call"
    STOP = "stop"
    TOOL_CALLS = "tool_calls"

    def __str__(self) -> str:
        return str(self.value)
