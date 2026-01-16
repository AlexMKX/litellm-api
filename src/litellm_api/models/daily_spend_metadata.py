from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DailySpendMetadata")



@_attrs_define
class DailySpendMetadata:
    """ 
        Attributes:
            total_spend (float | Unset):  Default: 0.0.
            total_prompt_tokens (int | Unset):  Default: 0.
            total_completion_tokens (int | Unset):  Default: 0.
            total_tokens (int | Unset):  Default: 0.
            total_api_requests (int | Unset):  Default: 0.
            total_successful_requests (int | Unset):  Default: 0.
            total_failed_requests (int | Unset):  Default: 0.
            total_cache_read_input_tokens (int | Unset):  Default: 0.
            total_cache_creation_input_tokens (int | Unset):  Default: 0.
            page (int | Unset):  Default: 1.
            total_pages (int | Unset):  Default: 1.
            has_more (bool | Unset):  Default: False.
     """

    total_spend: float | Unset = 0.0
    total_prompt_tokens: int | Unset = 0
    total_completion_tokens: int | Unset = 0
    total_tokens: int | Unset = 0
    total_api_requests: int | Unset = 0
    total_successful_requests: int | Unset = 0
    total_failed_requests: int | Unset = 0
    total_cache_read_input_tokens: int | Unset = 0
    total_cache_creation_input_tokens: int | Unset = 0
    page: int | Unset = 1
    total_pages: int | Unset = 1
    has_more: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        total_spend = self.total_spend

        total_prompt_tokens = self.total_prompt_tokens

        total_completion_tokens = self.total_completion_tokens

        total_tokens = self.total_tokens

        total_api_requests = self.total_api_requests

        total_successful_requests = self.total_successful_requests

        total_failed_requests = self.total_failed_requests

        total_cache_read_input_tokens = self.total_cache_read_input_tokens

        total_cache_creation_input_tokens = self.total_cache_creation_input_tokens

        page = self.page

        total_pages = self.total_pages

        has_more = self.has_more


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if total_spend is not UNSET:
            field_dict["total_spend"] = total_spend
        if total_prompt_tokens is not UNSET:
            field_dict["total_prompt_tokens"] = total_prompt_tokens
        if total_completion_tokens is not UNSET:
            field_dict["total_completion_tokens"] = total_completion_tokens
        if total_tokens is not UNSET:
            field_dict["total_tokens"] = total_tokens
        if total_api_requests is not UNSET:
            field_dict["total_api_requests"] = total_api_requests
        if total_successful_requests is not UNSET:
            field_dict["total_successful_requests"] = total_successful_requests
        if total_failed_requests is not UNSET:
            field_dict["total_failed_requests"] = total_failed_requests
        if total_cache_read_input_tokens is not UNSET:
            field_dict["total_cache_read_input_tokens"] = total_cache_read_input_tokens
        if total_cache_creation_input_tokens is not UNSET:
            field_dict["total_cache_creation_input_tokens"] = total_cache_creation_input_tokens
        if page is not UNSET:
            field_dict["page"] = page
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages
        if has_more is not UNSET:
            field_dict["has_more"] = has_more

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_spend = d.pop("total_spend", UNSET)

        total_prompt_tokens = d.pop("total_prompt_tokens", UNSET)

        total_completion_tokens = d.pop("total_completion_tokens", UNSET)

        total_tokens = d.pop("total_tokens", UNSET)

        total_api_requests = d.pop("total_api_requests", UNSET)

        total_successful_requests = d.pop("total_successful_requests", UNSET)

        total_failed_requests = d.pop("total_failed_requests", UNSET)

        total_cache_read_input_tokens = d.pop("total_cache_read_input_tokens", UNSET)

        total_cache_creation_input_tokens = d.pop("total_cache_creation_input_tokens", UNSET)

        page = d.pop("page", UNSET)

        total_pages = d.pop("total_pages", UNSET)

        has_more = d.pop("has_more", UNSET)

        daily_spend_metadata = cls(
            total_spend=total_spend,
            total_prompt_tokens=total_prompt_tokens,
            total_completion_tokens=total_completion_tokens,
            total_tokens=total_tokens,
            total_api_requests=total_api_requests,
            total_successful_requests=total_successful_requests,
            total_failed_requests=total_failed_requests,
            total_cache_read_input_tokens=total_cache_read_input_tokens,
            total_cache_creation_input_tokens=total_cache_creation_input_tokens,
            page=page,
            total_pages=total_pages,
            has_more=has_more,
        )


        daily_spend_metadata.additional_properties = d
        return daily_spend_metadata

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
