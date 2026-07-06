from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.callback_log_record_status import CallbackLogRecordStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.callback_log_record_standard_logging_payload import CallbackLogRecordStandardLoggingPayload





T = TypeVar("T", bound="CallbackLogRecord")



@_attrs_define
class CallbackLogRecord:
    """ A single finished logging event to replay through the callbacks.

        Attributes:
            status (CallbackLogRecordStatus):
            standard_logging_payload (CallbackLogRecordStandardLoggingPayload):
            error (None | str | Unset):
     """

    status: CallbackLogRecordStatus
    standard_logging_payload: CallbackLogRecordStandardLoggingPayload
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.callback_log_record_standard_logging_payload import CallbackLogRecordStandardLoggingPayload
        status = self.status.value

        standard_logging_payload = self.standard_logging_payload.to_dict()

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "standard_logging_payload": standard_logging_payload,
        })
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.callback_log_record_standard_logging_payload import CallbackLogRecordStandardLoggingPayload
        d = dict(src_dict)
        status = CallbackLogRecordStatus(d.pop("status"))




        standard_logging_payload = CallbackLogRecordStandardLoggingPayload.from_dict(d.pop("standard_logging_payload"))




        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        callback_log_record = cls(
            status=status,
            standard_logging_payload=standard_logging_payload,
            error=error,
        )


        callback_log_record.additional_properties = d
        return callback_log_record

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
