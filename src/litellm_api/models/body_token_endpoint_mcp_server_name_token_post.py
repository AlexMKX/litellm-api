from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BodyTokenEndpointMcpServerNameTokenPost")



@_attrs_define
class BodyTokenEndpointMcpServerNameTokenPost:
    """ 
        Attributes:
            grant_type (str):
            client_id (str):
            code (str | Unset):
            redirect_uri (str | Unset):
            client_secret (None | str | Unset):
            code_verifier (str | Unset):
     """

    grant_type: str
    client_id: str
    code: str | Unset = UNSET
    redirect_uri: str | Unset = UNSET
    client_secret: None | str | Unset = UNSET
    code_verifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type

        client_id = self.client_id

        code = self.code

        redirect_uri = self.redirect_uri

        client_secret: None | str | Unset
        if isinstance(self.client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = self.client_secret

        code_verifier = self.code_verifier


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "grant_type": grant_type,
            "client_id": client_id,
        })
        if code is not UNSET:
            field_dict["code"] = code
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if code_verifier is not UNSET:
            field_dict["code_verifier"] = code_verifier

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = d.pop("grant_type")

        client_id = d.pop("client_id")

        code = d.pop("code", UNSET)

        redirect_uri = d.pop("redirect_uri", UNSET)

        def _parse_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_secret = _parse_client_secret(d.pop("client_secret", UNSET))


        code_verifier = d.pop("code_verifier", UNSET)

        body_token_endpoint_mcp_server_name_token_post = cls(
            grant_type=grant_type,
            client_id=client_id,
            code=code,
            redirect_uri=redirect_uri,
            client_secret=client_secret,
            code_verifier=code_verifier,
        )


        body_token_endpoint_mcp_server_name_token_post.additional_properties = d
        return body_token_endpoint_mcp_server_name_token_post

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
