from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.test_policy_template_request_guardrail_definitions_item import TestPolicyTemplateRequestGuardrailDefinitionsItem





T = TypeVar("T", bound="TestPolicyTemplateRequest")



@_attrs_define
class TestPolicyTemplateRequest:
    """ 
        Attributes:
            guardrail_definitions (list[TestPolicyTemplateRequestGuardrailDefinitionsItem]): All guardrailDefinitions from
                the policy template
            text (str): Test input text to run guardrails against
     """

    guardrail_definitions: list[TestPolicyTemplateRequestGuardrailDefinitionsItem]
    text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.test_policy_template_request_guardrail_definitions_item import TestPolicyTemplateRequestGuardrailDefinitionsItem
        guardrail_definitions = []
        for guardrail_definitions_item_data in self.guardrail_definitions:
            guardrail_definitions_item = guardrail_definitions_item_data.to_dict()
            guardrail_definitions.append(guardrail_definitions_item)



        text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "guardrail_definitions": guardrail_definitions,
            "text": text,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_policy_template_request_guardrail_definitions_item import TestPolicyTemplateRequestGuardrailDefinitionsItem
        d = dict(src_dict)
        guardrail_definitions = []
        _guardrail_definitions = d.pop("guardrail_definitions")
        for guardrail_definitions_item_data in (_guardrail_definitions):
            guardrail_definitions_item = TestPolicyTemplateRequestGuardrailDefinitionsItem.from_dict(guardrail_definitions_item_data)



            guardrail_definitions.append(guardrail_definitions_item)


        text = d.pop("text")

        test_policy_template_request = cls(
            guardrail_definitions=guardrail_definitions,
            text=text,
        )


        test_policy_template_request.additional_properties = d
        return test_policy_template_request

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
