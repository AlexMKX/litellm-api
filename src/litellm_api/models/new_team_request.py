from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.new_team_request_rpm_limit_type_type_0 import NewTeamRequestRpmLimitTypeType0
from ..models.new_team_request_tpm_limit_type_type_0 import NewTeamRequestTpmLimitTypeType0
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.allowed_vector_store_index_item import AllowedVectorStoreIndexItem
  from ..models.lite_llm_object_permission_base import LiteLLMObjectPermissionBase
  from ..models.member import Member
  from ..models.new_team_request_metadata_type_0 import NewTeamRequestMetadataType0
  from ..models.new_team_request_model_aliases_type_0 import NewTeamRequestModelAliasesType0
  from ..models.new_team_request_model_rpm_limit_type_0 import NewTeamRequestModelRpmLimitType0
  from ..models.new_team_request_model_tpm_limit_type_0 import NewTeamRequestModelTpmLimitType0
  from ..models.new_team_request_router_settings_type_0 import NewTeamRequestRouterSettingsType0
  from ..models.new_team_request_secret_manager_settings_type_0 import NewTeamRequestSecretManagerSettingsType0





T = TypeVar("T", bound="NewTeamRequest")



@_attrs_define
class NewTeamRequest:
    """ 
        Attributes:
            team_alias (None | str | Unset):
            team_id (None | str | Unset):
            organization_id (None | str | Unset):
            admins (list[Any] | Unset):
            members (list[Any] | Unset):
            members_with_roles (list[Member] | Unset):
            team_member_permissions (list[str] | None | Unset):
            metadata (NewTeamRequestMetadataType0 | None | Unset):
            tpm_limit (int | None | Unset):
            rpm_limit (int | None | Unset):
            max_budget (float | None | Unset):
            budget_duration (None | str | Unset):
            models (list[Any] | Unset):
            blocked (bool | Unset):  Default: False.
            router_settings (NewTeamRequestRouterSettingsType0 | None | Unset):
            model_aliases (NewTeamRequestModelAliasesType0 | None | Unset):
            tags (list[Any] | None | Unset):
            guardrails (list[str] | None | Unset):
            prompts (list[str] | None | Unset):
            object_permission (LiteLLMObjectPermissionBase | None | Unset):
            allowed_passthrough_routes (list[Any] | None | Unset):
            secret_manager_settings (NewTeamRequestSecretManagerSettingsType0 | None | Unset):
            model_rpm_limit (NewTeamRequestModelRpmLimitType0 | None | Unset):
            rpm_limit_type (NewTeamRequestRpmLimitTypeType0 | None | Unset):
            tpm_limit_type (NewTeamRequestTpmLimitTypeType0 | None | Unset):
            model_tpm_limit (NewTeamRequestModelTpmLimitType0 | None | Unset):
            team_member_budget (float | None | Unset):
            team_member_rpm_limit (int | None | Unset):
            team_member_tpm_limit (int | None | Unset):
            team_member_key_duration (None | str | Unset):
            allowed_vector_store_indexes (list[AllowedVectorStoreIndexItem] | None | Unset):
     """

    team_alias: None | str | Unset = UNSET
    team_id: None | str | Unset = UNSET
    organization_id: None | str | Unset = UNSET
    admins: list[Any] | Unset = UNSET
    members: list[Any] | Unset = UNSET
    members_with_roles: list[Member] | Unset = UNSET
    team_member_permissions: list[str] | None | Unset = UNSET
    metadata: NewTeamRequestMetadataType0 | None | Unset = UNSET
    tpm_limit: int | None | Unset = UNSET
    rpm_limit: int | None | Unset = UNSET
    max_budget: float | None | Unset = UNSET
    budget_duration: None | str | Unset = UNSET
    models: list[Any] | Unset = UNSET
    blocked: bool | Unset = False
    router_settings: NewTeamRequestRouterSettingsType0 | None | Unset = UNSET
    model_aliases: NewTeamRequestModelAliasesType0 | None | Unset = UNSET
    tags: list[Any] | None | Unset = UNSET
    guardrails: list[str] | None | Unset = UNSET
    prompts: list[str] | None | Unset = UNSET
    object_permission: LiteLLMObjectPermissionBase | None | Unset = UNSET
    allowed_passthrough_routes: list[Any] | None | Unset = UNSET
    secret_manager_settings: NewTeamRequestSecretManagerSettingsType0 | None | Unset = UNSET
    model_rpm_limit: NewTeamRequestModelRpmLimitType0 | None | Unset = UNSET
    rpm_limit_type: NewTeamRequestRpmLimitTypeType0 | None | Unset = UNSET
    tpm_limit_type: NewTeamRequestTpmLimitTypeType0 | None | Unset = UNSET
    model_tpm_limit: NewTeamRequestModelTpmLimitType0 | None | Unset = UNSET
    team_member_budget: float | None | Unset = UNSET
    team_member_rpm_limit: int | None | Unset = UNSET
    team_member_tpm_limit: int | None | Unset = UNSET
    team_member_key_duration: None | str | Unset = UNSET
    allowed_vector_store_indexes: list[AllowedVectorStoreIndexItem] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.member import Member
        from ..models.allowed_vector_store_index_item import AllowedVectorStoreIndexItem
        from ..models.new_team_request_router_settings_type_0 import NewTeamRequestRouterSettingsType0
        from ..models.new_team_request_model_rpm_limit_type_0 import NewTeamRequestModelRpmLimitType0
        from ..models.new_team_request_model_tpm_limit_type_0 import NewTeamRequestModelTpmLimitType0
        from ..models.new_team_request_secret_manager_settings_type_0 import NewTeamRequestSecretManagerSettingsType0
        from ..models.new_team_request_model_aliases_type_0 import NewTeamRequestModelAliasesType0
        from ..models.new_team_request_metadata_type_0 import NewTeamRequestMetadataType0
        from ..models.lite_llm_object_permission_base import LiteLLMObjectPermissionBase
        team_alias: None | str | Unset
        if isinstance(self.team_alias, Unset):
            team_alias = UNSET
        else:
            team_alias = self.team_alias

        team_id: None | str | Unset
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        else:
            team_id = self.team_id

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = self.organization_id

        admins: list[Any] | Unset = UNSET
        if not isinstance(self.admins, Unset):
            admins = self.admins



        members: list[Any] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members



        members_with_roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members_with_roles, Unset):
            members_with_roles = []
            for members_with_roles_item_data in self.members_with_roles:
                members_with_roles_item = members_with_roles_item_data.to_dict()
                members_with_roles.append(members_with_roles_item)



        team_member_permissions: list[str] | None | Unset
        if isinstance(self.team_member_permissions, Unset):
            team_member_permissions = UNSET
        elif isinstance(self.team_member_permissions, list):
            team_member_permissions = self.team_member_permissions


        else:
            team_member_permissions = self.team_member_permissions

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, NewTeamRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        tpm_limit: int | None | Unset
        if isinstance(self.tpm_limit, Unset):
            tpm_limit = UNSET
        else:
            tpm_limit = self.tpm_limit

        rpm_limit: int | None | Unset
        if isinstance(self.rpm_limit, Unset):
            rpm_limit = UNSET
        else:
            rpm_limit = self.rpm_limit

        max_budget: float | None | Unset
        if isinstance(self.max_budget, Unset):
            max_budget = UNSET
        else:
            max_budget = self.max_budget

        budget_duration: None | str | Unset
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration

        models: list[Any] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = self.models



        blocked = self.blocked

        router_settings: dict[str, Any] | None | Unset
        if isinstance(self.router_settings, Unset):
            router_settings = UNSET
        elif isinstance(self.router_settings, NewTeamRequestRouterSettingsType0):
            router_settings = self.router_settings.to_dict()
        else:
            router_settings = self.router_settings

        model_aliases: dict[str, Any] | None | Unset
        if isinstance(self.model_aliases, Unset):
            model_aliases = UNSET
        elif isinstance(self.model_aliases, NewTeamRequestModelAliasesType0):
            model_aliases = self.model_aliases.to_dict()
        else:
            model_aliases = self.model_aliases

        tags: list[Any] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags


        else:
            tags = self.tags

        guardrails: list[str] | None | Unset
        if isinstance(self.guardrails, Unset):
            guardrails = UNSET
        elif isinstance(self.guardrails, list):
            guardrails = self.guardrails


        else:
            guardrails = self.guardrails

        prompts: list[str] | None | Unset
        if isinstance(self.prompts, Unset):
            prompts = UNSET
        elif isinstance(self.prompts, list):
            prompts = self.prompts


        else:
            prompts = self.prompts

        object_permission: dict[str, Any] | None | Unset
        if isinstance(self.object_permission, Unset):
            object_permission = UNSET
        elif isinstance(self.object_permission, LiteLLMObjectPermissionBase):
            object_permission = self.object_permission.to_dict()
        else:
            object_permission = self.object_permission

        allowed_passthrough_routes: list[Any] | None | Unset
        if isinstance(self.allowed_passthrough_routes, Unset):
            allowed_passthrough_routes = UNSET
        elif isinstance(self.allowed_passthrough_routes, list):
            allowed_passthrough_routes = self.allowed_passthrough_routes


        else:
            allowed_passthrough_routes = self.allowed_passthrough_routes

        secret_manager_settings: dict[str, Any] | None | Unset
        if isinstance(self.secret_manager_settings, Unset):
            secret_manager_settings = UNSET
        elif isinstance(self.secret_manager_settings, NewTeamRequestSecretManagerSettingsType0):
            secret_manager_settings = self.secret_manager_settings.to_dict()
        else:
            secret_manager_settings = self.secret_manager_settings

        model_rpm_limit: dict[str, Any] | None | Unset
        if isinstance(self.model_rpm_limit, Unset):
            model_rpm_limit = UNSET
        elif isinstance(self.model_rpm_limit, NewTeamRequestModelRpmLimitType0):
            model_rpm_limit = self.model_rpm_limit.to_dict()
        else:
            model_rpm_limit = self.model_rpm_limit

        rpm_limit_type: None | str | Unset
        if isinstance(self.rpm_limit_type, Unset):
            rpm_limit_type = UNSET
        elif isinstance(self.rpm_limit_type, NewTeamRequestRpmLimitTypeType0):
            rpm_limit_type = self.rpm_limit_type.value
        else:
            rpm_limit_type = self.rpm_limit_type

        tpm_limit_type: None | str | Unset
        if isinstance(self.tpm_limit_type, Unset):
            tpm_limit_type = UNSET
        elif isinstance(self.tpm_limit_type, NewTeamRequestTpmLimitTypeType0):
            tpm_limit_type = self.tpm_limit_type.value
        else:
            tpm_limit_type = self.tpm_limit_type

        model_tpm_limit: dict[str, Any] | None | Unset
        if isinstance(self.model_tpm_limit, Unset):
            model_tpm_limit = UNSET
        elif isinstance(self.model_tpm_limit, NewTeamRequestModelTpmLimitType0):
            model_tpm_limit = self.model_tpm_limit.to_dict()
        else:
            model_tpm_limit = self.model_tpm_limit

        team_member_budget: float | None | Unset
        if isinstance(self.team_member_budget, Unset):
            team_member_budget = UNSET
        else:
            team_member_budget = self.team_member_budget

        team_member_rpm_limit: int | None | Unset
        if isinstance(self.team_member_rpm_limit, Unset):
            team_member_rpm_limit = UNSET
        else:
            team_member_rpm_limit = self.team_member_rpm_limit

        team_member_tpm_limit: int | None | Unset
        if isinstance(self.team_member_tpm_limit, Unset):
            team_member_tpm_limit = UNSET
        else:
            team_member_tpm_limit = self.team_member_tpm_limit

        team_member_key_duration: None | str | Unset
        if isinstance(self.team_member_key_duration, Unset):
            team_member_key_duration = UNSET
        else:
            team_member_key_duration = self.team_member_key_duration

        allowed_vector_store_indexes: list[dict[str, Any]] | None | Unset
        if isinstance(self.allowed_vector_store_indexes, Unset):
            allowed_vector_store_indexes = UNSET
        elif isinstance(self.allowed_vector_store_indexes, list):
            allowed_vector_store_indexes = []
            for allowed_vector_store_indexes_type_0_item_data in self.allowed_vector_store_indexes:
                allowed_vector_store_indexes_type_0_item = allowed_vector_store_indexes_type_0_item_data.to_dict()
                allowed_vector_store_indexes.append(allowed_vector_store_indexes_type_0_item)


        else:
            allowed_vector_store_indexes = self.allowed_vector_store_indexes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if team_alias is not UNSET:
            field_dict["team_alias"] = team_alias
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if admins is not UNSET:
            field_dict["admins"] = admins
        if members is not UNSET:
            field_dict["members"] = members
        if members_with_roles is not UNSET:
            field_dict["members_with_roles"] = members_with_roles
        if team_member_permissions is not UNSET:
            field_dict["team_member_permissions"] = team_member_permissions
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tpm_limit is not UNSET:
            field_dict["tpm_limit"] = tpm_limit
        if rpm_limit is not UNSET:
            field_dict["rpm_limit"] = rpm_limit
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if budget_duration is not UNSET:
            field_dict["budget_duration"] = budget_duration
        if models is not UNSET:
            field_dict["models"] = models
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if router_settings is not UNSET:
            field_dict["router_settings"] = router_settings
        if model_aliases is not UNSET:
            field_dict["model_aliases"] = model_aliases
        if tags is not UNSET:
            field_dict["tags"] = tags
        if guardrails is not UNSET:
            field_dict["guardrails"] = guardrails
        if prompts is not UNSET:
            field_dict["prompts"] = prompts
        if object_permission is not UNSET:
            field_dict["object_permission"] = object_permission
        if allowed_passthrough_routes is not UNSET:
            field_dict["allowed_passthrough_routes"] = allowed_passthrough_routes
        if secret_manager_settings is not UNSET:
            field_dict["secret_manager_settings"] = secret_manager_settings
        if model_rpm_limit is not UNSET:
            field_dict["model_rpm_limit"] = model_rpm_limit
        if rpm_limit_type is not UNSET:
            field_dict["rpm_limit_type"] = rpm_limit_type
        if tpm_limit_type is not UNSET:
            field_dict["tpm_limit_type"] = tpm_limit_type
        if model_tpm_limit is not UNSET:
            field_dict["model_tpm_limit"] = model_tpm_limit
        if team_member_budget is not UNSET:
            field_dict["team_member_budget"] = team_member_budget
        if team_member_rpm_limit is not UNSET:
            field_dict["team_member_rpm_limit"] = team_member_rpm_limit
        if team_member_tpm_limit is not UNSET:
            field_dict["team_member_tpm_limit"] = team_member_tpm_limit
        if team_member_key_duration is not UNSET:
            field_dict["team_member_key_duration"] = team_member_key_duration
        if allowed_vector_store_indexes is not UNSET:
            field_dict["allowed_vector_store_indexes"] = allowed_vector_store_indexes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allowed_vector_store_index_item import AllowedVectorStoreIndexItem
        from ..models.lite_llm_object_permission_base import LiteLLMObjectPermissionBase
        from ..models.member import Member
        from ..models.new_team_request_metadata_type_0 import NewTeamRequestMetadataType0
        from ..models.new_team_request_model_aliases_type_0 import NewTeamRequestModelAliasesType0
        from ..models.new_team_request_model_rpm_limit_type_0 import NewTeamRequestModelRpmLimitType0
        from ..models.new_team_request_model_tpm_limit_type_0 import NewTeamRequestModelTpmLimitType0
        from ..models.new_team_request_router_settings_type_0 import NewTeamRequestRouterSettingsType0
        from ..models.new_team_request_secret_manager_settings_type_0 import NewTeamRequestSecretManagerSettingsType0
        d = dict(src_dict)
        def _parse_team_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_alias = _parse_team_alias(d.pop("team_alias", UNSET))


        def _parse_team_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_id = _parse_team_id(d.pop("team_id", UNSET))


        def _parse_organization_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))


        admins = cast(list[Any], d.pop("admins", UNSET))


        members = cast(list[Any], d.pop("members", UNSET))


        _members_with_roles = d.pop("members_with_roles", UNSET)
        members_with_roles: list[Member] | Unset = UNSET
        if _members_with_roles is not UNSET:
            members_with_roles = []
            for members_with_roles_item_data in _members_with_roles:
                members_with_roles_item = Member.from_dict(members_with_roles_item_data)



                members_with_roles.append(members_with_roles_item)


        def _parse_team_member_permissions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                team_member_permissions_type_0 = cast(list[str], data)

                return team_member_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        team_member_permissions = _parse_team_member_permissions(d.pop("team_member_permissions", UNSET))


        def _parse_metadata(data: object) -> NewTeamRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = NewTeamRequestMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewTeamRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        def _parse_tpm_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tpm_limit = _parse_tpm_limit(d.pop("tpm_limit", UNSET))


        def _parse_rpm_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rpm_limit = _parse_rpm_limit(d.pop("rpm_limit", UNSET))


        def _parse_max_budget(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_budget = _parse_max_budget(d.pop("max_budget", UNSET))


        def _parse_budget_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))


        models = cast(list[Any], d.pop("models", UNSET))


        blocked = d.pop("blocked", UNSET)

        def _parse_router_settings(data: object) -> NewTeamRequestRouterSettingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                router_settings_type_0 = NewTeamRequestRouterSettingsType0.from_dict(data)



                return router_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewTeamRequestRouterSettingsType0 | None | Unset, data)

        router_settings = _parse_router_settings(d.pop("router_settings", UNSET))


        def _parse_model_aliases(data: object) -> NewTeamRequestModelAliasesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_aliases_type_0 = NewTeamRequestModelAliasesType0.from_dict(data)



                return model_aliases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewTeamRequestModelAliasesType0 | None | Unset, data)

        model_aliases = _parse_model_aliases(d.pop("model_aliases", UNSET))


        def _parse_tags(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[Any], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))


        def _parse_guardrails(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                guardrails_type_0 = cast(list[str], data)

                return guardrails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        guardrails = _parse_guardrails(d.pop("guardrails", UNSET))


        def _parse_prompts(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prompts_type_0 = cast(list[str], data)

                return prompts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        prompts = _parse_prompts(d.pop("prompts", UNSET))


        def _parse_object_permission(data: object) -> LiteLLMObjectPermissionBase | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                object_permission_type_0 = LiteLLMObjectPermissionBase.from_dict(data)



                return object_permission_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMObjectPermissionBase | None | Unset, data)

        object_permission = _parse_object_permission(d.pop("object_permission", UNSET))


        def _parse_allowed_passthrough_routes(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_passthrough_routes_type_0 = cast(list[Any], data)

                return allowed_passthrough_routes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        allowed_passthrough_routes = _parse_allowed_passthrough_routes(d.pop("allowed_passthrough_routes", UNSET))


        def _parse_secret_manager_settings(data: object) -> NewTeamRequestSecretManagerSettingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secret_manager_settings_type_0 = NewTeamRequestSecretManagerSettingsType0.from_dict(data)



                return secret_manager_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewTeamRequestSecretManagerSettingsType0 | None | Unset, data)

        secret_manager_settings = _parse_secret_manager_settings(d.pop("secret_manager_settings", UNSET))


        def _parse_model_rpm_limit(data: object) -> NewTeamRequestModelRpmLimitType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_rpm_limit_type_0 = NewTeamRequestModelRpmLimitType0.from_dict(data)



                return model_rpm_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewTeamRequestModelRpmLimitType0 | None | Unset, data)

        model_rpm_limit = _parse_model_rpm_limit(d.pop("model_rpm_limit", UNSET))


        def _parse_rpm_limit_type(data: object) -> NewTeamRequestRpmLimitTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rpm_limit_type_type_0 = NewTeamRequestRpmLimitTypeType0(data)



                return rpm_limit_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewTeamRequestRpmLimitTypeType0 | None | Unset, data)

        rpm_limit_type = _parse_rpm_limit_type(d.pop("rpm_limit_type", UNSET))


        def _parse_tpm_limit_type(data: object) -> NewTeamRequestTpmLimitTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tpm_limit_type_type_0 = NewTeamRequestTpmLimitTypeType0(data)



                return tpm_limit_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewTeamRequestTpmLimitTypeType0 | None | Unset, data)

        tpm_limit_type = _parse_tpm_limit_type(d.pop("tpm_limit_type", UNSET))


        def _parse_model_tpm_limit(data: object) -> NewTeamRequestModelTpmLimitType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_tpm_limit_type_0 = NewTeamRequestModelTpmLimitType0.from_dict(data)



                return model_tpm_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewTeamRequestModelTpmLimitType0 | None | Unset, data)

        model_tpm_limit = _parse_model_tpm_limit(d.pop("model_tpm_limit", UNSET))


        def _parse_team_member_budget(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        team_member_budget = _parse_team_member_budget(d.pop("team_member_budget", UNSET))


        def _parse_team_member_rpm_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        team_member_rpm_limit = _parse_team_member_rpm_limit(d.pop("team_member_rpm_limit", UNSET))


        def _parse_team_member_tpm_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        team_member_tpm_limit = _parse_team_member_tpm_limit(d.pop("team_member_tpm_limit", UNSET))


        def _parse_team_member_key_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_member_key_duration = _parse_team_member_key_duration(d.pop("team_member_key_duration", UNSET))


        def _parse_allowed_vector_store_indexes(data: object) -> list[AllowedVectorStoreIndexItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_vector_store_indexes_type_0 = []
                _allowed_vector_store_indexes_type_0 = data
                for allowed_vector_store_indexes_type_0_item_data in (_allowed_vector_store_indexes_type_0):
                    allowed_vector_store_indexes_type_0_item = AllowedVectorStoreIndexItem.from_dict(allowed_vector_store_indexes_type_0_item_data)



                    allowed_vector_store_indexes_type_0.append(allowed_vector_store_indexes_type_0_item)

                return allowed_vector_store_indexes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AllowedVectorStoreIndexItem] | None | Unset, data)

        allowed_vector_store_indexes = _parse_allowed_vector_store_indexes(d.pop("allowed_vector_store_indexes", UNSET))


        new_team_request = cls(
            team_alias=team_alias,
            team_id=team_id,
            organization_id=organization_id,
            admins=admins,
            members=members,
            members_with_roles=members_with_roles,
            team_member_permissions=team_member_permissions,
            metadata=metadata,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
            max_budget=max_budget,
            budget_duration=budget_duration,
            models=models,
            blocked=blocked,
            router_settings=router_settings,
            model_aliases=model_aliases,
            tags=tags,
            guardrails=guardrails,
            prompts=prompts,
            object_permission=object_permission,
            allowed_passthrough_routes=allowed_passthrough_routes,
            secret_manager_settings=secret_manager_settings,
            model_rpm_limit=model_rpm_limit,
            rpm_limit_type=rpm_limit_type,
            tpm_limit_type=tpm_limit_type,
            model_tpm_limit=model_tpm_limit,
            team_member_budget=team_member_budget,
            team_member_rpm_limit=team_member_rpm_limit,
            team_member_tpm_limit=team_member_tpm_limit,
            team_member_key_duration=team_member_key_duration,
            allowed_vector_store_indexes=allowed_vector_store_indexes,
        )


        new_team_request.additional_properties = d
        return new_team_request

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
