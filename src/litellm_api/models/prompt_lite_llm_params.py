from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.prompt_lite_llm_params_provider_specific_query_params_type_0 import PromptLiteLLMParamsProviderSpecificQueryParamsType0





T = TypeVar("T", bound="PromptLiteLLMParams")



@_attrs_define
class PromptLiteLLMParams:
    """ 
        Attributes:
            prompt_integration (str):
            prompt_id (None | str | Unset):
            api_base (None | str | Unset):
            api_key (None | str | Unset):
            provider_specific_query_params (None | PromptLiteLLMParamsProviderSpecificQueryParamsType0 | Unset):
            ignore_prompt_manager_model (bool | None | Unset):  Default: False.
            ignore_prompt_manager_optional_params (bool | None | Unset):  Default: False.
            dotprompt_content (None | str | Unset):
     """

    prompt_integration: str
    prompt_id: None | str | Unset = UNSET
    api_base: None | str | Unset = UNSET
    api_key: None | str | Unset = UNSET
    provider_specific_query_params: None | PromptLiteLLMParamsProviderSpecificQueryParamsType0 | Unset = UNSET
    ignore_prompt_manager_model: bool | None | Unset = False
    ignore_prompt_manager_optional_params: bool | None | Unset = False
    dotprompt_content: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_lite_llm_params_provider_specific_query_params_type_0 import PromptLiteLLMParamsProviderSpecificQueryParamsType0
        prompt_integration = self.prompt_integration

        prompt_id: None | str | Unset
        if isinstance(self.prompt_id, Unset):
            prompt_id = UNSET
        else:
            prompt_id = self.prompt_id

        api_base: None | str | Unset
        if isinstance(self.api_base, Unset):
            api_base = UNSET
        else:
            api_base = self.api_base

        api_key: None | str | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

        provider_specific_query_params: dict[str, Any] | None | Unset
        if isinstance(self.provider_specific_query_params, Unset):
            provider_specific_query_params = UNSET
        elif isinstance(self.provider_specific_query_params, PromptLiteLLMParamsProviderSpecificQueryParamsType0):
            provider_specific_query_params = self.provider_specific_query_params.to_dict()
        else:
            provider_specific_query_params = self.provider_specific_query_params

        ignore_prompt_manager_model: bool | None | Unset
        if isinstance(self.ignore_prompt_manager_model, Unset):
            ignore_prompt_manager_model = UNSET
        else:
            ignore_prompt_manager_model = self.ignore_prompt_manager_model

        ignore_prompt_manager_optional_params: bool | None | Unset
        if isinstance(self.ignore_prompt_manager_optional_params, Unset):
            ignore_prompt_manager_optional_params = UNSET
        else:
            ignore_prompt_manager_optional_params = self.ignore_prompt_manager_optional_params

        dotprompt_content: None | str | Unset
        if isinstance(self.dotprompt_content, Unset):
            dotprompt_content = UNSET
        else:
            dotprompt_content = self.dotprompt_content


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "prompt_integration": prompt_integration,
        })
        if prompt_id is not UNSET:
            field_dict["prompt_id"] = prompt_id
        if api_base is not UNSET:
            field_dict["api_base"] = api_base
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if provider_specific_query_params is not UNSET:
            field_dict["provider_specific_query_params"] = provider_specific_query_params
        if ignore_prompt_manager_model is not UNSET:
            field_dict["ignore_prompt_manager_model"] = ignore_prompt_manager_model
        if ignore_prompt_manager_optional_params is not UNSET:
            field_dict["ignore_prompt_manager_optional_params"] = ignore_prompt_manager_optional_params
        if dotprompt_content is not UNSET:
            field_dict["dotprompt_content"] = dotprompt_content

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_lite_llm_params_provider_specific_query_params_type_0 import PromptLiteLLMParamsProviderSpecificQueryParamsType0
        d = dict(src_dict)
        prompt_integration = d.pop("prompt_integration")

        def _parse_prompt_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt_id = _parse_prompt_id(d.pop("prompt_id", UNSET))


        def _parse_api_base(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_base = _parse_api_base(d.pop("api_base", UNSET))


        def _parse_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))


        def _parse_provider_specific_query_params(data: object) -> None | PromptLiteLLMParamsProviderSpecificQueryParamsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_specific_query_params_type_0 = PromptLiteLLMParamsProviderSpecificQueryParamsType0.from_dict(data)



                return provider_specific_query_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PromptLiteLLMParamsProviderSpecificQueryParamsType0 | Unset, data)

        provider_specific_query_params = _parse_provider_specific_query_params(d.pop("provider_specific_query_params", UNSET))


        def _parse_ignore_prompt_manager_model(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ignore_prompt_manager_model = _parse_ignore_prompt_manager_model(d.pop("ignore_prompt_manager_model", UNSET))


        def _parse_ignore_prompt_manager_optional_params(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ignore_prompt_manager_optional_params = _parse_ignore_prompt_manager_optional_params(d.pop("ignore_prompt_manager_optional_params", UNSET))


        def _parse_dotprompt_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dotprompt_content = _parse_dotprompt_content(d.pop("dotprompt_content", UNSET))


        prompt_lite_llm_params = cls(
            prompt_integration=prompt_integration,
            prompt_id=prompt_id,
            api_base=api_base,
            api_key=api_key,
            provider_specific_query_params=provider_specific_query_params,
            ignore_prompt_manager_model=ignore_prompt_manager_model,
            ignore_prompt_manager_optional_params=ignore_prompt_manager_optional_params,
            dotprompt_content=dotprompt_content,
        )


        prompt_lite_llm_params.additional_properties = d
        return prompt_lite_llm_params

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
