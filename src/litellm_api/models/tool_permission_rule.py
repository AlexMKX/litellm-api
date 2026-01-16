from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tool_permission_rule_decision import ToolPermissionRuleDecision
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tool_permission_rule_allowed_param_patterns_type_0 import ToolPermissionRuleAllowedParamPatternsType0





T = TypeVar("T", bound="ToolPermissionRule")



@_attrs_define
class ToolPermissionRule:
    """ A rule defining permission for a specific tool or tool pattern

        Attributes:
            id (str): Unique identifier for the rule
            decision (ToolPermissionRuleDecision): Whether to allow or deny this tool usage
            tool_name (None | str | Unset): Regex pattern applied to the tool's function name
            tool_type (None | str | Unset): Regex pattern applied to the tool type (e.g., function)
            allowed_param_patterns (None | ToolPermissionRuleAllowedParamPatternsType0 | Unset): Optional regex map
                enforcing nested parameter values using dot/[] paths
     """

    id: str
    decision: ToolPermissionRuleDecision
    tool_name: None | str | Unset = UNSET
    tool_type: None | str | Unset = UNSET
    allowed_param_patterns: None | ToolPermissionRuleAllowedParamPatternsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tool_permission_rule_allowed_param_patterns_type_0 import ToolPermissionRuleAllowedParamPatternsType0
        id = self.id

        decision = self.decision.value

        tool_name: None | str | Unset
        if isinstance(self.tool_name, Unset):
            tool_name = UNSET
        else:
            tool_name = self.tool_name

        tool_type: None | str | Unset
        if isinstance(self.tool_type, Unset):
            tool_type = UNSET
        else:
            tool_type = self.tool_type

        allowed_param_patterns: dict[str, Any] | None | Unset
        if isinstance(self.allowed_param_patterns, Unset):
            allowed_param_patterns = UNSET
        elif isinstance(self.allowed_param_patterns, ToolPermissionRuleAllowedParamPatternsType0):
            allowed_param_patterns = self.allowed_param_patterns.to_dict()
        else:
            allowed_param_patterns = self.allowed_param_patterns


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "decision": decision,
        })
        if tool_name is not UNSET:
            field_dict["tool_name"] = tool_name
        if tool_type is not UNSET:
            field_dict["tool_type"] = tool_type
        if allowed_param_patterns is not UNSET:
            field_dict["allowed_param_patterns"] = allowed_param_patterns

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_permission_rule_allowed_param_patterns_type_0 import ToolPermissionRuleAllowedParamPatternsType0
        d = dict(src_dict)
        id = d.pop("id")

        decision = ToolPermissionRuleDecision(d.pop("decision"))




        def _parse_tool_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_name = _parse_tool_name(d.pop("tool_name", UNSET))


        def _parse_tool_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_type = _parse_tool_type(d.pop("tool_type", UNSET))


        def _parse_allowed_param_patterns(data: object) -> None | ToolPermissionRuleAllowedParamPatternsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                allowed_param_patterns_type_0 = ToolPermissionRuleAllowedParamPatternsType0.from_dict(data)



                return allowed_param_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ToolPermissionRuleAllowedParamPatternsType0 | Unset, data)

        allowed_param_patterns = _parse_allowed_param_patterns(d.pop("allowed_param_patterns", UNSET))


        tool_permission_rule = cls(
            id=id,
            decision=decision,
            tool_name=tool_name,
            tool_type=tool_type,
            allowed_param_patterns=allowed_param_patterns,
        )


        tool_permission_rule.additional_properties = d
        return tool_permission_rule

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
