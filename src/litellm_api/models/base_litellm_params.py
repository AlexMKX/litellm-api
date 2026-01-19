from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.base_litellm_params_additional_provider_specific_params_type_0 import BaseLitellmParamsAdditionalProviderSpecificParamsType0
  from ..models.base_litellm_params_detect_secrets_config_type_0 import BaseLitellmParamsDetectSecretsConfigType0
  from ..models.lakera_category_thresholds import LakeraCategoryThresholds





T = TypeVar("T", bound="BaseLitellmParams")



@_attrs_define
class BaseLitellmParams:
    """ 
        Attributes:
            api_key (None | str | Unset): API key for the guardrail service
            api_base (None | str | Unset): Base URL for the guardrail service API
            experimental_use_latest_role_message_only (bool | None | Unset): When True, guardrails only receive the latest
                message for the relevant role (e.g., newest user input pre-call, newest assistant output post-call) Default:
                False.
            category_thresholds (LakeraCategoryThresholds | None | Unset): Threshold configuration for Lakera guardrail
                categories
            detect_secrets_config (BaseLitellmParamsDetectSecretsConfigType0 | None | Unset): Configuration for detect-
                secrets guardrail
            guard_name (None | str | Unset): Name of the guardrail in guardrails.ai
            default_on (bool | None | Unset): Whether the guardrail is enabled by default
            mask_request_content (bool | None | Unset): Will mask request content if guardrail makes any changes
            mask_response_content (bool | None | Unset): Will mask response content if guardrail makes any changes
            pangea_input_recipe (None | str | Unset): Recipe for input (LLM request)
            pangea_output_recipe (None | str | Unset): Recipe for output (LLM response)
            model (None | str | Unset): Optional field if guardrail requires a 'model' parameter
            violation_message_template (None | str | Unset): Custom message when a guardrail blocks an action. Supports
                placeholders like {tool_name}, {rule_id}, and {default_message}.
            template_id (None | str | Unset): The ID of your Model Armor template
            location (None | str | Unset): Google Cloud location/region (e.g., us-central1)
            credentials (None | str | Unset): Path to Google Cloud credentials JSON file or JSON string
            api_endpoint (None | str | Unset): Optional custom API endpoint for Model Armor
            fail_on_error (bool | None | Unset): Whether to fail the request if Model Armor encounters an error Default:
                True.
            additional_provider_specific_params (BaseLitellmParamsAdditionalProviderSpecificParamsType0 | None | Unset):
                Additional provider-specific parameters for generic guardrail APIs
     """

    api_key: None | str | Unset = UNSET
    api_base: None | str | Unset = UNSET
    experimental_use_latest_role_message_only: bool | None | Unset = False
    category_thresholds: LakeraCategoryThresholds | None | Unset = UNSET
    detect_secrets_config: BaseLitellmParamsDetectSecretsConfigType0 | None | Unset = UNSET
    guard_name: None | str | Unset = UNSET
    default_on: bool | None | Unset = UNSET
    mask_request_content: bool | None | Unset = UNSET
    mask_response_content: bool | None | Unset = UNSET
    pangea_input_recipe: None | str | Unset = UNSET
    pangea_output_recipe: None | str | Unset = UNSET
    model: None | str | Unset = UNSET
    violation_message_template: None | str | Unset = UNSET
    template_id: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    credentials: None | str | Unset = UNSET
    api_endpoint: None | str | Unset = UNSET
    fail_on_error: bool | None | Unset = True
    additional_provider_specific_params: BaseLitellmParamsAdditionalProviderSpecificParamsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.base_litellm_params_detect_secrets_config_type_0 import BaseLitellmParamsDetectSecretsConfigType0
        from ..models.lakera_category_thresholds import LakeraCategoryThresholds
        from ..models.base_litellm_params_additional_provider_specific_params_type_0 import BaseLitellmParamsAdditionalProviderSpecificParamsType0
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

        experimental_use_latest_role_message_only: bool | None | Unset
        if isinstance(self.experimental_use_latest_role_message_only, Unset):
            experimental_use_latest_role_message_only = UNSET
        else:
            experimental_use_latest_role_message_only = self.experimental_use_latest_role_message_only

        category_thresholds: dict[str, Any] | None | Unset
        if isinstance(self.category_thresholds, Unset):
            category_thresholds = UNSET
        elif isinstance(self.category_thresholds, LakeraCategoryThresholds):
            category_thresholds = self.category_thresholds.to_dict()
        else:
            category_thresholds = self.category_thresholds

        detect_secrets_config: dict[str, Any] | None | Unset
        if isinstance(self.detect_secrets_config, Unset):
            detect_secrets_config = UNSET
        elif isinstance(self.detect_secrets_config, BaseLitellmParamsDetectSecretsConfigType0):
            detect_secrets_config = self.detect_secrets_config.to_dict()
        else:
            detect_secrets_config = self.detect_secrets_config

        guard_name: None | str | Unset
        if isinstance(self.guard_name, Unset):
            guard_name = UNSET
        else:
            guard_name = self.guard_name

        default_on: bool | None | Unset
        if isinstance(self.default_on, Unset):
            default_on = UNSET
        else:
            default_on = self.default_on

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

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        violation_message_template: None | str | Unset
        if isinstance(self.violation_message_template, Unset):
            violation_message_template = UNSET
        else:
            violation_message_template = self.violation_message_template

        template_id: None | str | Unset
        if isinstance(self.template_id, Unset):
            template_id = UNSET
        else:
            template_id = self.template_id

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        credentials: None | str | Unset
        if isinstance(self.credentials, Unset):
            credentials = UNSET
        else:
            credentials = self.credentials

        api_endpoint: None | str | Unset
        if isinstance(self.api_endpoint, Unset):
            api_endpoint = UNSET
        else:
            api_endpoint = self.api_endpoint

        fail_on_error: bool | None | Unset
        if isinstance(self.fail_on_error, Unset):
            fail_on_error = UNSET
        else:
            fail_on_error = self.fail_on_error

        additional_provider_specific_params: dict[str, Any] | None | Unset
        if isinstance(self.additional_provider_specific_params, Unset):
            additional_provider_specific_params = UNSET
        elif isinstance(self.additional_provider_specific_params, BaseLitellmParamsAdditionalProviderSpecificParamsType0):
            additional_provider_specific_params = self.additional_provider_specific_params.to_dict()
        else:
            additional_provider_specific_params = self.additional_provider_specific_params


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if api_base is not UNSET:
            field_dict["api_base"] = api_base
        if experimental_use_latest_role_message_only is not UNSET:
            field_dict["experimental_use_latest_role_message_only"] = experimental_use_latest_role_message_only
        if category_thresholds is not UNSET:
            field_dict["category_thresholds"] = category_thresholds
        if detect_secrets_config is not UNSET:
            field_dict["detect_secrets_config"] = detect_secrets_config
        if guard_name is not UNSET:
            field_dict["guard_name"] = guard_name
        if default_on is not UNSET:
            field_dict["default_on"] = default_on
        if mask_request_content is not UNSET:
            field_dict["mask_request_content"] = mask_request_content
        if mask_response_content is not UNSET:
            field_dict["mask_response_content"] = mask_response_content
        if pangea_input_recipe is not UNSET:
            field_dict["pangea_input_recipe"] = pangea_input_recipe
        if pangea_output_recipe is not UNSET:
            field_dict["pangea_output_recipe"] = pangea_output_recipe
        if model is not UNSET:
            field_dict["model"] = model
        if violation_message_template is not UNSET:
            field_dict["violation_message_template"] = violation_message_template
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if location is not UNSET:
            field_dict["location"] = location
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if api_endpoint is not UNSET:
            field_dict["api_endpoint"] = api_endpoint
        if fail_on_error is not UNSET:
            field_dict["fail_on_error"] = fail_on_error
        if additional_provider_specific_params is not UNSET:
            field_dict["additional_provider_specific_params"] = additional_provider_specific_params

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_litellm_params_additional_provider_specific_params_type_0 import BaseLitellmParamsAdditionalProviderSpecificParamsType0
        from ..models.base_litellm_params_detect_secrets_config_type_0 import BaseLitellmParamsDetectSecretsConfigType0
        from ..models.lakera_category_thresholds import LakeraCategoryThresholds
        d = dict(src_dict)
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


        def _parse_experimental_use_latest_role_message_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        experimental_use_latest_role_message_only = _parse_experimental_use_latest_role_message_only(d.pop("experimental_use_latest_role_message_only", UNSET))


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


        def _parse_detect_secrets_config(data: object) -> BaseLitellmParamsDetectSecretsConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                detect_secrets_config_type_0 = BaseLitellmParamsDetectSecretsConfigType0.from_dict(data)



                return detect_secrets_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BaseLitellmParamsDetectSecretsConfigType0 | None | Unset, data)

        detect_secrets_config = _parse_detect_secrets_config(d.pop("detect_secrets_config", UNSET))


        def _parse_guard_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guard_name = _parse_guard_name(d.pop("guard_name", UNSET))


        def _parse_default_on(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        default_on = _parse_default_on(d.pop("default_on", UNSET))


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


        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        def _parse_violation_message_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        violation_message_template = _parse_violation_message_template(d.pop("violation_message_template", UNSET))


        def _parse_template_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_id = _parse_template_id(d.pop("template_id", UNSET))


        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))


        def _parse_credentials(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        credentials = _parse_credentials(d.pop("credentials", UNSET))


        def _parse_api_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_endpoint = _parse_api_endpoint(d.pop("api_endpoint", UNSET))


        def _parse_fail_on_error(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        fail_on_error = _parse_fail_on_error(d.pop("fail_on_error", UNSET))


        def _parse_additional_provider_specific_params(data: object) -> BaseLitellmParamsAdditionalProviderSpecificParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                additional_provider_specific_params_type_0 = BaseLitellmParamsAdditionalProviderSpecificParamsType0.from_dict(data)



                return additional_provider_specific_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BaseLitellmParamsAdditionalProviderSpecificParamsType0 | None | Unset, data)

        additional_provider_specific_params = _parse_additional_provider_specific_params(d.pop("additional_provider_specific_params", UNSET))


        base_litellm_params = cls(
            api_key=api_key,
            api_base=api_base,
            experimental_use_latest_role_message_only=experimental_use_latest_role_message_only,
            category_thresholds=category_thresholds,
            detect_secrets_config=detect_secrets_config,
            guard_name=guard_name,
            default_on=default_on,
            mask_request_content=mask_request_content,
            mask_response_content=mask_response_content,
            pangea_input_recipe=pangea_input_recipe,
            pangea_output_recipe=pangea_output_recipe,
            model=model,
            violation_message_template=violation_message_template,
            template_id=template_id,
            location=location,
            credentials=credentials,
            api_endpoint=api_endpoint,
            fail_on_error=fail_on_error,
            additional_provider_specific_params=additional_provider_specific_params,
        )


        base_litellm_params.additional_properties = d
        return base_litellm_params

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
