from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CloudZeroSettingsView")



@_attrs_define
class CloudZeroSettingsView:
    """ Response model for viewing CloudZero settings with masked API key

        Attributes:
            api_key_masked (None | str | Unset): Masked API key showing only first 4 and last 4 characters
            connection_id (None | str | Unset): CloudZero connection ID for data submission
            timezone (None | str | Unset): Timezone for date handling
            status (None | str | Unset): Configuration status
     """

    api_key_masked: None | str | Unset = UNSET
    connection_id: None | str | Unset = UNSET
    timezone: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key_masked: None | str | Unset
        if isinstance(self.api_key_masked, Unset):
            api_key_masked = UNSET
        else:
            api_key_masked = self.api_key_masked

        connection_id: None | str | Unset
        if isinstance(self.connection_id, Unset):
            connection_id = UNSET
        else:
            connection_id = self.connection_id

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if api_key_masked is not UNSET:
            field_dict["api_key_masked"] = api_key_masked
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_api_key_masked(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_key_masked = _parse_api_key_masked(d.pop("api_key_masked", UNSET))


        def _parse_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_id = _parse_connection_id(d.pop("connection_id", UNSET))


        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        cloud_zero_settings_view = cls(
            api_key_masked=api_key_masked,
            connection_id=connection_id,
            timezone=timezone,
            status=status,
        )


        cloud_zero_settings_view.additional_properties = d
        return cloud_zero_settings_view

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
