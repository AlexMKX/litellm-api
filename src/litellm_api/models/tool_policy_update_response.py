from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tool_policy_update_response_call_policy import ToolPolicyUpdateResponseCallPolicy






T = TypeVar("T", bound="ToolPolicyUpdateResponse")



@_attrs_define
class ToolPolicyUpdateResponse:
    """ 
        Attributes:
            tool_name (str):
            call_policy (ToolPolicyUpdateResponseCallPolicy):
            updated (bool):
     """

    tool_name: str
    call_policy: ToolPolicyUpdateResponseCallPolicy
    updated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tool_name = self.tool_name

        call_policy = self.call_policy.value

        updated = self.updated


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tool_name": tool_name,
            "call_policy": call_policy,
            "updated": updated,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tool_name = d.pop("tool_name")

        call_policy = ToolPolicyUpdateResponseCallPolicy(d.pop("call_policy"))




        updated = d.pop("updated")

        tool_policy_update_response = cls(
            tool_name=tool_name,
            call_policy=call_policy,
            updated=updated,
        )


        tool_policy_update_response.additional_properties = d
        return tool_policy_update_response

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
