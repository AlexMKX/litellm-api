from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="FallbackGetResponse")



@_attrs_define
class FallbackGetResponse:
    """ Response model for getting fallbacks

        Attributes:
            model (str): The model name
            fallback_models (list[str]): List of fallback model names
            fallback_type (str): Type of fallback
     """

    model: str
    fallback_models: list[str]
    fallback_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        model = self.model

        fallback_models = self.fallback_models



        fallback_type = self.fallback_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "model": model,
            "fallback_models": fallback_models,
            "fallback_type": fallback_type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        fallback_models = cast(list[str], d.pop("fallback_models"))


        fallback_type = d.pop("fallback_type")

        fallback_get_response = cls(
            model=model,
            fallback_models=fallback_models,
            fallback_type=fallback_type,
        )


        fallback_get_response.additional_properties = d
        return fallback_get_response

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
