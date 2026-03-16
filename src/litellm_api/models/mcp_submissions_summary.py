from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.lite_llmmcp_server_table import LiteLLMMCPServerTable





T = TypeVar("T", bound="MCPSubmissionsSummary")



@_attrs_define
class MCPSubmissionsSummary:
    """ 
        Attributes:
            total (int):
            pending_review (int):
            active (int):
            rejected (int):
            items (list[LiteLLMMCPServerTable]):
     """

    total: int
    pending_review: int
    active: int
    rejected: int
    items: list[LiteLLMMCPServerTable]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llmmcp_server_table import LiteLLMMCPServerTable
        total = self.total

        pending_review = self.pending_review

        active = self.active

        rejected = self.rejected

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "total": total,
            "pending_review": pending_review,
            "active": active,
            "rejected": rejected,
            "items": items,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llmmcp_server_table import LiteLLMMCPServerTable
        d = dict(src_dict)
        total = d.pop("total")

        pending_review = d.pop("pending_review")

        active = d.pop("active")

        rejected = d.pop("rejected")

        items = []
        _items = d.pop("items")
        for items_item_data in (_items):
            items_item = LiteLLMMCPServerTable.from_dict(items_item_data)



            items.append(items_item)


        mcp_submissions_summary = cls(
            total=total,
            pending_review=pending_review,
            active=active,
            rejected=rejected,
            items=items,
        )


        mcp_submissions_summary.additional_properties = d
        return mcp_submissions_summary

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
