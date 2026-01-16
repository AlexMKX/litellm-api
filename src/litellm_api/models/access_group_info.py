from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AccessGroupInfo")



@_attrs_define
class AccessGroupInfo:
    """ 
        Attributes:
            access_group (str):
            model_names (list[str]):
            deployment_count (int):
     """

    access_group: str
    model_names: list[str]
    deployment_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        access_group = self.access_group

        model_names = self.model_names



        deployment_count = self.deployment_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "access_group": access_group,
            "model_names": model_names,
            "deployment_count": deployment_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_group = d.pop("access_group")

        model_names = cast(list[str], d.pop("model_names"))


        deployment_count = d.pop("deployment_count")

        access_group_info = cls(
            access_group=access_group,
            model_names=model_names,
            deployment_count=deployment_count,
        )


        access_group_info.additional_properties = d
        return access_group_info

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
