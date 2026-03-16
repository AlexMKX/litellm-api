from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MCPOAuthUserCredentialStatus")



@_attrs_define
class MCPOAuthUserCredentialStatus:
    """ Describes whether the calling user has a stored OAuth credential.

        Attributes:
            server_id (str):
            has_credential (bool):
            expires_at (None | str | Unset):
            is_expired (bool | Unset):  Default: False.
            connected_at (None | str | Unset):
     """

    server_id: str
    has_credential: bool
    expires_at: None | str | Unset = UNSET
    is_expired: bool | Unset = False
    connected_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        server_id = self.server_id

        has_credential = self.has_credential

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        is_expired = self.is_expired

        connected_at: None | str | Unset
        if isinstance(self.connected_at, Unset):
            connected_at = UNSET
        else:
            connected_at = self.connected_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "server_id": server_id,
            "has_credential": has_credential,
        })
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if is_expired is not UNSET:
            field_dict["is_expired"] = is_expired
        if connected_at is not UNSET:
            field_dict["connected_at"] = connected_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server_id = d.pop("server_id")

        has_credential = d.pop("has_credential")

        def _parse_expires_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))


        is_expired = d.pop("is_expired", UNSET)

        def _parse_connected_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connected_at = _parse_connected_at(d.pop("connected_at", UNSET))


        mcpo_auth_user_credential_status = cls(
            server_id=server_id,
            has_credential=has_credential,
            expires_at=expires_at,
            is_expired=is_expired,
            connected_at=connected_at,
        )


        mcpo_auth_user_credential_status.additional_properties = d
        return mcpo_auth_user_credential_status

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
