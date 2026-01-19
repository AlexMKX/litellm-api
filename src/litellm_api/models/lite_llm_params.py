from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.configurable_clientside_params_custom_auth import ConfigurableClientsideParamsCustomAuth
  from ..models.lite_llm_params_model_info_type_0 import LiteLLMParamsModelInfoType0
  from ..models.lite_llm_params_search_context_cost_per_query_type_0 import LiteLLMParamsSearchContextCostPerQueryType0
  from ..models.lite_llm_params_tiered_pricing_type_0_item import LiteLLMParamsTieredPricingType0Item
  from ..models.lite_llm_params_vertex_credentials_type_1 import LiteLLMParamsVertexCredentialsType1
  from ..models.model_response import ModelResponse





T = TypeVar("T", bound="LiteLLMParams")



@_attrs_define
class LiteLLMParams:
    """ LiteLLM Params with 'model' requirement - used for completions

        Attributes:
            model (str):
            input_cost_per_token (float | None | Unset):
            output_cost_per_token (float | None | Unset):
            input_cost_per_second (float | None | Unset):
            output_cost_per_second (float | None | Unset):
            input_cost_per_pixel (float | None | Unset):
            output_cost_per_pixel (float | None | Unset):
            input_cost_per_token_flex (float | None | Unset):
            input_cost_per_token_priority (float | None | Unset):
            cache_creation_input_token_cost (float | None | Unset):
            cache_creation_input_token_cost_above_1hr (float | None | Unset):
            cache_creation_input_token_cost_above_200k_tokens (float | None | Unset):
            cache_creation_input_audio_token_cost (float | None | Unset):
            cache_read_input_token_cost (float | None | Unset):
            cache_read_input_token_cost_flex (float | None | Unset):
            cache_read_input_token_cost_priority (float | None | Unset):
            cache_read_input_token_cost_above_200k_tokens (float | None | Unset):
            cache_read_input_audio_token_cost (float | None | Unset):
            input_cost_per_character (float | None | Unset):
            input_cost_per_character_above_128k_tokens (float | None | Unset):
            input_cost_per_audio_token (float | None | Unset):
            input_cost_per_token_cache_hit (float | None | Unset):
            input_cost_per_token_above_128k_tokens (float | None | Unset):
            input_cost_per_token_above_200k_tokens (float | None | Unset):
            input_cost_per_query (float | None | Unset):
            input_cost_per_image (float | None | Unset):
            input_cost_per_image_above_128k_tokens (float | None | Unset):
            input_cost_per_audio_per_second (float | None | Unset):
            input_cost_per_audio_per_second_above_128k_tokens (float | None | Unset):
            input_cost_per_video_per_second (float | None | Unset):
            input_cost_per_video_per_second_above_128k_tokens (float | None | Unset):
            input_cost_per_video_per_second_above_15s_interval (float | None | Unset):
            input_cost_per_video_per_second_above_8s_interval (float | None | Unset):
            input_cost_per_token_batches (float | None | Unset):
            output_cost_per_token_batches (float | None | Unset):
            output_cost_per_token_flex (float | None | Unset):
            output_cost_per_token_priority (float | None | Unset):
            output_cost_per_character (float | None | Unset):
            output_cost_per_audio_token (float | None | Unset):
            output_cost_per_token_above_128k_tokens (float | None | Unset):
            output_cost_per_token_above_200k_tokens (float | None | Unset):
            output_cost_per_character_above_128k_tokens (float | None | Unset):
            output_cost_per_image (float | None | Unset):
            output_cost_per_image_token (float | None | Unset):
            output_cost_per_reasoning_token (float | None | Unset):
            output_cost_per_video_per_second (float | None | Unset):
            output_cost_per_audio_per_second (float | None | Unset):
            search_context_cost_per_query (LiteLLMParamsSearchContextCostPerQueryType0 | None | Unset):
            citation_cost_per_token (float | None | Unset):
            tiered_pricing (list[LiteLLMParamsTieredPricingType0Item] | None | Unset):
            api_key (None | str | Unset):
            api_base (None | str | Unset):
            api_version (None | str | Unset):
            vertex_project (None | str | Unset):
            vertex_location (None | str | Unset):
            vertex_credentials (LiteLLMParamsVertexCredentialsType1 | None | str | Unset):
            region_name (None | str | Unset):
            aws_access_key_id (None | str | Unset):
            aws_secret_access_key (None | str | Unset):
            aws_region_name (None | str | Unset):
            aws_bedrock_runtime_endpoint (None | str | Unset):
            watsonx_region_name (None | str | Unset):
            custom_llm_provider (None | str | Unset):
            tpm (int | None | Unset):
            rpm (int | None | Unset):
            timeout (float | None | str | Unset):
            stream_timeout (float | None | str | Unset):
            max_retries (int | None | Unset):
            organization (None | str | Unset):
            configurable_clientside_auth_params (list[ConfigurableClientsideParamsCustomAuth | str] | None | Unset):
            litellm_credential_name (None | str | Unset):
            litellm_trace_id (None | str | Unset):
            max_file_size_mb (float | None | Unset):
            max_budget (float | None | Unset):
            budget_duration (None | str | Unset):
            use_in_pass_through (bool | None | Unset):  Default: False.
            use_litellm_proxy (bool | None | Unset):  Default: False.
            merge_reasoning_content_in_choices (bool | None | Unset):  Default: False.
            model_info (LiteLLMParamsModelInfoType0 | None | Unset):
            mock_response (Any | ModelResponse | None | str | Unset):
            auto_router_config_path (None | str | Unset):
            auto_router_config (None | str | Unset):
            auto_router_default_model (None | str | Unset):
            auto_router_embedding_model (None | str | Unset):
            s3_bucket_name (None | str | Unset):
            s3_encryption_key_id (None | str | Unset):
            gcs_bucket_name (None | str | Unset):
            vector_store_id (None | str | Unset):
            milvus_text_field (None | str | Unset):
     """

    model: str
    input_cost_per_token: float | None | Unset = UNSET
    output_cost_per_token: float | None | Unset = UNSET
    input_cost_per_second: float | None | Unset = UNSET
    output_cost_per_second: float | None | Unset = UNSET
    input_cost_per_pixel: float | None | Unset = UNSET
    output_cost_per_pixel: float | None | Unset = UNSET
    input_cost_per_token_flex: float | None | Unset = UNSET
    input_cost_per_token_priority: float | None | Unset = UNSET
    cache_creation_input_token_cost: float | None | Unset = UNSET
    cache_creation_input_token_cost_above_1hr: float | None | Unset = UNSET
    cache_creation_input_token_cost_above_200k_tokens: float | None | Unset = UNSET
    cache_creation_input_audio_token_cost: float | None | Unset = UNSET
    cache_read_input_token_cost: float | None | Unset = UNSET
    cache_read_input_token_cost_flex: float | None | Unset = UNSET
    cache_read_input_token_cost_priority: float | None | Unset = UNSET
    cache_read_input_token_cost_above_200k_tokens: float | None | Unset = UNSET
    cache_read_input_audio_token_cost: float | None | Unset = UNSET
    input_cost_per_character: float | None | Unset = UNSET
    input_cost_per_character_above_128k_tokens: float | None | Unset = UNSET
    input_cost_per_audio_token: float | None | Unset = UNSET
    input_cost_per_token_cache_hit: float | None | Unset = UNSET
    input_cost_per_token_above_128k_tokens: float | None | Unset = UNSET
    input_cost_per_token_above_200k_tokens: float | None | Unset = UNSET
    input_cost_per_query: float | None | Unset = UNSET
    input_cost_per_image: float | None | Unset = UNSET
    input_cost_per_image_above_128k_tokens: float | None | Unset = UNSET
    input_cost_per_audio_per_second: float | None | Unset = UNSET
    input_cost_per_audio_per_second_above_128k_tokens: float | None | Unset = UNSET
    input_cost_per_video_per_second: float | None | Unset = UNSET
    input_cost_per_video_per_second_above_128k_tokens: float | None | Unset = UNSET
    input_cost_per_video_per_second_above_15s_interval: float | None | Unset = UNSET
    input_cost_per_video_per_second_above_8s_interval: float | None | Unset = UNSET
    input_cost_per_token_batches: float | None | Unset = UNSET
    output_cost_per_token_batches: float | None | Unset = UNSET
    output_cost_per_token_flex: float | None | Unset = UNSET
    output_cost_per_token_priority: float | None | Unset = UNSET
    output_cost_per_character: float | None | Unset = UNSET
    output_cost_per_audio_token: float | None | Unset = UNSET
    output_cost_per_token_above_128k_tokens: float | None | Unset = UNSET
    output_cost_per_token_above_200k_tokens: float | None | Unset = UNSET
    output_cost_per_character_above_128k_tokens: float | None | Unset = UNSET
    output_cost_per_image: float | None | Unset = UNSET
    output_cost_per_image_token: float | None | Unset = UNSET
    output_cost_per_reasoning_token: float | None | Unset = UNSET
    output_cost_per_video_per_second: float | None | Unset = UNSET
    output_cost_per_audio_per_second: float | None | Unset = UNSET
    search_context_cost_per_query: LiteLLMParamsSearchContextCostPerQueryType0 | None | Unset = UNSET
    citation_cost_per_token: float | None | Unset = UNSET
    tiered_pricing: list[LiteLLMParamsTieredPricingType0Item] | None | Unset = UNSET
    api_key: None | str | Unset = UNSET
    api_base: None | str | Unset = UNSET
    api_version: None | str | Unset = UNSET
    vertex_project: None | str | Unset = UNSET
    vertex_location: None | str | Unset = UNSET
    vertex_credentials: LiteLLMParamsVertexCredentialsType1 | None | str | Unset = UNSET
    region_name: None | str | Unset = UNSET
    aws_access_key_id: None | str | Unset = UNSET
    aws_secret_access_key: None | str | Unset = UNSET
    aws_region_name: None | str | Unset = UNSET
    aws_bedrock_runtime_endpoint: None | str | Unset = UNSET
    watsonx_region_name: None | str | Unset = UNSET
    custom_llm_provider: None | str | Unset = UNSET
    tpm: int | None | Unset = UNSET
    rpm: int | None | Unset = UNSET
    timeout: float | None | str | Unset = UNSET
    stream_timeout: float | None | str | Unset = UNSET
    max_retries: int | None | Unset = UNSET
    organization: None | str | Unset = UNSET
    configurable_clientside_auth_params: list[ConfigurableClientsideParamsCustomAuth | str] | None | Unset = UNSET
    litellm_credential_name: None | str | Unset = UNSET
    litellm_trace_id: None | str | Unset = UNSET
    max_file_size_mb: float | None | Unset = UNSET
    max_budget: float | None | Unset = UNSET
    budget_duration: None | str | Unset = UNSET
    use_in_pass_through: bool | None | Unset = False
    use_litellm_proxy: bool | None | Unset = False
    merge_reasoning_content_in_choices: bool | None | Unset = False
    model_info: LiteLLMParamsModelInfoType0 | None | Unset = UNSET
    mock_response: Any | ModelResponse | None | str | Unset = UNSET
    auto_router_config_path: None | str | Unset = UNSET
    auto_router_config: None | str | Unset = UNSET
    auto_router_default_model: None | str | Unset = UNSET
    auto_router_embedding_model: None | str | Unset = UNSET
    s3_bucket_name: None | str | Unset = UNSET
    s3_encryption_key_id: None | str | Unset = UNSET
    gcs_bucket_name: None | str | Unset = UNSET
    vector_store_id: None | str | Unset = UNSET
    milvus_text_field: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_params_search_context_cost_per_query_type_0 import LiteLLMParamsSearchContextCostPerQueryType0
        from ..models.lite_llm_params_model_info_type_0 import LiteLLMParamsModelInfoType0
        from ..models.lite_llm_params_vertex_credentials_type_1 import LiteLLMParamsVertexCredentialsType1
        from ..models.lite_llm_params_tiered_pricing_type_0_item import LiteLLMParamsTieredPricingType0Item
        from ..models.configurable_clientside_params_custom_auth import ConfigurableClientsideParamsCustomAuth
        from ..models.model_response import ModelResponse
        model = self.model

        input_cost_per_token: float | None | Unset
        if isinstance(self.input_cost_per_token, Unset):
            input_cost_per_token = UNSET
        else:
            input_cost_per_token = self.input_cost_per_token

        output_cost_per_token: float | None | Unset
        if isinstance(self.output_cost_per_token, Unset):
            output_cost_per_token = UNSET
        else:
            output_cost_per_token = self.output_cost_per_token

        input_cost_per_second: float | None | Unset
        if isinstance(self.input_cost_per_second, Unset):
            input_cost_per_second = UNSET
        else:
            input_cost_per_second = self.input_cost_per_second

        output_cost_per_second: float | None | Unset
        if isinstance(self.output_cost_per_second, Unset):
            output_cost_per_second = UNSET
        else:
            output_cost_per_second = self.output_cost_per_second

        input_cost_per_pixel: float | None | Unset
        if isinstance(self.input_cost_per_pixel, Unset):
            input_cost_per_pixel = UNSET
        else:
            input_cost_per_pixel = self.input_cost_per_pixel

        output_cost_per_pixel: float | None | Unset
        if isinstance(self.output_cost_per_pixel, Unset):
            output_cost_per_pixel = UNSET
        else:
            output_cost_per_pixel = self.output_cost_per_pixel

        input_cost_per_token_flex: float | None | Unset
        if isinstance(self.input_cost_per_token_flex, Unset):
            input_cost_per_token_flex = UNSET
        else:
            input_cost_per_token_flex = self.input_cost_per_token_flex

        input_cost_per_token_priority: float | None | Unset
        if isinstance(self.input_cost_per_token_priority, Unset):
            input_cost_per_token_priority = UNSET
        else:
            input_cost_per_token_priority = self.input_cost_per_token_priority

        cache_creation_input_token_cost: float | None | Unset
        if isinstance(self.cache_creation_input_token_cost, Unset):
            cache_creation_input_token_cost = UNSET
        else:
            cache_creation_input_token_cost = self.cache_creation_input_token_cost

        cache_creation_input_token_cost_above_1hr: float | None | Unset
        if isinstance(self.cache_creation_input_token_cost_above_1hr, Unset):
            cache_creation_input_token_cost_above_1hr = UNSET
        else:
            cache_creation_input_token_cost_above_1hr = self.cache_creation_input_token_cost_above_1hr

        cache_creation_input_token_cost_above_200k_tokens: float | None | Unset
        if isinstance(self.cache_creation_input_token_cost_above_200k_tokens, Unset):
            cache_creation_input_token_cost_above_200k_tokens = UNSET
        else:
            cache_creation_input_token_cost_above_200k_tokens = self.cache_creation_input_token_cost_above_200k_tokens

        cache_creation_input_audio_token_cost: float | None | Unset
        if isinstance(self.cache_creation_input_audio_token_cost, Unset):
            cache_creation_input_audio_token_cost = UNSET
        else:
            cache_creation_input_audio_token_cost = self.cache_creation_input_audio_token_cost

        cache_read_input_token_cost: float | None | Unset
        if isinstance(self.cache_read_input_token_cost, Unset):
            cache_read_input_token_cost = UNSET
        else:
            cache_read_input_token_cost = self.cache_read_input_token_cost

        cache_read_input_token_cost_flex: float | None | Unset
        if isinstance(self.cache_read_input_token_cost_flex, Unset):
            cache_read_input_token_cost_flex = UNSET
        else:
            cache_read_input_token_cost_flex = self.cache_read_input_token_cost_flex

        cache_read_input_token_cost_priority: float | None | Unset
        if isinstance(self.cache_read_input_token_cost_priority, Unset):
            cache_read_input_token_cost_priority = UNSET
        else:
            cache_read_input_token_cost_priority = self.cache_read_input_token_cost_priority

        cache_read_input_token_cost_above_200k_tokens: float | None | Unset
        if isinstance(self.cache_read_input_token_cost_above_200k_tokens, Unset):
            cache_read_input_token_cost_above_200k_tokens = UNSET
        else:
            cache_read_input_token_cost_above_200k_tokens = self.cache_read_input_token_cost_above_200k_tokens

        cache_read_input_audio_token_cost: float | None | Unset
        if isinstance(self.cache_read_input_audio_token_cost, Unset):
            cache_read_input_audio_token_cost = UNSET
        else:
            cache_read_input_audio_token_cost = self.cache_read_input_audio_token_cost

        input_cost_per_character: float | None | Unset
        if isinstance(self.input_cost_per_character, Unset):
            input_cost_per_character = UNSET
        else:
            input_cost_per_character = self.input_cost_per_character

        input_cost_per_character_above_128k_tokens: float | None | Unset
        if isinstance(self.input_cost_per_character_above_128k_tokens, Unset):
            input_cost_per_character_above_128k_tokens = UNSET
        else:
            input_cost_per_character_above_128k_tokens = self.input_cost_per_character_above_128k_tokens

        input_cost_per_audio_token: float | None | Unset
        if isinstance(self.input_cost_per_audio_token, Unset):
            input_cost_per_audio_token = UNSET
        else:
            input_cost_per_audio_token = self.input_cost_per_audio_token

        input_cost_per_token_cache_hit: float | None | Unset
        if isinstance(self.input_cost_per_token_cache_hit, Unset):
            input_cost_per_token_cache_hit = UNSET
        else:
            input_cost_per_token_cache_hit = self.input_cost_per_token_cache_hit

        input_cost_per_token_above_128k_tokens: float | None | Unset
        if isinstance(self.input_cost_per_token_above_128k_tokens, Unset):
            input_cost_per_token_above_128k_tokens = UNSET
        else:
            input_cost_per_token_above_128k_tokens = self.input_cost_per_token_above_128k_tokens

        input_cost_per_token_above_200k_tokens: float | None | Unset
        if isinstance(self.input_cost_per_token_above_200k_tokens, Unset):
            input_cost_per_token_above_200k_tokens = UNSET
        else:
            input_cost_per_token_above_200k_tokens = self.input_cost_per_token_above_200k_tokens

        input_cost_per_query: float | None | Unset
        if isinstance(self.input_cost_per_query, Unset):
            input_cost_per_query = UNSET
        else:
            input_cost_per_query = self.input_cost_per_query

        input_cost_per_image: float | None | Unset
        if isinstance(self.input_cost_per_image, Unset):
            input_cost_per_image = UNSET
        else:
            input_cost_per_image = self.input_cost_per_image

        input_cost_per_image_above_128k_tokens: float | None | Unset
        if isinstance(self.input_cost_per_image_above_128k_tokens, Unset):
            input_cost_per_image_above_128k_tokens = UNSET
        else:
            input_cost_per_image_above_128k_tokens = self.input_cost_per_image_above_128k_tokens

        input_cost_per_audio_per_second: float | None | Unset
        if isinstance(self.input_cost_per_audio_per_second, Unset):
            input_cost_per_audio_per_second = UNSET
        else:
            input_cost_per_audio_per_second = self.input_cost_per_audio_per_second

        input_cost_per_audio_per_second_above_128k_tokens: float | None | Unset
        if isinstance(self.input_cost_per_audio_per_second_above_128k_tokens, Unset):
            input_cost_per_audio_per_second_above_128k_tokens = UNSET
        else:
            input_cost_per_audio_per_second_above_128k_tokens = self.input_cost_per_audio_per_second_above_128k_tokens

        input_cost_per_video_per_second: float | None | Unset
        if isinstance(self.input_cost_per_video_per_second, Unset):
            input_cost_per_video_per_second = UNSET
        else:
            input_cost_per_video_per_second = self.input_cost_per_video_per_second

        input_cost_per_video_per_second_above_128k_tokens: float | None | Unset
        if isinstance(self.input_cost_per_video_per_second_above_128k_tokens, Unset):
            input_cost_per_video_per_second_above_128k_tokens = UNSET
        else:
            input_cost_per_video_per_second_above_128k_tokens = self.input_cost_per_video_per_second_above_128k_tokens

        input_cost_per_video_per_second_above_15s_interval: float | None | Unset
        if isinstance(self.input_cost_per_video_per_second_above_15s_interval, Unset):
            input_cost_per_video_per_second_above_15s_interval = UNSET
        else:
            input_cost_per_video_per_second_above_15s_interval = self.input_cost_per_video_per_second_above_15s_interval

        input_cost_per_video_per_second_above_8s_interval: float | None | Unset
        if isinstance(self.input_cost_per_video_per_second_above_8s_interval, Unset):
            input_cost_per_video_per_second_above_8s_interval = UNSET
        else:
            input_cost_per_video_per_second_above_8s_interval = self.input_cost_per_video_per_second_above_8s_interval

        input_cost_per_token_batches: float | None | Unset
        if isinstance(self.input_cost_per_token_batches, Unset):
            input_cost_per_token_batches = UNSET
        else:
            input_cost_per_token_batches = self.input_cost_per_token_batches

        output_cost_per_token_batches: float | None | Unset
        if isinstance(self.output_cost_per_token_batches, Unset):
            output_cost_per_token_batches = UNSET
        else:
            output_cost_per_token_batches = self.output_cost_per_token_batches

        output_cost_per_token_flex: float | None | Unset
        if isinstance(self.output_cost_per_token_flex, Unset):
            output_cost_per_token_flex = UNSET
        else:
            output_cost_per_token_flex = self.output_cost_per_token_flex

        output_cost_per_token_priority: float | None | Unset
        if isinstance(self.output_cost_per_token_priority, Unset):
            output_cost_per_token_priority = UNSET
        else:
            output_cost_per_token_priority = self.output_cost_per_token_priority

        output_cost_per_character: float | None | Unset
        if isinstance(self.output_cost_per_character, Unset):
            output_cost_per_character = UNSET
        else:
            output_cost_per_character = self.output_cost_per_character

        output_cost_per_audio_token: float | None | Unset
        if isinstance(self.output_cost_per_audio_token, Unset):
            output_cost_per_audio_token = UNSET
        else:
            output_cost_per_audio_token = self.output_cost_per_audio_token

        output_cost_per_token_above_128k_tokens: float | None | Unset
        if isinstance(self.output_cost_per_token_above_128k_tokens, Unset):
            output_cost_per_token_above_128k_tokens = UNSET
        else:
            output_cost_per_token_above_128k_tokens = self.output_cost_per_token_above_128k_tokens

        output_cost_per_token_above_200k_tokens: float | None | Unset
        if isinstance(self.output_cost_per_token_above_200k_tokens, Unset):
            output_cost_per_token_above_200k_tokens = UNSET
        else:
            output_cost_per_token_above_200k_tokens = self.output_cost_per_token_above_200k_tokens

        output_cost_per_character_above_128k_tokens: float | None | Unset
        if isinstance(self.output_cost_per_character_above_128k_tokens, Unset):
            output_cost_per_character_above_128k_tokens = UNSET
        else:
            output_cost_per_character_above_128k_tokens = self.output_cost_per_character_above_128k_tokens

        output_cost_per_image: float | None | Unset
        if isinstance(self.output_cost_per_image, Unset):
            output_cost_per_image = UNSET
        else:
            output_cost_per_image = self.output_cost_per_image

        output_cost_per_image_token: float | None | Unset
        if isinstance(self.output_cost_per_image_token, Unset):
            output_cost_per_image_token = UNSET
        else:
            output_cost_per_image_token = self.output_cost_per_image_token

        output_cost_per_reasoning_token: float | None | Unset
        if isinstance(self.output_cost_per_reasoning_token, Unset):
            output_cost_per_reasoning_token = UNSET
        else:
            output_cost_per_reasoning_token = self.output_cost_per_reasoning_token

        output_cost_per_video_per_second: float | None | Unset
        if isinstance(self.output_cost_per_video_per_second, Unset):
            output_cost_per_video_per_second = UNSET
        else:
            output_cost_per_video_per_second = self.output_cost_per_video_per_second

        output_cost_per_audio_per_second: float | None | Unset
        if isinstance(self.output_cost_per_audio_per_second, Unset):
            output_cost_per_audio_per_second = UNSET
        else:
            output_cost_per_audio_per_second = self.output_cost_per_audio_per_second

        search_context_cost_per_query: dict[str, Any] | None | Unset
        if isinstance(self.search_context_cost_per_query, Unset):
            search_context_cost_per_query = UNSET
        elif isinstance(self.search_context_cost_per_query, LiteLLMParamsSearchContextCostPerQueryType0):
            search_context_cost_per_query = self.search_context_cost_per_query.to_dict()
        else:
            search_context_cost_per_query = self.search_context_cost_per_query

        citation_cost_per_token: float | None | Unset
        if isinstance(self.citation_cost_per_token, Unset):
            citation_cost_per_token = UNSET
        else:
            citation_cost_per_token = self.citation_cost_per_token

        tiered_pricing: list[dict[str, Any]] | None | Unset
        if isinstance(self.tiered_pricing, Unset):
            tiered_pricing = UNSET
        elif isinstance(self.tiered_pricing, list):
            tiered_pricing = []
            for tiered_pricing_type_0_item_data in self.tiered_pricing:
                tiered_pricing_type_0_item = tiered_pricing_type_0_item_data.to_dict()
                tiered_pricing.append(tiered_pricing_type_0_item)


        else:
            tiered_pricing = self.tiered_pricing

        api_key: None | str | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

        api_base: None | str | Unset
        if isinstance(self.api_base, Unset):
            api_base = UNSET
        else:
            api_base = self.api_base

        api_version: None | str | Unset
        if isinstance(self.api_version, Unset):
            api_version = UNSET
        else:
            api_version = self.api_version

        vertex_project: None | str | Unset
        if isinstance(self.vertex_project, Unset):
            vertex_project = UNSET
        else:
            vertex_project = self.vertex_project

        vertex_location: None | str | Unset
        if isinstance(self.vertex_location, Unset):
            vertex_location = UNSET
        else:
            vertex_location = self.vertex_location

        vertex_credentials: dict[str, Any] | None | str | Unset
        if isinstance(self.vertex_credentials, Unset):
            vertex_credentials = UNSET
        elif isinstance(self.vertex_credentials, LiteLLMParamsVertexCredentialsType1):
            vertex_credentials = self.vertex_credentials.to_dict()
        else:
            vertex_credentials = self.vertex_credentials

        region_name: None | str | Unset
        if isinstance(self.region_name, Unset):
            region_name = UNSET
        else:
            region_name = self.region_name

        aws_access_key_id: None | str | Unset
        if isinstance(self.aws_access_key_id, Unset):
            aws_access_key_id = UNSET
        else:
            aws_access_key_id = self.aws_access_key_id

        aws_secret_access_key: None | str | Unset
        if isinstance(self.aws_secret_access_key, Unset):
            aws_secret_access_key = UNSET
        else:
            aws_secret_access_key = self.aws_secret_access_key

        aws_region_name: None | str | Unset
        if isinstance(self.aws_region_name, Unset):
            aws_region_name = UNSET
        else:
            aws_region_name = self.aws_region_name

        aws_bedrock_runtime_endpoint: None | str | Unset
        if isinstance(self.aws_bedrock_runtime_endpoint, Unset):
            aws_bedrock_runtime_endpoint = UNSET
        else:
            aws_bedrock_runtime_endpoint = self.aws_bedrock_runtime_endpoint

        watsonx_region_name: None | str | Unset
        if isinstance(self.watsonx_region_name, Unset):
            watsonx_region_name = UNSET
        else:
            watsonx_region_name = self.watsonx_region_name

        custom_llm_provider: None | str | Unset
        if isinstance(self.custom_llm_provider, Unset):
            custom_llm_provider = UNSET
        else:
            custom_llm_provider = self.custom_llm_provider

        tpm: int | None | Unset
        if isinstance(self.tpm, Unset):
            tpm = UNSET
        else:
            tpm = self.tpm

        rpm: int | None | Unset
        if isinstance(self.rpm, Unset):
            rpm = UNSET
        else:
            rpm = self.rpm

        timeout: float | None | str | Unset
        if isinstance(self.timeout, Unset):
            timeout = UNSET
        else:
            timeout = self.timeout

        stream_timeout: float | None | str | Unset
        if isinstance(self.stream_timeout, Unset):
            stream_timeout = UNSET
        else:
            stream_timeout = self.stream_timeout

        max_retries: int | None | Unset
        if isinstance(self.max_retries, Unset):
            max_retries = UNSET
        else:
            max_retries = self.max_retries

        organization: None | str | Unset
        if isinstance(self.organization, Unset):
            organization = UNSET
        else:
            organization = self.organization

        configurable_clientside_auth_params: list[dict[str, Any] | str] | None | Unset
        if isinstance(self.configurable_clientside_auth_params, Unset):
            configurable_clientside_auth_params = UNSET
        elif isinstance(self.configurable_clientside_auth_params, list):
            configurable_clientside_auth_params = []
            for configurable_clientside_auth_params_type_0_item_data in self.configurable_clientside_auth_params:
                configurable_clientside_auth_params_type_0_item: dict[str, Any] | str
                if isinstance(configurable_clientside_auth_params_type_0_item_data, ConfigurableClientsideParamsCustomAuth):
                    configurable_clientside_auth_params_type_0_item = configurable_clientside_auth_params_type_0_item_data.to_dict()
                else:
                    configurable_clientside_auth_params_type_0_item = configurable_clientside_auth_params_type_0_item_data
                configurable_clientside_auth_params.append(configurable_clientside_auth_params_type_0_item)


        else:
            configurable_clientside_auth_params = self.configurable_clientside_auth_params

        litellm_credential_name: None | str | Unset
        if isinstance(self.litellm_credential_name, Unset):
            litellm_credential_name = UNSET
        else:
            litellm_credential_name = self.litellm_credential_name

        litellm_trace_id: None | str | Unset
        if isinstance(self.litellm_trace_id, Unset):
            litellm_trace_id = UNSET
        else:
            litellm_trace_id = self.litellm_trace_id

        max_file_size_mb: float | None | Unset
        if isinstance(self.max_file_size_mb, Unset):
            max_file_size_mb = UNSET
        else:
            max_file_size_mb = self.max_file_size_mb

        max_budget: float | None | Unset
        if isinstance(self.max_budget, Unset):
            max_budget = UNSET
        else:
            max_budget = self.max_budget

        budget_duration: None | str | Unset
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration

        use_in_pass_through: bool | None | Unset
        if isinstance(self.use_in_pass_through, Unset):
            use_in_pass_through = UNSET
        else:
            use_in_pass_through = self.use_in_pass_through

        use_litellm_proxy: bool | None | Unset
        if isinstance(self.use_litellm_proxy, Unset):
            use_litellm_proxy = UNSET
        else:
            use_litellm_proxy = self.use_litellm_proxy

        merge_reasoning_content_in_choices: bool | None | Unset
        if isinstance(self.merge_reasoning_content_in_choices, Unset):
            merge_reasoning_content_in_choices = UNSET
        else:
            merge_reasoning_content_in_choices = self.merge_reasoning_content_in_choices

        model_info: dict[str, Any] | None | Unset
        if isinstance(self.model_info, Unset):
            model_info = UNSET
        elif isinstance(self.model_info, LiteLLMParamsModelInfoType0):
            model_info = self.model_info.to_dict()
        else:
            model_info = self.model_info

        mock_response: Any | dict[str, Any] | None | str | Unset
        if isinstance(self.mock_response, Unset):
            mock_response = UNSET
        elif isinstance(self.mock_response, ModelResponse):
            mock_response = self.mock_response.to_dict()
        else:
            mock_response = self.mock_response

        auto_router_config_path: None | str | Unset
        if isinstance(self.auto_router_config_path, Unset):
            auto_router_config_path = UNSET
        else:
            auto_router_config_path = self.auto_router_config_path

        auto_router_config: None | str | Unset
        if isinstance(self.auto_router_config, Unset):
            auto_router_config = UNSET
        else:
            auto_router_config = self.auto_router_config

        auto_router_default_model: None | str | Unset
        if isinstance(self.auto_router_default_model, Unset):
            auto_router_default_model = UNSET
        else:
            auto_router_default_model = self.auto_router_default_model

        auto_router_embedding_model: None | str | Unset
        if isinstance(self.auto_router_embedding_model, Unset):
            auto_router_embedding_model = UNSET
        else:
            auto_router_embedding_model = self.auto_router_embedding_model

        s3_bucket_name: None | str | Unset
        if isinstance(self.s3_bucket_name, Unset):
            s3_bucket_name = UNSET
        else:
            s3_bucket_name = self.s3_bucket_name

        s3_encryption_key_id: None | str | Unset
        if isinstance(self.s3_encryption_key_id, Unset):
            s3_encryption_key_id = UNSET
        else:
            s3_encryption_key_id = self.s3_encryption_key_id

        gcs_bucket_name: None | str | Unset
        if isinstance(self.gcs_bucket_name, Unset):
            gcs_bucket_name = UNSET
        else:
            gcs_bucket_name = self.gcs_bucket_name

        vector_store_id: None | str | Unset
        if isinstance(self.vector_store_id, Unset):
            vector_store_id = UNSET
        else:
            vector_store_id = self.vector_store_id

        milvus_text_field: None | str | Unset
        if isinstance(self.milvus_text_field, Unset):
            milvus_text_field = UNSET
        else:
            milvus_text_field = self.milvus_text_field


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "model": model,
        })
        if input_cost_per_token is not UNSET:
            field_dict["input_cost_per_token"] = input_cost_per_token
        if output_cost_per_token is not UNSET:
            field_dict["output_cost_per_token"] = output_cost_per_token
        if input_cost_per_second is not UNSET:
            field_dict["input_cost_per_second"] = input_cost_per_second
        if output_cost_per_second is not UNSET:
            field_dict["output_cost_per_second"] = output_cost_per_second
        if input_cost_per_pixel is not UNSET:
            field_dict["input_cost_per_pixel"] = input_cost_per_pixel
        if output_cost_per_pixel is not UNSET:
            field_dict["output_cost_per_pixel"] = output_cost_per_pixel
        if input_cost_per_token_flex is not UNSET:
            field_dict["input_cost_per_token_flex"] = input_cost_per_token_flex
        if input_cost_per_token_priority is not UNSET:
            field_dict["input_cost_per_token_priority"] = input_cost_per_token_priority
        if cache_creation_input_token_cost is not UNSET:
            field_dict["cache_creation_input_token_cost"] = cache_creation_input_token_cost
        if cache_creation_input_token_cost_above_1hr is not UNSET:
            field_dict["cache_creation_input_token_cost_above_1hr"] = cache_creation_input_token_cost_above_1hr
        if cache_creation_input_token_cost_above_200k_tokens is not UNSET:
            field_dict["cache_creation_input_token_cost_above_200k_tokens"] = cache_creation_input_token_cost_above_200k_tokens
        if cache_creation_input_audio_token_cost is not UNSET:
            field_dict["cache_creation_input_audio_token_cost"] = cache_creation_input_audio_token_cost
        if cache_read_input_token_cost is not UNSET:
            field_dict["cache_read_input_token_cost"] = cache_read_input_token_cost
        if cache_read_input_token_cost_flex is not UNSET:
            field_dict["cache_read_input_token_cost_flex"] = cache_read_input_token_cost_flex
        if cache_read_input_token_cost_priority is not UNSET:
            field_dict["cache_read_input_token_cost_priority"] = cache_read_input_token_cost_priority
        if cache_read_input_token_cost_above_200k_tokens is not UNSET:
            field_dict["cache_read_input_token_cost_above_200k_tokens"] = cache_read_input_token_cost_above_200k_tokens
        if cache_read_input_audio_token_cost is not UNSET:
            field_dict["cache_read_input_audio_token_cost"] = cache_read_input_audio_token_cost
        if input_cost_per_character is not UNSET:
            field_dict["input_cost_per_character"] = input_cost_per_character
        if input_cost_per_character_above_128k_tokens is not UNSET:
            field_dict["input_cost_per_character_above_128k_tokens"] = input_cost_per_character_above_128k_tokens
        if input_cost_per_audio_token is not UNSET:
            field_dict["input_cost_per_audio_token"] = input_cost_per_audio_token
        if input_cost_per_token_cache_hit is not UNSET:
            field_dict["input_cost_per_token_cache_hit"] = input_cost_per_token_cache_hit
        if input_cost_per_token_above_128k_tokens is not UNSET:
            field_dict["input_cost_per_token_above_128k_tokens"] = input_cost_per_token_above_128k_tokens
        if input_cost_per_token_above_200k_tokens is not UNSET:
            field_dict["input_cost_per_token_above_200k_tokens"] = input_cost_per_token_above_200k_tokens
        if input_cost_per_query is not UNSET:
            field_dict["input_cost_per_query"] = input_cost_per_query
        if input_cost_per_image is not UNSET:
            field_dict["input_cost_per_image"] = input_cost_per_image
        if input_cost_per_image_above_128k_tokens is not UNSET:
            field_dict["input_cost_per_image_above_128k_tokens"] = input_cost_per_image_above_128k_tokens
        if input_cost_per_audio_per_second is not UNSET:
            field_dict["input_cost_per_audio_per_second"] = input_cost_per_audio_per_second
        if input_cost_per_audio_per_second_above_128k_tokens is not UNSET:
            field_dict["input_cost_per_audio_per_second_above_128k_tokens"] = input_cost_per_audio_per_second_above_128k_tokens
        if input_cost_per_video_per_second is not UNSET:
            field_dict["input_cost_per_video_per_second"] = input_cost_per_video_per_second
        if input_cost_per_video_per_second_above_128k_tokens is not UNSET:
            field_dict["input_cost_per_video_per_second_above_128k_tokens"] = input_cost_per_video_per_second_above_128k_tokens
        if input_cost_per_video_per_second_above_15s_interval is not UNSET:
            field_dict["input_cost_per_video_per_second_above_15s_interval"] = input_cost_per_video_per_second_above_15s_interval
        if input_cost_per_video_per_second_above_8s_interval is not UNSET:
            field_dict["input_cost_per_video_per_second_above_8s_interval"] = input_cost_per_video_per_second_above_8s_interval
        if input_cost_per_token_batches is not UNSET:
            field_dict["input_cost_per_token_batches"] = input_cost_per_token_batches
        if output_cost_per_token_batches is not UNSET:
            field_dict["output_cost_per_token_batches"] = output_cost_per_token_batches
        if output_cost_per_token_flex is not UNSET:
            field_dict["output_cost_per_token_flex"] = output_cost_per_token_flex
        if output_cost_per_token_priority is not UNSET:
            field_dict["output_cost_per_token_priority"] = output_cost_per_token_priority
        if output_cost_per_character is not UNSET:
            field_dict["output_cost_per_character"] = output_cost_per_character
        if output_cost_per_audio_token is not UNSET:
            field_dict["output_cost_per_audio_token"] = output_cost_per_audio_token
        if output_cost_per_token_above_128k_tokens is not UNSET:
            field_dict["output_cost_per_token_above_128k_tokens"] = output_cost_per_token_above_128k_tokens
        if output_cost_per_token_above_200k_tokens is not UNSET:
            field_dict["output_cost_per_token_above_200k_tokens"] = output_cost_per_token_above_200k_tokens
        if output_cost_per_character_above_128k_tokens is not UNSET:
            field_dict["output_cost_per_character_above_128k_tokens"] = output_cost_per_character_above_128k_tokens
        if output_cost_per_image is not UNSET:
            field_dict["output_cost_per_image"] = output_cost_per_image
        if output_cost_per_image_token is not UNSET:
            field_dict["output_cost_per_image_token"] = output_cost_per_image_token
        if output_cost_per_reasoning_token is not UNSET:
            field_dict["output_cost_per_reasoning_token"] = output_cost_per_reasoning_token
        if output_cost_per_video_per_second is not UNSET:
            field_dict["output_cost_per_video_per_second"] = output_cost_per_video_per_second
        if output_cost_per_audio_per_second is not UNSET:
            field_dict["output_cost_per_audio_per_second"] = output_cost_per_audio_per_second
        if search_context_cost_per_query is not UNSET:
            field_dict["search_context_cost_per_query"] = search_context_cost_per_query
        if citation_cost_per_token is not UNSET:
            field_dict["citation_cost_per_token"] = citation_cost_per_token
        if tiered_pricing is not UNSET:
            field_dict["tiered_pricing"] = tiered_pricing
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if api_base is not UNSET:
            field_dict["api_base"] = api_base
        if api_version is not UNSET:
            field_dict["api_version"] = api_version
        if vertex_project is not UNSET:
            field_dict["vertex_project"] = vertex_project
        if vertex_location is not UNSET:
            field_dict["vertex_location"] = vertex_location
        if vertex_credentials is not UNSET:
            field_dict["vertex_credentials"] = vertex_credentials
        if region_name is not UNSET:
            field_dict["region_name"] = region_name
        if aws_access_key_id is not UNSET:
            field_dict["aws_access_key_id"] = aws_access_key_id
        if aws_secret_access_key is not UNSET:
            field_dict["aws_secret_access_key"] = aws_secret_access_key
        if aws_region_name is not UNSET:
            field_dict["aws_region_name"] = aws_region_name
        if aws_bedrock_runtime_endpoint is not UNSET:
            field_dict["aws_bedrock_runtime_endpoint"] = aws_bedrock_runtime_endpoint
        if watsonx_region_name is not UNSET:
            field_dict["watsonx_region_name"] = watsonx_region_name
        if custom_llm_provider is not UNSET:
            field_dict["custom_llm_provider"] = custom_llm_provider
        if tpm is not UNSET:
            field_dict["tpm"] = tpm
        if rpm is not UNSET:
            field_dict["rpm"] = rpm
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if stream_timeout is not UNSET:
            field_dict["stream_timeout"] = stream_timeout
        if max_retries is not UNSET:
            field_dict["max_retries"] = max_retries
        if organization is not UNSET:
            field_dict["organization"] = organization
        if configurable_clientside_auth_params is not UNSET:
            field_dict["configurable_clientside_auth_params"] = configurable_clientside_auth_params
        if litellm_credential_name is not UNSET:
            field_dict["litellm_credential_name"] = litellm_credential_name
        if litellm_trace_id is not UNSET:
            field_dict["litellm_trace_id"] = litellm_trace_id
        if max_file_size_mb is not UNSET:
            field_dict["max_file_size_mb"] = max_file_size_mb
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if budget_duration is not UNSET:
            field_dict["budget_duration"] = budget_duration
        if use_in_pass_through is not UNSET:
            field_dict["use_in_pass_through"] = use_in_pass_through
        if use_litellm_proxy is not UNSET:
            field_dict["use_litellm_proxy"] = use_litellm_proxy
        if merge_reasoning_content_in_choices is not UNSET:
            field_dict["merge_reasoning_content_in_choices"] = merge_reasoning_content_in_choices
        if model_info is not UNSET:
            field_dict["model_info"] = model_info
        if mock_response is not UNSET:
            field_dict["mock_response"] = mock_response
        if auto_router_config_path is not UNSET:
            field_dict["auto_router_config_path"] = auto_router_config_path
        if auto_router_config is not UNSET:
            field_dict["auto_router_config"] = auto_router_config
        if auto_router_default_model is not UNSET:
            field_dict["auto_router_default_model"] = auto_router_default_model
        if auto_router_embedding_model is not UNSET:
            field_dict["auto_router_embedding_model"] = auto_router_embedding_model
        if s3_bucket_name is not UNSET:
            field_dict["s3_bucket_name"] = s3_bucket_name
        if s3_encryption_key_id is not UNSET:
            field_dict["s3_encryption_key_id"] = s3_encryption_key_id
        if gcs_bucket_name is not UNSET:
            field_dict["gcs_bucket_name"] = gcs_bucket_name
        if vector_store_id is not UNSET:
            field_dict["vector_store_id"] = vector_store_id
        if milvus_text_field is not UNSET:
            field_dict["milvus_text_field"] = milvus_text_field

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configurable_clientside_params_custom_auth import ConfigurableClientsideParamsCustomAuth
        from ..models.lite_llm_params_model_info_type_0 import LiteLLMParamsModelInfoType0
        from ..models.lite_llm_params_search_context_cost_per_query_type_0 import LiteLLMParamsSearchContextCostPerQueryType0
        from ..models.lite_llm_params_tiered_pricing_type_0_item import LiteLLMParamsTieredPricingType0Item
        from ..models.lite_llm_params_vertex_credentials_type_1 import LiteLLMParamsVertexCredentialsType1
        from ..models.model_response import ModelResponse
        d = dict(src_dict)
        model = d.pop("model")

        def _parse_input_cost_per_token(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_token = _parse_input_cost_per_token(d.pop("input_cost_per_token", UNSET))


        def _parse_output_cost_per_token(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_token = _parse_output_cost_per_token(d.pop("output_cost_per_token", UNSET))


        def _parse_input_cost_per_second(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_second = _parse_input_cost_per_second(d.pop("input_cost_per_second", UNSET))


        def _parse_output_cost_per_second(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_second = _parse_output_cost_per_second(d.pop("output_cost_per_second", UNSET))


        def _parse_input_cost_per_pixel(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_pixel = _parse_input_cost_per_pixel(d.pop("input_cost_per_pixel", UNSET))


        def _parse_output_cost_per_pixel(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_pixel = _parse_output_cost_per_pixel(d.pop("output_cost_per_pixel", UNSET))


        def _parse_input_cost_per_token_flex(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_token_flex = _parse_input_cost_per_token_flex(d.pop("input_cost_per_token_flex", UNSET))


        def _parse_input_cost_per_token_priority(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_token_priority = _parse_input_cost_per_token_priority(d.pop("input_cost_per_token_priority", UNSET))


        def _parse_cache_creation_input_token_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cache_creation_input_token_cost = _parse_cache_creation_input_token_cost(d.pop("cache_creation_input_token_cost", UNSET))


        def _parse_cache_creation_input_token_cost_above_1hr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cache_creation_input_token_cost_above_1hr = _parse_cache_creation_input_token_cost_above_1hr(d.pop("cache_creation_input_token_cost_above_1hr", UNSET))


        def _parse_cache_creation_input_token_cost_above_200k_tokens(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cache_creation_input_token_cost_above_200k_tokens = _parse_cache_creation_input_token_cost_above_200k_tokens(d.pop("cache_creation_input_token_cost_above_200k_tokens", UNSET))


        def _parse_cache_creation_input_audio_token_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cache_creation_input_audio_token_cost = _parse_cache_creation_input_audio_token_cost(d.pop("cache_creation_input_audio_token_cost", UNSET))


        def _parse_cache_read_input_token_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cache_read_input_token_cost = _parse_cache_read_input_token_cost(d.pop("cache_read_input_token_cost", UNSET))


        def _parse_cache_read_input_token_cost_flex(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cache_read_input_token_cost_flex = _parse_cache_read_input_token_cost_flex(d.pop("cache_read_input_token_cost_flex", UNSET))


        def _parse_cache_read_input_token_cost_priority(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cache_read_input_token_cost_priority = _parse_cache_read_input_token_cost_priority(d.pop("cache_read_input_token_cost_priority", UNSET))


        def _parse_cache_read_input_token_cost_above_200k_tokens(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cache_read_input_token_cost_above_200k_tokens = _parse_cache_read_input_token_cost_above_200k_tokens(d.pop("cache_read_input_token_cost_above_200k_tokens", UNSET))


        def _parse_cache_read_input_audio_token_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cache_read_input_audio_token_cost = _parse_cache_read_input_audio_token_cost(d.pop("cache_read_input_audio_token_cost", UNSET))


        def _parse_input_cost_per_character(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_character = _parse_input_cost_per_character(d.pop("input_cost_per_character", UNSET))


        def _parse_input_cost_per_character_above_128k_tokens(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_character_above_128k_tokens = _parse_input_cost_per_character_above_128k_tokens(d.pop("input_cost_per_character_above_128k_tokens", UNSET))


        def _parse_input_cost_per_audio_token(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_audio_token = _parse_input_cost_per_audio_token(d.pop("input_cost_per_audio_token", UNSET))


        def _parse_input_cost_per_token_cache_hit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_token_cache_hit = _parse_input_cost_per_token_cache_hit(d.pop("input_cost_per_token_cache_hit", UNSET))


        def _parse_input_cost_per_token_above_128k_tokens(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_token_above_128k_tokens = _parse_input_cost_per_token_above_128k_tokens(d.pop("input_cost_per_token_above_128k_tokens", UNSET))


        def _parse_input_cost_per_token_above_200k_tokens(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_token_above_200k_tokens = _parse_input_cost_per_token_above_200k_tokens(d.pop("input_cost_per_token_above_200k_tokens", UNSET))


        def _parse_input_cost_per_query(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_query = _parse_input_cost_per_query(d.pop("input_cost_per_query", UNSET))


        def _parse_input_cost_per_image(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_image = _parse_input_cost_per_image(d.pop("input_cost_per_image", UNSET))


        def _parse_input_cost_per_image_above_128k_tokens(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_image_above_128k_tokens = _parse_input_cost_per_image_above_128k_tokens(d.pop("input_cost_per_image_above_128k_tokens", UNSET))


        def _parse_input_cost_per_audio_per_second(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_audio_per_second = _parse_input_cost_per_audio_per_second(d.pop("input_cost_per_audio_per_second", UNSET))


        def _parse_input_cost_per_audio_per_second_above_128k_tokens(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_audio_per_second_above_128k_tokens = _parse_input_cost_per_audio_per_second_above_128k_tokens(d.pop("input_cost_per_audio_per_second_above_128k_tokens", UNSET))


        def _parse_input_cost_per_video_per_second(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_video_per_second = _parse_input_cost_per_video_per_second(d.pop("input_cost_per_video_per_second", UNSET))


        def _parse_input_cost_per_video_per_second_above_128k_tokens(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_video_per_second_above_128k_tokens = _parse_input_cost_per_video_per_second_above_128k_tokens(d.pop("input_cost_per_video_per_second_above_128k_tokens", UNSET))


        def _parse_input_cost_per_video_per_second_above_15s_interval(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_video_per_second_above_15s_interval = _parse_input_cost_per_video_per_second_above_15s_interval(d.pop("input_cost_per_video_per_second_above_15s_interval", UNSET))


        def _parse_input_cost_per_video_per_second_above_8s_interval(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_video_per_second_above_8s_interval = _parse_input_cost_per_video_per_second_above_8s_interval(d.pop("input_cost_per_video_per_second_above_8s_interval", UNSET))


        def _parse_input_cost_per_token_batches(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_token_batches = _parse_input_cost_per_token_batches(d.pop("input_cost_per_token_batches", UNSET))


        def _parse_output_cost_per_token_batches(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_token_batches = _parse_output_cost_per_token_batches(d.pop("output_cost_per_token_batches", UNSET))


        def _parse_output_cost_per_token_flex(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_token_flex = _parse_output_cost_per_token_flex(d.pop("output_cost_per_token_flex", UNSET))


        def _parse_output_cost_per_token_priority(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_token_priority = _parse_output_cost_per_token_priority(d.pop("output_cost_per_token_priority", UNSET))


        def _parse_output_cost_per_character(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_character = _parse_output_cost_per_character(d.pop("output_cost_per_character", UNSET))


        def _parse_output_cost_per_audio_token(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_audio_token = _parse_output_cost_per_audio_token(d.pop("output_cost_per_audio_token", UNSET))


        def _parse_output_cost_per_token_above_128k_tokens(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_token_above_128k_tokens = _parse_output_cost_per_token_above_128k_tokens(d.pop("output_cost_per_token_above_128k_tokens", UNSET))


        def _parse_output_cost_per_token_above_200k_tokens(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_token_above_200k_tokens = _parse_output_cost_per_token_above_200k_tokens(d.pop("output_cost_per_token_above_200k_tokens", UNSET))


        def _parse_output_cost_per_character_above_128k_tokens(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_character_above_128k_tokens = _parse_output_cost_per_character_above_128k_tokens(d.pop("output_cost_per_character_above_128k_tokens", UNSET))


        def _parse_output_cost_per_image(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_image = _parse_output_cost_per_image(d.pop("output_cost_per_image", UNSET))


        def _parse_output_cost_per_image_token(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_image_token = _parse_output_cost_per_image_token(d.pop("output_cost_per_image_token", UNSET))


        def _parse_output_cost_per_reasoning_token(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_reasoning_token = _parse_output_cost_per_reasoning_token(d.pop("output_cost_per_reasoning_token", UNSET))


        def _parse_output_cost_per_video_per_second(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_video_per_second = _parse_output_cost_per_video_per_second(d.pop("output_cost_per_video_per_second", UNSET))


        def _parse_output_cost_per_audio_per_second(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_audio_per_second = _parse_output_cost_per_audio_per_second(d.pop("output_cost_per_audio_per_second", UNSET))


        def _parse_search_context_cost_per_query(data: object) -> LiteLLMParamsSearchContextCostPerQueryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                search_context_cost_per_query_type_0 = LiteLLMParamsSearchContextCostPerQueryType0.from_dict(data)



                return search_context_cost_per_query_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMParamsSearchContextCostPerQueryType0 | None | Unset, data)

        search_context_cost_per_query = _parse_search_context_cost_per_query(d.pop("search_context_cost_per_query", UNSET))


        def _parse_citation_cost_per_token(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        citation_cost_per_token = _parse_citation_cost_per_token(d.pop("citation_cost_per_token", UNSET))


        def _parse_tiered_pricing(data: object) -> list[LiteLLMParamsTieredPricingType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tiered_pricing_type_0 = []
                _tiered_pricing_type_0 = data
                for tiered_pricing_type_0_item_data in (_tiered_pricing_type_0):
                    tiered_pricing_type_0_item = LiteLLMParamsTieredPricingType0Item.from_dict(tiered_pricing_type_0_item_data)



                    tiered_pricing_type_0.append(tiered_pricing_type_0_item)

                return tiered_pricing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LiteLLMParamsTieredPricingType0Item] | None | Unset, data)

        tiered_pricing = _parse_tiered_pricing(d.pop("tiered_pricing", UNSET))


        def _parse_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))


        def _parse_api_base(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_base = _parse_api_base(d.pop("api_base", UNSET))


        def _parse_api_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_version = _parse_api_version(d.pop("api_version", UNSET))


        def _parse_vertex_project(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vertex_project = _parse_vertex_project(d.pop("vertex_project", UNSET))


        def _parse_vertex_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vertex_location = _parse_vertex_location(d.pop("vertex_location", UNSET))


        def _parse_vertex_credentials(data: object) -> LiteLLMParamsVertexCredentialsType1 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vertex_credentials_type_1 = LiteLLMParamsVertexCredentialsType1.from_dict(data)



                return vertex_credentials_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMParamsVertexCredentialsType1 | None | str | Unset, data)

        vertex_credentials = _parse_vertex_credentials(d.pop("vertex_credentials", UNSET))


        def _parse_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name = _parse_region_name(d.pop("region_name", UNSET))


        def _parse_aws_access_key_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_access_key_id = _parse_aws_access_key_id(d.pop("aws_access_key_id", UNSET))


        def _parse_aws_secret_access_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_secret_access_key = _parse_aws_secret_access_key(d.pop("aws_secret_access_key", UNSET))


        def _parse_aws_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_region_name = _parse_aws_region_name(d.pop("aws_region_name", UNSET))


        def _parse_aws_bedrock_runtime_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_bedrock_runtime_endpoint = _parse_aws_bedrock_runtime_endpoint(d.pop("aws_bedrock_runtime_endpoint", UNSET))


        def _parse_watsonx_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        watsonx_region_name = _parse_watsonx_region_name(d.pop("watsonx_region_name", UNSET))


        def _parse_custom_llm_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_llm_provider = _parse_custom_llm_provider(d.pop("custom_llm_provider", UNSET))


        def _parse_tpm(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tpm = _parse_tpm(d.pop("tpm", UNSET))


        def _parse_rpm(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rpm = _parse_rpm(d.pop("rpm", UNSET))


        def _parse_timeout(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        timeout = _parse_timeout(d.pop("timeout", UNSET))


        def _parse_stream_timeout(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        stream_timeout = _parse_stream_timeout(d.pop("stream_timeout", UNSET))


        def _parse_max_retries(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_retries = _parse_max_retries(d.pop("max_retries", UNSET))


        def _parse_organization(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization = _parse_organization(d.pop("organization", UNSET))


        def _parse_configurable_clientside_auth_params(data: object) -> list[ConfigurableClientsideParamsCustomAuth | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                configurable_clientside_auth_params_type_0 = []
                _configurable_clientside_auth_params_type_0 = data
                for configurable_clientside_auth_params_type_0_item_data in (_configurable_clientside_auth_params_type_0):
                    def _parse_configurable_clientside_auth_params_type_0_item(data: object) -> ConfigurableClientsideParamsCustomAuth | str:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            configurable_clientside_auth_params_type_0_item_type_1 = ConfigurableClientsideParamsCustomAuth.from_dict(data)



                            return configurable_clientside_auth_params_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(ConfigurableClientsideParamsCustomAuth | str, data)

                    configurable_clientside_auth_params_type_0_item = _parse_configurable_clientside_auth_params_type_0_item(configurable_clientside_auth_params_type_0_item_data)

                    configurable_clientside_auth_params_type_0.append(configurable_clientside_auth_params_type_0_item)

                return configurable_clientside_auth_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ConfigurableClientsideParamsCustomAuth | str] | None | Unset, data)

        configurable_clientside_auth_params = _parse_configurable_clientside_auth_params(d.pop("configurable_clientside_auth_params", UNSET))


        def _parse_litellm_credential_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        litellm_credential_name = _parse_litellm_credential_name(d.pop("litellm_credential_name", UNSET))


        def _parse_litellm_trace_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        litellm_trace_id = _parse_litellm_trace_id(d.pop("litellm_trace_id", UNSET))


        def _parse_max_file_size_mb(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_file_size_mb = _parse_max_file_size_mb(d.pop("max_file_size_mb", UNSET))


        def _parse_max_budget(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_budget = _parse_max_budget(d.pop("max_budget", UNSET))


        def _parse_budget_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))


        def _parse_use_in_pass_through(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_in_pass_through = _parse_use_in_pass_through(d.pop("use_in_pass_through", UNSET))


        def _parse_use_litellm_proxy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_litellm_proxy = _parse_use_litellm_proxy(d.pop("use_litellm_proxy", UNSET))


        def _parse_merge_reasoning_content_in_choices(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        merge_reasoning_content_in_choices = _parse_merge_reasoning_content_in_choices(d.pop("merge_reasoning_content_in_choices", UNSET))


        def _parse_model_info(data: object) -> LiteLLMParamsModelInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_info_type_0 = LiteLLMParamsModelInfoType0.from_dict(data)



                return model_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMParamsModelInfoType0 | None | Unset, data)

        model_info = _parse_model_info(d.pop("model_info", UNSET))


        def _parse_mock_response(data: object) -> Any | ModelResponse | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mock_response_type_1 = ModelResponse.from_dict(data)



                return mock_response_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Any | ModelResponse | None | str | Unset, data)

        mock_response = _parse_mock_response(d.pop("mock_response", UNSET))


        def _parse_auto_router_config_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auto_router_config_path = _parse_auto_router_config_path(d.pop("auto_router_config_path", UNSET))


        def _parse_auto_router_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auto_router_config = _parse_auto_router_config(d.pop("auto_router_config", UNSET))


        def _parse_auto_router_default_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auto_router_default_model = _parse_auto_router_default_model(d.pop("auto_router_default_model", UNSET))


        def _parse_auto_router_embedding_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auto_router_embedding_model = _parse_auto_router_embedding_model(d.pop("auto_router_embedding_model", UNSET))


        def _parse_s3_bucket_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s3_bucket_name = _parse_s3_bucket_name(d.pop("s3_bucket_name", UNSET))


        def _parse_s3_encryption_key_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s3_encryption_key_id = _parse_s3_encryption_key_id(d.pop("s3_encryption_key_id", UNSET))


        def _parse_gcs_bucket_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gcs_bucket_name = _parse_gcs_bucket_name(d.pop("gcs_bucket_name", UNSET))


        def _parse_vector_store_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vector_store_id = _parse_vector_store_id(d.pop("vector_store_id", UNSET))


        def _parse_milvus_text_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        milvus_text_field = _parse_milvus_text_field(d.pop("milvus_text_field", UNSET))


        lite_llm_params = cls(
            model=model,
            input_cost_per_token=input_cost_per_token,
            output_cost_per_token=output_cost_per_token,
            input_cost_per_second=input_cost_per_second,
            output_cost_per_second=output_cost_per_second,
            input_cost_per_pixel=input_cost_per_pixel,
            output_cost_per_pixel=output_cost_per_pixel,
            input_cost_per_token_flex=input_cost_per_token_flex,
            input_cost_per_token_priority=input_cost_per_token_priority,
            cache_creation_input_token_cost=cache_creation_input_token_cost,
            cache_creation_input_token_cost_above_1hr=cache_creation_input_token_cost_above_1hr,
            cache_creation_input_token_cost_above_200k_tokens=cache_creation_input_token_cost_above_200k_tokens,
            cache_creation_input_audio_token_cost=cache_creation_input_audio_token_cost,
            cache_read_input_token_cost=cache_read_input_token_cost,
            cache_read_input_token_cost_flex=cache_read_input_token_cost_flex,
            cache_read_input_token_cost_priority=cache_read_input_token_cost_priority,
            cache_read_input_token_cost_above_200k_tokens=cache_read_input_token_cost_above_200k_tokens,
            cache_read_input_audio_token_cost=cache_read_input_audio_token_cost,
            input_cost_per_character=input_cost_per_character,
            input_cost_per_character_above_128k_tokens=input_cost_per_character_above_128k_tokens,
            input_cost_per_audio_token=input_cost_per_audio_token,
            input_cost_per_token_cache_hit=input_cost_per_token_cache_hit,
            input_cost_per_token_above_128k_tokens=input_cost_per_token_above_128k_tokens,
            input_cost_per_token_above_200k_tokens=input_cost_per_token_above_200k_tokens,
            input_cost_per_query=input_cost_per_query,
            input_cost_per_image=input_cost_per_image,
            input_cost_per_image_above_128k_tokens=input_cost_per_image_above_128k_tokens,
            input_cost_per_audio_per_second=input_cost_per_audio_per_second,
            input_cost_per_audio_per_second_above_128k_tokens=input_cost_per_audio_per_second_above_128k_tokens,
            input_cost_per_video_per_second=input_cost_per_video_per_second,
            input_cost_per_video_per_second_above_128k_tokens=input_cost_per_video_per_second_above_128k_tokens,
            input_cost_per_video_per_second_above_15s_interval=input_cost_per_video_per_second_above_15s_interval,
            input_cost_per_video_per_second_above_8s_interval=input_cost_per_video_per_second_above_8s_interval,
            input_cost_per_token_batches=input_cost_per_token_batches,
            output_cost_per_token_batches=output_cost_per_token_batches,
            output_cost_per_token_flex=output_cost_per_token_flex,
            output_cost_per_token_priority=output_cost_per_token_priority,
            output_cost_per_character=output_cost_per_character,
            output_cost_per_audio_token=output_cost_per_audio_token,
            output_cost_per_token_above_128k_tokens=output_cost_per_token_above_128k_tokens,
            output_cost_per_token_above_200k_tokens=output_cost_per_token_above_200k_tokens,
            output_cost_per_character_above_128k_tokens=output_cost_per_character_above_128k_tokens,
            output_cost_per_image=output_cost_per_image,
            output_cost_per_image_token=output_cost_per_image_token,
            output_cost_per_reasoning_token=output_cost_per_reasoning_token,
            output_cost_per_video_per_second=output_cost_per_video_per_second,
            output_cost_per_audio_per_second=output_cost_per_audio_per_second,
            search_context_cost_per_query=search_context_cost_per_query,
            citation_cost_per_token=citation_cost_per_token,
            tiered_pricing=tiered_pricing,
            api_key=api_key,
            api_base=api_base,
            api_version=api_version,
            vertex_project=vertex_project,
            vertex_location=vertex_location,
            vertex_credentials=vertex_credentials,
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_region_name=aws_region_name,
            aws_bedrock_runtime_endpoint=aws_bedrock_runtime_endpoint,
            watsonx_region_name=watsonx_region_name,
            custom_llm_provider=custom_llm_provider,
            tpm=tpm,
            rpm=rpm,
            timeout=timeout,
            stream_timeout=stream_timeout,
            max_retries=max_retries,
            organization=organization,
            configurable_clientside_auth_params=configurable_clientside_auth_params,
            litellm_credential_name=litellm_credential_name,
            litellm_trace_id=litellm_trace_id,
            max_file_size_mb=max_file_size_mb,
            max_budget=max_budget,
            budget_duration=budget_duration,
            use_in_pass_through=use_in_pass_through,
            use_litellm_proxy=use_litellm_proxy,
            merge_reasoning_content_in_choices=merge_reasoning_content_in_choices,
            model_info=model_info,
            mock_response=mock_response,
            auto_router_config_path=auto_router_config_path,
            auto_router_config=auto_router_config,
            auto_router_default_model=auto_router_default_model,
            auto_router_embedding_model=auto_router_embedding_model,
            s3_bucket_name=s3_bucket_name,
            s3_encryption_key_id=s3_encryption_key_id,
            gcs_bucket_name=gcs_bucket_name,
            vector_store_id=vector_store_id,
            milvus_text_field=milvus_text_field,
        )


        lite_llm_params.additional_properties = d
        return lite_llm_params

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
