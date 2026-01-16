from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.user_update_result import UserUpdateResult





T = TypeVar("T", bound="BulkUpdateUserResponse")



@_attrs_define
class BulkUpdateUserResponse:
    """ Response for bulk user update operations

        Attributes:
            results (list[UserUpdateResult]):
            total_requested (int):
            successful_updates (int):
            failed_updates (int):
     """

    results: list[UserUpdateResult]
    total_requested: int
    successful_updates: int
    failed_updates: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_update_result import UserUpdateResult
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)



        total_requested = self.total_requested

        successful_updates = self.successful_updates

        failed_updates = self.failed_updates


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "results": results,
            "total_requested": total_requested,
            "successful_updates": successful_updates,
            "failed_updates": failed_updates,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_update_result import UserUpdateResult
        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in (_results):
            results_item = UserUpdateResult.from_dict(results_item_data)



            results.append(results_item)


        total_requested = d.pop("total_requested")

        successful_updates = d.pop("successful_updates")

        failed_updates = d.pop("failed_updates")

        bulk_update_user_response = cls(
            results=results,
            total_requested=total_requested,
            successful_updates=successful_updates,
            failed_updates=failed_updates,
        )


        bulk_update_user_response.additional_properties = d
        return bulk_update_user_response

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
