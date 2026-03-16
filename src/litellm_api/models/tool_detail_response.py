from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.lite_llm_tool_table_row import LiteLLMToolTableRow
  from ..models.tool_policy_override_row import ToolPolicyOverrideRow





T = TypeVar("T", bound="ToolDetailResponse")



@_attrs_define
class ToolDetailResponse:
    """ 
        Attributes:
            tool (LiteLLMToolTableRow):
            overrides (list[ToolPolicyOverrideRow] | Unset):
     """

    tool: LiteLLMToolTableRow
    overrides: list[ToolPolicyOverrideRow] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_tool_table_row import LiteLLMToolTableRow
        from ..models.tool_policy_override_row import ToolPolicyOverrideRow
        tool = self.tool.to_dict()

        overrides: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = []
            for overrides_item_data in self.overrides:
                overrides_item = overrides_item_data.to_dict()
                overrides.append(overrides_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tool": tool,
        })
        if overrides is not UNSET:
            field_dict["overrides"] = overrides

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_tool_table_row import LiteLLMToolTableRow
        from ..models.tool_policy_override_row import ToolPolicyOverrideRow
        d = dict(src_dict)
        tool = LiteLLMToolTableRow.from_dict(d.pop("tool"))




        _overrides = d.pop("overrides", UNSET)
        overrides: list[ToolPolicyOverrideRow] | Unset = UNSET
        if _overrides is not UNSET:
            overrides = []
            for overrides_item_data in _overrides:
                overrides_item = ToolPolicyOverrideRow.from_dict(overrides_item_data)



                overrides.append(overrides_item)


        tool_detail_response = cls(
            tool=tool,
            overrides=overrides,
        )


        tool_detail_response.additional_properties = d
        return tool_detail_response

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
