from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SearchToolLiteLLMParams")



@_attrs_define
class SearchToolLiteLLMParams:
    """ LiteLLM params for search tools configuration.

        Attributes:
            search_provider (str):
            api_key (None | str | Unset):
            api_base (None | str | Unset):
            timeout (float | None | Unset):
            max_retries (int | None | Unset):
     """

    search_provider: str
    api_key: None | str | Unset = UNSET
    api_base: None | str | Unset = UNSET
    timeout: float | None | Unset = UNSET
    max_retries: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        search_provider = self.search_provider

        api_key: None | str | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

        api_base: None | str | Unset
        if isinstance(self.api_base, Unset):
            api_base = UNSET
        else:
            api_base = self.api_base

        timeout: float | None | Unset
        if isinstance(self.timeout, Unset):
            timeout = UNSET
        else:
            timeout = self.timeout

        max_retries: int | None | Unset
        if isinstance(self.max_retries, Unset):
            max_retries = UNSET
        else:
            max_retries = self.max_retries


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "search_provider": search_provider,
        })
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if api_base is not UNSET:
            field_dict["api_base"] = api_base
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if max_retries is not UNSET:
            field_dict["max_retries"] = max_retries

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        search_provider = d.pop("search_provider")

        def _parse_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))


        def _parse_api_base(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_base = _parse_api_base(d.pop("api_base", UNSET))


        def _parse_timeout(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        timeout = _parse_timeout(d.pop("timeout", UNSET))


        def _parse_max_retries(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_retries = _parse_max_retries(d.pop("max_retries", UNSET))


        search_tool_lite_llm_params = cls(
            search_provider=search_provider,
            api_key=api_key,
            api_base=api_base,
            timeout=timeout,
            max_retries=max_retries,
        )


        search_tool_lite_llm_params.additional_properties = d
        return search_tool_lite_llm_params

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
