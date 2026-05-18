from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.usage_overview_response_chart_item import UsageOverviewResponseChartItem
  from ..models.usage_overview_row import UsageOverviewRow





T = TypeVar("T", bound="UsageOverviewResponse")



@_attrs_define
class UsageOverviewResponse:
    """ 
        Attributes:
            chart (list[UsageOverviewResponseChartItem]):
            pass_rate (float):
            rows (list[UsageOverviewRow]):
            total_blocked (int):
            total_requests (int):
     """

    chart: list[UsageOverviewResponseChartItem]
    pass_rate: float
    rows: list[UsageOverviewRow]
    total_blocked: int
    total_requests: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.usage_overview_response_chart_item import UsageOverviewResponseChartItem
        from ..models.usage_overview_row import UsageOverviewRow
        chart = []
        for chart_item_data in self.chart:
            chart_item = chart_item_data.to_dict()
            chart.append(chart_item)



        pass_rate = self.pass_rate

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)



        total_blocked = self.total_blocked

        total_requests = self.total_requests


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "chart": chart,
            "passRate": pass_rate,
            "rows": rows,
            "totalBlocked": total_blocked,
            "totalRequests": total_requests,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_overview_response_chart_item import UsageOverviewResponseChartItem
        from ..models.usage_overview_row import UsageOverviewRow
        d = dict(src_dict)
        chart = []
        _chart = d.pop("chart")
        for chart_item_data in (_chart):
            chart_item = UsageOverviewResponseChartItem.from_dict(chart_item_data)



            chart.append(chart_item)


        pass_rate = d.pop("passRate")

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in (_rows):
            rows_item = UsageOverviewRow.from_dict(rows_item_data)



            rows.append(rows_item)


        total_blocked = d.pop("totalBlocked")

        total_requests = d.pop("totalRequests")

        usage_overview_response = cls(
            chart=chart,
            pass_rate=pass_rate,
            rows=rows,
            total_blocked=total_blocked,
            total_requests=total_requests,
        )


        usage_overview_response.additional_properties = d
        return usage_overview_response

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
