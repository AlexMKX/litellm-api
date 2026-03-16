from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tool_policy_update_response_input_policy_type_0 import ToolPolicyUpdateResponseInputPolicyType0
from ..models.tool_policy_update_response_output_policy_type_0 import ToolPolicyUpdateResponseOutputPolicyType0
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ToolPolicyUpdateResponse")



@_attrs_define
class ToolPolicyUpdateResponse:
    """ 
        Attributes:
            tool_name (str):
            updated (bool):
            input_policy (None | ToolPolicyUpdateResponseInputPolicyType0 | Unset):
            output_policy (None | ToolPolicyUpdateResponseOutputPolicyType0 | Unset):
            team_id (None | str | Unset):
            key_hash (None | str | Unset):
     """

    tool_name: str
    updated: bool
    input_policy: None | ToolPolicyUpdateResponseInputPolicyType0 | Unset = UNSET
    output_policy: None | ToolPolicyUpdateResponseOutputPolicyType0 | Unset = UNSET
    team_id: None | str | Unset = UNSET
    key_hash: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tool_name = self.tool_name

        updated = self.updated

        input_policy: None | str | Unset
        if isinstance(self.input_policy, Unset):
            input_policy = UNSET
        elif isinstance(self.input_policy, ToolPolicyUpdateResponseInputPolicyType0):
            input_policy = self.input_policy.value
        else:
            input_policy = self.input_policy

        output_policy: None | str | Unset
        if isinstance(self.output_policy, Unset):
            output_policy = UNSET
        elif isinstance(self.output_policy, ToolPolicyUpdateResponseOutputPolicyType0):
            output_policy = self.output_policy.value
        else:
            output_policy = self.output_policy

        team_id: None | str | Unset
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        else:
            team_id = self.team_id

        key_hash: None | str | Unset
        if isinstance(self.key_hash, Unset):
            key_hash = UNSET
        else:
            key_hash = self.key_hash


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tool_name": tool_name,
            "updated": updated,
        })
        if input_policy is not UNSET:
            field_dict["input_policy"] = input_policy
        if output_policy is not UNSET:
            field_dict["output_policy"] = output_policy
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if key_hash is not UNSET:
            field_dict["key_hash"] = key_hash

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tool_name = d.pop("tool_name")

        updated = d.pop("updated")

        def _parse_input_policy(data: object) -> None | ToolPolicyUpdateResponseInputPolicyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                input_policy_type_0 = ToolPolicyUpdateResponseInputPolicyType0(data)



                return input_policy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ToolPolicyUpdateResponseInputPolicyType0 | Unset, data)

        input_policy = _parse_input_policy(d.pop("input_policy", UNSET))


        def _parse_output_policy(data: object) -> None | ToolPolicyUpdateResponseOutputPolicyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                output_policy_type_0 = ToolPolicyUpdateResponseOutputPolicyType0(data)



                return output_policy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ToolPolicyUpdateResponseOutputPolicyType0 | Unset, data)

        output_policy = _parse_output_policy(d.pop("output_policy", UNSET))


        def _parse_team_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_id = _parse_team_id(d.pop("team_id", UNSET))


        def _parse_key_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_hash = _parse_key_hash(d.pop("key_hash", UNSET))


        tool_policy_update_response = cls(
            tool_name=tool_name,
            updated=updated,
            input_policy=input_policy,
            output_policy=output_policy,
            team_id=team_id,
            key_hash=key_hash,
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
