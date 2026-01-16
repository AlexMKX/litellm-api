from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.logging_callback_status_status import LoggingCallbackStatusStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="LoggingCallbackStatus")



@_attrs_define
class LoggingCallbackStatus:
    """ 
        Attributes:
            callbacks (list[str] | Unset):
            status (LoggingCallbackStatusStatus | Unset):
            details (None | str | Unset):
     """

    callbacks: list[str] | Unset = UNSET
    status: LoggingCallbackStatusStatus | Unset = UNSET
    details: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        callbacks: list[str] | Unset = UNSET
        if not isinstance(self.callbacks, Unset):
            callbacks = self.callbacks



        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        details: None | str | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        else:
            details = self.details


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if callbacks is not UNSET:
            field_dict["callbacks"] = callbacks
        if status is not UNSET:
            field_dict["status"] = status
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        callbacks = cast(list[str], d.pop("callbacks", UNSET))


        _status = d.pop("status", UNSET)
        status: LoggingCallbackStatusStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = LoggingCallbackStatusStatus(_status)




        def _parse_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        details = _parse_details(d.pop("details", UNSET))


        logging_callback_status = cls(
            callbacks=callbacks,
            status=status,
            details=details,
        )


        logging_callback_status.additional_properties = d
        return logging_callback_status

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
