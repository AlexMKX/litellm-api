from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_tool_lite_llm_params import SearchToolLiteLLMParams
  from ..models.search_tool_search_tool_info_type_0 import SearchToolSearchToolInfoType0





T = TypeVar("T", bound="SearchTool")



@_attrs_define
class SearchTool:
    """ Search tool configuration.

    Example:
        {
            "search_tool_id": "123e4567-e89b-12d3-a456-426614174000",
            "search_tool_name": "litellm-search",
            "litellm_params": {
                "search_provider": "perplexity",
                "api_key": "sk-..."
            },
            "search_tool_info": {
                "description": "Perplexity search tool"
            }
        }

        Attributes:
            search_tool_name (str):
            litellm_params (SearchToolLiteLLMParams): LiteLLM params for search tools configuration.
            search_tool_id (None | str | Unset):
            search_tool_info (None | SearchToolSearchToolInfoType0 | Unset):
            created_at (None | str | Unset):
            updated_at (None | str | Unset):
     """

    search_tool_name: str
    litellm_params: SearchToolLiteLLMParams
    search_tool_id: None | str | Unset = UNSET
    search_tool_info: None | SearchToolSearchToolInfoType0 | Unset = UNSET
    created_at: None | str | Unset = UNSET
    updated_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_tool_search_tool_info_type_0 import SearchToolSearchToolInfoType0
        from ..models.search_tool_lite_llm_params import SearchToolLiteLLMParams
        search_tool_name = self.search_tool_name

        litellm_params = self.litellm_params.to_dict()

        search_tool_id: None | str | Unset
        if isinstance(self.search_tool_id, Unset):
            search_tool_id = UNSET
        else:
            search_tool_id = self.search_tool_id

        search_tool_info: dict[str, Any] | None | Unset
        if isinstance(self.search_tool_info, Unset):
            search_tool_info = UNSET
        elif isinstance(self.search_tool_info, SearchToolSearchToolInfoType0):
            search_tool_info = self.search_tool_info.to_dict()
        else:
            search_tool_info = self.search_tool_info

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "search_tool_name": search_tool_name,
            "litellm_params": litellm_params,
        })
        if search_tool_id is not UNSET:
            field_dict["search_tool_id"] = search_tool_id
        if search_tool_info is not UNSET:
            field_dict["search_tool_info"] = search_tool_info
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_tool_lite_llm_params import SearchToolLiteLLMParams
        from ..models.search_tool_search_tool_info_type_0 import SearchToolSearchToolInfoType0
        d = dict(src_dict)
        search_tool_name = d.pop("search_tool_name")

        litellm_params = SearchToolLiteLLMParams.from_dict(d.pop("litellm_params"))




        def _parse_search_tool_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search_tool_id = _parse_search_tool_id(d.pop("search_tool_id", UNSET))


        def _parse_search_tool_info(data: object) -> None | SearchToolSearchToolInfoType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                search_tool_info_type_0 = SearchToolSearchToolInfoType0.from_dict(data)



                return search_tool_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchToolSearchToolInfoType0 | Unset, data)

        search_tool_info = _parse_search_tool_info(d.pop("search_tool_info", UNSET))


        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))


        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        search_tool = cls(
            search_tool_name=search_tool_name,
            litellm_params=litellm_params,
            search_tool_id=search_tool_id,
            search_tool_info=search_tool_info,
            created_at=created_at,
            updated_at=updated_at,
        )


        search_tool.additional_properties = d
        return search_tool

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
