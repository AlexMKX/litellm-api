from enum import Enum

class HealthServicesEndpointHealthServicesGetServiceType0(str, Enum):
    ARIZE = "arize"
    BRAINTRUST = "braintrust"
    DATADOG = "datadog"
    DATADOG_LLM_OBSERVABILITY = "datadog_llm_observability"
    EMAIL = "email"
    GALILEO = "galileo"
    GENERIC_API = "generic_api"
    LANGFUSE = "langfuse"
    LANGFUSE_OTEL = "langfuse_otel"
    NEWRELIC = "newrelic"
    OPENMETER = "openmeter"
    SLACK = "slack"
    SLACK_BUDGET_ALERTS = "slack_budget_alerts"
    SQS = "sqs"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
