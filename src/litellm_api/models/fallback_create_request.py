from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.fallback_create_request_fallback_type import FallbackCreateRequestFallbackType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="FallbackCreateRequest")



@_attrs_define
class FallbackCreateRequest:
    """ Request model for creating/updating fallbacks

        Attributes:
            model (str): The model name to configure fallbacks for (e.g., 'gpt-3.5-turbo')
            fallback_models (list[str]): List of fallback model names in order of priority
            fallback_type (FallbackCreateRequestFallbackType | Unset): Type of fallback: 'general' (default),
                'context_window', or 'content_policy' Default: FallbackCreateRequestFallbackType.GENERAL.
     """

    model: str
    fallback_models: list[str]
    fallback_type: FallbackCreateRequestFallbackType | Unset = FallbackCreateRequestFallbackType.GENERAL
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        model = self.model

        fallback_models = self.fallback_models



        fallback_type: str | Unset = UNSET
        if not isinstance(self.fallback_type, Unset):
            fallback_type = self.fallback_type.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "model": model,
            "fallback_models": fallback_models,
        })
        if fallback_type is not UNSET:
            field_dict["fallback_type"] = fallback_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        fallback_models = cast(list[str], d.pop("fallback_models"))


        _fallback_type = d.pop("fallback_type", UNSET)
        fallback_type: FallbackCreateRequestFallbackType | Unset
        if isinstance(_fallback_type,  Unset):
            fallback_type = UNSET
        else:
            fallback_type = FallbackCreateRequestFallbackType(_fallback_type)




        fallback_create_request = cls(
            model=model,
            fallback_models=fallback_models,
            fallback_type=fallback_type,
        )


        fallback_create_request.additional_properties = d
        return fallback_create_request

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
