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
  from ..models.new_organization_request_metadata_type_0 import NewOrganizationRequestMetadataType0
  from ..models.new_organization_request_model_max_budget_type_0 import NewOrganizationRequestModelMaxBudgetType0
  from ..models.new_organization_request_model_rpm_limit_type_0 import NewOrganizationRequestModelRpmLimitType0
  from ..models.new_organization_request_model_tpm_limit_type_0 import NewOrganizationRequestModelTpmLimitType0





T = TypeVar("T", bound="NewOrganizationRequest")



@_attrs_define
class NewOrganizationRequest:
    """ 
        Attributes:
            organization_alias (str):
            budget_id (None | str | Unset):
            soft_budget (float | None | Unset):
            max_budget (float | None | Unset):
            max_parallel_requests (int | None | Unset):
            tpm_limit (int | None | Unset):
            rpm_limit (int | None | Unset):
            model_max_budget (NewOrganizationRequestModelMaxBudgetType0 | None | Unset):
            budget_duration (None | str | Unset):
            organization_id (None | str | Unset):
            models (list[Any] | Unset):
            metadata (NewOrganizationRequestMetadataType0 | None | Unset):
            model_rpm_limit (NewOrganizationRequestModelRpmLimitType0 | None | Unset):
            model_tpm_limit (NewOrganizationRequestModelTpmLimitType0 | None | Unset):
            object_permission (LiteLLMObjectPermissionBase | None | Unset):
     """

    organization_alias: str
    budget_id: None | str | Unset = UNSET
    soft_budget: float | None | Unset = UNSET
    max_budget: float | None | Unset = UNSET
    max_parallel_requests: int | None | Unset = UNSET
    tpm_limit: int | None | Unset = UNSET
    rpm_limit: int | None | Unset = UNSET
    model_max_budget: NewOrganizationRequestModelMaxBudgetType0 | None | Unset = UNSET
    budget_duration: None | str | Unset = UNSET
    organization_id: None | str | Unset = UNSET
    models: list[Any] | Unset = UNSET
    metadata: NewOrganizationRequestMetadataType0 | None | Unset = UNSET
    model_rpm_limit: NewOrganizationRequestModelRpmLimitType0 | None | Unset = UNSET
    model_tpm_limit: NewOrganizationRequestModelTpmLimitType0 | None | Unset = UNSET
    object_permission: LiteLLMObjectPermissionBase | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.new_organization_request_model_max_budget_type_0 import NewOrganizationRequestModelMaxBudgetType0
        from ..models.lite_llm_object_permission_base import LiteLLMObjectPermissionBase
        from ..models.new_organization_request_metadata_type_0 import NewOrganizationRequestMetadataType0
        from ..models.new_organization_request_model_tpm_limit_type_0 import NewOrganizationRequestModelTpmLimitType0
        from ..models.new_organization_request_model_rpm_limit_type_0 import NewOrganizationRequestModelRpmLimitType0
        organization_alias = self.organization_alias

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
        elif isinstance(self.model_max_budget, NewOrganizationRequestModelMaxBudgetType0):
            model_max_budget = self.model_max_budget.to_dict()
        else:
            model_max_budget = self.model_max_budget

        budget_duration: None | str | Unset
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = self.organization_id

        models: list[Any] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = self.models



        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, NewOrganizationRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        model_rpm_limit: dict[str, Any] | None | Unset
        if isinstance(self.model_rpm_limit, Unset):
            model_rpm_limit = UNSET
        elif isinstance(self.model_rpm_limit, NewOrganizationRequestModelRpmLimitType0):
            model_rpm_limit = self.model_rpm_limit.to_dict()
        else:
            model_rpm_limit = self.model_rpm_limit

        model_tpm_limit: dict[str, Any] | None | Unset
        if isinstance(self.model_tpm_limit, Unset):
            model_tpm_limit = UNSET
        elif isinstance(self.model_tpm_limit, NewOrganizationRequestModelTpmLimitType0):
            model_tpm_limit = self.model_tpm_limit.to_dict()
        else:
            model_tpm_limit = self.model_tpm_limit

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
            "organization_alias": organization_alias,
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
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if models is not UNSET:
            field_dict["models"] = models
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if model_rpm_limit is not UNSET:
            field_dict["model_rpm_limit"] = model_rpm_limit
        if model_tpm_limit is not UNSET:
            field_dict["model_tpm_limit"] = model_tpm_limit
        if object_permission is not UNSET:
            field_dict["object_permission"] = object_permission

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_object_permission_base import LiteLLMObjectPermissionBase
        from ..models.new_organization_request_metadata_type_0 import NewOrganizationRequestMetadataType0
        from ..models.new_organization_request_model_max_budget_type_0 import NewOrganizationRequestModelMaxBudgetType0
        from ..models.new_organization_request_model_rpm_limit_type_0 import NewOrganizationRequestModelRpmLimitType0
        from ..models.new_organization_request_model_tpm_limit_type_0 import NewOrganizationRequestModelTpmLimitType0
        d = dict(src_dict)
        organization_alias = d.pop("organization_alias")

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


        def _parse_model_max_budget(data: object) -> NewOrganizationRequestModelMaxBudgetType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_max_budget_type_0 = NewOrganizationRequestModelMaxBudgetType0.from_dict(data)



                return model_max_budget_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewOrganizationRequestModelMaxBudgetType0 | None | Unset, data)

        model_max_budget = _parse_model_max_budget(d.pop("model_max_budget", UNSET))


        def _parse_budget_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))


        def _parse_organization_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))


        models = cast(list[Any], d.pop("models", UNSET))


        def _parse_metadata(data: object) -> NewOrganizationRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = NewOrganizationRequestMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewOrganizationRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        def _parse_model_rpm_limit(data: object) -> NewOrganizationRequestModelRpmLimitType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_rpm_limit_type_0 = NewOrganizationRequestModelRpmLimitType0.from_dict(data)



                return model_rpm_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewOrganizationRequestModelRpmLimitType0 | None | Unset, data)

        model_rpm_limit = _parse_model_rpm_limit(d.pop("model_rpm_limit", UNSET))


        def _parse_model_tpm_limit(data: object) -> NewOrganizationRequestModelTpmLimitType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_tpm_limit_type_0 = NewOrganizationRequestModelTpmLimitType0.from_dict(data)



                return model_tpm_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewOrganizationRequestModelTpmLimitType0 | None | Unset, data)

        model_tpm_limit = _parse_model_tpm_limit(d.pop("model_tpm_limit", UNSET))


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


        new_organization_request = cls(
            organization_alias=organization_alias,
            budget_id=budget_id,
            soft_budget=soft_budget,
            max_budget=max_budget,
            max_parallel_requests=max_parallel_requests,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
            model_max_budget=model_max_budget,
            budget_duration=budget_duration,
            organization_id=organization_id,
            models=models,
            metadata=metadata,
            model_rpm_limit=model_rpm_limit,
            model_tpm_limit=model_tpm_limit,
            object_permission=object_permission,
        )


        new_organization_request.additional_properties = d
        return new_organization_request

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
