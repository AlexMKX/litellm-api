from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.prompt_info_prompt_type import PromptInfoPromptType






T = TypeVar("T", bound="PromptInfo")



@_attrs_define
class PromptInfo:
    """ 
        Attributes:
            prompt_type (PromptInfoPromptType):
     """

    prompt_type: PromptInfoPromptType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        prompt_type = self.prompt_type.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "prompt_type": prompt_type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prompt_type = PromptInfoPromptType(d.pop("prompt_type"))




        prompt_info = cls(
            prompt_type=prompt_type,
        )


        prompt_info.additional_properties = d
        return prompt_info

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
