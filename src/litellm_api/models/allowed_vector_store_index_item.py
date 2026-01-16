from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.allowed_vector_store_index_item_index_permissions_item import AllowedVectorStoreIndexItemIndexPermissionsItem
from typing import cast






T = TypeVar("T", bound="AllowedVectorStoreIndexItem")



@_attrs_define
class AllowedVectorStoreIndexItem:
    """ 
        Attributes:
            index_name (str):
            index_permissions (list[AllowedVectorStoreIndexItemIndexPermissionsItem]):
     """

    index_name: str
    index_permissions: list[AllowedVectorStoreIndexItemIndexPermissionsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        index_name = self.index_name

        index_permissions = []
        for index_permissions_item_data in self.index_permissions:
            index_permissions_item = index_permissions_item_data.value
            index_permissions.append(index_permissions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "index_name": index_name,
            "index_permissions": index_permissions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index_name = d.pop("index_name")

        index_permissions = []
        _index_permissions = d.pop("index_permissions")
        for index_permissions_item_data in (_index_permissions):
            index_permissions_item = AllowedVectorStoreIndexItemIndexPermissionsItem(index_permissions_item_data)



            index_permissions.append(index_permissions_item)


        allowed_vector_store_index_item = cls(
            index_name=index_name,
            index_permissions=index_permissions,
        )


        allowed_vector_store_index_item.additional_properties = d
        return allowed_vector_store_index_item

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
