from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.access_group_info import AccessGroupInfo





T = TypeVar("T", bound="ListAccessGroupsResponse")



@_attrs_define
class ListAccessGroupsResponse:
    """ 
        Attributes:
            access_groups (list[AccessGroupInfo]):
     """

    access_groups: list[AccessGroupInfo]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.access_group_info import AccessGroupInfo
        access_groups = []
        for access_groups_item_data in self.access_groups:
            access_groups_item = access_groups_item_data.to_dict()
            access_groups.append(access_groups_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "access_groups": access_groups,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.access_group_info import AccessGroupInfo
        d = dict(src_dict)
        access_groups = []
        _access_groups = d.pop("access_groups")
        for access_groups_item_data in (_access_groups):
            access_groups_item = AccessGroupInfo.from_dict(access_groups_item_data)



            access_groups.append(access_groups_item)


        list_access_groups_response = cls(
            access_groups=access_groups,
        )


        list_access_groups_response.additional_properties = d
        return list_access_groups_response

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
