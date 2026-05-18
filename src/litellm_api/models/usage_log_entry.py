from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="UsageLogEntry")



@_attrs_define
class UsageLogEntry:
    """ 
        Attributes:
            action (str):
            id (str):
            input_snippet (None | str):
            latency_ms (float | None):
            model (None | str):
            output_snippet (None | str):
            reason (None | str):
            score (float | None):
            timestamp (str):
     """

    action: str
    id: str
    input_snippet: None | str
    latency_ms: float | None
    model: None | str
    output_snippet: None | str
    reason: None | str
    score: float | None
    timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        action = self.action

        id = self.id

        input_snippet: None | str
        input_snippet = self.input_snippet

        latency_ms: float | None
        latency_ms = self.latency_ms

        model: None | str
        model = self.model

        output_snippet: None | str
        output_snippet = self.output_snippet

        reason: None | str
        reason = self.reason

        score: float | None
        score = self.score

        timestamp = self.timestamp


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action": action,
            "id": id,
            "input_snippet": input_snippet,
            "latency_ms": latency_ms,
            "model": model,
            "output_snippet": output_snippet,
            "reason": reason,
            "score": score,
            "timestamp": timestamp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        id = d.pop("id")

        def _parse_input_snippet(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        input_snippet = _parse_input_snippet(d.pop("input_snippet"))


        def _parse_latency_ms(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        latency_ms = _parse_latency_ms(d.pop("latency_ms"))


        def _parse_model(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        model = _parse_model(d.pop("model"))


        def _parse_output_snippet(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        output_snippet = _parse_output_snippet(d.pop("output_snippet"))


        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(d.pop("reason"))


        def _parse_score(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        score = _parse_score(d.pop("score"))


        timestamp = d.pop("timestamp")

        usage_log_entry = cls(
            action=action,
            id=id,
            input_snippet=input_snippet,
            latency_ms=latency_ms,
            model=model,
            output_snippet=output_snippet,
            reason=reason,
            score=score,
            timestamp=timestamp,
        )


        usage_log_entry.additional_properties = d
        return usage_log_entry

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
