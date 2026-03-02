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
            id (str):
            name (str):
            type_ (str):
            provider (str):
            requests_evaluated (int):
            fail_rate (float):
            avg_score (float | None):
            avg_latency (float | None):
            status (str):
            trend (str):
     """

    id: str
    name: str
    type_: str
    provider: str
    requests_evaluated: int
    fail_rate: float
    avg_score: float | None
    avg_latency: float | None
    status: str
    trend: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "type": type_,
            "provider": provider,
            "requestsEvaluated": requests_evaluated,
            "failRate": fail_rate,
            "avgScore": avg_score,
            "avgLatency": avg_latency,
            "status": status,
            "trend": trend,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

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

        usage_overview_row = cls(
            id=id,
            name=name,
            type_=type_,
            provider=provider,
            requests_evaluated=requests_evaluated,
            fail_rate=fail_rate,
            avg_score=avg_score,
            avg_latency=avg_latency,
            status=status,
            trend=trend,
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
