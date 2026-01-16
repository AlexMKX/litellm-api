from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.litellm_user_roles import LitellmUserRoles
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.role_mappings_roles import RoleMappingsRoles





T = TypeVar("T", bound="RoleMappings")



@_attrs_define
class RoleMappings:
    """ Configuration for mapping SSO groups to LiteLLM roles.

    The system will look at the group_claim field in the SSO token to determine
    which role to assign the user based on the roles mapping.

        Attributes:
            provider (str): SSO Provider name (e.g., 'google', 'microsoft', 'generic')
            group_claim (str): The field name in the SSO token that contains the groups array (e.g., 'groups', 'roles')
            default_role (LitellmUserRoles | None | Unset): Default role to assign if user's groups don't match any role
                mappings. Must be a valid LitellmUserRoles value (e.g., 'proxy_admin', 'internal_user', 'proxy_admin_viewer')
            roles (RoleMappingsRoles | Unset): Mapping of LiteLLM role names to arrays of SSO group names. Example:
                {'proxy_admin': ['group-1', 'group-2'], 'proxy_admin_viewer': ['group-3']}
     """

    provider: str
    group_claim: str
    default_role: LitellmUserRoles | None | Unset = UNSET
    roles: RoleMappingsRoles | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.role_mappings_roles import RoleMappingsRoles
        provider = self.provider

        group_claim = self.group_claim

        default_role: None | str | Unset
        if isinstance(self.default_role, Unset):
            default_role = UNSET
        elif isinstance(self.default_role, LitellmUserRoles):
            default_role = self.default_role.value
        else:
            default_role = self.default_role

        roles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "provider": provider,
            "group_claim": group_claim,
        })
        if default_role is not UNSET:
            field_dict["default_role"] = default_role
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.role_mappings_roles import RoleMappingsRoles
        d = dict(src_dict)
        provider = d.pop("provider")

        group_claim = d.pop("group_claim")

        def _parse_default_role(data: object) -> LitellmUserRoles | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_role_type_0 = LitellmUserRoles(data)



                return default_role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LitellmUserRoles | None | Unset, data)

        default_role = _parse_default_role(d.pop("default_role", UNSET))


        _roles = d.pop("roles", UNSET)
        roles: RoleMappingsRoles | Unset
        if isinstance(_roles,  Unset):
            roles = UNSET
        else:
            roles = RoleMappingsRoles.from_dict(_roles)




        role_mappings = cls(
            provider=provider,
            group_claim=group_claim,
            default_role=default_role,
            roles=roles,
        )


        role_mappings.additional_properties = d
        return role_mappings

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
