from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="UsageOverviewRow")



@_attrs_define
class UsageOverviewRow:
    """ 
        Attributes:
            avg_latency (float | None):
            avg_score (float | None):
            fail_rate (float):
            id (str):
            name (str):
            provider (str):
            requests_evaluated (int):
            status (str):
            trend (str):
            type_ (str):
     """

    avg_latency: float | None
    avg_score: float | None
    fail_rate: float
    id: str
    name: str
    provider: str
    requests_evaluated: int
    status: str
    trend: str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        avg_latency: float | None
        avg_latency = self.avg_latency

        avg_score: float | None
        avg_score = self.avg_score

        fail_rate = self.fail_rate

        id = self.id

        name = self.name

        provider = self.provider

        requests_evaluated = self.requests_evaluated

        status = self.status

        trend = self.trend

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "avgLatency": avg_latency,
            "avgScore": avg_score,
            "failRate": fail_rate,
            "id": id,
            "name": name,
            "provider": provider,
            "requestsEvaluated": requests_evaluated,
            "status": status,
            "trend": trend,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_avg_latency(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        avg_latency = _parse_avg_latency(d.pop("avgLatency"))


        def _parse_avg_score(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        avg_score = _parse_avg_score(d.pop("avgScore"))


        fail_rate = d.pop("failRate")

        id = d.pop("id")

        name = d.pop("name")

        provider = d.pop("provider")

        requests_evaluated = d.pop("requestsEvaluated")

        status = d.pop("status")

        trend = d.pop("trend")

        type_ = d.pop("type")

        usage_overview_row = cls(
            avg_latency=avg_latency,
            avg_score=avg_score,
            fail_rate=fail_rate,
            id=id,
            name=name,
            provider=provider,
            requests_evaluated=requests_evaluated,
            status=status,
            trend=trend,
            type_=type_,
        )


        usage_overview_row.additional_properties = d
        return usage_overview_row

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
