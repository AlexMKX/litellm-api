from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="VantageSettingsUpdate")



@_attrs_define
class VantageSettingsUpdate:
    """ Request model for updating Vantage settings

        Attributes:
            api_key (None | str | Unset): New Vantage API key for authentication
            integration_token (None | str | Unset): New Vantage integration token
            base_url (None | str | Unset): New Vantage API base URL
     """

    api_key: None | str | Unset = UNSET
    integration_token: None | str | Unset = UNSET
    base_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key: None | str | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

        integration_token: None | str | Unset
        if isinstance(self.integration_token, Unset):
            integration_token = UNSET
        else:
            integration_token = self.integration_token

        base_url: None | str | Unset
        if isinstance(self.base_url, Unset):
            base_url = UNSET
        else:
            base_url = self.base_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if integration_token is not UNSET:
            field_dict["integration_token"] = integration_token
        if base_url is not UNSET:
            field_dict["base_url"] = base_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))


        def _parse_integration_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        integration_token = _parse_integration_token(d.pop("integration_token", UNSET))


        def _parse_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_url = _parse_base_url(d.pop("base_url", UNSET))


        vantage_settings_update = cls(
            api_key=api_key,
            integration_token=integration_token,
            base_url=base_url,
        )


        vantage_settings_update.additional_properties = d
        return vantage_settings_update

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
