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
  from ..models.lite_llm_object_permission_table import LiteLLMObjectPermissionTable
  from ..models.lite_llm_verification_token_aliases import LiteLLMVerificationTokenAliases
  from ..models.lite_llm_verification_token_config import LiteLLMVerificationTokenConfig
  from ..models.lite_llm_verification_token_litellm_budget_table_type_0 import LiteLLMVerificationTokenLitellmBudgetTableType0
  from ..models.lite_llm_verification_token_metadata import LiteLLMVerificationTokenMetadata
  from ..models.lite_llm_verification_token_model_max_budget import LiteLLMVerificationTokenModelMaxBudget
  from ..models.lite_llm_verification_token_model_spend import LiteLLMVerificationTokenModelSpend
  from ..models.lite_llm_verification_token_permissions import LiteLLMVerificationTokenPermissions
  from ..models.lite_llm_verification_token_router_settings_type_0 import LiteLLMVerificationTokenRouterSettingsType0





T = TypeVar("T", bound="LiteLLMVerificationToken")



@_attrs_define
class LiteLLMVerificationToken:
    """ 
        Attributes:
            token (None | str | Unset):
            key_name (None | str | Unset):
            key_alias (None | str | Unset):
            spend (float | Unset):  Default: 0.0.
            max_budget (float | None | Unset):
            expires (datetime.datetime | None | str | Unset):
            models (list[Any] | Unset):
            aliases (LiteLLMVerificationTokenAliases | Unset):
            config (LiteLLMVerificationTokenConfig | Unset):
            user_id (None | str | Unset):
            team_id (None | str | Unset):
            max_parallel_requests (int | None | Unset):
            metadata (LiteLLMVerificationTokenMetadata | Unset):
            tpm_limit (int | None | Unset):
            rpm_limit (int | None | Unset):
            budget_duration (None | str | Unset):
            budget_reset_at (datetime.datetime | None | Unset):
            allowed_cache_controls (list[Any] | None | Unset):
            allowed_routes (list[Any] | None | Unset):
            permissions (LiteLLMVerificationTokenPermissions | Unset):
            model_spend (LiteLLMVerificationTokenModelSpend | Unset):
            model_max_budget (LiteLLMVerificationTokenModelMaxBudget | Unset):
            soft_budget_cooldown (bool | Unset):  Default: False.
            blocked (bool | None | Unset):
            litellm_budget_table (LiteLLMVerificationTokenLitellmBudgetTableType0 | None | Unset):
            org_id (None | str | Unset):
            created_at (datetime.datetime | None | Unset):
            created_by (None | str | Unset):
            updated_at (datetime.datetime | None | Unset):
            updated_by (None | str | Unset):
            object_permission_id (None | str | Unset):
            object_permission (LiteLLMObjectPermissionTable | None | Unset):
            rotation_count (int | None | Unset):  Default: 0.
            auto_rotate (bool | None | Unset):  Default: False.
            rotation_interval (None | str | Unset):
            last_rotation_at (datetime.datetime | None | Unset):
            key_rotation_at (datetime.datetime | None | Unset):
            router_settings (LiteLLMVerificationTokenRouterSettingsType0 | None | Unset):
     """

    token: None | str | Unset = UNSET
    key_name: None | str | Unset = UNSET
    key_alias: None | str | Unset = UNSET
    spend: float | Unset = 0.0
    max_budget: float | None | Unset = UNSET
    expires: datetime.datetime | None | str | Unset = UNSET
    models: list[Any] | Unset = UNSET
    aliases: LiteLLMVerificationTokenAliases | Unset = UNSET
    config: LiteLLMVerificationTokenConfig | Unset = UNSET
    user_id: None | str | Unset = UNSET
    team_id: None | str | Unset = UNSET
    max_parallel_requests: int | None | Unset = UNSET
    metadata: LiteLLMVerificationTokenMetadata | Unset = UNSET
    tpm_limit: int | None | Unset = UNSET
    rpm_limit: int | None | Unset = UNSET
    budget_duration: None | str | Unset = UNSET
    budget_reset_at: datetime.datetime | None | Unset = UNSET
    allowed_cache_controls: list[Any] | None | Unset = UNSET
    allowed_routes: list[Any] | None | Unset = UNSET
    permissions: LiteLLMVerificationTokenPermissions | Unset = UNSET
    model_spend: LiteLLMVerificationTokenModelSpend | Unset = UNSET
    model_max_budget: LiteLLMVerificationTokenModelMaxBudget | Unset = UNSET
    soft_budget_cooldown: bool | Unset = False
    blocked: bool | None | Unset = UNSET
    litellm_budget_table: LiteLLMVerificationTokenLitellmBudgetTableType0 | None | Unset = UNSET
    org_id: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    object_permission_id: None | str | Unset = UNSET
    object_permission: LiteLLMObjectPermissionTable | None | Unset = UNSET
    rotation_count: int | None | Unset = 0
    auto_rotate: bool | None | Unset = False
    rotation_interval: None | str | Unset = UNSET
    last_rotation_at: datetime.datetime | None | Unset = UNSET
    key_rotation_at: datetime.datetime | None | Unset = UNSET
    router_settings: LiteLLMVerificationTokenRouterSettingsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_verification_token_router_settings_type_0 import LiteLLMVerificationTokenRouterSettingsType0
        from ..models.lite_llm_verification_token_model_max_budget import LiteLLMVerificationTokenModelMaxBudget
        from ..models.lite_llm_verification_token_permissions import LiteLLMVerificationTokenPermissions
        from ..models.lite_llm_verification_token_config import LiteLLMVerificationTokenConfig
        from ..models.lite_llm_verification_token_metadata import LiteLLMVerificationTokenMetadata
        from ..models.lite_llm_verification_token_litellm_budget_table_type_0 import LiteLLMVerificationTokenLitellmBudgetTableType0
        from ..models.lite_llm_object_permission_table import LiteLLMObjectPermissionTable
        from ..models.lite_llm_verification_token_aliases import LiteLLMVerificationTokenAliases
        from ..models.lite_llm_verification_token_model_spend import LiteLLMVerificationTokenModelSpend
        token: None | str | Unset
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        key_name: None | str | Unset
        if isinstance(self.key_name, Unset):
            key_name = UNSET
        else:
            key_name = self.key_name

        key_alias: None | str | Unset
        if isinstance(self.key_alias, Unset):
            key_alias = UNSET
        else:
            key_alias = self.key_alias

        spend = self.spend

        max_budget: float | None | Unset
        if isinstance(self.max_budget, Unset):
            max_budget = UNSET
        else:
            max_budget = self.max_budget

        expires: None | str | Unset
        if isinstance(self.expires, Unset):
            expires = UNSET
        elif isinstance(self.expires, datetime.datetime):
            expires = self.expires.isoformat()
        else:
            expires = self.expires

        models: list[Any] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = self.models



        aliases: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases.to_dict()

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        team_id: None | str | Unset
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        else:
            team_id = self.team_id

        max_parallel_requests: int | None | Unset
        if isinstance(self.max_parallel_requests, Unset):
            max_parallel_requests = UNSET
        else:
            max_parallel_requests = self.max_parallel_requests

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

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

        budget_duration: None | str | Unset
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration

        budget_reset_at: None | str | Unset
        if isinstance(self.budget_reset_at, Unset):
            budget_reset_at = UNSET
        elif isinstance(self.budget_reset_at, datetime.datetime):
            budget_reset_at = self.budget_reset_at.isoformat()
        else:
            budget_reset_at = self.budget_reset_at

        allowed_cache_controls: list[Any] | None | Unset
        if isinstance(self.allowed_cache_controls, Unset):
            allowed_cache_controls = UNSET
        elif isinstance(self.allowed_cache_controls, list):
            allowed_cache_controls = self.allowed_cache_controls


        else:
            allowed_cache_controls = self.allowed_cache_controls

        allowed_routes: list[Any] | None | Unset
        if isinstance(self.allowed_routes, Unset):
            allowed_routes = UNSET
        elif isinstance(self.allowed_routes, list):
            allowed_routes = self.allowed_routes


        else:
            allowed_routes = self.allowed_routes

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        model_spend: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_spend, Unset):
            model_spend = self.model_spend.to_dict()

        model_max_budget: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_max_budget, Unset):
            model_max_budget = self.model_max_budget.to_dict()

        soft_budget_cooldown = self.soft_budget_cooldown

        blocked: bool | None | Unset
        if isinstance(self.blocked, Unset):
            blocked = UNSET
        else:
            blocked = self.blocked

        litellm_budget_table: dict[str, Any] | None | Unset
        if isinstance(self.litellm_budget_table, Unset):
            litellm_budget_table = UNSET
        elif isinstance(self.litellm_budget_table, LiteLLMVerificationTokenLitellmBudgetTableType0):
            litellm_budget_table = self.litellm_budget_table.to_dict()
        else:
            litellm_budget_table = self.litellm_budget_table

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        else:
            org_id = self.org_id

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        object_permission_id: None | str | Unset
        if isinstance(self.object_permission_id, Unset):
            object_permission_id = UNSET
        else:
            object_permission_id = self.object_permission_id

        object_permission: dict[str, Any] | None | Unset
        if isinstance(self.object_permission, Unset):
            object_permission = UNSET
        elif isinstance(self.object_permission, LiteLLMObjectPermissionTable):
            object_permission = self.object_permission.to_dict()
        else:
            object_permission = self.object_permission

        rotation_count: int | None | Unset
        if isinstance(self.rotation_count, Unset):
            rotation_count = UNSET
        else:
            rotation_count = self.rotation_count

        auto_rotate: bool | None | Unset
        if isinstance(self.auto_rotate, Unset):
            auto_rotate = UNSET
        else:
            auto_rotate = self.auto_rotate

        rotation_interval: None | str | Unset
        if isinstance(self.rotation_interval, Unset):
            rotation_interval = UNSET
        else:
            rotation_interval = self.rotation_interval

        last_rotation_at: None | str | Unset
        if isinstance(self.last_rotation_at, Unset):
            last_rotation_at = UNSET
        elif isinstance(self.last_rotation_at, datetime.datetime):
            last_rotation_at = self.last_rotation_at.isoformat()
        else:
            last_rotation_at = self.last_rotation_at

        key_rotation_at: None | str | Unset
        if isinstance(self.key_rotation_at, Unset):
            key_rotation_at = UNSET
        elif isinstance(self.key_rotation_at, datetime.datetime):
            key_rotation_at = self.key_rotation_at.isoformat()
        else:
            key_rotation_at = self.key_rotation_at

        router_settings: dict[str, Any] | None | Unset
        if isinstance(self.router_settings, Unset):
            router_settings = UNSET
        elif isinstance(self.router_settings, LiteLLMVerificationTokenRouterSettingsType0):
            router_settings = self.router_settings.to_dict()
        else:
            router_settings = self.router_settings


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if token is not UNSET:
            field_dict["token"] = token
        if key_name is not UNSET:
            field_dict["key_name"] = key_name
        if key_alias is not UNSET:
            field_dict["key_alias"] = key_alias
        if spend is not UNSET:
            field_dict["spend"] = spend
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if expires is not UNSET:
            field_dict["expires"] = expires
        if models is not UNSET:
            field_dict["models"] = models
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if config is not UNSET:
            field_dict["config"] = config
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if max_parallel_requests is not UNSET:
            field_dict["max_parallel_requests"] = max_parallel_requests
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tpm_limit is not UNSET:
            field_dict["tpm_limit"] = tpm_limit
        if rpm_limit is not UNSET:
            field_dict["rpm_limit"] = rpm_limit
        if budget_duration is not UNSET:
            field_dict["budget_duration"] = budget_duration
        if budget_reset_at is not UNSET:
            field_dict["budget_reset_at"] = budget_reset_at
        if allowed_cache_controls is not UNSET:
            field_dict["allowed_cache_controls"] = allowed_cache_controls
        if allowed_routes is not UNSET:
            field_dict["allowed_routes"] = allowed_routes
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if model_spend is not UNSET:
            field_dict["model_spend"] = model_spend
        if model_max_budget is not UNSET:
            field_dict["model_max_budget"] = model_max_budget
        if soft_budget_cooldown is not UNSET:
            field_dict["soft_budget_cooldown"] = soft_budget_cooldown
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if litellm_budget_table is not UNSET:
            field_dict["litellm_budget_table"] = litellm_budget_table
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if object_permission_id is not UNSET:
            field_dict["object_permission_id"] = object_permission_id
        if object_permission is not UNSET:
            field_dict["object_permission"] = object_permission
        if rotation_count is not UNSET:
            field_dict["rotation_count"] = rotation_count
        if auto_rotate is not UNSET:
            field_dict["auto_rotate"] = auto_rotate
        if rotation_interval is not UNSET:
            field_dict["rotation_interval"] = rotation_interval
        if last_rotation_at is not UNSET:
            field_dict["last_rotation_at"] = last_rotation_at
        if key_rotation_at is not UNSET:
            field_dict["key_rotation_at"] = key_rotation_at
        if router_settings is not UNSET:
            field_dict["router_settings"] = router_settings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_object_permission_table import LiteLLMObjectPermissionTable
        from ..models.lite_llm_verification_token_aliases import LiteLLMVerificationTokenAliases
        from ..models.lite_llm_verification_token_config import LiteLLMVerificationTokenConfig
        from ..models.lite_llm_verification_token_litellm_budget_table_type_0 import LiteLLMVerificationTokenLitellmBudgetTableType0
        from ..models.lite_llm_verification_token_metadata import LiteLLMVerificationTokenMetadata
        from ..models.lite_llm_verification_token_model_max_budget import LiteLLMVerificationTokenModelMaxBudget
        from ..models.lite_llm_verification_token_model_spend import LiteLLMVerificationTokenModelSpend
        from ..models.lite_llm_verification_token_permissions import LiteLLMVerificationTokenPermissions
        from ..models.lite_llm_verification_token_router_settings_type_0 import LiteLLMVerificationTokenRouterSettingsType0
        d = dict(src_dict)
        def _parse_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token = _parse_token(d.pop("token", UNSET))


        def _parse_key_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_name = _parse_key_name(d.pop("key_name", UNSET))


        def _parse_key_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_alias = _parse_key_alias(d.pop("key_alias", UNSET))


        spend = d.pop("spend", UNSET)

        def _parse_max_budget(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_budget = _parse_max_budget(d.pop("max_budget", UNSET))


        def _parse_expires(data: object) -> datetime.datetime | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_type_1 = isoparse(data)



                return expires_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | str | Unset, data)

        expires = _parse_expires(d.pop("expires", UNSET))


        models = cast(list[Any], d.pop("models", UNSET))


        _aliases = d.pop("aliases", UNSET)
        aliases: LiteLLMVerificationTokenAliases | Unset
        if isinstance(_aliases,  Unset):
            aliases = UNSET
        else:
            aliases = LiteLLMVerificationTokenAliases.from_dict(_aliases)




        _config = d.pop("config", UNSET)
        config: LiteLLMVerificationTokenConfig | Unset
        if isinstance(_config,  Unset):
            config = UNSET
        else:
            config = LiteLLMVerificationTokenConfig.from_dict(_config)




        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))


        def _parse_team_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_id = _parse_team_id(d.pop("team_id", UNSET))


        def _parse_max_parallel_requests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_parallel_requests = _parse_max_parallel_requests(d.pop("max_parallel_requests", UNSET))


        _metadata = d.pop("metadata", UNSET)
        metadata: LiteLLMVerificationTokenMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = LiteLLMVerificationTokenMetadata.from_dict(_metadata)




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


        def _parse_budget_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))


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


        def _parse_allowed_cache_controls(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_cache_controls_type_0 = cast(list[Any], data)

                return allowed_cache_controls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        allowed_cache_controls = _parse_allowed_cache_controls(d.pop("allowed_cache_controls", UNSET))


        def _parse_allowed_routes(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_routes_type_0 = cast(list[Any], data)

                return allowed_routes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        allowed_routes = _parse_allowed_routes(d.pop("allowed_routes", UNSET))


        _permissions = d.pop("permissions", UNSET)
        permissions: LiteLLMVerificationTokenPermissions | Unset
        if isinstance(_permissions,  Unset):
            permissions = UNSET
        else:
            permissions = LiteLLMVerificationTokenPermissions.from_dict(_permissions)




        _model_spend = d.pop("model_spend", UNSET)
        model_spend: LiteLLMVerificationTokenModelSpend | Unset
        if isinstance(_model_spend,  Unset):
            model_spend = UNSET
        else:
            model_spend = LiteLLMVerificationTokenModelSpend.from_dict(_model_spend)




        _model_max_budget = d.pop("model_max_budget", UNSET)
        model_max_budget: LiteLLMVerificationTokenModelMaxBudget | Unset
        if isinstance(_model_max_budget,  Unset):
            model_max_budget = UNSET
        else:
            model_max_budget = LiteLLMVerificationTokenModelMaxBudget.from_dict(_model_max_budget)




        soft_budget_cooldown = d.pop("soft_budget_cooldown", UNSET)

        def _parse_blocked(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        blocked = _parse_blocked(d.pop("blocked", UNSET))


        def _parse_litellm_budget_table(data: object) -> LiteLLMVerificationTokenLitellmBudgetTableType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_budget_table_type_0 = LiteLLMVerificationTokenLitellmBudgetTableType0.from_dict(data)



                return litellm_budget_table_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMVerificationTokenLitellmBudgetTableType0 | None | Unset, data)

        litellm_budget_table = _parse_litellm_budget_table(d.pop("litellm_budget_table", UNSET))


        def _parse_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))


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


        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))


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


        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))


        def _parse_object_permission_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_permission_id = _parse_object_permission_id(d.pop("object_permission_id", UNSET))


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


        def _parse_rotation_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rotation_count = _parse_rotation_count(d.pop("rotation_count", UNSET))


        def _parse_auto_rotate(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_rotate = _parse_auto_rotate(d.pop("auto_rotate", UNSET))


        def _parse_rotation_interval(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rotation_interval = _parse_rotation_interval(d.pop("rotation_interval", UNSET))


        def _parse_last_rotation_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_rotation_at_type_0 = isoparse(data)



                return last_rotation_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_rotation_at = _parse_last_rotation_at(d.pop("last_rotation_at", UNSET))


        def _parse_key_rotation_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                key_rotation_at_type_0 = isoparse(data)



                return key_rotation_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        key_rotation_at = _parse_key_rotation_at(d.pop("key_rotation_at", UNSET))


        def _parse_router_settings(data: object) -> LiteLLMVerificationTokenRouterSettingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                router_settings_type_0 = LiteLLMVerificationTokenRouterSettingsType0.from_dict(data)



                return router_settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMVerificationTokenRouterSettingsType0 | None | Unset, data)

        router_settings = _parse_router_settings(d.pop("router_settings", UNSET))


        lite_llm_verification_token = cls(
            token=token,
            key_name=key_name,
            key_alias=key_alias,
            spend=spend,
            max_budget=max_budget,
            expires=expires,
            models=models,
            aliases=aliases,
            config=config,
            user_id=user_id,
            team_id=team_id,
            max_parallel_requests=max_parallel_requests,
            metadata=metadata,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
            budget_duration=budget_duration,
            budget_reset_at=budget_reset_at,
            allowed_cache_controls=allowed_cache_controls,
            allowed_routes=allowed_routes,
            permissions=permissions,
            model_spend=model_spend,
            model_max_budget=model_max_budget,
            soft_budget_cooldown=soft_budget_cooldown,
            blocked=blocked,
            litellm_budget_table=litellm_budget_table,
            org_id=org_id,
            created_at=created_at,
            created_by=created_by,
            updated_at=updated_at,
            updated_by=updated_by,
            object_permission_id=object_permission_id,
            object_permission=object_permission,
            rotation_count=rotation_count,
            auto_rotate=auto_rotate,
            rotation_interval=rotation_interval,
            last_rotation_at=last_rotation_at,
            key_rotation_at=key_rotation_at,
            router_settings=router_settings,
        )


        lite_llm_verification_token.additional_properties = d
        return lite_llm_verification_token

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
