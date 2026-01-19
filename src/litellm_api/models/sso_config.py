from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.access_control_ui_access_mode import AccessControlUIAccessMode
  from ..models.role_mappings import RoleMappings





T = TypeVar("T", bound="SSOConfig")



@_attrs_define
class SSOConfig:
    """ Configuration for SSO environment variables and settings

        Attributes:
            google_client_id (None | str | Unset): Google OAuth Client ID for SSO authentication
            google_client_secret (None | str | Unset): Google OAuth Client Secret for SSO authentication
            microsoft_client_id (None | str | Unset): Microsoft OAuth Client ID for SSO authentication
            microsoft_client_secret (None | str | Unset): Microsoft OAuth Client Secret for SSO authentication
            microsoft_tenant (None | str | Unset): Microsoft Azure Tenant ID for SSO authentication
            generic_client_id (None | str | Unset): Generic OAuth Client ID for SSO authentication (used for Okta and other
                providers)
            generic_client_secret (None | str | Unset): Generic OAuth Client Secret for SSO authentication
            generic_authorization_endpoint (None | str | Unset): Authorization endpoint URL for generic OAuth provider
            generic_token_endpoint (None | str | Unset): Token endpoint URL for generic OAuth provider
            generic_userinfo_endpoint (None | str | Unset): User info endpoint URL for generic OAuth provider
            proxy_base_url (None | str | Unset): Base URL of the proxy server for SSO redirects
            user_email (None | str | Unset): Email of the proxy admin user
            ui_access_mode (AccessControlUIAccessMode | None | str | Unset): Access mode for the UI
            role_mappings (None | RoleMappings | Unset): Configuration for mapping SSO groups to LiteLLM roles based on
                group claims in the SSO token
     """

    google_client_id: None | str | Unset = UNSET
    google_client_secret: None | str | Unset = UNSET
    microsoft_client_id: None | str | Unset = UNSET
    microsoft_client_secret: None | str | Unset = UNSET
    microsoft_tenant: None | str | Unset = UNSET
    generic_client_id: None | str | Unset = UNSET
    generic_client_secret: None | str | Unset = UNSET
    generic_authorization_endpoint: None | str | Unset = UNSET
    generic_token_endpoint: None | str | Unset = UNSET
    generic_userinfo_endpoint: None | str | Unset = UNSET
    proxy_base_url: None | str | Unset = UNSET
    user_email: None | str | Unset = UNSET
    ui_access_mode: AccessControlUIAccessMode | None | str | Unset = UNSET
    role_mappings: None | RoleMappings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.role_mappings import RoleMappings
        from ..models.access_control_ui_access_mode import AccessControlUIAccessMode
        google_client_id: None | str | Unset
        if isinstance(self.google_client_id, Unset):
            google_client_id = UNSET
        else:
            google_client_id = self.google_client_id

        google_client_secret: None | str | Unset
        if isinstance(self.google_client_secret, Unset):
            google_client_secret = UNSET
        else:
            google_client_secret = self.google_client_secret

        microsoft_client_id: None | str | Unset
        if isinstance(self.microsoft_client_id, Unset):
            microsoft_client_id = UNSET
        else:
            microsoft_client_id = self.microsoft_client_id

        microsoft_client_secret: None | str | Unset
        if isinstance(self.microsoft_client_secret, Unset):
            microsoft_client_secret = UNSET
        else:
            microsoft_client_secret = self.microsoft_client_secret

        microsoft_tenant: None | str | Unset
        if isinstance(self.microsoft_tenant, Unset):
            microsoft_tenant = UNSET
        else:
            microsoft_tenant = self.microsoft_tenant

        generic_client_id: None | str | Unset
        if isinstance(self.generic_client_id, Unset):
            generic_client_id = UNSET
        else:
            generic_client_id = self.generic_client_id

        generic_client_secret: None | str | Unset
        if isinstance(self.generic_client_secret, Unset):
            generic_client_secret = UNSET
        else:
            generic_client_secret = self.generic_client_secret

        generic_authorization_endpoint: None | str | Unset
        if isinstance(self.generic_authorization_endpoint, Unset):
            generic_authorization_endpoint = UNSET
        else:
            generic_authorization_endpoint = self.generic_authorization_endpoint

        generic_token_endpoint: None | str | Unset
        if isinstance(self.generic_token_endpoint, Unset):
            generic_token_endpoint = UNSET
        else:
            generic_token_endpoint = self.generic_token_endpoint

        generic_userinfo_endpoint: None | str | Unset
        if isinstance(self.generic_userinfo_endpoint, Unset):
            generic_userinfo_endpoint = UNSET
        else:
            generic_userinfo_endpoint = self.generic_userinfo_endpoint

        proxy_base_url: None | str | Unset
        if isinstance(self.proxy_base_url, Unset):
            proxy_base_url = UNSET
        else:
            proxy_base_url = self.proxy_base_url

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        ui_access_mode: dict[str, Any] | None | str | Unset
        if isinstance(self.ui_access_mode, Unset):
            ui_access_mode = UNSET
        elif isinstance(self.ui_access_mode, AccessControlUIAccessMode):
            ui_access_mode = self.ui_access_mode.to_dict()
        else:
            ui_access_mode = self.ui_access_mode

        role_mappings: dict[str, Any] | None | Unset
        if isinstance(self.role_mappings, Unset):
            role_mappings = UNSET
        elif isinstance(self.role_mappings, RoleMappings):
            role_mappings = self.role_mappings.to_dict()
        else:
            role_mappings = self.role_mappings


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if google_client_id is not UNSET:
            field_dict["google_client_id"] = google_client_id
        if google_client_secret is not UNSET:
            field_dict["google_client_secret"] = google_client_secret
        if microsoft_client_id is not UNSET:
            field_dict["microsoft_client_id"] = microsoft_client_id
        if microsoft_client_secret is not UNSET:
            field_dict["microsoft_client_secret"] = microsoft_client_secret
        if microsoft_tenant is not UNSET:
            field_dict["microsoft_tenant"] = microsoft_tenant
        if generic_client_id is not UNSET:
            field_dict["generic_client_id"] = generic_client_id
        if generic_client_secret is not UNSET:
            field_dict["generic_client_secret"] = generic_client_secret
        if generic_authorization_endpoint is not UNSET:
            field_dict["generic_authorization_endpoint"] = generic_authorization_endpoint
        if generic_token_endpoint is not UNSET:
            field_dict["generic_token_endpoint"] = generic_token_endpoint
        if generic_userinfo_endpoint is not UNSET:
            field_dict["generic_userinfo_endpoint"] = generic_userinfo_endpoint
        if proxy_base_url is not UNSET:
            field_dict["proxy_base_url"] = proxy_base_url
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if ui_access_mode is not UNSET:
            field_dict["ui_access_mode"] = ui_access_mode
        if role_mappings is not UNSET:
            field_dict["role_mappings"] = role_mappings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.access_control_ui_access_mode import AccessControlUIAccessMode
        from ..models.role_mappings import RoleMappings
        d = dict(src_dict)
        def _parse_google_client_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        google_client_id = _parse_google_client_id(d.pop("google_client_id", UNSET))


        def _parse_google_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        google_client_secret = _parse_google_client_secret(d.pop("google_client_secret", UNSET))


        def _parse_microsoft_client_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        microsoft_client_id = _parse_microsoft_client_id(d.pop("microsoft_client_id", UNSET))


        def _parse_microsoft_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        microsoft_client_secret = _parse_microsoft_client_secret(d.pop("microsoft_client_secret", UNSET))


        def _parse_microsoft_tenant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        microsoft_tenant = _parse_microsoft_tenant(d.pop("microsoft_tenant", UNSET))


        def _parse_generic_client_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        generic_client_id = _parse_generic_client_id(d.pop("generic_client_id", UNSET))


        def _parse_generic_client_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        generic_client_secret = _parse_generic_client_secret(d.pop("generic_client_secret", UNSET))


        def _parse_generic_authorization_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        generic_authorization_endpoint = _parse_generic_authorization_endpoint(d.pop("generic_authorization_endpoint", UNSET))


        def _parse_generic_token_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        generic_token_endpoint = _parse_generic_token_endpoint(d.pop("generic_token_endpoint", UNSET))


        def _parse_generic_userinfo_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        generic_userinfo_endpoint = _parse_generic_userinfo_endpoint(d.pop("generic_userinfo_endpoint", UNSET))


        def _parse_proxy_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proxy_base_url = _parse_proxy_base_url(d.pop("proxy_base_url", UNSET))


        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))


        def _parse_ui_access_mode(data: object) -> AccessControlUIAccessMode | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ui_access_mode_type_0 = AccessControlUIAccessMode.from_dict(data)



                return ui_access_mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccessControlUIAccessMode | None | str | Unset, data)

        ui_access_mode = _parse_ui_access_mode(d.pop("ui_access_mode", UNSET))


        def _parse_role_mappings(data: object) -> None | RoleMappings | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_mappings_type_0 = RoleMappings.from_dict(data)



                return role_mappings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RoleMappings | Unset, data)

        role_mappings = _parse_role_mappings(d.pop("role_mappings", UNSET))


        sso_config = cls(
            google_client_id=google_client_id,
            google_client_secret=google_client_secret,
            microsoft_client_id=microsoft_client_id,
            microsoft_client_secret=microsoft_client_secret,
            microsoft_tenant=microsoft_tenant,
            generic_client_id=generic_client_id,
            generic_client_secret=generic_client_secret,
            generic_authorization_endpoint=generic_authorization_endpoint,
            generic_token_endpoint=generic_token_endpoint,
            generic_userinfo_endpoint=generic_userinfo_endpoint,
            proxy_base_url=proxy_base_url,
            user_email=user_email,
            ui_access_mode=ui_access_mode,
            role_mappings=role_mappings,
        )


        sso_config.additional_properties = d
        return sso_config

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
