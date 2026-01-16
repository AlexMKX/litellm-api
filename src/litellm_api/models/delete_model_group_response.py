from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DeleteModelGroupResponse")



@_attrs_define
class DeleteModelGroupResponse:
    """ 
        Attributes:
            access_group (str):
            models_updated (int):
            message (str):
     """

    access_group: str
    models_updated: int
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        access_group = self.access_group

        models_updated = self.models_updated

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "access_group": access_group,
            "models_updated": models_updated,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_group = d.pop("access_group")

        models_updated = d.pop("models_updated")

        message = d.pop("message")

        delete_model_group_response = cls(
            access_group=access_group,
            models_updated=models_updated,
            message=message,
        )


        delete_model_group_response.additional_properties = d
        return delete_model_group_response

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
