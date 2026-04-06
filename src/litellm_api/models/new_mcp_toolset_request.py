from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mcp_toolset_tool import MCPToolsetTool





T = TypeVar("T", bound="NewMCPToolsetRequest")



@_attrs_define
class NewMCPToolsetRequest:
    """ 
        Attributes:
            toolset_name (str):
            description (None | str | Unset):
            tools (list[MCPToolsetTool] | Unset):
     """

    toolset_name: str
    description: None | str | Unset = UNSET
    tools: list[MCPToolsetTool] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.mcp_toolset_tool import MCPToolsetTool
        toolset_name = self.toolset_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tools: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tools, Unset):
            tools = []
            for tools_item_data in self.tools:
                tools_item = tools_item_data.to_dict()
                tools.append(tools_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "toolset_name": toolset_name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if tools is not UNSET:
            field_dict["tools"] = tools

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_toolset_tool import MCPToolsetTool
        d = dict(src_dict)
        toolset_name = d.pop("toolset_name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        _tools = d.pop("tools", UNSET)
        tools: list[MCPToolsetTool] | Unset = UNSET
        if _tools is not UNSET:
            tools = []
            for tools_item_data in _tools:
                tools_item = MCPToolsetTool.from_dict(tools_item_data)



                tools.append(tools_item)


        new_mcp_toolset_request = cls(
            toolset_name=toolset_name,
            description=description,
            tools=tools,
        )


        new_mcp_toolset_request.additional_properties = d
        return new_mcp_toolset_request

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
