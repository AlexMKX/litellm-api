from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.usage_log_entry import UsageLogEntry





T = TypeVar("T", bound="UsageLogsResponse")



@_attrs_define
class UsageLogsResponse:
    """ 
        Attributes:
            logs (list[UsageLogEntry]):
            page (int):
            page_size (int):
            total (int):
     """

    logs: list[UsageLogEntry]
    page: int
    page_size: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.usage_log_entry import UsageLogEntry
        logs = []
        for logs_item_data in self.logs:
            logs_item = logs_item_data.to_dict()
            logs.append(logs_item)



        page = self.page

        page_size = self.page_size

        total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "logs": logs,
            "page": page,
            "page_size": page_size,
            "total": total,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_log_entry import UsageLogEntry
        d = dict(src_dict)
        logs = []
        _logs = d.pop("logs")
        for logs_item_data in (_logs):
            logs_item = UsageLogEntry.from_dict(logs_item_data)



            logs.append(logs_item)


        page = d.pop("page")

        page_size = d.pop("page_size")

        total = d.pop("total")

        usage_logs_response = cls(
            logs=logs,
            page=page,
            page_size=page_size,
            total=total,
        )


        usage_logs_response.additional_properties = d
        return usage_logs_response

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
