from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="VantageSettingsView")



@_attrs_define
class VantageSettingsView:
    """ Response model for viewing Vantage settings with masked API key

        Attributes:
            api_key_masked (None | str | Unset): Masked API key showing only first 4 and last 4 characters
            integration_token_masked (None | str | Unset): Masked integration token showing only first 4 and last 4
                characters
            base_url (None | str | Unset): Vantage API base URL
            status (None | str | Unset): Configuration status
     """

    api_key_masked: None | str | Unset = UNSET
    integration_token_masked: None | str | Unset = UNSET
    base_url: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key_masked: None | str | Unset
        if isinstance(self.api_key_masked, Unset):
            api_key_masked = UNSET
        else:
            api_key_masked = self.api_key_masked

        integration_token_masked: None | str | Unset
        if isinstance(self.integration_token_masked, Unset):
            integration_token_masked = UNSET
        else:
            integration_token_masked = self.integration_token_masked

        base_url: None | str | Unset
        if isinstance(self.base_url, Unset):
            base_url = UNSET
        else:
            base_url = self.base_url

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
        if integration_token_masked is not UNSET:
            field_dict["integration_token_masked"] = integration_token_masked
        if base_url is not UNSET:
            field_dict["base_url"] = base_url
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


        def _parse_integration_token_masked(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        integration_token_masked = _parse_integration_token_masked(d.pop("integration_token_masked", UNSET))


        def _parse_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_url = _parse_base_url(d.pop("base_url", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        vantage_settings_view = cls(
            api_key_masked=api_key_masked,
            integration_token_masked=integration_token_masked,
            base_url=base_url,
            status=status,
        )


        vantage_settings_view.additional_properties = d
        return vantage_settings_view

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
