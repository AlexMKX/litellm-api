from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.bulk_update_key_request_item import BulkUpdateKeyRequestItem





T = TypeVar("T", bound="BulkUpdateKeyRequest")



@_attrs_define
class BulkUpdateKeyRequest:
    """ Request for bulk key updates

        Attributes:
            keys (list[BulkUpdateKeyRequestItem]):
     """

    keys: list[BulkUpdateKeyRequestItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_update_key_request_item import BulkUpdateKeyRequestItem
        keys = []
        for keys_item_data in self.keys:
            keys_item = keys_item_data.to_dict()
            keys.append(keys_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "keys": keys,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_update_key_request_item import BulkUpdateKeyRequestItem
        d = dict(src_dict)
        keys = []
        _keys = d.pop("keys")
        for keys_item_data in (_keys):
            keys_item = BulkUpdateKeyRequestItem.from_dict(keys_item_data)



            keys.append(keys_item)


        bulk_update_key_request = cls(
            keys=keys,
        )


        bulk_update_key_request.additional_properties = d
        return bulk_update_key_request

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
