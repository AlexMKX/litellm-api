from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.tool_policy_option import ToolPolicyOption





T = TypeVar("T", bound="ToolPolicyOptionsResponse")



@_attrs_define
class ToolPolicyOptionsResponse:
    """ 
        Attributes:
            input_policies (list[ToolPolicyOption]):
            output_policies (list[ToolPolicyOption]):
     """

    input_policies: list[ToolPolicyOption]
    output_policies: list[ToolPolicyOption]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tool_policy_option import ToolPolicyOption
        input_policies = []
        for input_policies_item_data in self.input_policies:
            input_policies_item = input_policies_item_data.to_dict()
            input_policies.append(input_policies_item)



        output_policies = []
        for output_policies_item_data in self.output_policies:
            output_policies_item = output_policies_item_data.to_dict()
            output_policies.append(output_policies_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "input_policies": input_policies,
            "output_policies": output_policies,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_policy_option import ToolPolicyOption
        d = dict(src_dict)
        input_policies = []
        _input_policies = d.pop("input_policies")
        for input_policies_item_data in (_input_policies):
            input_policies_item = ToolPolicyOption.from_dict(input_policies_item_data)



            input_policies.append(input_policies_item)


        output_policies = []
        _output_policies = d.pop("output_policies")
        for output_policies_item_data in (_output_policies):
            output_policies_item = ToolPolicyOption.from_dict(output_policies_item_data)



            output_policies.append(output_policies_item)


        tool_policy_options_response = cls(
            input_policies=input_policies,
            output_policies=output_policies,
        )


        tool_policy_options_response.additional_properties = d
        return tool_policy_options_response

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
