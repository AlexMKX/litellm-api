from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MCPUserCredentialListItem")



@_attrs_define
class MCPUserCredentialListItem:
    """ One entry in the /user-credentials list.

        Attributes:
            credential_type (str):
            has_credential (bool):
            server_id (str):
            alias (None | str | Unset):
            connected_at (None | str | Unset):
            expires_at (None | str | Unset):
            server_name (None | str | Unset):
     """

    credential_type: str
    has_credential: bool
    server_id: str
    alias: None | str | Unset = UNSET
    connected_at: None | str | Unset = UNSET
    expires_at: None | str | Unset = UNSET
    server_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        credential_type = self.credential_type

        has_credential = self.has_credential

        server_id = self.server_id

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        connected_at: None | str | Unset
        if isinstance(self.connected_at, Unset):
            connected_at = UNSET
        else:
            connected_at = self.connected_at

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        server_name: None | str | Unset
        if isinstance(self.server_name, Unset):
            server_name = UNSET
        else:
            server_name = self.server_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "credential_type": credential_type,
            "has_credential": has_credential,
            "server_id": server_id,
        })
        if alias is not UNSET:
            field_dict["alias"] = alias
        if connected_at is not UNSET:
            field_dict["connected_at"] = connected_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if server_name is not UNSET:
            field_dict["server_name"] = server_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credential_type = d.pop("credential_type")

        has_credential = d.pop("has_credential")

        server_id = d.pop("server_id")

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))


        def _parse_connected_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connected_at = _parse_connected_at(d.pop("connected_at", UNSET))


        def _parse_expires_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))


        def _parse_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_name = _parse_server_name(d.pop("server_name", UNSET))


        mcp_user_credential_list_item = cls(
            credential_type=credential_type,
            has_credential=has_credential,
            server_id=server_id,
            alias=alias,
            connected_at=connected_at,
            expires_at=expires_at,
            server_name=server_name,
        )


        mcp_user_credential_list_item.additional_properties = d
        return mcp_user_credential_list_item

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
