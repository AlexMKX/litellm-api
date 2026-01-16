from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.new_customer_request_allowed_model_region_type_0 import NewCustomerRequestAllowedModelRegionType0
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.new_customer_request_model_max_budget_type_0 import NewCustomerRequestModelMaxBudgetType0





T = TypeVar("T", bound="NewCustomerRequest")



@_attrs_define
class NewCustomerRequest:
    """ Create a new customer, allocate a budget to them

        Attributes:
            user_id (str):
            budget_id (None | str | Unset):
            max_budget (float | None | Unset): Requests will fail if this budget (in USD) is exceeded.
            soft_budget (float | None | Unset): Requests will NOT fail if this is exceeded. Will fire alerting though.
            max_parallel_requests (int | None | Unset): Max concurrent requests allowed for this budget id.
            tpm_limit (int | None | Unset): Max tokens per minute, allowed for this budget id.
            rpm_limit (int | None | Unset): Max requests per minute, allowed for this budget id.
            budget_duration (None | str | Unset): Max duration budget should be set for (e.g. '1hr', '1d', '28d')
            model_max_budget (NewCustomerRequestModelMaxBudgetType0 | None | Unset): Max budget for each model (e.g.
                {'gpt-4o': {'max_budget': '0.0000001', 'budget_duration': '1d', 'tpm_limit': 1000, 'rpm_limit': 1000}})
            budget_reset_at (datetime.datetime | None | Unset): Datetime when the budget is reset
            alias (None | str | Unset):
            blocked (bool | Unset):  Default: False.
            spend (float | None | Unset):
            allowed_model_region (NewCustomerRequestAllowedModelRegionType0 | None | Unset):
            default_model (None | str | Unset):
     """

    user_id: str
    budget_id: None | str | Unset = UNSET
    max_budget: float | None | Unset = UNSET
    soft_budget: float | None | Unset = UNSET
    max_parallel_requests: int | None | Unset = UNSET
    tpm_limit: int | None | Unset = UNSET
    rpm_limit: int | None | Unset = UNSET
    budget_duration: None | str | Unset = UNSET
    model_max_budget: NewCustomerRequestModelMaxBudgetType0 | None | Unset = UNSET
    budget_reset_at: datetime.datetime | None | Unset = UNSET
    alias: None | str | Unset = UNSET
    blocked: bool | Unset = False
    spend: float | None | Unset = UNSET
    allowed_model_region: NewCustomerRequestAllowedModelRegionType0 | None | Unset = UNSET
    default_model: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.new_customer_request_model_max_budget_type_0 import NewCustomerRequestModelMaxBudgetType0
        user_id = self.user_id

        budget_id: None | str | Unset
        if isinstance(self.budget_id, Unset):
            budget_id = UNSET
        else:
            budget_id = self.budget_id

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

        budget_duration: None | str | Unset
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration

        model_max_budget: dict[str, Any] | None | Unset
        if isinstance(self.model_max_budget, Unset):
            model_max_budget = UNSET
        elif isinstance(self.model_max_budget, NewCustomerRequestModelMaxBudgetType0):
            model_max_budget = self.model_max_budget.to_dict()
        else:
            model_max_budget = self.model_max_budget

        budget_reset_at: None | str | Unset
        if isinstance(self.budget_reset_at, Unset):
            budget_reset_at = UNSET
        elif isinstance(self.budget_reset_at, datetime.datetime):
            budget_reset_at = self.budget_reset_at.isoformat()
        else:
            budget_reset_at = self.budget_reset_at

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        blocked = self.blocked

        spend: float | None | Unset
        if isinstance(self.spend, Unset):
            spend = UNSET
        else:
            spend = self.spend

        allowed_model_region: None | str | Unset
        if isinstance(self.allowed_model_region, Unset):
            allowed_model_region = UNSET
        elif isinstance(self.allowed_model_region, NewCustomerRequestAllowedModelRegionType0):
            allowed_model_region = self.allowed_model_region.value
        else:
            allowed_model_region = self.allowed_model_region

        default_model: None | str | Unset
        if isinstance(self.default_model, Unset):
            default_model = UNSET
        else:
            default_model = self.default_model


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "user_id": user_id,
        })
        if budget_id is not UNSET:
            field_dict["budget_id"] = budget_id
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if soft_budget is not UNSET:
            field_dict["soft_budget"] = soft_budget
        if max_parallel_requests is not UNSET:
            field_dict["max_parallel_requests"] = max_parallel_requests
        if tpm_limit is not UNSET:
            field_dict["tpm_limit"] = tpm_limit
        if rpm_limit is not UNSET:
            field_dict["rpm_limit"] = rpm_limit
        if budget_duration is not UNSET:
            field_dict["budget_duration"] = budget_duration
        if model_max_budget is not UNSET:
            field_dict["model_max_budget"] = model_max_budget
        if budget_reset_at is not UNSET:
            field_dict["budget_reset_at"] = budget_reset_at
        if alias is not UNSET:
            field_dict["alias"] = alias
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if spend is not UNSET:
            field_dict["spend"] = spend
        if allowed_model_region is not UNSET:
            field_dict["allowed_model_region"] = allowed_model_region
        if default_model is not UNSET:
            field_dict["default_model"] = default_model

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_customer_request_model_max_budget_type_0 import NewCustomerRequestModelMaxBudgetType0
        d = dict(src_dict)
        user_id = d.pop("user_id")

        def _parse_budget_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_id = _parse_budget_id(d.pop("budget_id", UNSET))


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


        def _parse_budget_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))


        def _parse_model_max_budget(data: object) -> NewCustomerRequestModelMaxBudgetType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_max_budget_type_0 = NewCustomerRequestModelMaxBudgetType0.from_dict(data)



                return model_max_budget_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewCustomerRequestModelMaxBudgetType0 | None | Unset, data)

        model_max_budget = _parse_model_max_budget(d.pop("model_max_budget", UNSET))


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


        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))


        blocked = d.pop("blocked", UNSET)

        def _parse_spend(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        spend = _parse_spend(d.pop("spend", UNSET))


        def _parse_allowed_model_region(data: object) -> NewCustomerRequestAllowedModelRegionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                allowed_model_region_type_0 = NewCustomerRequestAllowedModelRegionType0(data)



                return allowed_model_region_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewCustomerRequestAllowedModelRegionType0 | None | Unset, data)

        allowed_model_region = _parse_allowed_model_region(d.pop("allowed_model_region", UNSET))


        def _parse_default_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_model = _parse_default_model(d.pop("default_model", UNSET))


        new_customer_request = cls(
            user_id=user_id,
            budget_id=budget_id,
            max_budget=max_budget,
            soft_budget=soft_budget,
            max_parallel_requests=max_parallel_requests,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
            budget_duration=budget_duration,
            model_max_budget=model_max_budget,
            budget_reset_at=budget_reset_at,
            alias=alias,
            blocked=blocked,
            spend=spend,
            allowed_model_region=allowed_model_region,
            default_model=default_model,
        )


        new_customer_request.additional_properties = d
        return new_customer_request

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
