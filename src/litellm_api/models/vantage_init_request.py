from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="VantageInitRequest")



@_attrs_define
class VantageInitRequest:
    """ Request model for initializing Vantage settings

        Attributes:
            api_key (str): Vantage API key for authentication
            integration_token (str): Vantage integration token for the cost-import endpoint
            base_url (str | Unset): Vantage API base URL (default: https://api.vantage.sh) Default:
                'https://api.vantage.sh'.
     """

    api_key: str
    integration_token: str
    base_url: str | Unset = 'https://api.vantage.sh'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        integration_token = self.integration_token

        base_url = self.base_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "api_key": api_key,
            "integration_token": integration_token,
        })
        if base_url is not UNSET:
            field_dict["base_url"] = base_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("api_key")

        integration_token = d.pop("integration_token")

        base_url = d.pop("base_url", UNSET)

        vantage_init_request = cls(
            api_key=api_key,
            integration_token=integration_token,
            base_url=base_url,
        )


        vantage_init_request.additional_properties = d
        return vantage_init_request

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
