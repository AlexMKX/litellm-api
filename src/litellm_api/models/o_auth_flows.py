from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.o_auth_flows_authorization_code_type_0 import OAuthFlowsAuthorizationCodeType0
  from ..models.o_auth_flows_client_credentials_type_0 import OAuthFlowsClientCredentialsType0
  from ..models.o_auth_flows_implicit_type_0 import OAuthFlowsImplicitType0
  from ..models.o_auth_flows_password_type_0 import OAuthFlowsPasswordType0





T = TypeVar("T", bound="OAuthFlows")



@_attrs_define
class OAuthFlows:
    """ Defines the configuration for the supported OAuth 2.0 flows.

        Attributes:
            authorization_code (None | OAuthFlowsAuthorizationCodeType0 | Unset):
            client_credentials (None | OAuthFlowsClientCredentialsType0 | Unset):
            implicit (None | OAuthFlowsImplicitType0 | Unset):
            password (None | OAuthFlowsPasswordType0 | Unset):
     """

    authorization_code: None | OAuthFlowsAuthorizationCodeType0 | Unset = UNSET
    client_credentials: None | OAuthFlowsClientCredentialsType0 | Unset = UNSET
    implicit: None | OAuthFlowsImplicitType0 | Unset = UNSET
    password: None | OAuthFlowsPasswordType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.o_auth_flows_authorization_code_type_0 import OAuthFlowsAuthorizationCodeType0
        from ..models.o_auth_flows_implicit_type_0 import OAuthFlowsImplicitType0
        from ..models.o_auth_flows_password_type_0 import OAuthFlowsPasswordType0
        from ..models.o_auth_flows_client_credentials_type_0 import OAuthFlowsClientCredentialsType0
        authorization_code: dict[str, Any] | None | Unset
        if isinstance(self.authorization_code, Unset):
            authorization_code = UNSET
        elif isinstance(self.authorization_code, OAuthFlowsAuthorizationCodeType0):
            authorization_code = self.authorization_code.to_dict()
        else:
            authorization_code = self.authorization_code

        client_credentials: dict[str, Any] | None | Unset
        if isinstance(self.client_credentials, Unset):
            client_credentials = UNSET
        elif isinstance(self.client_credentials, OAuthFlowsClientCredentialsType0):
            client_credentials = self.client_credentials.to_dict()
        else:
            client_credentials = self.client_credentials

        implicit: dict[str, Any] | None | Unset
        if isinstance(self.implicit, Unset):
            implicit = UNSET
        elif isinstance(self.implicit, OAuthFlowsImplicitType0):
            implicit = self.implicit.to_dict()
        else:
            implicit = self.implicit

        password: dict[str, Any] | None | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        elif isinstance(self.password, OAuthFlowsPasswordType0):
            password = self.password.to_dict()
        else:
            password = self.password


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if authorization_code is not UNSET:
            field_dict["authorizationCode"] = authorization_code
        if client_credentials is not UNSET:
            field_dict["clientCredentials"] = client_credentials
        if implicit is not UNSET:
            field_dict["implicit"] = implicit
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_flows_authorization_code_type_0 import OAuthFlowsAuthorizationCodeType0
        from ..models.o_auth_flows_client_credentials_type_0 import OAuthFlowsClientCredentialsType0
        from ..models.o_auth_flows_implicit_type_0 import OAuthFlowsImplicitType0
        from ..models.o_auth_flows_password_type_0 import OAuthFlowsPasswordType0
        d = dict(src_dict)
        def _parse_authorization_code(data: object) -> None | OAuthFlowsAuthorizationCodeType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                authorization_code_type_0 = OAuthFlowsAuthorizationCodeType0.from_dict(data)



                return authorization_code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OAuthFlowsAuthorizationCodeType0 | Unset, data)

        authorization_code = _parse_authorization_code(d.pop("authorizationCode", UNSET))


        def _parse_client_credentials(data: object) -> None | OAuthFlowsClientCredentialsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                client_credentials_type_0 = OAuthFlowsClientCredentialsType0.from_dict(data)



                return client_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OAuthFlowsClientCredentialsType0 | Unset, data)

        client_credentials = _parse_client_credentials(d.pop("clientCredentials", UNSET))


        def _parse_implicit(data: object) -> None | OAuthFlowsImplicitType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                implicit_type_0 = OAuthFlowsImplicitType0.from_dict(data)



                return implicit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OAuthFlowsImplicitType0 | Unset, data)

        implicit = _parse_implicit(d.pop("implicit", UNSET))


        def _parse_password(data: object) -> None | OAuthFlowsPasswordType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                password_type_0 = OAuthFlowsPasswordType0.from_dict(data)



                return password_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OAuthFlowsPasswordType0 | Unset, data)

        password = _parse_password(d.pop("password", UNSET))


        o_auth_flows = cls(
            authorization_code=authorization_code,
            client_credentials=client_credentials,
            implicit=implicit,
            password=password,
        )


        o_auth_flows.additional_properties = d
        return o_auth_flows

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
