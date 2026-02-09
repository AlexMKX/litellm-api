from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.failed_key_update import FailedKeyUpdate
  from ..models.successful_key_update import SuccessfulKeyUpdate





T = TypeVar("T", bound="BulkUpdateKeyResponse")



@_attrs_define
class BulkUpdateKeyResponse:
    """ Response for bulk key update operations

        Attributes:
            total_requested (int):
            successful_updates (list[SuccessfulKeyUpdate]):
            failed_updates (list[FailedKeyUpdate]):
     """

    total_requested: int
    successful_updates: list[SuccessfulKeyUpdate]
    failed_updates: list[FailedKeyUpdate]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.failed_key_update import FailedKeyUpdate
        from ..models.successful_key_update import SuccessfulKeyUpdate
        total_requested = self.total_requested

        successful_updates = []
        for successful_updates_item_data in self.successful_updates:
            successful_updates_item = successful_updates_item_data.to_dict()
            successful_updates.append(successful_updates_item)



        failed_updates = []
        for failed_updates_item_data in self.failed_updates:
            failed_updates_item = failed_updates_item_data.to_dict()
            failed_updates.append(failed_updates_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "total_requested": total_requested,
            "successful_updates": successful_updates,
            "failed_updates": failed_updates,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.failed_key_update import FailedKeyUpdate
        from ..models.successful_key_update import SuccessfulKeyUpdate
        d = dict(src_dict)
        total_requested = d.pop("total_requested")

        successful_updates = []
        _successful_updates = d.pop("successful_updates")
        for successful_updates_item_data in (_successful_updates):
            successful_updates_item = SuccessfulKeyUpdate.from_dict(successful_updates_item_data)



            successful_updates.append(successful_updates_item)


        failed_updates = []
        _failed_updates = d.pop("failed_updates")
        for failed_updates_item_data in (_failed_updates):
            failed_updates_item = FailedKeyUpdate.from_dict(failed_updates_item_data)



            failed_updates.append(failed_updates_item)


        bulk_update_key_response = cls(
            total_requested=total_requested,
            successful_updates=successful_updates,
            failed_updates=failed_updates,
        )


        bulk_update_key_response.additional_properties = d
        return bulk_update_key_response

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
