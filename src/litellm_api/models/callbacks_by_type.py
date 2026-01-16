from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="CallbacksByType")



@_attrs_define
class CallbacksByType:
    """ 
        Attributes:
            success (list[str]):
            failure (list[str]):
            success_and_failure (list[str]):
     """

    success: list[str]
    failure: list[str]
    success_and_failure: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        success = self.success



        failure = self.failure



        success_and_failure = self.success_and_failure




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "success": success,
            "failure": failure,
            "success_and_failure": success_and_failure,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = cast(list[str], d.pop("success"))


        failure = cast(list[str], d.pop("failure"))


        success_and_failure = cast(list[str], d.pop("success_and_failure"))


        callbacks_by_type = cls(
            success=success,
            failure=failure,
            success_and_failure=success_and_failure,
        )


        callbacks_by_type.additional_properties = d
        return callbacks_by_type

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
