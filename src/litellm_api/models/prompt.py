from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.prompt_info import PromptInfo
  from ..models.prompt_lite_llm_params import PromptLiteLLMParams





T = TypeVar("T", bound="Prompt")



@_attrs_define
class Prompt:
    """ 
        Attributes:
            prompt_id (str):
            litellm_params (PromptLiteLLMParams):
            prompt_info (None | PromptInfo | Unset):
     """

    prompt_id: str
    litellm_params: PromptLiteLLMParams
    prompt_info: None | PromptInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_info import PromptInfo
        from ..models.prompt_lite_llm_params import PromptLiteLLMParams
        prompt_id = self.prompt_id

        litellm_params = self.litellm_params.to_dict()

        prompt_info: dict[str, Any] | None | Unset
        if isinstance(self.prompt_info, Unset):
            prompt_info = UNSET
        elif isinstance(self.prompt_info, PromptInfo):
            prompt_info = self.prompt_info.to_dict()
        else:
            prompt_info = self.prompt_info


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "prompt_id": prompt_id,
            "litellm_params": litellm_params,
        })
        if prompt_info is not UNSET:
            field_dict["prompt_info"] = prompt_info

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_info import PromptInfo
        from ..models.prompt_lite_llm_params import PromptLiteLLMParams
        d = dict(src_dict)
        prompt_id = d.pop("prompt_id")

        litellm_params = PromptLiteLLMParams.from_dict(d.pop("litellm_params"))




        def _parse_prompt_info(data: object) -> None | PromptInfo | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                prompt_info_type_0 = PromptInfo.from_dict(data)



                return prompt_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PromptInfo | Unset, data)

        prompt_info = _parse_prompt_info(d.pop("prompt_info", UNSET))


        prompt = cls(
            prompt_id=prompt_id,
            litellm_params=litellm_params,
            prompt_info=prompt_info,
        )


        prompt.additional_properties = d
        return prompt

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
