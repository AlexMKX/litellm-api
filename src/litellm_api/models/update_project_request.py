from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.lite_llm_object_permission_base import LiteLLMObjectPermissionBase
  from ..models.update_project_request_metadata_type_0 import UpdateProjectRequestMetadataType0
  from ..models.update_project_request_model_max_budget_type_0 import UpdateProjectRequestModelMaxBudgetType0
  from ..models.update_project_request_model_rpm_limit_type_0 import UpdateProjectRequestModelRpmLimitType0
  from ..models.update_project_request_model_tpm_limit_type_0 import UpdateProjectRequestModelTpmLimitType0





T = TypeVar("T", bound="UpdateProjectRequest")



@_attrs_define
class UpdateProjectRequest:
    """ Request model for POST /project/update

        Attributes:
            project_id (str):
            budget_id (None | str | Unset):
            soft_budget (float | None | Unset):
            max_budget (float | None | Unset):
            max_parallel_requests (int | None | Unset):
            tpm_limit (int | None | Unset):
            rpm_limit (int | None | Unset):
            model_max_budget (None | Unset | UpdateProjectRequestModelMaxBudgetType0):
            budget_duration (None | str | Unset):
            project_alias (None | str | Unset):
            description (None | str | Unset):
            team_id (None | str | Unset):
            metadata (None | Unset | UpdateProjectRequestMetadataType0):
            models (list[str] | None | Unset):
            model_rpm_limit (None | Unset | UpdateProjectRequestModelRpmLimitType0):
            model_tpm_limit (None | Unset | UpdateProjectRequestModelTpmLimitType0):
            blocked (bool | None | Unset):
            object_permission (LiteLLMObjectPermissionBase | None | Unset):
     """

    project_id: str
    budget_id: None | str | Unset = UNSET
    soft_budget: float | None | Unset = UNSET
    max_budget: float | None | Unset = UNSET
    max_parallel_requests: int | None | Unset = UNSET
    tpm_limit: int | None | Unset = UNSET
    rpm_limit: int | None | Unset = UNSET
    model_max_budget: None | Unset | UpdateProjectRequestModelMaxBudgetType0 = UNSET
    budget_duration: None | str | Unset = UNSET
    project_alias: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    team_id: None | str | Unset = UNSET
    metadata: None | Unset | UpdateProjectRequestMetadataType0 = UNSET
    models: list[str] | None | Unset = UNSET
    model_rpm_limit: None | Unset | UpdateProjectRequestModelRpmLimitType0 = UNSET
    model_tpm_limit: None | Unset | UpdateProjectRequestModelTpmLimitType0 = UNSET
    blocked: bool | None | Unset = UNSET
    object_permission: LiteLLMObjectPermissionBase | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_project_request_metadata_type_0 import UpdateProjectRequestMetadataType0
        from ..models.update_project_request_model_tpm_limit_type_0 import UpdateProjectRequestModelTpmLimitType0
        from ..models.update_project_request_model_max_budget_type_0 import UpdateProjectRequestModelMaxBudgetType0
        from ..models.lite_llm_object_permission_base import LiteLLMObjectPermissionBase
        from ..models.update_project_request_model_rpm_limit_type_0 import UpdateProjectRequestModelRpmLimitType0
        project_id = self.project_id

        budget_id: None | str | Unset
        if isinstance(self.budget_id, Unset):
            budget_id = UNSET
        else:
            budget_id = self.budget_id

        soft_budget: float | None | Unset
        if isinstance(self.soft_budget, Unset):
            soft_budget = UNSET
        else:
            soft_budget = self.soft_budget

        max_budget: float | None | Unset
        if isinstance(self.max_budget, Unset):
            max_budget = UNSET
        else:
            max_budget = self.max_budget

        max_parallel_requests: int | None | Unset
        if isinstance(self.max_parallel_requests, Unset):
            max_parallel_requests = UNSET
        else:
            max_parallel_requests = self.max_parallel_requests

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

        model_max_budget: dict[str, Any] | None | Unset
        if isinstance(self.model_max_budget, Unset):
            model_max_budget = UNSET
        elif isinstance(self.model_max_budget, UpdateProjectRequestModelMaxBudgetType0):
            model_max_budget = self.model_max_budget.to_dict()
        else:
            model_max_budget = self.model_max_budget

        budget_duration: None | str | Unset
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration

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

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, UpdateProjectRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        models: list[str] | None | Unset
        if isinstance(self.models, Unset):
            models = UNSET
        elif isinstance(self.models, list):
            models = self.models


        else:
            models = self.models

        model_rpm_limit: dict[str, Any] | None | Unset
        if isinstance(self.model_rpm_limit, Unset):
            model_rpm_limit = UNSET
        elif isinstance(self.model_rpm_limit, UpdateProjectRequestModelRpmLimitType0):
            model_rpm_limit = self.model_rpm_limit.to_dict()
        else:
            model_rpm_limit = self.model_rpm_limit

        model_tpm_limit: dict[str, Any] | None | Unset
        if isinstance(self.model_tpm_limit, Unset):
            model_tpm_limit = UNSET
        elif isinstance(self.model_tpm_limit, UpdateProjectRequestModelTpmLimitType0):
            model_tpm_limit = self.model_tpm_limit.to_dict()
        else:
            model_tpm_limit = self.model_tpm_limit

        blocked: bool | None | Unset
        if isinstance(self.blocked, Unset):
            blocked = UNSET
        else:
            blocked = self.blocked

        object_permission: dict[str, Any] | None | Unset
        if isinstance(self.object_permission, Unset):
            object_permission = UNSET
        elif isinstance(self.object_permission, LiteLLMObjectPermissionBase):
            object_permission = self.object_permission.to_dict()
        else:
            object_permission = self.object_permission


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "project_id": project_id,
        })
        if budget_id is not UNSET:
            field_dict["budget_id"] = budget_id
        if soft_budget is not UNSET:
            field_dict["soft_budget"] = soft_budget
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if max_parallel_requests is not UNSET:
            field_dict["max_parallel_requests"] = max_parallel_requests
        if tpm_limit is not UNSET:
            field_dict["tpm_limit"] = tpm_limit
        if rpm_limit is not UNSET:
            field_dict["rpm_limit"] = rpm_limit
        if model_max_budget is not UNSET:
            field_dict["model_max_budget"] = model_max_budget
        if budget_duration is not UNSET:
            field_dict["budget_duration"] = budget_duration
        if project_alias is not UNSET:
            field_dict["project_alias"] = project_alias
        if description is not UNSET:
            field_dict["description"] = description
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if models is not UNSET:
            field_dict["models"] = models
        if model_rpm_limit is not UNSET:
            field_dict["model_rpm_limit"] = model_rpm_limit
        if model_tpm_limit is not UNSET:
            field_dict["model_tpm_limit"] = model_tpm_limit
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if object_permission is not UNSET:
            field_dict["object_permission"] = object_permission

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_object_permission_base import LiteLLMObjectPermissionBase
        from ..models.update_project_request_metadata_type_0 import UpdateProjectRequestMetadataType0
        from ..models.update_project_request_model_max_budget_type_0 import UpdateProjectRequestModelMaxBudgetType0
        from ..models.update_project_request_model_rpm_limit_type_0 import UpdateProjectRequestModelRpmLimitType0
        from ..models.update_project_request_model_tpm_limit_type_0 import UpdateProjectRequestModelTpmLimitType0
        d = dict(src_dict)
        project_id = d.pop("project_id")

        def _parse_budget_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_id = _parse_budget_id(d.pop("budget_id", UNSET))


        def _parse_soft_budget(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        soft_budget = _parse_soft_budget(d.pop("soft_budget", UNSET))


        def _parse_max_budget(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_budget = _parse_max_budget(d.pop("max_budget", UNSET))


        def _parse_max_parallel_requests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_parallel_requests = _parse_max_parallel_requests(d.pop("max_parallel_requests", UNSET))


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


        def _parse_model_max_budget(data: object) -> None | Unset | UpdateProjectRequestModelMaxBudgetType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_max_budget_type_0 = UpdateProjectRequestModelMaxBudgetType0.from_dict(data)



                return model_max_budget_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateProjectRequestModelMaxBudgetType0, data)

        model_max_budget = _parse_model_max_budget(d.pop("model_max_budget", UNSET))


        def _parse_budget_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))


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


        def _parse_metadata(data: object) -> None | Unset | UpdateProjectRequestMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = UpdateProjectRequestMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateProjectRequestMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        def _parse_models(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                models_type_0 = cast(list[str], data)

                return models_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        models = _parse_models(d.pop("models", UNSET))


        def _parse_model_rpm_limit(data: object) -> None | Unset | UpdateProjectRequestModelRpmLimitType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_rpm_limit_type_0 = UpdateProjectRequestModelRpmLimitType0.from_dict(data)



                return model_rpm_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateProjectRequestModelRpmLimitType0, data)

        model_rpm_limit = _parse_model_rpm_limit(d.pop("model_rpm_limit", UNSET))


        def _parse_model_tpm_limit(data: object) -> None | Unset | UpdateProjectRequestModelTpmLimitType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_tpm_limit_type_0 = UpdateProjectRequestModelTpmLimitType0.from_dict(data)



                return model_tpm_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateProjectRequestModelTpmLimitType0, data)

        model_tpm_limit = _parse_model_tpm_limit(d.pop("model_tpm_limit", UNSET))


        def _parse_blocked(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        blocked = _parse_blocked(d.pop("blocked", UNSET))


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


        update_project_request = cls(
            project_id=project_id,
            budget_id=budget_id,
            soft_budget=soft_budget,
            max_budget=max_budget,
            max_parallel_requests=max_parallel_requests,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
            model_max_budget=model_max_budget,
            budget_duration=budget_duration,
            project_alias=project_alias,
            description=description,
            team_id=team_id,
            metadata=metadata,
            models=models,
            model_rpm_limit=model_rpm_limit,
            model_tpm_limit=model_tpm_limit,
            blocked=blocked,
            object_permission=object_permission,
        )


        update_project_request.additional_properties = d
        return update_project_request

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
