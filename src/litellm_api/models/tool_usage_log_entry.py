from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ToolUsageLogEntry")



@_attrs_define
class ToolUsageLogEntry:
    """ One spend log row for a tool call (for UI "recent logs" table).

        Attributes:
            id (str):
            timestamp (str):
            model (None | str | Unset):
            spend (float | None | Unset):
            total_tokens (int | None | Unset):
            input_snippet (None | str | Unset):
     """

    id: str
    timestamp: str
    model: None | str | Unset = UNSET
    spend: float | None | Unset = UNSET
    total_tokens: int | None | Unset = UNSET
    input_snippet: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        timestamp = self.timestamp

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        spend: float | None | Unset
        if isinstance(self.spend, Unset):
            spend = UNSET
        else:
            spend = self.spend

        total_tokens: int | None | Unset
        if isinstance(self.total_tokens, Unset):
            total_tokens = UNSET
        else:
            total_tokens = self.total_tokens

        input_snippet: None | str | Unset
        if isinstance(self.input_snippet, Unset):
            input_snippet = UNSET
        else:
            input_snippet = self.input_snippet


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "timestamp": timestamp,
        })
        if model is not UNSET:
            field_dict["model"] = model
        if spend is not UNSET:
            field_dict["spend"] = spend
        if total_tokens is not UNSET:
            field_dict["total_tokens"] = total_tokens
        if input_snippet is not UNSET:
            field_dict["input_snippet"] = input_snippet

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        timestamp = d.pop("timestamp")

        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        def _parse_spend(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        spend = _parse_spend(d.pop("spend", UNSET))


        def _parse_total_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_tokens = _parse_total_tokens(d.pop("total_tokens", UNSET))


        def _parse_input_snippet(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        input_snippet = _parse_input_snippet(d.pop("input_snippet", UNSET))


        tool_usage_log_entry = cls(
            id=id,
            timestamp=timestamp,
            model=model,
            spend=spend,
            total_tokens=total_tokens,
            input_snippet=input_snippet,
        )


        tool_usage_log_entry.additional_properties = d
        return tool_usage_log_entry

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
