from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.callback_log_record import CallbackLogRecord





T = TypeVar("T", bound="CallbackLogsRequest")



@_attrs_define
class CallbackLogsRequest:
    """ A batch of logging events posted by an external producer.

        Attributes:
            records (list[CallbackLogRecord]):
     """

    records: list[CallbackLogRecord]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.callback_log_record import CallbackLogRecord
        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "records": records,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.callback_log_record import CallbackLogRecord
        d = dict(src_dict)
        records = []
        _records = d.pop("records")
        for records_item_data in (_records):
            records_item = CallbackLogRecord.from_dict(records_item_data)



            records.append(records_item)


        callback_logs_request = cls(
            records=records,
        )


        callback_logs_request.additional_properties = d
        return callback_logs_request

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
