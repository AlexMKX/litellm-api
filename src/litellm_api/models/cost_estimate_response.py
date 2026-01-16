from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CostEstimateResponse")



@_attrs_define
class CostEstimateResponse:
    """ Response body for /cost/estimate endpoint.

        Attributes:
            model (str):
            input_tokens (int):
            output_tokens (int):
            cost_per_request (float): Total cost per request (includes margin)
            input_cost_per_request (float): Input token cost per request (before margin)
            output_cost_per_request (float): Output token cost per request (before margin)
            num_requests_per_day (int | None | Unset):
            num_requests_per_month (int | None | Unset):
            margin_cost_per_request (float | Unset): Margin/fee added per request Default: 0.0.
            daily_cost (float | None | Unset): Total daily cost (includes margin)
            daily_input_cost (float | None | Unset): Daily input token cost
            daily_output_cost (float | None | Unset): Daily output token cost
            daily_margin_cost (float | None | Unset): Daily margin/fee
            monthly_cost (float | None | Unset): Total monthly cost (includes margin)
            monthly_input_cost (float | None | Unset): Monthly input token cost
            monthly_output_cost (float | None | Unset): Monthly output token cost
            monthly_margin_cost (float | None | Unset): Monthly margin/fee
            input_cost_per_token (float | None | Unset):
            output_cost_per_token (float | None | Unset):
            provider (None | str | Unset):
     """

    model: str
    input_tokens: int
    output_tokens: int
    cost_per_request: float
    input_cost_per_request: float
    output_cost_per_request: float
    num_requests_per_day: int | None | Unset = UNSET
    num_requests_per_month: int | None | Unset = UNSET
    margin_cost_per_request: float | Unset = 0.0
    daily_cost: float | None | Unset = UNSET
    daily_input_cost: float | None | Unset = UNSET
    daily_output_cost: float | None | Unset = UNSET
    daily_margin_cost: float | None | Unset = UNSET
    monthly_cost: float | None | Unset = UNSET
    monthly_input_cost: float | None | Unset = UNSET
    monthly_output_cost: float | None | Unset = UNSET
    monthly_margin_cost: float | None | Unset = UNSET
    input_cost_per_token: float | None | Unset = UNSET
    output_cost_per_token: float | None | Unset = UNSET
    provider: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        model = self.model

        input_tokens = self.input_tokens

        output_tokens = self.output_tokens

        cost_per_request = self.cost_per_request

        input_cost_per_request = self.input_cost_per_request

        output_cost_per_request = self.output_cost_per_request

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

        margin_cost_per_request = self.margin_cost_per_request

        daily_cost: float | None | Unset
        if isinstance(self.daily_cost, Unset):
            daily_cost = UNSET
        else:
            daily_cost = self.daily_cost

        daily_input_cost: float | None | Unset
        if isinstance(self.daily_input_cost, Unset):
            daily_input_cost = UNSET
        else:
            daily_input_cost = self.daily_input_cost

        daily_output_cost: float | None | Unset
        if isinstance(self.daily_output_cost, Unset):
            daily_output_cost = UNSET
        else:
            daily_output_cost = self.daily_output_cost

        daily_margin_cost: float | None | Unset
        if isinstance(self.daily_margin_cost, Unset):
            daily_margin_cost = UNSET
        else:
            daily_margin_cost = self.daily_margin_cost

        monthly_cost: float | None | Unset
        if isinstance(self.monthly_cost, Unset):
            monthly_cost = UNSET
        else:
            monthly_cost = self.monthly_cost

        monthly_input_cost: float | None | Unset
        if isinstance(self.monthly_input_cost, Unset):
            monthly_input_cost = UNSET
        else:
            monthly_input_cost = self.monthly_input_cost

        monthly_output_cost: float | None | Unset
        if isinstance(self.monthly_output_cost, Unset):
            monthly_output_cost = UNSET
        else:
            monthly_output_cost = self.monthly_output_cost

        monthly_margin_cost: float | None | Unset
        if isinstance(self.monthly_margin_cost, Unset):
            monthly_margin_cost = UNSET
        else:
            monthly_margin_cost = self.monthly_margin_cost

        input_cost_per_token: float | None | Unset
        if isinstance(self.input_cost_per_token, Unset):
            input_cost_per_token = UNSET
        else:
            input_cost_per_token = self.input_cost_per_token

        output_cost_per_token: float | None | Unset
        if isinstance(self.output_cost_per_token, Unset):
            output_cost_per_token = UNSET
        else:
            output_cost_per_token = self.output_cost_per_token

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "model": model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost_per_request": cost_per_request,
            "input_cost_per_request": input_cost_per_request,
            "output_cost_per_request": output_cost_per_request,
        })
        if num_requests_per_day is not UNSET:
            field_dict["num_requests_per_day"] = num_requests_per_day
        if num_requests_per_month is not UNSET:
            field_dict["num_requests_per_month"] = num_requests_per_month
        if margin_cost_per_request is not UNSET:
            field_dict["margin_cost_per_request"] = margin_cost_per_request
        if daily_cost is not UNSET:
            field_dict["daily_cost"] = daily_cost
        if daily_input_cost is not UNSET:
            field_dict["daily_input_cost"] = daily_input_cost
        if daily_output_cost is not UNSET:
            field_dict["daily_output_cost"] = daily_output_cost
        if daily_margin_cost is not UNSET:
            field_dict["daily_margin_cost"] = daily_margin_cost
        if monthly_cost is not UNSET:
            field_dict["monthly_cost"] = monthly_cost
        if monthly_input_cost is not UNSET:
            field_dict["monthly_input_cost"] = monthly_input_cost
        if monthly_output_cost is not UNSET:
            field_dict["monthly_output_cost"] = monthly_output_cost
        if monthly_margin_cost is not UNSET:
            field_dict["monthly_margin_cost"] = monthly_margin_cost
        if input_cost_per_token is not UNSET:
            field_dict["input_cost_per_token"] = input_cost_per_token
        if output_cost_per_token is not UNSET:
            field_dict["output_cost_per_token"] = output_cost_per_token
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        input_tokens = d.pop("input_tokens")

        output_tokens = d.pop("output_tokens")

        cost_per_request = d.pop("cost_per_request")

        input_cost_per_request = d.pop("input_cost_per_request")

        output_cost_per_request = d.pop("output_cost_per_request")

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


        margin_cost_per_request = d.pop("margin_cost_per_request", UNSET)

        def _parse_daily_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        daily_cost = _parse_daily_cost(d.pop("daily_cost", UNSET))


        def _parse_daily_input_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        daily_input_cost = _parse_daily_input_cost(d.pop("daily_input_cost", UNSET))


        def _parse_daily_output_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        daily_output_cost = _parse_daily_output_cost(d.pop("daily_output_cost", UNSET))


        def _parse_daily_margin_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        daily_margin_cost = _parse_daily_margin_cost(d.pop("daily_margin_cost", UNSET))


        def _parse_monthly_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        monthly_cost = _parse_monthly_cost(d.pop("monthly_cost", UNSET))


        def _parse_monthly_input_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        monthly_input_cost = _parse_monthly_input_cost(d.pop("monthly_input_cost", UNSET))


        def _parse_monthly_output_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        monthly_output_cost = _parse_monthly_output_cost(d.pop("monthly_output_cost", UNSET))


        def _parse_monthly_margin_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        monthly_margin_cost = _parse_monthly_margin_cost(d.pop("monthly_margin_cost", UNSET))


        def _parse_input_cost_per_token(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_token = _parse_input_cost_per_token(d.pop("input_cost_per_token", UNSET))


        def _parse_output_cost_per_token(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_token = _parse_output_cost_per_token(d.pop("output_cost_per_token", UNSET))


        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))


        cost_estimate_response = cls(
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cost_per_request=cost_per_request,
            input_cost_per_request=input_cost_per_request,
            output_cost_per_request=output_cost_per_request,
            num_requests_per_day=num_requests_per_day,
            num_requests_per_month=num_requests_per_month,
            margin_cost_per_request=margin_cost_per_request,
            daily_cost=daily_cost,
            daily_input_cost=daily_input_cost,
            daily_output_cost=daily_output_cost,
            daily_margin_cost=daily_margin_cost,
            monthly_cost=monthly_cost,
            monthly_input_cost=monthly_input_cost,
            monthly_output_cost=monthly_output_cost,
            monthly_margin_cost=monthly_margin_cost,
            input_cost_per_token=input_cost_per_token,
            output_cost_per_token=output_cost_per_token,
            provider=provider,
        )


        cost_estimate_response.additional_properties = d
        return cost_estimate_response

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
