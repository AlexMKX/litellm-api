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
  from ..models.lite_llm_budget_table import LiteLLMBudgetTable
  from ..models.lite_llm_object_permission_table import LiteLLMObjectPermissionTable
  from ..models.lite_llm_project_table_metadata_type_0 import LiteLLMProjectTableMetadataType0
  from ..models.lite_llm_project_table_model_rpm_limit_type_0 import LiteLLMProjectTableModelRpmLimitType0
  from ..models.lite_llm_project_table_model_spend_type_0 import LiteLLMProjectTableModelSpendType0
  from ..models.lite_llm_project_table_model_tpm_limit_type_0 import LiteLLMProjectTableModelTpmLimitType0





T = TypeVar("T", bound="LiteLLMProjectTable")



@_attrs_define
class LiteLLMProjectTable:
    """ Database model representation for project

        Attributes:
            project_id (str):
            created_by (str):
            updated_by (str):
            project_alias (None | str | Unset):
            description (None | str | Unset):
            team_id (None | str | Unset):
            budget_id (None | str | Unset):
            metadata (LiteLLMProjectTableMetadataType0 | None | Unset):
            models (list[str] | Unset):
            spend (float | Unset):  Default: 0.0.
            model_spend (LiteLLMProjectTableModelSpendType0 | None | Unset):
            model_rpm_limit (LiteLLMProjectTableModelRpmLimitType0 | None | Unset):
            model_tpm_limit (LiteLLMProjectTableModelTpmLimitType0 | None | Unset):
            blocked (bool | Unset):  Default: False.
            object_permission_id (None | str | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            litellm_budget_table (LiteLLMBudgetTable | None | Unset):
            object_permission (LiteLLMObjectPermissionTable | None | Unset):
     """

    project_id: str
    created_by: str
    updated_by: str
    project_alias: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    team_id: None | str | Unset = UNSET
    budget_id: None | str | Unset = UNSET
    metadata: LiteLLMProjectTableMetadataType0 | None | Unset = UNSET
    models: list[str] | Unset = UNSET
    spend: float | Unset = 0.0
    model_spend: LiteLLMProjectTableModelSpendType0 | None | Unset = UNSET
    model_rpm_limit: LiteLLMProjectTableModelRpmLimitType0 | None | Unset = UNSET
    model_tpm_limit: LiteLLMProjectTableModelTpmLimitType0 | None | Unset = UNSET
    blocked: bool | Unset = False
    object_permission_id: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    litellm_budget_table: LiteLLMBudgetTable | None | Unset = UNSET
    object_permission: LiteLLMObjectPermissionTable | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_budget_table import LiteLLMBudgetTable
        from ..models.lite_llm_object_permission_table import LiteLLMObjectPermissionTable
        from ..models.lite_llm_project_table_metadata_type_0 import LiteLLMProjectTableMetadataType0
        from ..models.lite_llm_project_table_model_rpm_limit_type_0 import LiteLLMProjectTableModelRpmLimitType0
        from ..models.lite_llm_project_table_model_spend_type_0 import LiteLLMProjectTableModelSpendType0
        from ..models.lite_llm_project_table_model_tpm_limit_type_0 import LiteLLMProjectTableModelTpmLimitType0
        project_id = self.project_id

        created_by = self.created_by

        updated_by = self.updated_by

        project_alias: None | str | Unset
        if isinstance(self.project_alias, Unset):
            project_alias = UNSET
        else:
            project_alias = self.project_alias

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        team_id: None | str | Unset
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        else:
            team_id = self.team_id

        budget_id: None | str | Unset
        if isinstance(self.budget_id, Unset):
            budget_id = UNSET
        else:
            budget_id = self.budget_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, LiteLLMProjectTableMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        models: list[str] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = self.models



        spend = self.spend

        model_spend: dict[str, Any] | None | Unset
        if isinstance(self.model_spend, Unset):
            model_spend = UNSET
        elif isinstance(self.model_spend, LiteLLMProjectTableModelSpendType0):
            model_spend = self.model_spend.to_dict()
        else:
            model_spend = self.model_spend

        model_rpm_limit: dict[str, Any] | None | Unset
        if isinstance(self.model_rpm_limit, Unset):
            model_rpm_limit = UNSET
        elif isinstance(self.model_rpm_limit, LiteLLMProjectTableModelRpmLimitType0):
            model_rpm_limit = self.model_rpm_limit.to_dict()
        else:
            model_rpm_limit = self.model_rpm_limit

        model_tpm_limit: dict[str, Any] | None | Unset
        if isinstance(self.model_tpm_limit, Unset):
            model_tpm_limit = UNSET
        elif isinstance(self.model_tpm_limit, LiteLLMProjectTableModelTpmLimitType0):
            model_tpm_limit = self.model_tpm_limit.to_dict()
        else:
            model_tpm_limit = self.model_tpm_limit

        blocked = self.blocked

        object_permission_id: None | str | Unset
        if isinstance(self.object_permission_id, Unset):
            object_permission_id = UNSET
        else:
            object_permission_id = self.object_permission_id

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        litellm_budget_table: dict[str, Any] | None | Unset
        if isinstance(self.litellm_budget_table, Unset):
            litellm_budget_table = UNSET
        elif isinstance(self.litellm_budget_table, LiteLLMBudgetTable):
            litellm_budget_table = self.litellm_budget_table.to_dict()
        else:
            litellm_budget_table = self.litellm_budget_table

        object_permission: dict[str, Any] | None | Unset
        if isinstance(self.object_permission, Unset):
            object_permission = UNSET
        elif isinstance(self.object_permission, LiteLLMObjectPermissionTable):
            object_permission = self.object_permission.to_dict()
        else:
            object_permission = self.object_permission


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "project_id": project_id,
            "created_by": created_by,
            "updated_by": updated_by,
        })
        if project_alias is not UNSET:
            field_dict["project_alias"] = project_alias
        if description is not UNSET:
            field_dict["description"] = description
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if budget_id is not UNSET:
            field_dict["budget_id"] = budget_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if models is not UNSET:
            field_dict["models"] = models
        if spend is not UNSET:
            field_dict["spend"] = spend
        if model_spend is not UNSET:
            field_dict["model_spend"] = model_spend
        if model_rpm_limit is not UNSET:
            field_dict["model_rpm_limit"] = model_rpm_limit
        if model_tpm_limit is not UNSET:
            field_dict["model_tpm_limit"] = model_tpm_limit
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if object_permission_id is not UNSET:
            field_dict["object_permission_id"] = object_permission_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if litellm_budget_table is not UNSET:
            field_dict["litellm_budget_table"] = litellm_budget_table
        if object_permission is not UNSET:
            field_dict["object_permission"] = object_permission

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_budget_table import LiteLLMBudgetTable
        from ..models.lite_llm_object_permission_table import LiteLLMObjectPermissionTable
        from ..models.lite_llm_project_table_metadata_type_0 import LiteLLMProjectTableMetadataType0
        from ..models.lite_llm_project_table_model_rpm_limit_type_0 import LiteLLMProjectTableModelRpmLimitType0
        from ..models.lite_llm_project_table_model_spend_type_0 import LiteLLMProjectTableModelSpendType0
        from ..models.lite_llm_project_table_model_tpm_limit_type_0 import LiteLLMProjectTableModelTpmLimitType0
        d = dict(src_dict)
        project_id = d.pop("project_id")

        created_by = d.pop("created_by")

        updated_by = d.pop("updated_by")

        def _parse_project_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_alias = _parse_project_alias(d.pop("project_alias", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_team_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_id = _parse_team_id(d.pop("team_id", UNSET))


        def _parse_budget_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_id = _parse_budget_id(d.pop("budget_id", UNSET))


        def _parse_metadata(data: object) -> LiteLLMProjectTableMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = LiteLLMProjectTableMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMProjectTableMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        models = cast(list[str], d.pop("models", UNSET))


        spend = d.pop("spend", UNSET)

        def _parse_model_spend(data: object) -> LiteLLMProjectTableModelSpendType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_spend_type_0 = LiteLLMProjectTableModelSpendType0.from_dict(data)



                return model_spend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMProjectTableModelSpendType0 | None | Unset, data)

        model_spend = _parse_model_spend(d.pop("model_spend", UNSET))


        def _parse_model_rpm_limit(data: object) -> LiteLLMProjectTableModelRpmLimitType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_rpm_limit_type_0 = LiteLLMProjectTableModelRpmLimitType0.from_dict(data)



                return model_rpm_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMProjectTableModelRpmLimitType0 | None | Unset, data)

        model_rpm_limit = _parse_model_rpm_limit(d.pop("model_rpm_limit", UNSET))


        def _parse_model_tpm_limit(data: object) -> LiteLLMProjectTableModelTpmLimitType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_tpm_limit_type_0 = LiteLLMProjectTableModelTpmLimitType0.from_dict(data)



                return model_tpm_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMProjectTableModelTpmLimitType0 | None | Unset, data)

        model_tpm_limit = _parse_model_tpm_limit(d.pop("model_tpm_limit", UNSET))


        blocked = d.pop("blocked", UNSET)

        def _parse_object_permission_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_permission_id = _parse_object_permission_id(d.pop("object_permission_id", UNSET))


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


        def _parse_litellm_budget_table(data: object) -> LiteLLMBudgetTable | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_budget_table_type_0 = LiteLLMBudgetTable.from_dict(data)



                return litellm_budget_table_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMBudgetTable | None | Unset, data)

        litellm_budget_table = _parse_litellm_budget_table(d.pop("litellm_budget_table", UNSET))


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


        lite_llm_project_table = cls(
            project_id=project_id,
            created_by=created_by,
            updated_by=updated_by,
            project_alias=project_alias,
            description=description,
            team_id=team_id,
            budget_id=budget_id,
            metadata=metadata,
            models=models,
            spend=spend,
            model_spend=model_spend,
            model_rpm_limit=model_rpm_limit,
            model_tpm_limit=model_tpm_limit,
            blocked=blocked,
            object_permission_id=object_permission_id,
            created_at=created_at,
            updated_at=updated_at,
            litellm_budget_table=litellm_budget_table,
            object_permission=object_permission,
        )


        lite_llm_project_table.additional_properties = d
        return lite_llm_project_table

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
