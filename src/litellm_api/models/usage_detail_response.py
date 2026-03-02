from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.usage_detail_response_time_series_item import UsageDetailResponseTimeSeriesItem





T = TypeVar("T", bound="UsageDetailResponse")



@_attrs_define
class UsageDetailResponse:
    """ 
        Attributes:
            guardrail_id (str):
            guardrail_name (str):
            type_ (str):
            provider (str):
            requests_evaluated (int):
            fail_rate (float):
            avg_score (float | None):
            avg_latency (float | None):
            status (str):
            trend (str):
            description (None | str):
            time_series (list[UsageDetailResponseTimeSeriesItem]):
     """

    guardrail_id: str
    guardrail_name: str
    type_: str
    provider: str
    requests_evaluated: int
    fail_rate: float
    avg_score: float | None
    avg_latency: float | None
    status: str
    trend: str
    description: None | str
    time_series: list[UsageDetailResponseTimeSeriesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.usage_detail_response_time_series_item import UsageDetailResponseTimeSeriesItem
        guardrail_id = self.guardrail_id

        guardrail_name = self.guardrail_name

        type_ = self.type_

        provider = self.provider

        requests_evaluated = self.requests_evaluated

        fail_rate = self.fail_rate

        avg_score: float | None
        avg_score = self.avg_score

        avg_latency: float | None
        avg_latency = self.avg_latency

        status = self.status

        trend = self.trend

        description: None | str
        description = self.description

        time_series = []
        for time_series_item_data in self.time_series:
            time_series_item = time_series_item_data.to_dict()
            time_series.append(time_series_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "guardrail_id": guardrail_id,
            "guardrail_name": guardrail_name,
            "type": type_,
            "provider": provider,
            "requestsEvaluated": requests_evaluated,
            "failRate": fail_rate,
            "avgScore": avg_score,
            "avgLatency": avg_latency,
            "status": status,
            "trend": trend,
            "description": description,
            "time_series": time_series,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_detail_response_time_series_item import UsageDetailResponseTimeSeriesItem
        d = dict(src_dict)
        guardrail_id = d.pop("guardrail_id")

        guardrail_name = d.pop("guardrail_name")

        type_ = d.pop("type")

        provider = d.pop("provider")

        requests_evaluated = d.pop("requestsEvaluated")

        fail_rate = d.pop("failRate")

        def _parse_avg_score(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        avg_score = _parse_avg_score(d.pop("avgScore"))


        def _parse_avg_latency(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        avg_latency = _parse_avg_latency(d.pop("avgLatency"))


        status = d.pop("status")

        trend = d.pop("trend")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        time_series = []
        _time_series = d.pop("time_series")
        for time_series_item_data in (_time_series):
            time_series_item = UsageDetailResponseTimeSeriesItem.from_dict(time_series_item_data)



            time_series.append(time_series_item)


        usage_detail_response = cls(
            guardrail_id=guardrail_id,
            guardrail_name=guardrail_name,
            type_=type_,
            provider=provider,
            requests_evaluated=requests_evaluated,
            fail_rate=fail_rate,
            avg_score=avg_score,
            avg_latency=avg_latency,
            status=status,
            trend=trend,
            description=description,
            time_series=time_series,
        )


        usage_detail_response.additional_properties = d
        return usage_detail_response

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
