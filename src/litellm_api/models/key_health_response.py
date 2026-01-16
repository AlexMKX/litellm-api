from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.key_health_response_key import KeyHealthResponseKey
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.logging_callback_status import LoggingCallbackStatus





T = TypeVar("T", bound="KeyHealthResponse")



@_attrs_define
class KeyHealthResponse:
    """ 
        Attributes:
            key (KeyHealthResponseKey | Unset):
            logging_callbacks (LoggingCallbackStatus | None | Unset):
     """

    key: KeyHealthResponseKey | Unset = UNSET
    logging_callbacks: LoggingCallbackStatus | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.logging_callback_status import LoggingCallbackStatus
        key: str | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.value


        logging_callbacks: dict[str, Any] | None | Unset
        if isinstance(self.logging_callbacks, Unset):
            logging_callbacks = UNSET
        elif isinstance(self.logging_callbacks, LoggingCallbackStatus):
            logging_callbacks = self.logging_callbacks.to_dict()
        else:
            logging_callbacks = self.logging_callbacks


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if key is not UNSET:
            field_dict["key"] = key
        if logging_callbacks is not UNSET:
            field_dict["logging_callbacks"] = logging_callbacks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logging_callback_status import LoggingCallbackStatus
        d = dict(src_dict)
        _key = d.pop("key", UNSET)
        key: KeyHealthResponseKey | Unset
        if isinstance(_key,  Unset):
            key = UNSET
        else:
            key = KeyHealthResponseKey(_key)




        def _parse_logging_callbacks(data: object) -> LoggingCallbackStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                logging_callbacks_type_0 = LoggingCallbackStatus.from_dict(data)



                return logging_callbacks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LoggingCallbackStatus | None | Unset, data)

        logging_callbacks = _parse_logging_callbacks(d.pop("logging_callbacks", UNSET))


        key_health_response = cls(
            key=key,
            logging_callbacks=logging_callbacks,
        )


        key_health_response.additional_properties = d
        return key_health_response

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
