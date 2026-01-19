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
  from ..models.breakdown_metrics import BreakdownMetrics
  from ..models.spend_metrics import SpendMetrics





T = TypeVar("T", bound="DailySpendData")



@_attrs_define
class DailySpendData:
    """ 
        Attributes:
            date (datetime.date):
            metrics (SpendMetrics):
            breakdown (BreakdownMetrics | Unset): Breakdown of spend by different dimensions
     """

    date: datetime.date
    metrics: SpendMetrics
    breakdown: BreakdownMetrics | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.spend_metrics import SpendMetrics
        from ..models.breakdown_metrics import BreakdownMetrics
        date = self.date.isoformat()

        metrics = self.metrics.to_dict()

        breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.breakdown, Unset):
            breakdown = self.breakdown.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "date": date,
            "metrics": metrics,
        })
        if breakdown is not UNSET:
            field_dict["breakdown"] = breakdown

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.breakdown_metrics import BreakdownMetrics
        from ..models.spend_metrics import SpendMetrics
        d = dict(src_dict)
        date = isoparse(d.pop("date")).date()




        metrics = SpendMetrics.from_dict(d.pop("metrics"))




        _breakdown = d.pop("breakdown", UNSET)
        breakdown: BreakdownMetrics | Unset
        if isinstance(_breakdown,  Unset):
            breakdown = UNSET
        else:
            breakdown = BreakdownMetrics.from_dict(_breakdown)




        daily_spend_data = cls(
            date=date,
            metrics=metrics,
            breakdown=breakdown,
        )


        daily_spend_data.additional_properties = d
        return daily_spend_data

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
