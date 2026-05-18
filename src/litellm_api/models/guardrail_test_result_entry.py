from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GuardrailTestResultEntry")



@_attrs_define
class GuardrailTestResultEntry:
    """ 
        Attributes:
            action (str):
            details (str):
            guardrail_name (str):
            output_text (str):
     """

    action: str
    details: str
    guardrail_name: str
    output_text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        action = self.action

        details = self.details

        guardrail_name = self.guardrail_name

        output_text = self.output_text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action": action,
            "details": details,
            "guardrail_name": guardrail_name,
            "output_text": output_text,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        details = d.pop("details")

        guardrail_name = d.pop("guardrail_name")

        output_text = d.pop("output_text")

        guardrail_test_result_entry = cls(
            action=action,
            details=details,
            guardrail_name=guardrail_name,
            output_text=output_text,
        )


        guardrail_test_result_entry.additional_properties = d
        return guardrail_test_result_entry

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
