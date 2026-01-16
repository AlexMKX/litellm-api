from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CostEstimateRequest")



@_attrs_define
class CostEstimateRequest:
    """ Request body for /cost/estimate endpoint.

        Attributes:
            model (str): Model name (from /model_group/info)
            input_tokens (int): Expected input tokens per request
            output_tokens (int): Expected output tokens per request
            num_requests_per_day (int | None | Unset): Number of requests per day
            num_requests_per_month (int | None | Unset): Number of requests per month
     """

    model: str
    input_tokens: int
    output_tokens: int
    num_requests_per_day: int | None | Unset = UNSET
    num_requests_per_month: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        model = self.model

        input_tokens = self.input_tokens

        output_tokens = self.output_tokens

        num_requests_per_day: int | None | Unset
        if isinstance(self.num_requests_per_day, Unset):
            num_requests_per_day = UNSET
        else:
            num_requests_per_day = self.num_requests_per_day

        num_requests_per_month: int | None | Unset
        if isinstance(self.num_requests_per_month, Unset):
            num_requests_per_month = UNSET
        else:
            num_requests_per_month = self.num_requests_per_month


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "model": model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
        })
        if num_requests_per_day is not UNSET:
            field_dict["num_requests_per_day"] = num_requests_per_day
        if num_requests_per_month is not UNSET:
            field_dict["num_requests_per_month"] = num_requests_per_month

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        input_tokens = d.pop("input_tokens")

        output_tokens = d.pop("output_tokens")

        def _parse_num_requests_per_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_requests_per_day = _parse_num_requests_per_day(d.pop("num_requests_per_day", UNSET))


        def _parse_num_requests_per_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_requests_per_month = _parse_num_requests_per_month(d.pop("num_requests_per_month", UNSET))


        cost_estimate_request = cls(
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            num_requests_per_day=num_requests_per_day,
            num_requests_per_month=num_requests_per_month,
        )


        cost_estimate_request.additional_properties = d
        return cost_estimate_request

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
