from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.lite_llm_budget_table_model_max_budget_type_0 import LiteLLMBudgetTableModelMaxBudgetType0





T = TypeVar("T", bound="LiteLLMBudgetTable")



@_attrs_define
class LiteLLMBudgetTable:
    """ Represents user-controllable params for a LiteLLM_BudgetTable record

        Attributes:
            budget_id (None | str | Unset):
            soft_budget (float | None | Unset):
            max_budget (float | None | Unset):
            max_parallel_requests (int | None | Unset):
            tpm_limit (int | None | Unset):
            rpm_limit (int | None | Unset):
            model_max_budget (LiteLLMBudgetTableModelMaxBudgetType0 | None | Unset):
            budget_duration (None | str | Unset):
     """

    budget_id: None | str | Unset = UNSET
    soft_budget: float | None | Unset = UNSET
    max_budget: float | None | Unset = UNSET
    max_parallel_requests: int | None | Unset = UNSET
    tpm_limit: int | None | Unset = UNSET
    rpm_limit: int | None | Unset = UNSET
    model_max_budget: LiteLLMBudgetTableModelMaxBudgetType0 | None | Unset = UNSET
    budget_duration: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_budget_table_model_max_budget_type_0 import LiteLLMBudgetTableModelMaxBudgetType0
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
        elif isinstance(self.model_max_budget, LiteLLMBudgetTableModelMaxBudgetType0):
            model_max_budget = self.model_max_budget.to_dict()
        else:
            model_max_budget = self.model_max_budget

        budget_duration: None | str | Unset
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_budget_table_model_max_budget_type_0 import LiteLLMBudgetTableModelMaxBudgetType0
        d = dict(src_dict)
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


        def _parse_model_max_budget(data: object) -> LiteLLMBudgetTableModelMaxBudgetType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_max_budget_type_0 = LiteLLMBudgetTableModelMaxBudgetType0.from_dict(data)



                return model_max_budget_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMBudgetTableModelMaxBudgetType0 | None | Unset, data)

        model_max_budget = _parse_model_max_budget(d.pop("model_max_budget", UNSET))


        def _parse_budget_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))


        lite_llm_budget_table = cls(
            budget_id=budget_id,
            soft_budget=soft_budget,
            max_budget=max_budget,
            max_parallel_requests=max_parallel_requests,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
            model_max_budget=model_max_budget,
            budget_duration=budget_duration,
        )


        lite_llm_budget_table.additional_properties = d
        return lite_llm_budget_table

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
