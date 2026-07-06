from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PluginAuthTokenApiPluginsAuthTokenGetResponsePluginAuthTokenApiPluginsAuthTokenGet")



@_attrs_define
class PluginAuthTokenApiPluginsAuthTokenGetResponsePluginAuthTokenApiPluginsAuthTokenGet:
    """ 
     """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plugin_auth_token_api_plugins_auth_token_get_response_plugin_auth_token_api_plugins_auth_token_get = cls(
        )


        plugin_auth_token_api_plugins_auth_token_get_response_plugin_auth_token_api_plugins_auth_token_get.additional_properties = d
        return plugin_auth_token_api_plugins_auth_token_get_response_plugin_auth_token_api_plugins_auth_token_get

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
