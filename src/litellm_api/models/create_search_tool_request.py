from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.search_tool import SearchTool





T = TypeVar("T", bound="CreateSearchToolRequest")



@_attrs_define
class CreateSearchToolRequest:
    """ 
        Attributes:
            search_tool (SearchTool): Search tool configuration.

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
     """

    search_tool: SearchTool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_tool import SearchTool
        search_tool = self.search_tool.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "search_tool": search_tool,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_tool import SearchTool
        d = dict(src_dict)
        search_tool = SearchTool.from_dict(d.pop("search_tool"))




        create_search_tool_request = cls(
            search_tool=search_tool,
        )


        create_search_tool_request.additional_properties = d
        return create_search_tool_request

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
