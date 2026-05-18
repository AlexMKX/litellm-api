from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="MCPUserCredentialResponse")



@_attrs_define
class MCPUserCredentialResponse:
    """ 
        Attributes:
            has_credential (bool):
            server_id (str):
     """

    has_credential: bool
    server_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        has_credential = self.has_credential

        server_id = self.server_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "has_credential": has_credential,
            "server_id": server_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_credential = d.pop("has_credential")

        server_id = d.pop("server_id")

        mcp_user_credential_response = cls(
            has_credential=has_credential,
            server_id=server_id,
        )


        mcp_user_credential_response.additional_properties = d
        return mcp_user_credential_response

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
