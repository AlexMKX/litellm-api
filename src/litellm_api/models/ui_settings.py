from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UISettings")



@_attrs_define
class UISettings:
    """ Configuration for UI-specific flags

        Attributes:
            disable_model_add_for_internal_users (bool | Unset): If true, internal users cannot add models from the UI
                Default: False.
            disable_team_admin_delete_team_user (bool | Unset): Prevents Team Admins from deleting users from the teams they
                manage. Useful for SCIM provisioning where team membership is defined externally. Default: False.
            enabled_ui_pages_internal_users (list[str] | None | Unset): List of page keys that internal users (non-admins)
                can see in the UI sidebar. If not set, all pages are visible based on role permissions.
     """

    disable_model_add_for_internal_users: bool | Unset = False
    disable_team_admin_delete_team_user: bool | Unset = False
    enabled_ui_pages_internal_users: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        disable_model_add_for_internal_users = self.disable_model_add_for_internal_users

        disable_team_admin_delete_team_user = self.disable_team_admin_delete_team_user

        enabled_ui_pages_internal_users: list[str] | None | Unset
        if isinstance(self.enabled_ui_pages_internal_users, Unset):
            enabled_ui_pages_internal_users = UNSET
        elif isinstance(self.enabled_ui_pages_internal_users, list):
            enabled_ui_pages_internal_users = self.enabled_ui_pages_internal_users


        else:
            enabled_ui_pages_internal_users = self.enabled_ui_pages_internal_users


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if disable_model_add_for_internal_users is not UNSET:
            field_dict["disable_model_add_for_internal_users"] = disable_model_add_for_internal_users
        if disable_team_admin_delete_team_user is not UNSET:
            field_dict["disable_team_admin_delete_team_user"] = disable_team_admin_delete_team_user
        if enabled_ui_pages_internal_users is not UNSET:
            field_dict["enabled_ui_pages_internal_users"] = enabled_ui_pages_internal_users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disable_model_add_for_internal_users = d.pop("disable_model_add_for_internal_users", UNSET)

        disable_team_admin_delete_team_user = d.pop("disable_team_admin_delete_team_user", UNSET)

        def _parse_enabled_ui_pages_internal_users(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                enabled_ui_pages_internal_users_type_0 = cast(list[str], data)

                return enabled_ui_pages_internal_users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        enabled_ui_pages_internal_users = _parse_enabled_ui_pages_internal_users(d.pop("enabled_ui_pages_internal_users", UNSET))


        ui_settings = cls(
            disable_model_add_for_internal_users=disable_model_add_for_internal_users,
            disable_team_admin_delete_team_user=disable_team_admin_delete_team_user,
            enabled_ui_pages_internal_users=enabled_ui_pages_internal_users,
        )


        ui_settings.additional_properties = d
        return ui_settings

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
