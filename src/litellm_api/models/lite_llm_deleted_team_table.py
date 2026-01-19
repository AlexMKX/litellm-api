from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.lite_llm_deleted_team_table_metadata_type_0 import LiteLLMDeletedTeamTableMetadataType0
  from ..models.lite_llm_deleted_team_table_router_settings_type_0 import LiteLLMDeletedTeamTableRouterSettingsType0
  from ..models.lite_llm_model_table import LiteLLMModelTable
  from ..models.lite_llm_object_permission_table import LiteLLMObjectPermissionTable
  from ..models.member import Member





T = TypeVar("T", bound="LiteLLMDeletedTeamTable")



@_attrs_define
class LiteLLMDeletedTeamTable:
    """ Recording of deleted teams for audit purposes. Mirrors LiteLLM_TeamTable
    plus metadata captured at deletion time.

        Attributes:
            team_id (str):
            team_alias (None | str | Unset):
            organization_id (None | str | Unset):
            admins (list[Any] | Unset):
            members (list[Any] | Unset):
            members_with_roles (list[Member] | Unset):
            team_member_permissions (list[str] | None | Unset):
            metadata (LiteLLMDeletedTeamTableMetadataType0 | None | Unset):
            tpm_limit (int | None | Unset):
            rpm_limit (int | None | Unset):
            max_budget (float | None | Unset):
            budget_duration (None | str | Unset):
            models (list[Any] | Unset):
            blocked (bool | Unset):  Default: False.
            router_settings (LiteLLMDeletedTeamTableRouterSettingsType0 | None | Unset):
            spend (float | None | Unset):
            max_parallel_requests (int | None | Unset):
            budget_reset_at (datetime.datetime | None | Unset):
            model_id (int | None | Unset):
            litellm_model_table (LiteLLMModelTable | None | Unset):
            object_permission (LiteLLMObjectPermissionTable | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            created_at (datetime.datetime | None | Unset):
            object_permission_id (None | str | Unset):
            id (None | str | Unset):
            deleted_at (datetime.datetime | None | Unset):
            deleted_by (None | str | Unset):
            deleted_by_api_key (None | str | Unset):
            litellm_changed_by (None | str | Unset):
     """

    team_id: str
    team_alias: None | str | Unset = UNSET
    organization_id: None | str | Unset = UNSET
    admins: list[Any] | Unset = UNSET
    members: list[Any] | Unset = UNSET
    members_with_roles: list[Member] | Unset = UNSET
    team_member_permissions: list[str] | None | Unset = UNSET
    metadata: LiteLLMDeletedTeamTableMetadataType0 | None | Unset = UNSET
    tpm_limit: int | None | Unset = UNSET
    rpm_limit: int | None | Unset = UNSET
    max_budget: float | None | Unset = UNSET
    budget_duration: None | str | Unset = UNSET
    models: list[Any] | Unset = UNSET
    blocked: bool | Unset = False
    router_settings: LiteLLMDeletedTeamTableRouterSettingsType0 | None | Unset = UNSET
    spend: float | None | Unset = UNSET
    max_parallel_requests: int | None | Unset = UNSET
    budget_reset_at: datetime.datetime | None | Unset = UNSET
    model_id: int | None | Unset = UNSET
    litellm_model_table: LiteLLMModelTable | None | Unset = UNSET
    object_permission: LiteLLMObjectPermissionTable | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    object_permission_id: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    deleted_at: datetime.datetime | None | Unset = UNSET
    deleted_by: None | str | Unset = UNSET
    deleted_by_api_key: None | str | Unset = UNSET
    litellm_changed_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.member import Member
        from ..models.lite_llm_model_table import LiteLLMModelTable
        from ..models.lite_llm_deleted_team_table_router_settings_type_0 import LiteLLMDeletedTeamTableRouterSettingsType0
        from ..models.lite_llm_deleted_team_table_metadata_type_0 import LiteLLMDeletedTeamTableMetadataType0
        from ..models.lite_llm_object_permission_table import LiteLLMObjectPermissionTable
        team_id = self.team_id

        team_alias: None | str | Unset
        if isinstance(self.team_alias, Unset):
            team_alias = UNSET
        else:
            team_alias = self.team_alias

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
        elif isinstance(self.metadata, LiteLLMDeletedTeamTableMetadataType0):
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
        elif isinstance(self.router_settings, LiteLLMDeletedTeamTableRouterSettingsType0):
            router_settings = self.router_settings.to_dict()
        else:
            router_settings = self.router_settings

        spend: float | None | Unset
        if isinstance(self.spend, Unset):
            spend = UNSET
        else:
            spend = self.spend

        max_parallel_requests: int | None | Unset
        if isinstance(self.max_parallel_requests, Unset):
            max_parallel_requests = UNSET
        else:
            max_parallel_requests = self.max_parallel_requests

        budget_reset_at: None | str | Unset
        if isinstance(self.budget_reset_at, Unset):
            budget_reset_at = UNSET
        elif isinstance(self.budget_reset_at, datetime.datetime):
            budget_reset_at = self.budget_reset_at.isoformat()
        else:
            budget_reset_at = self.budget_reset_at

        model_id: int | None | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        litellm_model_table: dict[str, Any] | None | Unset
        if isinstance(self.litellm_model_table, Unset):
            litellm_model_table = UNSET
        elif isinstance(self.litellm_model_table, LiteLLMModelTable):
            litellm_model_table = self.litellm_model_table.to_dict()
        else:
            litellm_model_table = self.litellm_model_table

        object_permission: dict[str, Any] | None | Unset
        if isinstance(self.object_permission, Unset):
            object_permission = UNSET
        elif isinstance(self.object_permission, LiteLLMObjectPermissionTable):
            object_permission = self.object_permission.to_dict()
        else:
            object_permission = self.object_permission

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        object_permission_id: None | str | Unset
        if isinstance(self.object_permission_id, Unset):
            object_permission_id = UNSET
        else:
            object_permission_id = self.object_permission_id

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        deleted_by: None | str | Unset
        if isinstance(self.deleted_by, Unset):
            deleted_by = UNSET
        else:
            deleted_by = self.deleted_by

        deleted_by_api_key: None | str | Unset
        if isinstance(self.deleted_by_api_key, Unset):
            deleted_by_api_key = UNSET
        else:
            deleted_by_api_key = self.deleted_by_api_key

        litellm_changed_by: None | str | Unset
        if isinstance(self.litellm_changed_by, Unset):
            litellm_changed_by = UNSET
        else:
            litellm_changed_by = self.litellm_changed_by


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "team_id": team_id,
        })
        if team_alias is not UNSET:
            field_dict["team_alias"] = team_alias
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
        if spend is not UNSET:
            field_dict["spend"] = spend
        if max_parallel_requests is not UNSET:
            field_dict["max_parallel_requests"] = max_parallel_requests
        if budget_reset_at is not UNSET:
            field_dict["budget_reset_at"] = budget_reset_at
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if litellm_model_table is not UNSET:
            field_dict["litellm_model_table"] = litellm_model_table
        if object_permission is not UNSET:
            field_dict["object_permission"] = object_permission
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if object_permission_id is not UNSET:
            field_dict["object_permission_id"] = object_permission_id
        if id is not UNSET:
            field_dict["id"] = id
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if deleted_by is not UNSET:
            field_dict["deleted_by"] = deleted_by
        if deleted_by_api_key is not UNSET:
            field_dict["deleted_by_api_key"] = deleted_by_api_key
        if litellm_changed_by is not UNSET:
            field_dict["litellm_changed_by"] = litellm_changed_by

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_deleted_team_table_metadata_type_0 import LiteLLMDeletedTeamTableMetadataType0
        from ..models.lite_llm_deleted_team_table_router_settings_type_0 import LiteLLMDeletedTeamTableRouterSettingsType0
        from ..models.lite_llm_model_table import LiteLLMModelTable
        from ..models.lite_llm_object_permission_table import LiteLLMObjectPermissionTable
        from ..models.member import Member
        d = dict(src_dict)
        team_id = d.pop("team_id")

        def _parse_team_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_alias = _parse_team_alias(d.pop("team_alias", UNSET))


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


        def _parse_metadata(data: object) -> LiteLLMDeletedTeamTableMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = LiteLLMDeletedTeamTableMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMDeletedTeamTableMetadataType0 | None | Unset, data)

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

        def _parse_router_settings(data: object) -> LiteLLMDeletedTeamTableRouterSettingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                router_settings_type_0 = LiteLLMDeletedTeamTableRouterSettingsType0.from_dict(data)



                return router_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMDeletedTeamTableRouterSettingsType0 | None | Unset, data)

        router_settings = _parse_router_settings(d.pop("router_settings", UNSET))


        def _parse_spend(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        spend = _parse_spend(d.pop("spend", UNSET))


        def _parse_max_parallel_requests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_parallel_requests = _parse_max_parallel_requests(d.pop("max_parallel_requests", UNSET))


        def _parse_budget_reset_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                budget_reset_at_type_0 = isoparse(data)



                return budget_reset_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        budget_reset_at = _parse_budget_reset_at(d.pop("budget_reset_at", UNSET))


        def _parse_model_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))


        def _parse_litellm_model_table(data: object) -> LiteLLMModelTable | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_model_table_type_0 = LiteLLMModelTable.from_dict(data)



                return litellm_model_table_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMModelTable | None | Unset, data)

        litellm_model_table = _parse_litellm_model_table(d.pop("litellm_model_table", UNSET))


        def _parse_object_permission(data: object) -> LiteLLMObjectPermissionTable | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                object_permission_type_0 = LiteLLMObjectPermissionTable.from_dict(data)



                return object_permission_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMObjectPermissionTable | None | Unset, data)

        object_permission = _parse_object_permission(d.pop("object_permission", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))


        def _parse_object_permission_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_permission_id = _parse_object_permission_id(d.pop("object_permission_id", UNSET))


        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_deleted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = isoparse(data)



                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))


        def _parse_deleted_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_by = _parse_deleted_by(d.pop("deleted_by", UNSET))


        def _parse_deleted_by_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_by_api_key = _parse_deleted_by_api_key(d.pop("deleted_by_api_key", UNSET))


        def _parse_litellm_changed_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        litellm_changed_by = _parse_litellm_changed_by(d.pop("litellm_changed_by", UNSET))


        lite_llm_deleted_team_table = cls(
            team_id=team_id,
            team_alias=team_alias,
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
            spend=spend,
            max_parallel_requests=max_parallel_requests,
            budget_reset_at=budget_reset_at,
            model_id=model_id,
            litellm_model_table=litellm_model_table,
            object_permission=object_permission,
            updated_at=updated_at,
            created_at=created_at,
            object_permission_id=object_permission_id,
            id=id,
            deleted_at=deleted_at,
            deleted_by=deleted_by,
            deleted_by_api_key=deleted_by_api_key,
            litellm_changed_by=litellm_changed_by,
        )


        lite_llm_deleted_team_table.additional_properties = d
        return lite_llm_deleted_team_table

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
