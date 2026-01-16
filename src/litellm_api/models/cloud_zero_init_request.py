from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CloudZeroInitRequest")



@_attrs_define
class CloudZeroInitRequest:
    """ Request model for initializing CloudZero settings

        Attributes:
            api_key (str): CloudZero API key for authentication
            connection_id (str): CloudZero connection ID for data submission
            timezone (str | Unset): Timezone for date handling (default: UTC) Default: 'UTC'.
     """

    api_key: str
    connection_id: str
    timezone: str | Unset = 'UTC'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        connection_id = self.connection_id

        timezone = self.timezone


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "api_key": api_key,
            "connection_id": connection_id,
        })
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("api_key")

        connection_id = d.pop("connection_id")

        timezone = d.pop("timezone", UNSET)

        cloud_zero_init_request = cls(
            api_key=api_key,
            connection_id=connection_id,
            timezone=timezone,
        )


        cloud_zero_init_request.additional_properties = d
        return cloud_zero_init_request

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
