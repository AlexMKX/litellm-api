from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ProviderBudgetResponseObject")



@_attrs_define
class ProviderBudgetResponseObject:
    """ Configuration for a single provider's budget settings

        Attributes:
            budget_limit (float | None):
            time_period (None | str):
            spend (float | None | Unset):  Default: 0.0.
            budget_reset_at (None | str | Unset):
     """

    budget_limit: float | None
    time_period: None | str
    spend: float | None | Unset = 0.0
    budget_reset_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        budget_limit: float | None
        budget_limit = self.budget_limit

        time_period: None | str
        time_period = self.time_period

        spend: float | None | Unset
        if isinstance(self.spend, Unset):
            spend = UNSET
        else:
            spend = self.spend

        budget_reset_at: None | str | Unset
        if isinstance(self.budget_reset_at, Unset):
            budget_reset_at = UNSET
        else:
            budget_reset_at = self.budget_reset_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "budget_limit": budget_limit,
            "time_period": time_period,
        })
        if spend is not UNSET:
            field_dict["spend"] = spend
        if budget_reset_at is not UNSET:
            field_dict["budget_reset_at"] = budget_reset_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_budget_limit(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        budget_limit = _parse_budget_limit(d.pop("budget_limit"))


        def _parse_time_period(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        time_period = _parse_time_period(d.pop("time_period"))


        def _parse_spend(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        spend = _parse_spend(d.pop("spend", UNSET))


        def _parse_budget_reset_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_reset_at = _parse_budget_reset_at(d.pop("budget_reset_at", UNSET))


        provider_budget_response_object = cls(
            budget_limit=budget_limit,
            time_period=time_period,
            spend=spend,
            budget_reset_at=budget_reset_at,
        )


        provider_budget_response_object.additional_properties = d
        return provider_budget_response_object

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
