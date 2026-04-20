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






T = TypeVar("T", bound="BudgetLimitEntry")



@_attrs_define
class BudgetLimitEntry:
    """ A single budget window with its own limit and independent reset schedule.

        Attributes:
            budget_duration (str):
            max_budget (float):
            reset_at (datetime.datetime | None | Unset):
     """

    budget_duration: str
    max_budget: float
    reset_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        budget_duration = self.budget_duration

        max_budget = self.max_budget

        reset_at: None | str | Unset
        if isinstance(self.reset_at, Unset):
            reset_at = UNSET
        elif isinstance(self.reset_at, datetime.datetime):
            reset_at = self.reset_at.isoformat()
        else:
            reset_at = self.reset_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "budget_duration": budget_duration,
            "max_budget": max_budget,
        })
        if reset_at is not UNSET:
            field_dict["reset_at"] = reset_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        budget_duration = d.pop("budget_duration")

        max_budget = d.pop("max_budget")

        def _parse_reset_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reset_at_type_0 = isoparse(data)



                return reset_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reset_at = _parse_reset_at(d.pop("reset_at", UNSET))


        budget_limit_entry = cls(
            budget_duration=budget_duration,
            max_budget=max_budget,
            reset_at=reset_at,
        )


        budget_limit_entry.additional_properties = d
        return budget_limit_entry

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
