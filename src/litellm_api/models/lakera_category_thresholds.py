from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="LakeraCategoryThresholds")



@_attrs_define
class LakeraCategoryThresholds:
    """ 
        Attributes:
            jailbreak (float | Unset):
            prompt_injection (float | Unset):
     """

    jailbreak: float | Unset = UNSET
    prompt_injection: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        jailbreak = self.jailbreak

        prompt_injection = self.prompt_injection


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if jailbreak is not UNSET:
            field_dict["jailbreak"] = jailbreak
        if prompt_injection is not UNSET:
            field_dict["prompt_injection"] = prompt_injection

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        jailbreak = d.pop("jailbreak", UNSET)

        prompt_injection = d.pop("prompt_injection", UNSET)

        lakera_category_thresholds = cls(
            jailbreak=jailbreak,
            prompt_injection=prompt_injection,
        )


        lakera_category_thresholds.additional_properties = d
        return lakera_category_thresholds

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
