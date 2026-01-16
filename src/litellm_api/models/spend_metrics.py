from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SpendMetrics")



@_attrs_define
class SpendMetrics:
    """ 
        Attributes:
            spend (float | Unset):  Default: 0.0.
            prompt_tokens (int | Unset):  Default: 0.
            completion_tokens (int | Unset):  Default: 0.
            cache_read_input_tokens (int | Unset):  Default: 0.
            cache_creation_input_tokens (int | Unset):  Default: 0.
            total_tokens (int | Unset):  Default: 0.
            successful_requests (int | Unset):  Default: 0.
            failed_requests (int | Unset):  Default: 0.
            api_requests (int | Unset):  Default: 0.
     """

    spend: float | Unset = 0.0
    prompt_tokens: int | Unset = 0
    completion_tokens: int | Unset = 0
    cache_read_input_tokens: int | Unset = 0
    cache_creation_input_tokens: int | Unset = 0
    total_tokens: int | Unset = 0
    successful_requests: int | Unset = 0
    failed_requests: int | Unset = 0
    api_requests: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        spend = self.spend

        prompt_tokens = self.prompt_tokens

        completion_tokens = self.completion_tokens

        cache_read_input_tokens = self.cache_read_input_tokens

        cache_creation_input_tokens = self.cache_creation_input_tokens

        total_tokens = self.total_tokens

        successful_requests = self.successful_requests

        failed_requests = self.failed_requests

        api_requests = self.api_requests


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if spend is not UNSET:
            field_dict["spend"] = spend
        if prompt_tokens is not UNSET:
            field_dict["prompt_tokens"] = prompt_tokens
        if completion_tokens is not UNSET:
            field_dict["completion_tokens"] = completion_tokens
        if cache_read_input_tokens is not UNSET:
            field_dict["cache_read_input_tokens"] = cache_read_input_tokens
        if cache_creation_input_tokens is not UNSET:
            field_dict["cache_creation_input_tokens"] = cache_creation_input_tokens
        if total_tokens is not UNSET:
            field_dict["total_tokens"] = total_tokens
        if successful_requests is not UNSET:
            field_dict["successful_requests"] = successful_requests
        if failed_requests is not UNSET:
            field_dict["failed_requests"] = failed_requests
        if api_requests is not UNSET:
            field_dict["api_requests"] = api_requests

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        spend = d.pop("spend", UNSET)

        prompt_tokens = d.pop("prompt_tokens", UNSET)

        completion_tokens = d.pop("completion_tokens", UNSET)

        cache_read_input_tokens = d.pop("cache_read_input_tokens", UNSET)

        cache_creation_input_tokens = d.pop("cache_creation_input_tokens", UNSET)

        total_tokens = d.pop("total_tokens", UNSET)

        successful_requests = d.pop("successful_requests", UNSET)

        failed_requests = d.pop("failed_requests", UNSET)

        api_requests = d.pop("api_requests", UNSET)

        spend_metrics = cls(
            spend=spend,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            cache_read_input_tokens=cache_read_input_tokens,
            cache_creation_input_tokens=cache_creation_input_tokens,
            total_tokens=total_tokens,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
            api_requests=api_requests,
        )


        spend_metrics.additional_properties = d
        return spend_metrics

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
