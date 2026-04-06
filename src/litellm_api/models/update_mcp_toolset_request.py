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





T = TypeVar("T", bound="UpdateMCPToolsetRequest")



@_attrs_define
class UpdateMCPToolsetRequest:
    """ 
        Attributes:
            toolset_id (str):
            toolset_name (None | str | Unset):
            description (None | str | Unset):
            tools (list[MCPToolsetTool] | None | Unset):
     """

    toolset_id: str
    toolset_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    tools: list[MCPToolsetTool] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.mcp_toolset_tool import MCPToolsetTool
        toolset_id = self.toolset_id

        toolset_name: None | str | Unset
        if isinstance(self.toolset_name, Unset):
            toolset_name = UNSET
        else:
            toolset_name = self.toolset_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tools: list[dict[str, Any]] | None | Unset
        if isinstance(self.tools, Unset):
            tools = UNSET
        elif isinstance(self.tools, list):
            tools = []
            for tools_type_0_item_data in self.tools:
                tools_type_0_item = tools_type_0_item_data.to_dict()
                tools.append(tools_type_0_item)


        else:
            tools = self.tools


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "toolset_id": toolset_id,
        })
        if toolset_name is not UNSET:
            field_dict["toolset_name"] = toolset_name
        if description is not UNSET:
            field_dict["description"] = description
        if tools is not UNSET:
            field_dict["tools"] = tools

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_toolset_tool import MCPToolsetTool
        d = dict(src_dict)
        toolset_id = d.pop("toolset_id")

        def _parse_toolset_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        toolset_name = _parse_toolset_name(d.pop("toolset_name", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_tools(data: object) -> list[MCPToolsetTool] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tools_type_0 = []
                _tools_type_0 = data
                for tools_type_0_item_data in (_tools_type_0):
                    tools_type_0_item = MCPToolsetTool.from_dict(tools_type_0_item_data)



                    tools_type_0.append(tools_type_0_item)

                return tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MCPToolsetTool] | None | Unset, data)

        tools = _parse_tools(d.pop("tools", UNSET))


        update_mcp_toolset_request = cls(
            toolset_id=toolset_id,
            toolset_name=toolset_name,
            description=description,
            tools=tools,
        )


        update_mcp_toolset_request.additional_properties = d
        return update_mcp_toolset_request

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
