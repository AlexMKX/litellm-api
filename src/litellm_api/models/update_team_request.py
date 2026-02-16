from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.allowed_vector_store_index_item import AllowedVectorStoreIndexItem
  from ..models.lite_llm_object_permission_base import LiteLLMObjectPermissionBase
  from ..models.update_team_request_metadata_type_0 import UpdateTeamRequestMetadataType0
  from ..models.update_team_request_model_aliases_type_0 import UpdateTeamRequestModelAliasesType0
  from ..models.update_team_request_model_rpm_limit_type_0 import UpdateTeamRequestModelRpmLimitType0
  from ..models.update_team_request_model_tpm_limit_type_0 import UpdateTeamRequestModelTpmLimitType0
  from ..models.update_team_request_router_settings_type_0 import UpdateTeamRequestRouterSettingsType0
  from ..models.update_team_request_secret_manager_settings_type_0 import UpdateTeamRequestSecretManagerSettingsType0





T = TypeVar("T", bound="UpdateTeamRequest")



@_attrs_define
class UpdateTeamRequest:
    """ UpdateTeamRequest, used by /team/update when you need to update a team

    team_id: str
    team_alias: Optional[str] = None
    organization_id: Optional[str] = None
    metadata: Optional[dict] = None
    tpm_limit: Optional[int] = None
    rpm_limit: Optional[int] = None
    max_budget: Optional[float] = None
    models: Optional[list] = None
    blocked: Optional[bool] = None
    budget_duration: Optional[str] = None
    guardrails: Optional[List[str]] = None
    policies: Optional[List[str]] = None

        Attributes:
            team_id (str):
            team_alias (None | str | Unset):
            organization_id (None | str | Unset):
            metadata (None | Unset | UpdateTeamRequestMetadataType0):
            tpm_limit (int | None | Unset):
            rpm_limit (int | None | Unset):
            max_budget (float | None | Unset):
            soft_budget (float | None | Unset):
            models (list[Any] | None | Unset):
            blocked (bool | None | Unset):
            budget_duration (None | str | Unset):
            tags (list[Any] | None | Unset):
            model_aliases (None | Unset | UpdateTeamRequestModelAliasesType0):
            guardrails (list[str] | None | Unset):
            policies (list[str] | None | Unset):
            object_permission (LiteLLMObjectPermissionBase | None | Unset):
            team_member_budget (float | None | Unset):
            team_member_budget_duration (None | str | Unset):
            team_member_rpm_limit (int | None | Unset):
            team_member_tpm_limit (int | None | Unset):
            team_member_key_duration (None | str | Unset):
            allowed_passthrough_routes (list[Any] | None | Unset):
            secret_manager_settings (None | Unset | UpdateTeamRequestSecretManagerSettingsType0):
            prompts (list[str] | None | Unset):
            model_rpm_limit (None | Unset | UpdateTeamRequestModelRpmLimitType0):
            model_tpm_limit (None | Unset | UpdateTeamRequestModelTpmLimitType0):
            allowed_vector_store_indexes (list[AllowedVectorStoreIndexItem] | None | Unset):
            router_settings (None | Unset | UpdateTeamRequestRouterSettingsType0):
            access_group_ids (list[str] | None | Unset):
     """

    team_id: str
    team_alias: None | str | Unset = UNSET
    organization_id: None | str | Unset = UNSET
    metadata: None | Unset | UpdateTeamRequestMetadataType0 = UNSET
    tpm_limit: int | None | Unset = UNSET
    rpm_limit: int | None | Unset = UNSET
    max_budget: float | None | Unset = UNSET
    soft_budget: float | None | Unset = UNSET
    models: list[Any] | None | Unset = UNSET
    blocked: bool | None | Unset = UNSET
    budget_duration: None | str | Unset = UNSET
    tags: list[Any] | None | Unset = UNSET
    model_aliases: None | Unset | UpdateTeamRequestModelAliasesType0 = UNSET
    guardrails: list[str] | None | Unset = UNSET
    policies: list[str] | None | Unset = UNSET
    object_permission: LiteLLMObjectPermissionBase | None | Unset = UNSET
    team_member_budget: float | None | Unset = UNSET
    team_member_budget_duration: None | str | Unset = UNSET
    team_member_rpm_limit: int | None | Unset = UNSET
    team_member_tpm_limit: int | None | Unset = UNSET
    team_member_key_duration: None | str | Unset = UNSET
    allowed_passthrough_routes: list[Any] | None | Unset = UNSET
    secret_manager_settings: None | Unset | UpdateTeamRequestSecretManagerSettingsType0 = UNSET
    prompts: list[str] | None | Unset = UNSET
    model_rpm_limit: None | Unset | UpdateTeamRequestModelRpmLimitType0 = UNSET
    model_tpm_limit: None | Unset | UpdateTeamRequestModelTpmLimitType0 = UNSET
    allowed_vector_store_indexes: list[AllowedVectorStoreIndexItem] | None | Unset = UNSET
    router_settings: None | Unset | UpdateTeamRequestRouterSettingsType0 = UNSET
    access_group_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_team_request_router_settings_type_0 import UpdateTeamRequestRouterSettingsType0
        from ..models.lite_llm_object_permission_base import LiteLLMObjectPermissionBase
        from ..models.update_team_request_model_rpm_limit_type_0 import UpdateTeamRequestModelRpmLimitType0
        from ..models.update_team_request_model_tpm_limit_type_0 import UpdateTeamRequestModelTpmLimitType0
        from ..models.update_team_request_model_aliases_type_0 import UpdateTeamRequestModelAliasesType0
        from ..models.update_team_request_metadata_type_0 import UpdateTeamRequestMetadataType0
        from ..models.allowed_vector_store_index_item import AllowedVectorStoreIndexItem
        from ..models.update_team_request_secret_manager_settings_type_0 import UpdateTeamRequestSecretManagerSettingsType0
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

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, UpdateTeamRequestMetadataType0):
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

        soft_budget: float | None | Unset
        if isinstance(self.soft_budget, Unset):
            soft_budget = UNSET
        else:
            soft_budget = self.soft_budget

        models: list[Any] | None | Unset
        if isinstance(self.models, Unset):
            models = UNSET
        elif isinstance(self.models, list):
            models = self.models


        else:
            models = self.models

        blocked: bool | None | Unset
        if isinstance(self.blocked, Unset):
            blocked = UNSET
        else:
            blocked = self.blocked

        budget_duration: None | str | Unset
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration

        tags: list[Any] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags


        else:
            tags = self.tags

        model_aliases: dict[str, Any] | None | Unset
        if isinstance(self.model_aliases, Unset):
            model_aliases = UNSET
        elif isinstance(self.model_aliases, UpdateTeamRequestModelAliasesType0):
            model_aliases = self.model_aliases.to_dict()
        else:
            model_aliases = self.model_aliases

        guardrails: list[str] | None | Unset
        if isinstance(self.guardrails, Unset):
            guardrails = UNSET
        elif isinstance(self.guardrails, list):
            guardrails = self.guardrails


        else:
            guardrails = self.guardrails

        policies: list[str] | None | Unset
        if isinstance(self.policies, Unset):
            policies = UNSET
        elif isinstance(self.policies, list):
            policies = self.policies


        else:
            policies = self.policies

        object_permission: dict[str, Any] | None | Unset
        if isinstance(self.object_permission, Unset):
            object_permission = UNSET
        elif isinstance(self.object_permission, LiteLLMObjectPermissionBase):
            object_permission = self.object_permission.to_dict()
        else:
            object_permission = self.object_permission

        team_member_budget: float | None | Unset
        if isinstance(self.team_member_budget, Unset):
            team_member_budget = UNSET
        else:
            team_member_budget = self.team_member_budget

        team_member_budget_duration: None | str | Unset
        if isinstance(self.team_member_budget_duration, Unset):
            team_member_budget_duration = UNSET
        else:
            team_member_budget_duration = self.team_member_budget_duration

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
        elif isinstance(self.secret_manager_settings, UpdateTeamRequestSecretManagerSettingsType0):
            secret_manager_settings = self.secret_manager_settings.to_dict()
        else:
            secret_manager_settings = self.secret_manager_settings

        prompts: list[str] | None | Unset
        if isinstance(self.prompts, Unset):
            prompts = UNSET
        elif isinstance(self.prompts, list):
            prompts = self.prompts


        else:
            prompts = self.prompts

        model_rpm_limit: dict[str, Any] | None | Unset
        if isinstance(self.model_rpm_limit, Unset):
            model_rpm_limit = UNSET
        elif isinstance(self.model_rpm_limit, UpdateTeamRequestModelRpmLimitType0):
            model_rpm_limit = self.model_rpm_limit.to_dict()
        else:
            model_rpm_limit = self.model_rpm_limit

        model_tpm_limit: dict[str, Any] | None | Unset
        if isinstance(self.model_tpm_limit, Unset):
            model_tpm_limit = UNSET
        elif isinstance(self.model_tpm_limit, UpdateTeamRequestModelTpmLimitType0):
            model_tpm_limit = self.model_tpm_limit.to_dict()
        else:
            model_tpm_limit = self.model_tpm_limit

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

        router_settings: dict[str, Any] | None | Unset
        if isinstance(self.router_settings, Unset):
            router_settings = UNSET
        elif isinstance(self.router_settings, UpdateTeamRequestRouterSettingsType0):
            router_settings = self.router_settings.to_dict()
        else:
            router_settings = self.router_settings

        access_group_ids: list[str] | None | Unset
        if isinstance(self.access_group_ids, Unset):
            access_group_ids = UNSET
        elif isinstance(self.access_group_ids, list):
            access_group_ids = self.access_group_ids


        else:
            access_group_ids = self.access_group_ids


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "team_id": team_id,
        })
        if team_alias is not UNSET:
            field_dict["team_alias"] = team_alias
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tpm_limit is not UNSET:
            field_dict["tpm_limit"] = tpm_limit
        if rpm_limit is not UNSET:
            field_dict["rpm_limit"] = rpm_limit
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if soft_budget is not UNSET:
            field_dict["soft_budget"] = soft_budget
        if models is not UNSET:
            field_dict["models"] = models
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if budget_duration is not UNSET:
            field_dict["budget_duration"] = budget_duration
        if tags is not UNSET:
            field_dict["tags"] = tags
        if model_aliases is not UNSET:
            field_dict["model_aliases"] = model_aliases
        if guardrails is not UNSET:
            field_dict["guardrails"] = guardrails
        if policies is not UNSET:
            field_dict["policies"] = policies
        if object_permission is not UNSET:
            field_dict["object_permission"] = object_permission
        if team_member_budget is not UNSET:
            field_dict["team_member_budget"] = team_member_budget
        if team_member_budget_duration is not UNSET:
            field_dict["team_member_budget_duration"] = team_member_budget_duration
        if team_member_rpm_limit is not UNSET:
            field_dict["team_member_rpm_limit"] = team_member_rpm_limit
        if team_member_tpm_limit is not UNSET:
            field_dict["team_member_tpm_limit"] = team_member_tpm_limit
        if team_member_key_duration is not UNSET:
            field_dict["team_member_key_duration"] = team_member_key_duration
        if allowed_passthrough_routes is not UNSET:
            field_dict["allowed_passthrough_routes"] = allowed_passthrough_routes
        if secret_manager_settings is not UNSET:
            field_dict["secret_manager_settings"] = secret_manager_settings
        if prompts is not UNSET:
            field_dict["prompts"] = prompts
        if model_rpm_limit is not UNSET:
            field_dict["model_rpm_limit"] = model_rpm_limit
        if model_tpm_limit is not UNSET:
            field_dict["model_tpm_limit"] = model_tpm_limit
        if allowed_vector_store_indexes is not UNSET:
            field_dict["allowed_vector_store_indexes"] = allowed_vector_store_indexes
        if router_settings is not UNSET:
            field_dict["router_settings"] = router_settings
        if access_group_ids is not UNSET:
            field_dict["access_group_ids"] = access_group_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allowed_vector_store_index_item import AllowedVectorStoreIndexItem
        from ..models.lite_llm_object_permission_base import LiteLLMObjectPermissionBase
        from ..models.update_team_request_metadata_type_0 import UpdateTeamRequestMetadataType0
        from ..models.update_team_request_model_aliases_type_0 import UpdateTeamRequestModelAliasesType0
        from ..models.update_team_request_model_rpm_limit_type_0 import UpdateTeamRequestModelRpmLimitType0
        from ..models.update_team_request_model_tpm_limit_type_0 import UpdateTeamRequestModelTpmLimitType0
        from ..models.update_team_request_router_settings_type_0 import UpdateTeamRequestRouterSettingsType0
        from ..models.update_team_request_secret_manager_settings_type_0 import UpdateTeamRequestSecretManagerSettingsType0
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


        def _parse_metadata(data: object) -> None | Unset | UpdateTeamRequestMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = UpdateTeamRequestMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateTeamRequestMetadataType0, data)

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


        def _parse_soft_budget(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        soft_budget = _parse_soft_budget(d.pop("soft_budget", UNSET))


        def _parse_models(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                models_type_0 = cast(list[Any], data)

                return models_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        models = _parse_models(d.pop("models", UNSET))


        def _parse_blocked(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        blocked = _parse_blocked(d.pop("blocked", UNSET))


        def _parse_budget_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))


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


        def _parse_model_aliases(data: object) -> None | Unset | UpdateTeamRequestModelAliasesType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_aliases_type_0 = UpdateTeamRequestModelAliasesType0.from_dict(data)



                return model_aliases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateTeamRequestModelAliasesType0, data)

        model_aliases = _parse_model_aliases(d.pop("model_aliases", UNSET))


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


        def _parse_policies(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                policies_type_0 = cast(list[str], data)

                return policies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        policies = _parse_policies(d.pop("policies", UNSET))


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


        def _parse_team_member_budget(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        team_member_budget = _parse_team_member_budget(d.pop("team_member_budget", UNSET))


        def _parse_team_member_budget_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_member_budget_duration = _parse_team_member_budget_duration(d.pop("team_member_budget_duration", UNSET))


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


        def _parse_secret_manager_settings(data: object) -> None | Unset | UpdateTeamRequestSecretManagerSettingsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secret_manager_settings_type_0 = UpdateTeamRequestSecretManagerSettingsType0.from_dict(data)



                return secret_manager_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateTeamRequestSecretManagerSettingsType0, data)

        secret_manager_settings = _parse_secret_manager_settings(d.pop("secret_manager_settings", UNSET))


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


        def _parse_model_rpm_limit(data: object) -> None | Unset | UpdateTeamRequestModelRpmLimitType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_rpm_limit_type_0 = UpdateTeamRequestModelRpmLimitType0.from_dict(data)



                return model_rpm_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateTeamRequestModelRpmLimitType0, data)

        model_rpm_limit = _parse_model_rpm_limit(d.pop("model_rpm_limit", UNSET))


        def _parse_model_tpm_limit(data: object) -> None | Unset | UpdateTeamRequestModelTpmLimitType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_tpm_limit_type_0 = UpdateTeamRequestModelTpmLimitType0.from_dict(data)



                return model_tpm_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateTeamRequestModelTpmLimitType0, data)

        model_tpm_limit = _parse_model_tpm_limit(d.pop("model_tpm_limit", UNSET))


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


        def _parse_router_settings(data: object) -> None | Unset | UpdateTeamRequestRouterSettingsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                router_settings_type_0 = UpdateTeamRequestRouterSettingsType0.from_dict(data)



                return router_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateTeamRequestRouterSettingsType0, data)

        router_settings = _parse_router_settings(d.pop("router_settings", UNSET))


        def _parse_access_group_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_group_ids_type_0 = cast(list[str], data)

                return access_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        access_group_ids = _parse_access_group_ids(d.pop("access_group_ids", UNSET))


        update_team_request = cls(
            team_id=team_id,
            team_alias=team_alias,
            organization_id=organization_id,
            metadata=metadata,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
            max_budget=max_budget,
            soft_budget=soft_budget,
            models=models,
            blocked=blocked,
            budget_duration=budget_duration,
            tags=tags,
            model_aliases=model_aliases,
            guardrails=guardrails,
            policies=policies,
            object_permission=object_permission,
            team_member_budget=team_member_budget,
            team_member_budget_duration=team_member_budget_duration,
            team_member_rpm_limit=team_member_rpm_limit,
            team_member_tpm_limit=team_member_tpm_limit,
            team_member_key_duration=team_member_key_duration,
            allowed_passthrough_routes=allowed_passthrough_routes,
            secret_manager_settings=secret_manager_settings,
            prompts=prompts,
            model_rpm_limit=model_rpm_limit,
            model_tpm_limit=model_tpm_limit,
            allowed_vector_store_indexes=allowed_vector_store_indexes,
            router_settings=router_settings,
            access_group_ids=access_group_ids,
        )


        update_team_request.additional_properties = d
        return update_team_request

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
