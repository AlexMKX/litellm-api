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
            require_auth_for_public_ai_hub (bool | Unset): If true, requires authentication for accessing the public AI Hub.
                Default: False.
            forward_client_headers_to_llm_api (bool | Unset): If enabled, forwards client headers (e.g. Authorization) to
                the LLM API. Required for Claude Code with Max subscription. Default: False.
            enable_projects_ui (bool | Unset): If enabled, shows the Projects feature in the UI sidebar and the project
                field in key management. Default: False.
            disable_agents_for_internal_users (bool | Unset): If true, internal users cannot access agent management
                endpoints or the Agents page in the UI. Default: False.
            allow_agents_for_team_admins (bool | Unset): If true, team admins are exempt from the agents disable restriction
                (only takes effect when disable_agents_for_internal_users is true). Default: False.
            disable_vector_stores_for_internal_users (bool | Unset): If true, internal users cannot access vector store
                management endpoints or the Vector Stores page in the UI. Default: False.
            allow_vector_stores_for_team_admins (bool | Unset): If true, team admins are exempt from the vector stores
                disable restriction (only takes effect when disable_vector_stores_for_internal_users is true). Default: False.
            scope_user_search_to_org (bool | Unset): If enabled, the user search endpoint (/user/filter/ui) restricts
                results by organization. When off, any authenticated user can search all users. Default: False.
     """

    disable_model_add_for_internal_users: bool | Unset = False
    disable_team_admin_delete_team_user: bool | Unset = False
    enabled_ui_pages_internal_users: list[str] | None | Unset = UNSET
    require_auth_for_public_ai_hub: bool | Unset = False
    forward_client_headers_to_llm_api: bool | Unset = False
    enable_projects_ui: bool | Unset = False
    disable_agents_for_internal_users: bool | Unset = False
    allow_agents_for_team_admins: bool | Unset = False
    disable_vector_stores_for_internal_users: bool | Unset = False
    allow_vector_stores_for_team_admins: bool | Unset = False
    scope_user_search_to_org: bool | Unset = False
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

        require_auth_for_public_ai_hub = self.require_auth_for_public_ai_hub

        forward_client_headers_to_llm_api = self.forward_client_headers_to_llm_api

        enable_projects_ui = self.enable_projects_ui

        disable_agents_for_internal_users = self.disable_agents_for_internal_users

        allow_agents_for_team_admins = self.allow_agents_for_team_admins

        disable_vector_stores_for_internal_users = self.disable_vector_stores_for_internal_users

        allow_vector_stores_for_team_admins = self.allow_vector_stores_for_team_admins

        scope_user_search_to_org = self.scope_user_search_to_org


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
        if require_auth_for_public_ai_hub is not UNSET:
            field_dict["require_auth_for_public_ai_hub"] = require_auth_for_public_ai_hub
        if forward_client_headers_to_llm_api is not UNSET:
            field_dict["forward_client_headers_to_llm_api"] = forward_client_headers_to_llm_api
        if enable_projects_ui is not UNSET:
            field_dict["enable_projects_ui"] = enable_projects_ui
        if disable_agents_for_internal_users is not UNSET:
            field_dict["disable_agents_for_internal_users"] = disable_agents_for_internal_users
        if allow_agents_for_team_admins is not UNSET:
            field_dict["allow_agents_for_team_admins"] = allow_agents_for_team_admins
        if disable_vector_stores_for_internal_users is not UNSET:
            field_dict["disable_vector_stores_for_internal_users"] = disable_vector_stores_for_internal_users
        if allow_vector_stores_for_team_admins is not UNSET:
            field_dict["allow_vector_stores_for_team_admins"] = allow_vector_stores_for_team_admins
        if scope_user_search_to_org is not UNSET:
            field_dict["scope_user_search_to_org"] = scope_user_search_to_org

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


        require_auth_for_public_ai_hub = d.pop("require_auth_for_public_ai_hub", UNSET)

        forward_client_headers_to_llm_api = d.pop("forward_client_headers_to_llm_api", UNSET)

        enable_projects_ui = d.pop("enable_projects_ui", UNSET)

        disable_agents_for_internal_users = d.pop("disable_agents_for_internal_users", UNSET)

        allow_agents_for_team_admins = d.pop("allow_agents_for_team_admins", UNSET)

        disable_vector_stores_for_internal_users = d.pop("disable_vector_stores_for_internal_users", UNSET)

        allow_vector_stores_for_team_admins = d.pop("allow_vector_stores_for_team_admins", UNSET)

        scope_user_search_to_org = d.pop("scope_user_search_to_org", UNSET)

        ui_settings = cls(
            disable_model_add_for_internal_users=disable_model_add_for_internal_users,
            disable_team_admin_delete_team_user=disable_team_admin_delete_team_user,
            enabled_ui_pages_internal_users=enabled_ui_pages_internal_users,
            require_auth_for_public_ai_hub=require_auth_for_public_ai_hub,
            forward_client_headers_to_llm_api=forward_client_headers_to_llm_api,
            enable_projects_ui=enable_projects_ui,
            disable_agents_for_internal_users=disable_agents_for_internal_users,
            allow_agents_for_team_admins=allow_agents_for_team_admins,
            disable_vector_stores_for_internal_users=disable_vector_stores_for_internal_users,
            allow_vector_stores_for_team_admins=allow_vector_stores_for_team_admins,
            scope_user_search_to_org=scope_user_search_to_org,
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
