from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.litellm_params_action import LitellmParamsAction
from ..models.litellm_params_default_action import LitellmParamsDefaultAction
from ..models.litellm_params_grounding_strictness_type_0 import LitellmParamsGroundingStrictnessType0
from ..models.litellm_params_on_disallowed_action import LitellmParamsOnDisallowedAction
from ..models.litellm_params_on_flagged_type_0 import LitellmParamsOnFlaggedType0
from ..models.litellm_params_on_violation_type_0 import LitellmParamsOnViolationType0
from ..models.litellm_params_presidio_filter_scope_type_0 import LitellmParamsPresidioFilterScopeType0
from ..models.litellm_params_presidio_run_on_type_0 import LitellmParamsPresidioRunOnType0
from ..models.litellm_params_unreachable_fallback import LitellmParamsUnreachableFallback
from ..models.pii_entity_type import PiiEntityType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.blocked_word import BlockedWord
  from ..models.content_filter_category_config import ContentFilterCategoryConfig
  from ..models.content_filter_pattern import ContentFilterPattern
  from ..models.gray_swan_guardrail_config_model_optional_params import GraySwanGuardrailConfigModelOptionalParams
  from ..models.lakera_category_thresholds import LakeraCategoryThresholds
  from ..models.litellm_params_additional_provider_specific_params_type_0 import LitellmParamsAdditionalProviderSpecificParamsType0
  from ..models.litellm_params_config_type_0 import LitellmParamsConfigType0
  from ..models.litellm_params_detect_secrets_config_type_0 import LitellmParamsDetectSecretsConfigType0
  from ..models.litellm_params_detectors_type_0 import LitellmParamsDetectorsType0
  from ..models.litellm_params_metadata_type_0 import LitellmParamsMetadataType0
  from ..models.litellm_params_mock_redacted_text_type_0 import LitellmParamsMockRedactedTextType0
  from ..models.litellm_params_pii_entities_config_type_0 import LitellmParamsPiiEntitiesConfigType0
  from ..models.litellm_params_presidio_score_thresholds_type_0 import LitellmParamsPresidioScoreThresholdsType0
  from ..models.mode import Mode
  from ..models.tool_permission_rule import ToolPermissionRule





T = TypeVar("T", bound="LitellmParams")



@_attrs_define
class LitellmParams:
    """ 
        Attributes:
            guardrail (str): The type of guardrail integration to use
            mode (list[str] | Mode | str): When to apply the guardrail (pre_call, post_call, during_call, logging_only)
            action (LitellmParamsAction | Unset): 'block' raises an error; 'mask' replaces the code block with a
                placeholder. Default: LitellmParamsAction.BLOCK.
            additional_provider_specific_params (LitellmParamsAdditionalProviderSpecificParamsType0 | None | Unset):
                Additional provider-specific parameters for generic guardrail APIs
            akto_account_id (None | str | Unset): Akto account ID for multi-tenant deployments. Env: AKTO_ACCOUNT_ID.
                Default: '1000000'.
            akto_api_key (None | str | Unset): API key for Akto. Env: AKTO_API_KEY.
            akto_base_url (None | str | Unset): Akto Guardrail API Base URL. Env: AKTO_GUARDRAIL_API_BASE.
            akto_vxlan_id (None | str | Unset): Akto VXLAN ID. Env: AKTO_VXLAN_ID. Default: '0'.
            anonymize_input (bool | None | Unset): If True, replaces sensitive content with anonymized version when only
                PII/PCI/secrets are detected. Only applies in blocking mode. Defaults to False if not provided
            api_base (None | str | Unset): Base URL for the Lakera AI API
            api_endpoint (None | str | Unset): Optional custom API endpoint for Model Armor
            api_id (None | str | Unset): The Hiddenlayer API Id for the Hiddenlayer API. If not provided, the
                `HIDDENLAYER_CLIENT_ID` environment variable is checked or https://api.hiddenlayer.ai is used.
            api_key (None | str | Unset): API key for the Lakera AI service
            api_version (None | str | Unset): API version for Javelin service Default: 'v1'.
            application (None | str | Unset): Application name for Javelin service
            application_id (None | str | Unset): Application ID for Noma Security. Defaults to 'litellm' if not provided
            assertions (list[str] | None | Unset): Custom assertions to validate against the output. Each assertion is a
                string describing a condition.
            async_mode (bool | None | Unset): Set to True to request asynchronous analysis (sets `plr_async` header).
                Defaults to provider behaviour when omitted.
            auth_token (None | str | Unset): Authorization bearer token for IBM Guardrails API. Reads from
                IBM_GUARDRAILS_AUTH_TOKEN env var if None.
            aws_access_key_id (None | str | Unset): AWS access key ID for authentication
            aws_bedrock_runtime_endpoint (None | str | Unset): AWS Bedrock runtime endpoint URL
            aws_profile_name (None | str | Unset): AWS profile name for credential retrieval
            aws_region_name (None | str | Unset): AWS region where your guardrail is deployed
            aws_role_name (None | str | Unset): AWS role name for assuming roles
            aws_secret_access_key (None | str | Unset): AWS secret access key for authentication
            aws_session_name (None | str | Unset): Name of the AWS session
            aws_session_token (None | str | Unset): AWS session token for temporary credentials
            aws_sts_endpoint (None | str | Unset): AWS STS endpoint URL
            aws_web_identity_token (None | str | Unset): Web identity token for AWS role assumption
            base_url (None | str | Unset): Base URL for the IBM Guardrails server
            block_failures (bool | None | Unset): If True, blocks requests on API failures. Defaults to True if not provided
            block_on_error (bool | None | Unset): Whether to block the request when the PromptGuard API is unreachable.
                Defaults to true (fail-closed). Set to false for fail-open behaviour.
            block_on_violation (bool | None | Unset): Whether to block requests when violations are detected. Defaults to
                True. Default: True.
            blocked_languages (list[str] | None | Unset): Language tags to block (e.g. python, javascript, bash). Empty or
                None = block all fenced code blocks.
            blocked_words (list[BlockedWord] | None | Unset): List of blocked words with individual actions
            blocked_words_file (None | str | Unset): Path to YAML file containing blocked_words list
            breakdown (bool | None | Unset): Whether to include breakdown in the response Default: True.
            categories (list[ContentFilterCategoryConfig] | None | Unset): List of prebuilt categories to enable (harmful_*,
                bias_*)
            category_thresholds (LakeraCategoryThresholds | None | Unset): Threshold configuration for Lakera guardrail
                categories
            confidence_threshold (float | Unset): Only block or mask when detection confidence >= this value; below
                threshold, allow or log_only. Default: 0.5.
            config (LitellmParamsConfigType0 | None | Unset): Additional configuration for the guardrail
            content_moderation_check (bool | None | Unset): Enable content moderation to check for harmful content
                (harassment, hate speech, etc.).
            credentials (None | str | Unset): Path to Google Cloud credentials JSON file or JSON string
            custom_code (None | str | Unset): Python-like code containing the apply_guardrail function for custom guardrail
                logic
            default_action (LitellmParamsDefaultAction | Unset): Fallback decision when no rule matches Default:
                LitellmParamsDefaultAction.DENY.
            default_on (bool | None | Unset): Whether the guardrail is enabled by default
            deployment_name (None | str | Unset): The EnkryptAI deployment name to use. Sent via X-Enkrypt-Deployment
                header.
            detect_execution_intent (bool | Unset): When True, block only when user intent is to run/execute; allow when
                intent is explain/refactor/don't run. Also block text-only execution requests (e.g. 'run `ls`', 'read
                /etc/passwd'). Default: True.
            detect_secrets_config (LitellmParamsDetectSecretsConfigType0 | None | Unset): Configuration for detect-secrets
                guardrail
            detector_id (None | str | Unset): Name of the detector inside the server (e.g., 'jailbreak-detector')
            detectors (LitellmParamsDetectorsType0 | None | Unset): Dictionary of detector configurations (e.g., {'nsfw':
                {'enabled': True}, 'toxicity': {'enabled': True}}).
            dev_info (bool | None | Unset): Whether to include developer information in the response Default: True.
            disable_exception_on_block (bool | None | Unset): If True, will not raise an exception when the guardrail is
                blocked. Useful for OpenWebUI where exceptions can end the chat flow. Default: False.
            end_session_after_n_fails (int | None | Unset): For /v1/realtime sessions: automatically close the session after
                this many guardrail violations.
            evaluation_id (None | str | Unset): Pre-configured evaluation ID from Qualifire dashboard. When provided, uses
                invoke_evaluation() instead of evaluate().
            experimental_use_latest_role_message_only (bool | None | Unset): When True, guardrails only receive the latest
                message for the relevant role (e.g., newest user input pre-call, newest assistant output post-call) Default:
                False.
            extra_headers (list[str] | None | Unset): Header names to forward from the client request to the guardrail (e.g.
                x-request-id). Only these headers' values are sent; others may be omitted or sent as [present]. Used by
                generic_guardrail_api (similar to MCP extra_headers).
            fail_on_error (bool | None | Unset): Whether to fail the request if Model Armor encounters an error Default:
                True.
            grounding_check (bool | None | Unset): Enable grounding verification to ensure output is grounded in provided
                context.
            grounding_strictness (LitellmParamsGroundingStrictnessType0 | None | Unset): Strictness level for XecGuard
                context-grounding validation. 'BALANCED' (default) treats INCOMPLETE answers as SAFE; 'STRICT' flags them as
                UNSAFE. Grounding only runs in post_call when `metadata.xecguard_grounding_documents` is provided.
            guard_name (None | str | Unset): Name of the Javelin guard to use
            guardrail_identifier (None | str | Unset): The ID of your guardrail on Bedrock
            guardrail_version (None | str | Unset): The version of your Bedrock guardrail (e.g., DRAFT or version number)
            guardrail_timeout (int | None | Unset): HTTP timeout in seconds. Default: 5.
            hallucinations_check (bool | None | Unset): Enable hallucination detection to detect factual inaccuracies.
            include_evidence (bool | None | Unset): Include detailed evidence payloads in responses (sets `plr_evidence`
                header). Default: True.
            include_scanners (bool | None | Unset): Include scanner category summaries in responses (sets `plr_scanners`
                header). Default: True.
            is_detector_server (bool | None | Unset): Boolean flag to determine if calling a detector server (True) or the
                FMS Orchestrator (False). Defaults to True. Default: True.
            keyword_redaction_tag (None | str | Unset): Tag to use for keyword redaction
            lasso_conversation_id (None | str | Unset): Conversation ID for the Lasso guardrail
            lasso_user_id (None | str | Unset): User ID for the Lasso guardrail
            location (None | str | Unset): Google Cloud location/region (e.g., us-central1)
            mask (bool | None | Unset): Enable content masking using Lasso classifix API Default: False.
            mask_request_content (bool | None | Unset): Will mask request content if guardrail makes any changes
            mask_response_content (bool | None | Unset): Will mask response content if guardrail makes any changes
            metadata (LitellmParamsMetadataType0 | None | Unset): Additional metadata to include in the request
            mock_redacted_text (LitellmParamsMockRedactedTextType0 | None | Unset): Mock redacted text for testing
            model (None | str | Unset): Optional field if guardrail requires a 'model' parameter
            monitor_mode (bool | None | Unset): If True, logs violations without blocking. Defaults to False if not provided
            on_disallowed_action (LitellmParamsOnDisallowedAction | Unset): Choose whether disallowed tools block the
                request or get rewritten out of the payload Default: LitellmParamsOnDisallowedAction.BLOCK.
            on_flagged (LitellmParamsOnFlaggedType0 | None | Unset): Action to take when content is flagged: 'block' (raise
                exception) or 'monitor' (log only) Default: LitellmParamsOnFlaggedType0.BLOCK.
            on_flagged_action (None | str | Unset): Action to take when content is flagged: 'block' (raise exception) or
                'monitor' (log only) Default: 'monitor'.
            on_violation (LitellmParamsOnViolationType0 | None | Unset): For /v1/realtime sessions: 'warn' speaks the
                violation message and continues; 'end_session' speaks the message and closes the connection.
            optional_params (GraySwanGuardrailConfigModelOptionalParams | None | Unset): Optional parameters for the
                guardrail
            output_parse_pii (bool | None | Unset): When True, LiteLLM will replace the masked text with the original text
                in the response
            pangea_input_recipe (None | str | Unset): Recipe for input (LLM request)
            pangea_output_recipe (None | str | Unset): Recipe for output (LLM response)
            pattern_redaction_format (None | str | Unset): Format string for pattern redaction (use {pattern_name}
                placeholder)
            patterns (list[ContentFilterPattern] | None | Unset): List of patterns (prebuilt or custom regex) to detect
            payload (bool | None | Unset): Whether to include payload in the response Default: True.
            persist_session (bool | None | Unset): Controls Pillar session persistence (sets `plr_persist` header). Set to
                False to disable persistence.
            pii_check (bool | None | Unset): Enable PII (Personally Identifiable Information) detection.
            pii_entities_config (LitellmParamsPiiEntitiesConfigType0 | None | Unset): Configuration for PII entity types and
                actions
            policy_id (int | None | Unset): Policy ID for Zscaler AI Guard. Can also be set via ZSCALER_AI_GUARD_POLICY_ID
                environment variable
            policy_name (None | str | Unset): The EnkryptAI policy name to use. Sent via x-enkrypt-policy header.
            policy_names (list[str] | None | Unset): XecGuard policies to apply on each scan. Select one or more of the
                built-in default policies; if none are selected, the guardrail defaults to System Prompt Enforcement + Harmful
                Content Protection.
            presidio_ad_hoc_recognizers (None | str | Unset): Path to a JSON file containing ad-hoc recognizers for Presidio
            presidio_analyzer_api_base (None | str | Unset): Base URL for the Presidio analyzer API
            presidio_anonymizer_api_base (None | str | Unset): Base URL for the Presidio anonymizer API
            presidio_entities_deny_list (list[PiiEntityType | str] | None | Unset): List of entity types to exclude from
                Presidio detection results. Detections of these types will be silently dropped. Useful for suppressing false
                positives (e.g., US_DRIVER_LICENSE on coding routes).
            presidio_filter_scope (LitellmParamsPresidioFilterScopeType0 | None | Unset): Where to apply Presidio checks:
                'input' (user -> model), 'output' (model -> user), or 'both' (default).
            presidio_language (None | str | Unset): Language code for Presidio PII analysis (e.g., 'en', 'de', 'es', 'fr')
                Default: 'en'.
            presidio_run_on (LitellmParamsPresidioRunOnType0 | None | Unset): Where to apply Presidio checks: input, output,
                or both (default).
            presidio_score_thresholds (LitellmParamsPresidioScoreThresholdsType0 | None | Unset): Optional per-entity
                minimum confidence scores for Presidio detections. Entities below the threshold are ignored.
            project_id (None | str | Unset): Project ID for the Lakera AI project
            prompt_injections (bool | None | Unset): Enable prompt injection detection. Default check if no evaluation_id
                and no other checks are specified.
            realtime_violation_message (None | str | Unset): The message the bot speaks aloud when a /v1/realtime guardrail
                fires. Falls back to violation_message_template if not set.
            rules (list[ToolPermissionRule] | None | Unset): Ordered allow/deny rules. Patterns use regex for tool
                names/types and optional regex constraints on tool arguments.
            send_user_api_key_alias (bool | None | Unset): Whether to send user_API_key_alias in headers Default: False.
            send_user_api_key_team_id (bool | None | Unset): Whether to send user_API_key_team_id in headers Default: False.
            send_user_api_key_user_id (bool | None | Unset): Whether to send user_API_key_user_id in headers Default: False.
            severity_threshold (None | str | Unset): Minimum severity to block (high, medium, low)
            skip_system_message_in_guardrail (bool | None | Unset): When True, unified guardrails skip system-role messages
                when building evaluation inputs (texts and structured_messages). When False, system messages are included even
                if litellm_settings sets a global skip. When None, use the global litellm.skip_system_message_in_guardrail
                setting.
            template_id (None | str | Unset): The ID of your Model Armor template
            tool_selection_quality_check (bool | None | Unset): Enable tool selection quality check to evaluate quality of
                tool/function calls.
            unreachable_fallback (LitellmParamsUnreachableFallback | Unset): What to do when Akto is unreachable.
                'fail_open' = allow, 'fail_closed' = block. Default: LitellmParamsUnreachableFallback.FAIL_CLOSED.
            use_v2 (bool | None | Unset): If True and guardrail='noma', route to the new Noma v2 implementation instead of
                the legacy implementation. Default: False.
            verify_ssl (bool | None | Unset): Whether to verify SSL certificates. Defaults to True. Default: True.
            version (int | None | Unset): Hiddenlayer guardrail version to use. Default: 2.
            violation_message_template (None | str | Unset): Custom message when a guardrail blocks an action. Supports
                placeholders like {tool_name}, {rule_id}, and {default_message}.
            xecguard_model (None | str | Unset): XecGuard scanning model identifier. Defaults to 'xecguard_v2'.
     """

    guardrail: str
    mode: list[str] | Mode | str
    action: LitellmParamsAction | Unset = LitellmParamsAction.BLOCK
    additional_provider_specific_params: LitellmParamsAdditionalProviderSpecificParamsType0 | None | Unset = UNSET
    akto_account_id: None | str | Unset = UNSET
    akto_api_key: None | str | Unset = UNSET
    akto_base_url: None | str | Unset = UNSET
    akto_vxlan_id: None | str | Unset = UNSET
    anonymize_input: bool | None | Unset = UNSET
    api_base: None | str | Unset = UNSET
    api_endpoint: None | str | Unset = UNSET
    api_id: None | str | Unset = UNSET
    api_key: None | str | Unset = UNSET
    api_version: None | str | Unset = 'v1'
    application: None | str | Unset = UNSET
    application_id: None | str | Unset = UNSET
    assertions: list[str] | None | Unset = UNSET
    async_mode: bool | None | Unset = UNSET
    auth_token: None | str | Unset = UNSET
    aws_access_key_id: None | str | Unset = UNSET
    aws_bedrock_runtime_endpoint: None | str | Unset = UNSET
    aws_profile_name: None | str | Unset = UNSET
    aws_region_name: None | str | Unset = UNSET
    aws_role_name: None | str | Unset = UNSET
    aws_secret_access_key: None | str | Unset = UNSET
    aws_session_name: None | str | Unset = UNSET
    aws_session_token: None | str | Unset = UNSET
    aws_sts_endpoint: None | str | Unset = UNSET
    aws_web_identity_token: None | str | Unset = UNSET
    base_url: None | str | Unset = UNSET
    block_failures: bool | None | Unset = UNSET
    block_on_error: bool | None | Unset = UNSET
    block_on_violation: bool | None | Unset = True
    blocked_languages: list[str] | None | Unset = UNSET
    blocked_words: list[BlockedWord] | None | Unset = UNSET
    blocked_words_file: None | str | Unset = UNSET
    breakdown: bool | None | Unset = True
    categories: list[ContentFilterCategoryConfig] | None | Unset = UNSET
    category_thresholds: LakeraCategoryThresholds | None | Unset = UNSET
    confidence_threshold: float | Unset = 0.5
    config: LitellmParamsConfigType0 | None | Unset = UNSET
    content_moderation_check: bool | None | Unset = UNSET
    credentials: None | str | Unset = UNSET
    custom_code: None | str | Unset = UNSET
    default_action: LitellmParamsDefaultAction | Unset = LitellmParamsDefaultAction.DENY
    default_on: bool | None | Unset = UNSET
    deployment_name: None | str | Unset = UNSET
    detect_execution_intent: bool | Unset = True
    detect_secrets_config: LitellmParamsDetectSecretsConfigType0 | None | Unset = UNSET
    detector_id: None | str | Unset = UNSET
    detectors: LitellmParamsDetectorsType0 | None | Unset = UNSET
    dev_info: bool | None | Unset = True
    disable_exception_on_block: bool | None | Unset = False
    end_session_after_n_fails: int | None | Unset = UNSET
    evaluation_id: None | str | Unset = UNSET
    experimental_use_latest_role_message_only: bool | None | Unset = False
    extra_headers: list[str] | None | Unset = UNSET
    fail_on_error: bool | None | Unset = True
    grounding_check: bool | None | Unset = UNSET
    grounding_strictness: LitellmParamsGroundingStrictnessType0 | None | Unset = UNSET
    guard_name: None | str | Unset = UNSET
    guardrail_identifier: None | str | Unset = UNSET
    guardrail_version: None | str | Unset = UNSET
    guardrail_timeout: int | None | Unset = UNSET
    hallucinations_check: bool | None | Unset = UNSET
    include_evidence: bool | None | Unset = True
    include_scanners: bool | None | Unset = True
    is_detector_server: bool | None | Unset = True
    keyword_redaction_tag: None | str | Unset = UNSET
    lasso_conversation_id: None | str | Unset = UNSET
    lasso_user_id: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    mask: bool | None | Unset = False
    mask_request_content: bool | None | Unset = UNSET
    mask_response_content: bool | None | Unset = UNSET
    metadata: LitellmParamsMetadataType0 | None | Unset = UNSET
    mock_redacted_text: LitellmParamsMockRedactedTextType0 | None | Unset = UNSET
    model: None | str | Unset = UNSET
    monitor_mode: bool | None | Unset = UNSET
    on_disallowed_action: LitellmParamsOnDisallowedAction | Unset = LitellmParamsOnDisallowedAction.BLOCK
    on_flagged: LitellmParamsOnFlaggedType0 | None | Unset = LitellmParamsOnFlaggedType0.BLOCK
    on_flagged_action: None | str | Unset = 'monitor'
    on_violation: LitellmParamsOnViolationType0 | None | Unset = UNSET
    optional_params: GraySwanGuardrailConfigModelOptionalParams | None | Unset = UNSET
    output_parse_pii: bool | None | Unset = UNSET
    pangea_input_recipe: None | str | Unset = UNSET
    pangea_output_recipe: None | str | Unset = UNSET
    pattern_redaction_format: None | str | Unset = UNSET
    patterns: list[ContentFilterPattern] | None | Unset = UNSET
    payload: bool | None | Unset = True
    persist_session: bool | None | Unset = UNSET
    pii_check: bool | None | Unset = UNSET
    pii_entities_config: LitellmParamsPiiEntitiesConfigType0 | None | Unset = UNSET
    policy_id: int | None | Unset = UNSET
    policy_name: None | str | Unset = UNSET
    policy_names: list[str] | None | Unset = UNSET
    presidio_ad_hoc_recognizers: None | str | Unset = UNSET
    presidio_analyzer_api_base: None | str | Unset = UNSET
    presidio_anonymizer_api_base: None | str | Unset = UNSET
    presidio_entities_deny_list: list[PiiEntityType | str] | None | Unset = UNSET
    presidio_filter_scope: LitellmParamsPresidioFilterScopeType0 | None | Unset = UNSET
    presidio_language: None | str | Unset = 'en'
    presidio_run_on: LitellmParamsPresidioRunOnType0 | None | Unset = UNSET
    presidio_score_thresholds: LitellmParamsPresidioScoreThresholdsType0 | None | Unset = UNSET
    project_id: None | str | Unset = UNSET
    prompt_injections: bool | None | Unset = UNSET
    realtime_violation_message: None | str | Unset = UNSET
    rules: list[ToolPermissionRule] | None | Unset = UNSET
    send_user_api_key_alias: bool | None | Unset = False
    send_user_api_key_team_id: bool | None | Unset = False
    send_user_api_key_user_id: bool | None | Unset = False
    severity_threshold: None | str | Unset = UNSET
    skip_system_message_in_guardrail: bool | None | Unset = UNSET
    template_id: None | str | Unset = UNSET
    tool_selection_quality_check: bool | None | Unset = UNSET
    unreachable_fallback: LitellmParamsUnreachableFallback | Unset = LitellmParamsUnreachableFallback.FAIL_CLOSED
    use_v2: bool | None | Unset = False
    verify_ssl: bool | None | Unset = True
    version: int | None | Unset = 2
    violation_message_template: None | str | Unset = UNSET
    xecguard_model: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.blocked_word import BlockedWord
        from ..models.content_filter_category_config import ContentFilterCategoryConfig
        from ..models.content_filter_pattern import ContentFilterPattern
        from ..models.gray_swan_guardrail_config_model_optional_params import GraySwanGuardrailConfigModelOptionalParams
        from ..models.lakera_category_thresholds import LakeraCategoryThresholds
        from ..models.litellm_params_additional_provider_specific_params_type_0 import LitellmParamsAdditionalProviderSpecificParamsType0
        from ..models.litellm_params_config_type_0 import LitellmParamsConfigType0
        from ..models.litellm_params_detect_secrets_config_type_0 import LitellmParamsDetectSecretsConfigType0
        from ..models.litellm_params_detectors_type_0 import LitellmParamsDetectorsType0
        from ..models.litellm_params_metadata_type_0 import LitellmParamsMetadataType0
        from ..models.litellm_params_mock_redacted_text_type_0 import LitellmParamsMockRedactedTextType0
        from ..models.litellm_params_pii_entities_config_type_0 import LitellmParamsPiiEntitiesConfigType0
        from ..models.litellm_params_presidio_score_thresholds_type_0 import LitellmParamsPresidioScoreThresholdsType0
        from ..models.mode import Mode
        from ..models.tool_permission_rule import ToolPermissionRule
        guardrail = self.guardrail

        mode: dict[str, Any] | list[str] | str
        if isinstance(self.mode, list):
            mode = self.mode


        elif isinstance(self.mode, Mode):
            mode = self.mode.to_dict()
        else:
            mode = self.mode

        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value


        additional_provider_specific_params: dict[str, Any] | None | Unset
        if isinstance(self.additional_provider_specific_params, Unset):
            additional_provider_specific_params = UNSET
        elif isinstance(self.additional_provider_specific_params, LitellmParamsAdditionalProviderSpecificParamsType0):
            additional_provider_specific_params = self.additional_provider_specific_params.to_dict()
        else:
            additional_provider_specific_params = self.additional_provider_specific_params

        akto_account_id: None | str | Unset
        if isinstance(self.akto_account_id, Unset):
            akto_account_id = UNSET
        else:
            akto_account_id = self.akto_account_id

        akto_api_key: None | str | Unset
        if isinstance(self.akto_api_key, Unset):
            akto_api_key = UNSET
        else:
            akto_api_key = self.akto_api_key

        akto_base_url: None | str | Unset
        if isinstance(self.akto_base_url, Unset):
            akto_base_url = UNSET
        else:
            akto_base_url = self.akto_base_url

        akto_vxlan_id: None | str | Unset
        if isinstance(self.akto_vxlan_id, Unset):
            akto_vxlan_id = UNSET
        else:
            akto_vxlan_id = self.akto_vxlan_id

        anonymize_input: bool | None | Unset
        if isinstance(self.anonymize_input, Unset):
            anonymize_input = UNSET
        else:
            anonymize_input = self.anonymize_input

        api_base: None | str | Unset
        if isinstance(self.api_base, Unset):
            api_base = UNSET
        else:
            api_base = self.api_base

        api_endpoint: None | str | Unset
        if isinstance(self.api_endpoint, Unset):
            api_endpoint = UNSET
        else:
            api_endpoint = self.api_endpoint

        api_id: None | str | Unset
        if isinstance(self.api_id, Unset):
            api_id = UNSET
        else:
            api_id = self.api_id

        api_key: None | str | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

        api_version: None | str | Unset
        if isinstance(self.api_version, Unset):
            api_version = UNSET
        else:
            api_version = self.api_version

        application: None | str | Unset
        if isinstance(self.application, Unset):
            application = UNSET
        else:
            application = self.application

        application_id: None | str | Unset
        if isinstance(self.application_id, Unset):
            application_id = UNSET
        else:
            application_id = self.application_id

        assertions: list[str] | None | Unset
        if isinstance(self.assertions, Unset):
            assertions = UNSET
        elif isinstance(self.assertions, list):
            assertions = self.assertions


        else:
            assertions = self.assertions

        async_mode: bool | None | Unset
        if isinstance(self.async_mode, Unset):
            async_mode = UNSET
        else:
            async_mode = self.async_mode

        auth_token: None | str | Unset
        if isinstance(self.auth_token, Unset):
            auth_token = UNSET
        else:
            auth_token = self.auth_token

        aws_access_key_id: None | str | Unset
        if isinstance(self.aws_access_key_id, Unset):
            aws_access_key_id = UNSET
        else:
            aws_access_key_id = self.aws_access_key_id

        aws_bedrock_runtime_endpoint: None | str | Unset
        if isinstance(self.aws_bedrock_runtime_endpoint, Unset):
            aws_bedrock_runtime_endpoint = UNSET
        else:
            aws_bedrock_runtime_endpoint = self.aws_bedrock_runtime_endpoint

        aws_profile_name: None | str | Unset
        if isinstance(self.aws_profile_name, Unset):
            aws_profile_name = UNSET
        else:
            aws_profile_name = self.aws_profile_name

        aws_region_name: None | str | Unset
        if isinstance(self.aws_region_name, Unset):
            aws_region_name = UNSET
        else:
            aws_region_name = self.aws_region_name

        aws_role_name: None | str | Unset
        if isinstance(self.aws_role_name, Unset):
            aws_role_name = UNSET
        else:
            aws_role_name = self.aws_role_name

        aws_secret_access_key: None | str | Unset
        if isinstance(self.aws_secret_access_key, Unset):
            aws_secret_access_key = UNSET
        else:
            aws_secret_access_key = self.aws_secret_access_key

        aws_session_name: None | str | Unset
        if isinstance(self.aws_session_name, Unset):
            aws_session_name = UNSET
        else:
            aws_session_name = self.aws_session_name

        aws_session_token: None | str | Unset
        if isinstance(self.aws_session_token, Unset):
            aws_session_token = UNSET
        else:
            aws_session_token = self.aws_session_token

        aws_sts_endpoint: None | str | Unset
        if isinstance(self.aws_sts_endpoint, Unset):
            aws_sts_endpoint = UNSET
        else:
            aws_sts_endpoint = self.aws_sts_endpoint

        aws_web_identity_token: None | str | Unset
        if isinstance(self.aws_web_identity_token, Unset):
            aws_web_identity_token = UNSET
        else:
            aws_web_identity_token = self.aws_web_identity_token

        base_url: None | str | Unset
        if isinstance(self.base_url, Unset):
            base_url = UNSET
        else:
            base_url = self.base_url

        block_failures: bool | None | Unset
        if isinstance(self.block_failures, Unset):
            block_failures = UNSET
        else:
            block_failures = self.block_failures

        block_on_error: bool | None | Unset
        if isinstance(self.block_on_error, Unset):
            block_on_error = UNSET
        else:
            block_on_error = self.block_on_error

        block_on_violation: bool | None | Unset
        if isinstance(self.block_on_violation, Unset):
            block_on_violation = UNSET
        else:
            block_on_violation = self.block_on_violation

        blocked_languages: list[str] | None | Unset
        if isinstance(self.blocked_languages, Unset):
            blocked_languages = UNSET
        elif isinstance(self.blocked_languages, list):
            blocked_languages = self.blocked_languages


        else:
            blocked_languages = self.blocked_languages

        blocked_words: list[dict[str, Any]] | None | Unset
        if isinstance(self.blocked_words, Unset):
            blocked_words = UNSET
        elif isinstance(self.blocked_words, list):
            blocked_words = []
            for blocked_words_type_0_item_data in self.blocked_words:
                blocked_words_type_0_item = blocked_words_type_0_item_data.to_dict()
                blocked_words.append(blocked_words_type_0_item)


        else:
            blocked_words = self.blocked_words

        blocked_words_file: None | str | Unset
        if isinstance(self.blocked_words_file, Unset):
            blocked_words_file = UNSET
        else:
            blocked_words_file = self.blocked_words_file

        breakdown: bool | None | Unset
        if isinstance(self.breakdown, Unset):
            breakdown = UNSET
        else:
            breakdown = self.breakdown

        categories: list[dict[str, Any]] | None | Unset
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = []
            for categories_type_0_item_data in self.categories:
                categories_type_0_item = categories_type_0_item_data.to_dict()
                categories.append(categories_type_0_item)


        else:
            categories = self.categories

        category_thresholds: dict[str, Any] | None | Unset
        if isinstance(self.category_thresholds, Unset):
            category_thresholds = UNSET
        elif isinstance(self.category_thresholds, LakeraCategoryThresholds):
            category_thresholds = self.category_thresholds.to_dict()
        else:
            category_thresholds = self.category_thresholds

        confidence_threshold = self.confidence_threshold

        config: dict[str, Any] | None | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, LitellmParamsConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

        content_moderation_check: bool | None | Unset
        if isinstance(self.content_moderation_check, Unset):
            content_moderation_check = UNSET
        else:
            content_moderation_check = self.content_moderation_check

        credentials: None | str | Unset
        if isinstance(self.credentials, Unset):
            credentials = UNSET
        else:
            credentials = self.credentials

        custom_code: None | str | Unset
        if isinstance(self.custom_code, Unset):
            custom_code = UNSET
        else:
            custom_code = self.custom_code

        default_action: str | Unset = UNSET
        if not isinstance(self.default_action, Unset):
            default_action = self.default_action.value


        default_on: bool | None | Unset
        if isinstance(self.default_on, Unset):
            default_on = UNSET
        else:
            default_on = self.default_on

        deployment_name: None | str | Unset
        if isinstance(self.deployment_name, Unset):
            deployment_name = UNSET
        else:
            deployment_name = self.deployment_name

        detect_execution_intent = self.detect_execution_intent

        detect_secrets_config: dict[str, Any] | None | Unset
        if isinstance(self.detect_secrets_config, Unset):
            detect_secrets_config = UNSET
        elif isinstance(self.detect_secrets_config, LitellmParamsDetectSecretsConfigType0):
            detect_secrets_config = self.detect_secrets_config.to_dict()
        else:
            detect_secrets_config = self.detect_secrets_config

        detector_id: None | str | Unset
        if isinstance(self.detector_id, Unset):
            detector_id = UNSET
        else:
            detector_id = self.detector_id

        detectors: dict[str, Any] | None | Unset
        if isinstance(self.detectors, Unset):
            detectors = UNSET
        elif isinstance(self.detectors, LitellmParamsDetectorsType0):
            detectors = self.detectors.to_dict()
        else:
            detectors = self.detectors

        dev_info: bool | None | Unset
        if isinstance(self.dev_info, Unset):
            dev_info = UNSET
        else:
            dev_info = self.dev_info

        disable_exception_on_block: bool | None | Unset
        if isinstance(self.disable_exception_on_block, Unset):
            disable_exception_on_block = UNSET
        else:
            disable_exception_on_block = self.disable_exception_on_block

        end_session_after_n_fails: int | None | Unset
        if isinstance(self.end_session_after_n_fails, Unset):
            end_session_after_n_fails = UNSET
        else:
            end_session_after_n_fails = self.end_session_after_n_fails

        evaluation_id: None | str | Unset
        if isinstance(self.evaluation_id, Unset):
            evaluation_id = UNSET
        else:
            evaluation_id = self.evaluation_id

        experimental_use_latest_role_message_only: bool | None | Unset
        if isinstance(self.experimental_use_latest_role_message_only, Unset):
            experimental_use_latest_role_message_only = UNSET
        else:
            experimental_use_latest_role_message_only = self.experimental_use_latest_role_message_only

        extra_headers: list[str] | None | Unset
        if isinstance(self.extra_headers, Unset):
            extra_headers = UNSET
        elif isinstance(self.extra_headers, list):
            extra_headers = self.extra_headers


        else:
            extra_headers = self.extra_headers

        fail_on_error: bool | None | Unset
        if isinstance(self.fail_on_error, Unset):
            fail_on_error = UNSET
        else:
            fail_on_error = self.fail_on_error

        grounding_check: bool | None | Unset
        if isinstance(self.grounding_check, Unset):
            grounding_check = UNSET
        else:
            grounding_check = self.grounding_check

        grounding_strictness: None | str | Unset
        if isinstance(self.grounding_strictness, Unset):
            grounding_strictness = UNSET
        elif isinstance(self.grounding_strictness, LitellmParamsGroundingStrictnessType0):
            grounding_strictness = self.grounding_strictness.value
        else:
            grounding_strictness = self.grounding_strictness

        guard_name: None | str | Unset
        if isinstance(self.guard_name, Unset):
            guard_name = UNSET
        else:
            guard_name = self.guard_name

        guardrail_identifier: None | str | Unset
        if isinstance(self.guardrail_identifier, Unset):
            guardrail_identifier = UNSET
        else:
            guardrail_identifier = self.guardrail_identifier

        guardrail_version: None | str | Unset
        if isinstance(self.guardrail_version, Unset):
            guardrail_version = UNSET
        else:
            guardrail_version = self.guardrail_version

        guardrail_timeout: int | None | Unset
        if isinstance(self.guardrail_timeout, Unset):
            guardrail_timeout = UNSET
        else:
            guardrail_timeout = self.guardrail_timeout

        hallucinations_check: bool | None | Unset
        if isinstance(self.hallucinations_check, Unset):
            hallucinations_check = UNSET
        else:
            hallucinations_check = self.hallucinations_check

        include_evidence: bool | None | Unset
        if isinstance(self.include_evidence, Unset):
            include_evidence = UNSET
        else:
            include_evidence = self.include_evidence

        include_scanners: bool | None | Unset
        if isinstance(self.include_scanners, Unset):
            include_scanners = UNSET
        else:
            include_scanners = self.include_scanners

        is_detector_server: bool | None | Unset
        if isinstance(self.is_detector_server, Unset):
            is_detector_server = UNSET
        else:
            is_detector_server = self.is_detector_server

        keyword_redaction_tag: None | str | Unset
        if isinstance(self.keyword_redaction_tag, Unset):
            keyword_redaction_tag = UNSET
        else:
            keyword_redaction_tag = self.keyword_redaction_tag

        lasso_conversation_id: None | str | Unset
        if isinstance(self.lasso_conversation_id, Unset):
            lasso_conversation_id = UNSET
        else:
            lasso_conversation_id = self.lasso_conversation_id

        lasso_user_id: None | str | Unset
        if isinstance(self.lasso_user_id, Unset):
            lasso_user_id = UNSET
        else:
            lasso_user_id = self.lasso_user_id

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        mask: bool | None | Unset
        if isinstance(self.mask, Unset):
            mask = UNSET
        else:
            mask = self.mask

        mask_request_content: bool | None | Unset
        if isinstance(self.mask_request_content, Unset):
            mask_request_content = UNSET
        else:
            mask_request_content = self.mask_request_content

        mask_response_content: bool | None | Unset
        if isinstance(self.mask_response_content, Unset):
            mask_response_content = UNSET
        else:
            mask_response_content = self.mask_response_content

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, LitellmParamsMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        mock_redacted_text: dict[str, Any] | None | Unset
        if isinstance(self.mock_redacted_text, Unset):
            mock_redacted_text = UNSET
        elif isinstance(self.mock_redacted_text, LitellmParamsMockRedactedTextType0):
            mock_redacted_text = self.mock_redacted_text.to_dict()
        else:
            mock_redacted_text = self.mock_redacted_text

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        monitor_mode: bool | None | Unset
        if isinstance(self.monitor_mode, Unset):
            monitor_mode = UNSET
        else:
            monitor_mode = self.monitor_mode

        on_disallowed_action: str | Unset = UNSET
        if not isinstance(self.on_disallowed_action, Unset):
            on_disallowed_action = self.on_disallowed_action.value


        on_flagged: None | str | Unset
        if isinstance(self.on_flagged, Unset):
            on_flagged = UNSET
        elif isinstance(self.on_flagged, LitellmParamsOnFlaggedType0):
            on_flagged = self.on_flagged.value
        else:
            on_flagged = self.on_flagged

        on_flagged_action: None | str | Unset
        if isinstance(self.on_flagged_action, Unset):
            on_flagged_action = UNSET
        else:
            on_flagged_action = self.on_flagged_action

        on_violation: None | str | Unset
        if isinstance(self.on_violation, Unset):
            on_violation = UNSET
        elif isinstance(self.on_violation, LitellmParamsOnViolationType0):
            on_violation = self.on_violation.value
        else:
            on_violation = self.on_violation

        optional_params: dict[str, Any] | None | Unset
        if isinstance(self.optional_params, Unset):
            optional_params = UNSET
        elif isinstance(self.optional_params, GraySwanGuardrailConfigModelOptionalParams):
            optional_params = self.optional_params.to_dict()
        else:
            optional_params = self.optional_params

        output_parse_pii: bool | None | Unset
        if isinstance(self.output_parse_pii, Unset):
            output_parse_pii = UNSET
        else:
            output_parse_pii = self.output_parse_pii

        pangea_input_recipe: None | str | Unset
        if isinstance(self.pangea_input_recipe, Unset):
            pangea_input_recipe = UNSET
        else:
            pangea_input_recipe = self.pangea_input_recipe

        pangea_output_recipe: None | str | Unset
        if isinstance(self.pangea_output_recipe, Unset):
            pangea_output_recipe = UNSET
        else:
            pangea_output_recipe = self.pangea_output_recipe

        pattern_redaction_format: None | str | Unset
        if isinstance(self.pattern_redaction_format, Unset):
            pattern_redaction_format = UNSET
        else:
            pattern_redaction_format = self.pattern_redaction_format

        patterns: list[dict[str, Any]] | None | Unset
        if isinstance(self.patterns, Unset):
            patterns = UNSET
        elif isinstance(self.patterns, list):
            patterns = []
            for patterns_type_0_item_data in self.patterns:
                patterns_type_0_item = patterns_type_0_item_data.to_dict()
                patterns.append(patterns_type_0_item)


        else:
            patterns = self.patterns

        payload: bool | None | Unset
        if isinstance(self.payload, Unset):
            payload = UNSET
        else:
            payload = self.payload

        persist_session: bool | None | Unset
        if isinstance(self.persist_session, Unset):
            persist_session = UNSET
        else:
            persist_session = self.persist_session

        pii_check: bool | None | Unset
        if isinstance(self.pii_check, Unset):
            pii_check = UNSET
        else:
            pii_check = self.pii_check

        pii_entities_config: dict[str, Any] | None | Unset
        if isinstance(self.pii_entities_config, Unset):
            pii_entities_config = UNSET
        elif isinstance(self.pii_entities_config, LitellmParamsPiiEntitiesConfigType0):
            pii_entities_config = self.pii_entities_config.to_dict()
        else:
            pii_entities_config = self.pii_entities_config

        policy_id: int | None | Unset
        if isinstance(self.policy_id, Unset):
            policy_id = UNSET
        else:
            policy_id = self.policy_id

        policy_name: None | str | Unset
        if isinstance(self.policy_name, Unset):
            policy_name = UNSET
        else:
            policy_name = self.policy_name

        policy_names: list[str] | None | Unset
        if isinstance(self.policy_names, Unset):
            policy_names = UNSET
        elif isinstance(self.policy_names, list):
            policy_names = self.policy_names


        else:
            policy_names = self.policy_names

        presidio_ad_hoc_recognizers: None | str | Unset
        if isinstance(self.presidio_ad_hoc_recognizers, Unset):
            presidio_ad_hoc_recognizers = UNSET
        else:
            presidio_ad_hoc_recognizers = self.presidio_ad_hoc_recognizers

        presidio_analyzer_api_base: None | str | Unset
        if isinstance(self.presidio_analyzer_api_base, Unset):
            presidio_analyzer_api_base = UNSET
        else:
            presidio_analyzer_api_base = self.presidio_analyzer_api_base

        presidio_anonymizer_api_base: None | str | Unset
        if isinstance(self.presidio_anonymizer_api_base, Unset):
            presidio_anonymizer_api_base = UNSET
        else:
            presidio_anonymizer_api_base = self.presidio_anonymizer_api_base

        presidio_entities_deny_list: list[str] | None | Unset
        if isinstance(self.presidio_entities_deny_list, Unset):
            presidio_entities_deny_list = UNSET
        elif isinstance(self.presidio_entities_deny_list, list):
            presidio_entities_deny_list = []
            for presidio_entities_deny_list_type_0_item_data in self.presidio_entities_deny_list:
                presidio_entities_deny_list_type_0_item: str
                if isinstance(presidio_entities_deny_list_type_0_item_data, PiiEntityType):
                    presidio_entities_deny_list_type_0_item = presidio_entities_deny_list_type_0_item_data.value
                else:
                    presidio_entities_deny_list_type_0_item = presidio_entities_deny_list_type_0_item_data
                presidio_entities_deny_list.append(presidio_entities_deny_list_type_0_item)


        else:
            presidio_entities_deny_list = self.presidio_entities_deny_list

        presidio_filter_scope: None | str | Unset
        if isinstance(self.presidio_filter_scope, Unset):
            presidio_filter_scope = UNSET
        elif isinstance(self.presidio_filter_scope, LitellmParamsPresidioFilterScopeType0):
            presidio_filter_scope = self.presidio_filter_scope.value
        else:
            presidio_filter_scope = self.presidio_filter_scope

        presidio_language: None | str | Unset
        if isinstance(self.presidio_language, Unset):
            presidio_language = UNSET
        else:
            presidio_language = self.presidio_language

        presidio_run_on: None | str | Unset
        if isinstance(self.presidio_run_on, Unset):
            presidio_run_on = UNSET
        elif isinstance(self.presidio_run_on, LitellmParamsPresidioRunOnType0):
            presidio_run_on = self.presidio_run_on.value
        else:
            presidio_run_on = self.presidio_run_on

        presidio_score_thresholds: dict[str, Any] | None | Unset
        if isinstance(self.presidio_score_thresholds, Unset):
            presidio_score_thresholds = UNSET
        elif isinstance(self.presidio_score_thresholds, LitellmParamsPresidioScoreThresholdsType0):
            presidio_score_thresholds = self.presidio_score_thresholds.to_dict()
        else:
            presidio_score_thresholds = self.presidio_score_thresholds

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        prompt_injections: bool | None | Unset
        if isinstance(self.prompt_injections, Unset):
            prompt_injections = UNSET
        else:
            prompt_injections = self.prompt_injections

        realtime_violation_message: None | str | Unset
        if isinstance(self.realtime_violation_message, Unset):
            realtime_violation_message = UNSET
        else:
            realtime_violation_message = self.realtime_violation_message

        rules: list[dict[str, Any]] | None | Unset
        if isinstance(self.rules, Unset):
            rules = UNSET
        elif isinstance(self.rules, list):
            rules = []
            for rules_type_0_item_data in self.rules:
                rules_type_0_item = rules_type_0_item_data.to_dict()
                rules.append(rules_type_0_item)


        else:
            rules = self.rules

        send_user_api_key_alias: bool | None | Unset
        if isinstance(self.send_user_api_key_alias, Unset):
            send_user_api_key_alias = UNSET
        else:
            send_user_api_key_alias = self.send_user_api_key_alias

        send_user_api_key_team_id: bool | None | Unset
        if isinstance(self.send_user_api_key_team_id, Unset):
            send_user_api_key_team_id = UNSET
        else:
            send_user_api_key_team_id = self.send_user_api_key_team_id

        send_user_api_key_user_id: bool | None | Unset
        if isinstance(self.send_user_api_key_user_id, Unset):
            send_user_api_key_user_id = UNSET
        else:
            send_user_api_key_user_id = self.send_user_api_key_user_id

        severity_threshold: None | str | Unset
        if isinstance(self.severity_threshold, Unset):
            severity_threshold = UNSET
        else:
            severity_threshold = self.severity_threshold

        skip_system_message_in_guardrail: bool | None | Unset
        if isinstance(self.skip_system_message_in_guardrail, Unset):
            skip_system_message_in_guardrail = UNSET
        else:
            skip_system_message_in_guardrail = self.skip_system_message_in_guardrail

        template_id: None | str | Unset
        if isinstance(self.template_id, Unset):
            template_id = UNSET
        else:
            template_id = self.template_id

        tool_selection_quality_check: bool | None | Unset
        if isinstance(self.tool_selection_quality_check, Unset):
            tool_selection_quality_check = UNSET
        else:
            tool_selection_quality_check = self.tool_selection_quality_check

        unreachable_fallback: str | Unset = UNSET
        if not isinstance(self.unreachable_fallback, Unset):
            unreachable_fallback = self.unreachable_fallback.value


        use_v2: bool | None | Unset
        if isinstance(self.use_v2, Unset):
            use_v2 = UNSET
        else:
            use_v2 = self.use_v2

        verify_ssl: bool | None | Unset
        if isinstance(self.verify_ssl, Unset):
            verify_ssl = UNSET
        else:
            verify_ssl = self.verify_ssl

        version: int | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        violation_message_template: None | str | Unset
        if isinstance(self.violation_message_template, Unset):
            violation_message_template = UNSET
        else:
            violation_message_template = self.violation_message_template

        xecguard_model: None | str | Unset
        if isinstance(self.xecguard_model, Unset):
            xecguard_model = UNSET
        else:
            xecguard_model = self.xecguard_model


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "guardrail": guardrail,
            "mode": mode,
        })
        if action is not UNSET:
            field_dict["action"] = action
        if additional_provider_specific_params is not UNSET:
            field_dict["additional_provider_specific_params"] = additional_provider_specific_params
        if akto_account_id is not UNSET:
            field_dict["akto_account_id"] = akto_account_id
        if akto_api_key is not UNSET:
            field_dict["akto_api_key"] = akto_api_key
        if akto_base_url is not UNSET:
            field_dict["akto_base_url"] = akto_base_url
        if akto_vxlan_id is not UNSET:
            field_dict["akto_vxlan_id"] = akto_vxlan_id
        if anonymize_input is not UNSET:
            field_dict["anonymize_input"] = anonymize_input
        if api_base is not UNSET:
            field_dict["api_base"] = api_base
        if api_endpoint is not UNSET:
            field_dict["api_endpoint"] = api_endpoint
        if api_id is not UNSET:
            field_dict["api_id"] = api_id
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if api_version is not UNSET:
            field_dict["api_version"] = api_version
        if application is not UNSET:
            field_dict["application"] = application
        if application_id is not UNSET:
            field_dict["application_id"] = application_id
        if assertions is not UNSET:
            field_dict["assertions"] = assertions
        if async_mode is not UNSET:
            field_dict["async_mode"] = async_mode
        if auth_token is not UNSET:
            field_dict["auth_token"] = auth_token
        if aws_access_key_id is not UNSET:
            field_dict["aws_access_key_id"] = aws_access_key_id
        if aws_bedrock_runtime_endpoint is not UNSET:
            field_dict["aws_bedrock_runtime_endpoint"] = aws_bedrock_runtime_endpoint
        if aws_profile_name is not UNSET:
            field_dict["aws_profile_name"] = aws_profile_name
        if aws_region_name is not UNSET:
            field_dict["aws_region_name"] = aws_region_name
        if aws_role_name is not UNSET:
            field_dict["aws_role_name"] = aws_role_name
        if aws_secret_access_key is not UNSET:
            field_dict["aws_secret_access_key"] = aws_secret_access_key
        if aws_session_name is not UNSET:
            field_dict["aws_session_name"] = aws_session_name
        if aws_session_token is not UNSET:
            field_dict["aws_session_token"] = aws_session_token
        if aws_sts_endpoint is not UNSET:
            field_dict["aws_sts_endpoint"] = aws_sts_endpoint
        if aws_web_identity_token is not UNSET:
            field_dict["aws_web_identity_token"] = aws_web_identity_token
        if base_url is not UNSET:
            field_dict["base_url"] = base_url
        if block_failures is not UNSET:
            field_dict["block_failures"] = block_failures
        if block_on_error is not UNSET:
            field_dict["block_on_error"] = block_on_error
        if block_on_violation is not UNSET:
            field_dict["block_on_violation"] = block_on_violation
        if blocked_languages is not UNSET:
            field_dict["blocked_languages"] = blocked_languages
        if blocked_words is not UNSET:
            field_dict["blocked_words"] = blocked_words
        if blocked_words_file is not UNSET:
            field_dict["blocked_words_file"] = blocked_words_file
        if breakdown is not UNSET:
            field_dict["breakdown"] = breakdown
        if categories is not UNSET:
            field_dict["categories"] = categories
        if category_thresholds is not UNSET:
            field_dict["category_thresholds"] = category_thresholds
        if confidence_threshold is not UNSET:
            field_dict["confidence_threshold"] = confidence_threshold
        if config is not UNSET:
            field_dict["config"] = config
        if content_moderation_check is not UNSET:
            field_dict["content_moderation_check"] = content_moderation_check
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if custom_code is not UNSET:
            field_dict["custom_code"] = custom_code
        if default_action is not UNSET:
            field_dict["default_action"] = default_action
        if default_on is not UNSET:
            field_dict["default_on"] = default_on
        if deployment_name is not UNSET:
            field_dict["deployment_name"] = deployment_name
        if detect_execution_intent is not UNSET:
            field_dict["detect_execution_intent"] = detect_execution_intent
        if detect_secrets_config is not UNSET:
            field_dict["detect_secrets_config"] = detect_secrets_config
        if detector_id is not UNSET:
            field_dict["detector_id"] = detector_id
        if detectors is not UNSET:
            field_dict["detectors"] = detectors
        if dev_info is not UNSET:
            field_dict["dev_info"] = dev_info
        if disable_exception_on_block is not UNSET:
            field_dict["disable_exception_on_block"] = disable_exception_on_block
        if end_session_after_n_fails is not UNSET:
            field_dict["end_session_after_n_fails"] = end_session_after_n_fails
        if evaluation_id is not UNSET:
            field_dict["evaluation_id"] = evaluation_id
        if experimental_use_latest_role_message_only is not UNSET:
            field_dict["experimental_use_latest_role_message_only"] = experimental_use_latest_role_message_only
        if extra_headers is not UNSET:
            field_dict["extra_headers"] = extra_headers
        if fail_on_error is not UNSET:
            field_dict["fail_on_error"] = fail_on_error
        if grounding_check is not UNSET:
            field_dict["grounding_check"] = grounding_check
        if grounding_strictness is not UNSET:
            field_dict["grounding_strictness"] = grounding_strictness
        if guard_name is not UNSET:
            field_dict["guard_name"] = guard_name
        if guardrail_identifier is not UNSET:
            field_dict["guardrailIdentifier"] = guardrail_identifier
        if guardrail_version is not UNSET:
            field_dict["guardrailVersion"] = guardrail_version
        if guardrail_timeout is not UNSET:
            field_dict["guardrail_timeout"] = guardrail_timeout
        if hallucinations_check is not UNSET:
            field_dict["hallucinations_check"] = hallucinations_check
        if include_evidence is not UNSET:
            field_dict["include_evidence"] = include_evidence
        if include_scanners is not UNSET:
            field_dict["include_scanners"] = include_scanners
        if is_detector_server is not UNSET:
            field_dict["is_detector_server"] = is_detector_server
        if keyword_redaction_tag is not UNSET:
            field_dict["keyword_redaction_tag"] = keyword_redaction_tag
        if lasso_conversation_id is not UNSET:
            field_dict["lasso_conversation_id"] = lasso_conversation_id
        if lasso_user_id is not UNSET:
            field_dict["lasso_user_id"] = lasso_user_id
        if location is not UNSET:
            field_dict["location"] = location
        if mask is not UNSET:
            field_dict["mask"] = mask
        if mask_request_content is not UNSET:
            field_dict["mask_request_content"] = mask_request_content
        if mask_response_content is not UNSET:
            field_dict["mask_response_content"] = mask_response_content
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if mock_redacted_text is not UNSET:
            field_dict["mock_redacted_text"] = mock_redacted_text
        if model is not UNSET:
            field_dict["model"] = model
        if monitor_mode is not UNSET:
            field_dict["monitor_mode"] = monitor_mode
        if on_disallowed_action is not UNSET:
            field_dict["on_disallowed_action"] = on_disallowed_action
        if on_flagged is not UNSET:
            field_dict["on_flagged"] = on_flagged
        if on_flagged_action is not UNSET:
            field_dict["on_flagged_action"] = on_flagged_action
        if on_violation is not UNSET:
            field_dict["on_violation"] = on_violation
        if optional_params is not UNSET:
            field_dict["optional_params"] = optional_params
        if output_parse_pii is not UNSET:
            field_dict["output_parse_pii"] = output_parse_pii
        if pangea_input_recipe is not UNSET:
            field_dict["pangea_input_recipe"] = pangea_input_recipe
        if pangea_output_recipe is not UNSET:
            field_dict["pangea_output_recipe"] = pangea_output_recipe
        if pattern_redaction_format is not UNSET:
            field_dict["pattern_redaction_format"] = pattern_redaction_format
        if patterns is not UNSET:
            field_dict["patterns"] = patterns
        if payload is not UNSET:
            field_dict["payload"] = payload
        if persist_session is not UNSET:
            field_dict["persist_session"] = persist_session
        if pii_check is not UNSET:
            field_dict["pii_check"] = pii_check
        if pii_entities_config is not UNSET:
            field_dict["pii_entities_config"] = pii_entities_config
        if policy_id is not UNSET:
            field_dict["policy_id"] = policy_id
        if policy_name is not UNSET:
            field_dict["policy_name"] = policy_name
        if policy_names is not UNSET:
            field_dict["policy_names"] = policy_names
        if presidio_ad_hoc_recognizers is not UNSET:
            field_dict["presidio_ad_hoc_recognizers"] = presidio_ad_hoc_recognizers
        if presidio_analyzer_api_base is not UNSET:
            field_dict["presidio_analyzer_api_base"] = presidio_analyzer_api_base
        if presidio_anonymizer_api_base is not UNSET:
            field_dict["presidio_anonymizer_api_base"] = presidio_anonymizer_api_base
        if presidio_entities_deny_list is not UNSET:
            field_dict["presidio_entities_deny_list"] = presidio_entities_deny_list
        if presidio_filter_scope is not UNSET:
            field_dict["presidio_filter_scope"] = presidio_filter_scope
        if presidio_language is not UNSET:
            field_dict["presidio_language"] = presidio_language
        if presidio_run_on is not UNSET:
            field_dict["presidio_run_on"] = presidio_run_on
        if presidio_score_thresholds is not UNSET:
            field_dict["presidio_score_thresholds"] = presidio_score_thresholds
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if prompt_injections is not UNSET:
            field_dict["prompt_injections"] = prompt_injections
        if realtime_violation_message is not UNSET:
            field_dict["realtime_violation_message"] = realtime_violation_message
        if rules is not UNSET:
            field_dict["rules"] = rules
        if send_user_api_key_alias is not UNSET:
            field_dict["send_user_api_key_alias"] = send_user_api_key_alias
        if send_user_api_key_team_id is not UNSET:
            field_dict["send_user_api_key_team_id"] = send_user_api_key_team_id
        if send_user_api_key_user_id is not UNSET:
            field_dict["send_user_api_key_user_id"] = send_user_api_key_user_id
        if severity_threshold is not UNSET:
            field_dict["severity_threshold"] = severity_threshold
        if skip_system_message_in_guardrail is not UNSET:
            field_dict["skip_system_message_in_guardrail"] = skip_system_message_in_guardrail
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if tool_selection_quality_check is not UNSET:
            field_dict["tool_selection_quality_check"] = tool_selection_quality_check
        if unreachable_fallback is not UNSET:
            field_dict["unreachable_fallback"] = unreachable_fallback
        if use_v2 is not UNSET:
            field_dict["use_v2"] = use_v2
        if verify_ssl is not UNSET:
            field_dict["verify_ssl"] = verify_ssl
        if version is not UNSET:
            field_dict["version"] = version
        if violation_message_template is not UNSET:
            field_dict["violation_message_template"] = violation_message_template
        if xecguard_model is not UNSET:
            field_dict["xecguard_model"] = xecguard_model

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.blocked_word import BlockedWord
        from ..models.content_filter_category_config import ContentFilterCategoryConfig
        from ..models.content_filter_pattern import ContentFilterPattern
        from ..models.gray_swan_guardrail_config_model_optional_params import GraySwanGuardrailConfigModelOptionalParams
        from ..models.lakera_category_thresholds import LakeraCategoryThresholds
        from ..models.litellm_params_additional_provider_specific_params_type_0 import LitellmParamsAdditionalProviderSpecificParamsType0
        from ..models.litellm_params_config_type_0 import LitellmParamsConfigType0
        from ..models.litellm_params_detect_secrets_config_type_0 import LitellmParamsDetectSecretsConfigType0
        from ..models.litellm_params_detectors_type_0 import LitellmParamsDetectorsType0
        from ..models.litellm_params_metadata_type_0 import LitellmParamsMetadataType0
        from ..models.litellm_params_mock_redacted_text_type_0 import LitellmParamsMockRedactedTextType0
        from ..models.litellm_params_pii_entities_config_type_0 import LitellmParamsPiiEntitiesConfigType0
        from ..models.litellm_params_presidio_score_thresholds_type_0 import LitellmParamsPresidioScoreThresholdsType0
        from ..models.mode import Mode
        from ..models.tool_permission_rule import ToolPermissionRule
        d = dict(src_dict)
        guardrail = d.pop("guardrail")

        def _parse_mode(data: object) -> list[str] | Mode | str:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mode_type_1 = cast(list[str], data)

                return mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mode_type_2 = Mode.from_dict(data)



                return mode_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | Mode | str, data)

        mode = _parse_mode(d.pop("mode"))


        _action = d.pop("action", UNSET)
        action: LitellmParamsAction | Unset
        if isinstance(_action,  Unset):
            action = UNSET
        else:
            action = LitellmParamsAction(_action)




        def _parse_additional_provider_specific_params(data: object) -> LitellmParamsAdditionalProviderSpecificParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_provider_specific_params_type_0 = LitellmParamsAdditionalProviderSpecificParamsType0.from_dict(data)



                return additional_provider_specific_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LitellmParamsAdditionalProviderSpecificParamsType0 | None | Unset, data)

        additional_provider_specific_params = _parse_additional_provider_specific_params(d.pop("additional_provider_specific_params", UNSET))


        def _parse_akto_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        akto_account_id = _parse_akto_account_id(d.pop("akto_account_id", UNSET))


        def _parse_akto_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        akto_api_key = _parse_akto_api_key(d.pop("akto_api_key", UNSET))


        def _parse_akto_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        akto_base_url = _parse_akto_base_url(d.pop("akto_base_url", UNSET))


        def _parse_akto_vxlan_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        akto_vxlan_id = _parse_akto_vxlan_id(d.pop("akto_vxlan_id", UNSET))


        def _parse_anonymize_input(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        anonymize_input = _parse_anonymize_input(d.pop("anonymize_input", UNSET))


        def _parse_api_base(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_base = _parse_api_base(d.pop("api_base", UNSET))


        def _parse_api_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_endpoint = _parse_api_endpoint(d.pop("api_endpoint", UNSET))


        def _parse_api_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_id = _parse_api_id(d.pop("api_id", UNSET))


        def _parse_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))


        def _parse_api_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_version = _parse_api_version(d.pop("api_version", UNSET))


        def _parse_application(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application = _parse_application(d.pop("application", UNSET))


        def _parse_application_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_id = _parse_application_id(d.pop("application_id", UNSET))


        def _parse_assertions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assertions_type_0 = cast(list[str], data)

                return assertions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        assertions = _parse_assertions(d.pop("assertions", UNSET))


        def _parse_async_mode(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        async_mode = _parse_async_mode(d.pop("async_mode", UNSET))


        def _parse_auth_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auth_token = _parse_auth_token(d.pop("auth_token", UNSET))


        def _parse_aws_access_key_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_access_key_id = _parse_aws_access_key_id(d.pop("aws_access_key_id", UNSET))


        def _parse_aws_bedrock_runtime_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_bedrock_runtime_endpoint = _parse_aws_bedrock_runtime_endpoint(d.pop("aws_bedrock_runtime_endpoint", UNSET))


        def _parse_aws_profile_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_profile_name = _parse_aws_profile_name(d.pop("aws_profile_name", UNSET))


        def _parse_aws_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_region_name = _parse_aws_region_name(d.pop("aws_region_name", UNSET))


        def _parse_aws_role_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_role_name = _parse_aws_role_name(d.pop("aws_role_name", UNSET))


        def _parse_aws_secret_access_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_secret_access_key = _parse_aws_secret_access_key(d.pop("aws_secret_access_key", UNSET))


        def _parse_aws_session_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_session_name = _parse_aws_session_name(d.pop("aws_session_name", UNSET))


        def _parse_aws_session_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_session_token = _parse_aws_session_token(d.pop("aws_session_token", UNSET))


        def _parse_aws_sts_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_sts_endpoint = _parse_aws_sts_endpoint(d.pop("aws_sts_endpoint", UNSET))


        def _parse_aws_web_identity_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_web_identity_token = _parse_aws_web_identity_token(d.pop("aws_web_identity_token", UNSET))


        def _parse_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_url = _parse_base_url(d.pop("base_url", UNSET))


        def _parse_block_failures(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        block_failures = _parse_block_failures(d.pop("block_failures", UNSET))


        def _parse_block_on_error(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        block_on_error = _parse_block_on_error(d.pop("block_on_error", UNSET))


        def _parse_block_on_violation(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        block_on_violation = _parse_block_on_violation(d.pop("block_on_violation", UNSET))


        def _parse_blocked_languages(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blocked_languages_type_0 = cast(list[str], data)

                return blocked_languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        blocked_languages = _parse_blocked_languages(d.pop("blocked_languages", UNSET))


        def _parse_blocked_words(data: object) -> list[BlockedWord] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blocked_words_type_0 = []
                _blocked_words_type_0 = data
                for blocked_words_type_0_item_data in (_blocked_words_type_0):
                    blocked_words_type_0_item = BlockedWord.from_dict(blocked_words_type_0_item_data)



                    blocked_words_type_0.append(blocked_words_type_0_item)

                return blocked_words_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BlockedWord] | None | Unset, data)

        blocked_words = _parse_blocked_words(d.pop("blocked_words", UNSET))


        def _parse_blocked_words_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        blocked_words_file = _parse_blocked_words_file(d.pop("blocked_words_file", UNSET))


        def _parse_breakdown(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        breakdown = _parse_breakdown(d.pop("breakdown", UNSET))


        def _parse_categories(data: object) -> list[ContentFilterCategoryConfig] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = []
                _categories_type_0 = data
                for categories_type_0_item_data in (_categories_type_0):
                    categories_type_0_item = ContentFilterCategoryConfig.from_dict(categories_type_0_item_data)



                    categories_type_0.append(categories_type_0_item)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContentFilterCategoryConfig] | None | Unset, data)

        categories = _parse_categories(d.pop("categories", UNSET))


        def _parse_category_thresholds(data: object) -> LakeraCategoryThresholds | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                category_thresholds_type_0 = LakeraCategoryThresholds.from_dict(data)



                return category_thresholds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LakeraCategoryThresholds | None | Unset, data)

        category_thresholds = _parse_category_thresholds(d.pop("category_thresholds", UNSET))


        confidence_threshold = d.pop("confidence_threshold", UNSET)

        def _parse_config(data: object) -> LitellmParamsConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = LitellmParamsConfigType0.from_dict(data)



                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LitellmParamsConfigType0 | None | Unset, data)

        config = _parse_config(d.pop("config", UNSET))


        def _parse_content_moderation_check(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        content_moderation_check = _parse_content_moderation_check(d.pop("content_moderation_check", UNSET))


        def _parse_credentials(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        credentials = _parse_credentials(d.pop("credentials", UNSET))


        def _parse_custom_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_code = _parse_custom_code(d.pop("custom_code", UNSET))


        _default_action = d.pop("default_action", UNSET)
        default_action: LitellmParamsDefaultAction | Unset
        if isinstance(_default_action,  Unset):
            default_action = UNSET
        else:
            default_action = LitellmParamsDefaultAction(_default_action)




        def _parse_default_on(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        default_on = _parse_default_on(d.pop("default_on", UNSET))


        def _parse_deployment_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deployment_name = _parse_deployment_name(d.pop("deployment_name", UNSET))


        detect_execution_intent = d.pop("detect_execution_intent", UNSET)

        def _parse_detect_secrets_config(data: object) -> LitellmParamsDetectSecretsConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                detect_secrets_config_type_0 = LitellmParamsDetectSecretsConfigType0.from_dict(data)



                return detect_secrets_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LitellmParamsDetectSecretsConfigType0 | None | Unset, data)

        detect_secrets_config = _parse_detect_secrets_config(d.pop("detect_secrets_config", UNSET))


        def _parse_detector_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detector_id = _parse_detector_id(d.pop("detector_id", UNSET))


        def _parse_detectors(data: object) -> LitellmParamsDetectorsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                detectors_type_0 = LitellmParamsDetectorsType0.from_dict(data)



                return detectors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LitellmParamsDetectorsType0 | None | Unset, data)

        detectors = _parse_detectors(d.pop("detectors", UNSET))


        def _parse_dev_info(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        dev_info = _parse_dev_info(d.pop("dev_info", UNSET))


        def _parse_disable_exception_on_block(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        disable_exception_on_block = _parse_disable_exception_on_block(d.pop("disable_exception_on_block", UNSET))


        def _parse_end_session_after_n_fails(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        end_session_after_n_fails = _parse_end_session_after_n_fails(d.pop("end_session_after_n_fails", UNSET))


        def _parse_evaluation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        evaluation_id = _parse_evaluation_id(d.pop("evaluation_id", UNSET))


        def _parse_experimental_use_latest_role_message_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        experimental_use_latest_role_message_only = _parse_experimental_use_latest_role_message_only(d.pop("experimental_use_latest_role_message_only", UNSET))


        def _parse_extra_headers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                extra_headers_type_0 = cast(list[str], data)

                return extra_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        extra_headers = _parse_extra_headers(d.pop("extra_headers", UNSET))


        def _parse_fail_on_error(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        fail_on_error = _parse_fail_on_error(d.pop("fail_on_error", UNSET))


        def _parse_grounding_check(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        grounding_check = _parse_grounding_check(d.pop("grounding_check", UNSET))


        def _parse_grounding_strictness(data: object) -> LitellmParamsGroundingStrictnessType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                grounding_strictness_type_0 = LitellmParamsGroundingStrictnessType0(data)



                return grounding_strictness_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LitellmParamsGroundingStrictnessType0 | None | Unset, data)

        grounding_strictness = _parse_grounding_strictness(d.pop("grounding_strictness", UNSET))


        def _parse_guard_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guard_name = _parse_guard_name(d.pop("guard_name", UNSET))


        def _parse_guardrail_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guardrail_identifier = _parse_guardrail_identifier(d.pop("guardrailIdentifier", UNSET))


        def _parse_guardrail_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guardrail_version = _parse_guardrail_version(d.pop("guardrailVersion", UNSET))


        def _parse_guardrail_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        guardrail_timeout = _parse_guardrail_timeout(d.pop("guardrail_timeout", UNSET))


        def _parse_hallucinations_check(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hallucinations_check = _parse_hallucinations_check(d.pop("hallucinations_check", UNSET))


        def _parse_include_evidence(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_evidence = _parse_include_evidence(d.pop("include_evidence", UNSET))


        def _parse_include_scanners(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_scanners = _parse_include_scanners(d.pop("include_scanners", UNSET))


        def _parse_is_detector_server(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_detector_server = _parse_is_detector_server(d.pop("is_detector_server", UNSET))


        def _parse_keyword_redaction_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keyword_redaction_tag = _parse_keyword_redaction_tag(d.pop("keyword_redaction_tag", UNSET))


        def _parse_lasso_conversation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lasso_conversation_id = _parse_lasso_conversation_id(d.pop("lasso_conversation_id", UNSET))


        def _parse_lasso_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lasso_user_id = _parse_lasso_user_id(d.pop("lasso_user_id", UNSET))


        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))


        def _parse_mask(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        mask = _parse_mask(d.pop("mask", UNSET))


        def _parse_mask_request_content(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        mask_request_content = _parse_mask_request_content(d.pop("mask_request_content", UNSET))


        def _parse_mask_response_content(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        mask_response_content = _parse_mask_response_content(d.pop("mask_response_content", UNSET))


        def _parse_metadata(data: object) -> LitellmParamsMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = LitellmParamsMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LitellmParamsMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        def _parse_mock_redacted_text(data: object) -> LitellmParamsMockRedactedTextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mock_redacted_text_type_0 = LitellmParamsMockRedactedTextType0.from_dict(data)



                return mock_redacted_text_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LitellmParamsMockRedactedTextType0 | None | Unset, data)

        mock_redacted_text = _parse_mock_redacted_text(d.pop("mock_redacted_text", UNSET))


        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        def _parse_monitor_mode(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        monitor_mode = _parse_monitor_mode(d.pop("monitor_mode", UNSET))


        _on_disallowed_action = d.pop("on_disallowed_action", UNSET)
        on_disallowed_action: LitellmParamsOnDisallowedAction | Unset
        if isinstance(_on_disallowed_action,  Unset):
            on_disallowed_action = UNSET
        else:
            on_disallowed_action = LitellmParamsOnDisallowedAction(_on_disallowed_action)




        def _parse_on_flagged(data: object) -> LitellmParamsOnFlaggedType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                on_flagged_type_0 = LitellmParamsOnFlaggedType0(data)



                return on_flagged_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LitellmParamsOnFlaggedType0 | None | Unset, data)

        on_flagged = _parse_on_flagged(d.pop("on_flagged", UNSET))


        def _parse_on_flagged_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        on_flagged_action = _parse_on_flagged_action(d.pop("on_flagged_action", UNSET))


        def _parse_on_violation(data: object) -> LitellmParamsOnViolationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                on_violation_type_0 = LitellmParamsOnViolationType0(data)



                return on_violation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LitellmParamsOnViolationType0 | None | Unset, data)

        on_violation = _parse_on_violation(d.pop("on_violation", UNSET))


        def _parse_optional_params(data: object) -> GraySwanGuardrailConfigModelOptionalParams | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                optional_params_type_0 = GraySwanGuardrailConfigModelOptionalParams.from_dict(data)



                return optional_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GraySwanGuardrailConfigModelOptionalParams | None | Unset, data)

        optional_params = _parse_optional_params(d.pop("optional_params", UNSET))


        def _parse_output_parse_pii(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        output_parse_pii = _parse_output_parse_pii(d.pop("output_parse_pii", UNSET))


        def _parse_pangea_input_recipe(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pangea_input_recipe = _parse_pangea_input_recipe(d.pop("pangea_input_recipe", UNSET))


        def _parse_pangea_output_recipe(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pangea_output_recipe = _parse_pangea_output_recipe(d.pop("pangea_output_recipe", UNSET))


        def _parse_pattern_redaction_format(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pattern_redaction_format = _parse_pattern_redaction_format(d.pop("pattern_redaction_format", UNSET))


        def _parse_patterns(data: object) -> list[ContentFilterPattern] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                patterns_type_0 = []
                _patterns_type_0 = data
                for patterns_type_0_item_data in (_patterns_type_0):
                    patterns_type_0_item = ContentFilterPattern.from_dict(patterns_type_0_item_data)



                    patterns_type_0.append(patterns_type_0_item)

                return patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContentFilterPattern] | None | Unset, data)

        patterns = _parse_patterns(d.pop("patterns", UNSET))


        def _parse_payload(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        payload = _parse_payload(d.pop("payload", UNSET))


        def _parse_persist_session(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        persist_session = _parse_persist_session(d.pop("persist_session", UNSET))


        def _parse_pii_check(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        pii_check = _parse_pii_check(d.pop("pii_check", UNSET))


        def _parse_pii_entities_config(data: object) -> LitellmParamsPiiEntitiesConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pii_entities_config_type_0 = LitellmParamsPiiEntitiesConfigType0.from_dict(data)



                return pii_entities_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LitellmParamsPiiEntitiesConfigType0 | None | Unset, data)

        pii_entities_config = _parse_pii_entities_config(d.pop("pii_entities_config", UNSET))


        def _parse_policy_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        policy_id = _parse_policy_id(d.pop("policy_id", UNSET))


        def _parse_policy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_name = _parse_policy_name(d.pop("policy_name", UNSET))


        def _parse_policy_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                policy_names_type_0 = cast(list[str], data)

                return policy_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        policy_names = _parse_policy_names(d.pop("policy_names", UNSET))


        def _parse_presidio_ad_hoc_recognizers(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        presidio_ad_hoc_recognizers = _parse_presidio_ad_hoc_recognizers(d.pop("presidio_ad_hoc_recognizers", UNSET))


        def _parse_presidio_analyzer_api_base(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        presidio_analyzer_api_base = _parse_presidio_analyzer_api_base(d.pop("presidio_analyzer_api_base", UNSET))


        def _parse_presidio_anonymizer_api_base(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        presidio_anonymizer_api_base = _parse_presidio_anonymizer_api_base(d.pop("presidio_anonymizer_api_base", UNSET))


        def _parse_presidio_entities_deny_list(data: object) -> list[PiiEntityType | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                presidio_entities_deny_list_type_0 = []
                _presidio_entities_deny_list_type_0 = data
                for presidio_entities_deny_list_type_0_item_data in (_presidio_entities_deny_list_type_0):
                    def _parse_presidio_entities_deny_list_type_0_item(data: object) -> PiiEntityType | str:
                        try:
                            if not isinstance(data, str):
                                raise TypeError()
                            presidio_entities_deny_list_type_0_item_type_0 = PiiEntityType(data)



                            return presidio_entities_deny_list_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(PiiEntityType | str, data)

                    presidio_entities_deny_list_type_0_item = _parse_presidio_entities_deny_list_type_0_item(presidio_entities_deny_list_type_0_item_data)

                    presidio_entities_deny_list_type_0.append(presidio_entities_deny_list_type_0_item)

                return presidio_entities_deny_list_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PiiEntityType | str] | None | Unset, data)

        presidio_entities_deny_list = _parse_presidio_entities_deny_list(d.pop("presidio_entities_deny_list", UNSET))


        def _parse_presidio_filter_scope(data: object) -> LitellmParamsPresidioFilterScopeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                presidio_filter_scope_type_0 = LitellmParamsPresidioFilterScopeType0(data)



                return presidio_filter_scope_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LitellmParamsPresidioFilterScopeType0 | None | Unset, data)

        presidio_filter_scope = _parse_presidio_filter_scope(d.pop("presidio_filter_scope", UNSET))


        def _parse_presidio_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        presidio_language = _parse_presidio_language(d.pop("presidio_language", UNSET))


        def _parse_presidio_run_on(data: object) -> LitellmParamsPresidioRunOnType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                presidio_run_on_type_0 = LitellmParamsPresidioRunOnType0(data)



                return presidio_run_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LitellmParamsPresidioRunOnType0 | None | Unset, data)

        presidio_run_on = _parse_presidio_run_on(d.pop("presidio_run_on", UNSET))


        def _parse_presidio_score_thresholds(data: object) -> LitellmParamsPresidioScoreThresholdsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                presidio_score_thresholds_type_0 = LitellmParamsPresidioScoreThresholdsType0.from_dict(data)



                return presidio_score_thresholds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LitellmParamsPresidioScoreThresholdsType0 | None | Unset, data)

        presidio_score_thresholds = _parse_presidio_score_thresholds(d.pop("presidio_score_thresholds", UNSET))


        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        def _parse_prompt_injections(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        prompt_injections = _parse_prompt_injections(d.pop("prompt_injections", UNSET))


        def _parse_realtime_violation_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        realtime_violation_message = _parse_realtime_violation_message(d.pop("realtime_violation_message", UNSET))


        def _parse_rules(data: object) -> list[ToolPermissionRule] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rules_type_0 = []
                _rules_type_0 = data
                for rules_type_0_item_data in (_rules_type_0):
                    rules_type_0_item = ToolPermissionRule.from_dict(rules_type_0_item_data)



                    rules_type_0.append(rules_type_0_item)

                return rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ToolPermissionRule] | None | Unset, data)

        rules = _parse_rules(d.pop("rules", UNSET))


        def _parse_send_user_api_key_alias(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        send_user_api_key_alias = _parse_send_user_api_key_alias(d.pop("send_user_api_key_alias", UNSET))


        def _parse_send_user_api_key_team_id(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        send_user_api_key_team_id = _parse_send_user_api_key_team_id(d.pop("send_user_api_key_team_id", UNSET))


        def _parse_send_user_api_key_user_id(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        send_user_api_key_user_id = _parse_send_user_api_key_user_id(d.pop("send_user_api_key_user_id", UNSET))


        def _parse_severity_threshold(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        severity_threshold = _parse_severity_threshold(d.pop("severity_threshold", UNSET))


        def _parse_skip_system_message_in_guardrail(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_system_message_in_guardrail = _parse_skip_system_message_in_guardrail(d.pop("skip_system_message_in_guardrail", UNSET))


        def _parse_template_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_id = _parse_template_id(d.pop("template_id", UNSET))


        def _parse_tool_selection_quality_check(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        tool_selection_quality_check = _parse_tool_selection_quality_check(d.pop("tool_selection_quality_check", UNSET))


        _unreachable_fallback = d.pop("unreachable_fallback", UNSET)
        unreachable_fallback: LitellmParamsUnreachableFallback | Unset
        if isinstance(_unreachable_fallback,  Unset):
            unreachable_fallback = UNSET
        else:
            unreachable_fallback = LitellmParamsUnreachableFallback(_unreachable_fallback)




        def _parse_use_v2(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_v2 = _parse_use_v2(d.pop("use_v2", UNSET))


        def _parse_verify_ssl(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        verify_ssl = _parse_verify_ssl(d.pop("verify_ssl", UNSET))


        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))


        def _parse_violation_message_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        violation_message_template = _parse_violation_message_template(d.pop("violation_message_template", UNSET))


        def _parse_xecguard_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        xecguard_model = _parse_xecguard_model(d.pop("xecguard_model", UNSET))


        litellm_params = cls(
            guardrail=guardrail,
            mode=mode,
            action=action,
            additional_provider_specific_params=additional_provider_specific_params,
            akto_account_id=akto_account_id,
            akto_api_key=akto_api_key,
            akto_base_url=akto_base_url,
            akto_vxlan_id=akto_vxlan_id,
            anonymize_input=anonymize_input,
            api_base=api_base,
            api_endpoint=api_endpoint,
            api_id=api_id,
            api_key=api_key,
            api_version=api_version,
            application=application,
            application_id=application_id,
            assertions=assertions,
            async_mode=async_mode,
            auth_token=auth_token,
            aws_access_key_id=aws_access_key_id,
            aws_bedrock_runtime_endpoint=aws_bedrock_runtime_endpoint,
            aws_profile_name=aws_profile_name,
            aws_region_name=aws_region_name,
            aws_role_name=aws_role_name,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_name=aws_session_name,
            aws_session_token=aws_session_token,
            aws_sts_endpoint=aws_sts_endpoint,
            aws_web_identity_token=aws_web_identity_token,
            base_url=base_url,
            block_failures=block_failures,
            block_on_error=block_on_error,
            block_on_violation=block_on_violation,
            blocked_languages=blocked_languages,
            blocked_words=blocked_words,
            blocked_words_file=blocked_words_file,
            breakdown=breakdown,
            categories=categories,
            category_thresholds=category_thresholds,
            confidence_threshold=confidence_threshold,
            config=config,
            content_moderation_check=content_moderation_check,
            credentials=credentials,
            custom_code=custom_code,
            default_action=default_action,
            default_on=default_on,
            deployment_name=deployment_name,
            detect_execution_intent=detect_execution_intent,
            detect_secrets_config=detect_secrets_config,
            detector_id=detector_id,
            detectors=detectors,
            dev_info=dev_info,
            disable_exception_on_block=disable_exception_on_block,
            end_session_after_n_fails=end_session_after_n_fails,
            evaluation_id=evaluation_id,
            experimental_use_latest_role_message_only=experimental_use_latest_role_message_only,
            extra_headers=extra_headers,
            fail_on_error=fail_on_error,
            grounding_check=grounding_check,
            grounding_strictness=grounding_strictness,
            guard_name=guard_name,
            guardrail_identifier=guardrail_identifier,
            guardrail_version=guardrail_version,
            guardrail_timeout=guardrail_timeout,
            hallucinations_check=hallucinations_check,
            include_evidence=include_evidence,
            include_scanners=include_scanners,
            is_detector_server=is_detector_server,
            keyword_redaction_tag=keyword_redaction_tag,
            lasso_conversation_id=lasso_conversation_id,
            lasso_user_id=lasso_user_id,
            location=location,
            mask=mask,
            mask_request_content=mask_request_content,
            mask_response_content=mask_response_content,
            metadata=metadata,
            mock_redacted_text=mock_redacted_text,
            model=model,
            monitor_mode=monitor_mode,
            on_disallowed_action=on_disallowed_action,
            on_flagged=on_flagged,
            on_flagged_action=on_flagged_action,
            on_violation=on_violation,
            optional_params=optional_params,
            output_parse_pii=output_parse_pii,
            pangea_input_recipe=pangea_input_recipe,
            pangea_output_recipe=pangea_output_recipe,
            pattern_redaction_format=pattern_redaction_format,
            patterns=patterns,
            payload=payload,
            persist_session=persist_session,
            pii_check=pii_check,
            pii_entities_config=pii_entities_config,
            policy_id=policy_id,
            policy_name=policy_name,
            policy_names=policy_names,
            presidio_ad_hoc_recognizers=presidio_ad_hoc_recognizers,
            presidio_analyzer_api_base=presidio_analyzer_api_base,
            presidio_anonymizer_api_base=presidio_anonymizer_api_base,
            presidio_entities_deny_list=presidio_entities_deny_list,
            presidio_filter_scope=presidio_filter_scope,
            presidio_language=presidio_language,
            presidio_run_on=presidio_run_on,
            presidio_score_thresholds=presidio_score_thresholds,
            project_id=project_id,
            prompt_injections=prompt_injections,
            realtime_violation_message=realtime_violation_message,
            rules=rules,
            send_user_api_key_alias=send_user_api_key_alias,
            send_user_api_key_team_id=send_user_api_key_team_id,
            send_user_api_key_user_id=send_user_api_key_user_id,
            severity_threshold=severity_threshold,
            skip_system_message_in_guardrail=skip_system_message_in_guardrail,
            template_id=template_id,
            tool_selection_quality_check=tool_selection_quality_check,
            unreachable_fallback=unreachable_fallback,
            use_v2=use_v2,
            verify_ssl=verify_ssl,
            version=version,
            violation_message_template=violation_message_template,
            xecguard_model=xecguard_model,
        )


        litellm_params.additional_properties = d
        return litellm_params

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
