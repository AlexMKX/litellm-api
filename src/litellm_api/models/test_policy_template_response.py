from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.guardrail_test_result_entry import GuardrailTestResultEntry





T = TypeVar("T", bound="TestPolicyTemplateResponse")



@_attrs_define
class TestPolicyTemplateResponse:
    """ 
        Attributes:
            overall_action (str):
            results (list[GuardrailTestResultEntry]):
     """

    overall_action: str
    results: list[GuardrailTestResultEntry]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.guardrail_test_result_entry import GuardrailTestResultEntry
        overall_action = self.overall_action

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "overall_action": overall_action,
            "results": results,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.guardrail_test_result_entry import GuardrailTestResultEntry
        d = dict(src_dict)
        overall_action = d.pop("overall_action")

        results = []
        _results = d.pop("results")
        for results_item_data in (_results):
            results_item = GuardrailTestResultEntry.from_dict(results_item_data)



            results.append(results_item)


        test_policy_template_response = cls(
            overall_action=overall_action,
            results=results,
        )


        test_policy_template_response.additional_properties = d
        return test_policy_template_response

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
