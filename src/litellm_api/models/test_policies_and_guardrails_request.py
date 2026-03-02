from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.test_policies_and_guardrails_request_input_type import TestPoliciesAndGuardrailsRequestInputType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.generic_guardrail_api_inputs import GenericGuardrailAPIInputs
  from ..models.test_policies_and_guardrails_request_request_data import TestPoliciesAndGuardrailsRequestRequestData





T = TypeVar("T", bound="TestPoliciesAndGuardrailsRequest")



@_attrs_define
class TestPoliciesAndGuardrailsRequest:
    """ Request body for POST /utils/test_policies_and_guardrails.

        Attributes:
            policy_names (list[str] | None | Unset): Policy names to resolve guardrails from
            guardrail_names (list[str] | None | Unset): Guardrail names to apply directly
            inputs_list (list[GenericGuardrailAPIInputs] | Unset): List of GenericGuardrailAPIInputs; each item processed
                separately (for batch compliance testing).
            request_data (TestPoliciesAndGuardrailsRequestRequestData | Unset): Request context (model, user_id, etc.)
            input_type (TestPoliciesAndGuardrailsRequestInputType | Unset): Whether inputs are request or response Default:
                TestPoliciesAndGuardrailsRequestInputType.REQUEST.
            agent_id (None | str | Unset): When set, call chat completion with this model/agent for each input and include
                the response in the result.
     """

    policy_names: list[str] | None | Unset = UNSET
    guardrail_names: list[str] | None | Unset = UNSET
    inputs_list: list[GenericGuardrailAPIInputs] | Unset = UNSET
    request_data: TestPoliciesAndGuardrailsRequestRequestData | Unset = UNSET
    input_type: TestPoliciesAndGuardrailsRequestInputType | Unset = TestPoliciesAndGuardrailsRequestInputType.REQUEST
    agent_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.generic_guardrail_api_inputs import GenericGuardrailAPIInputs
        from ..models.test_policies_and_guardrails_request_request_data import TestPoliciesAndGuardrailsRequestRequestData
        policy_names: list[str] | None | Unset
        if isinstance(self.policy_names, Unset):
            policy_names = UNSET
        elif isinstance(self.policy_names, list):
            policy_names = self.policy_names


        else:
            policy_names = self.policy_names

        guardrail_names: list[str] | None | Unset
        if isinstance(self.guardrail_names, Unset):
            guardrail_names = UNSET
        elif isinstance(self.guardrail_names, list):
            guardrail_names = self.guardrail_names


        else:
            guardrail_names = self.guardrail_names

        inputs_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inputs_list, Unset):
            inputs_list = []
            for inputs_list_item_data in self.inputs_list:
                inputs_list_item = inputs_list_item_data.to_dict()
                inputs_list.append(inputs_list_item)



        request_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request_data, Unset):
            request_data = self.request_data.to_dict()

        input_type: str | Unset = UNSET
        if not isinstance(self.input_type, Unset):
            input_type = self.input_type.value


        agent_id: None | str | Unset
        if isinstance(self.agent_id, Unset):
            agent_id = UNSET
        else:
            agent_id = self.agent_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if policy_names is not UNSET:
            field_dict["policy_names"] = policy_names
        if guardrail_names is not UNSET:
            field_dict["guardrail_names"] = guardrail_names
        if inputs_list is not UNSET:
            field_dict["inputs_list"] = inputs_list
        if request_data is not UNSET:
            field_dict["request_data"] = request_data
        if input_type is not UNSET:
            field_dict["input_type"] = input_type
        if agent_id is not UNSET:
            field_dict["agent_id"] = agent_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generic_guardrail_api_inputs import GenericGuardrailAPIInputs
        from ..models.test_policies_and_guardrails_request_request_data import TestPoliciesAndGuardrailsRequestRequestData
        d = dict(src_dict)
        def _parse_policy_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                policy_names_type_0 = cast(list[str], data)

                return policy_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        policy_names = _parse_policy_names(d.pop("policy_names", UNSET))


        def _parse_guardrail_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                guardrail_names_type_0 = cast(list[str], data)

                return guardrail_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        guardrail_names = _parse_guardrail_names(d.pop("guardrail_names", UNSET))


        _inputs_list = d.pop("inputs_list", UNSET)
        inputs_list: list[GenericGuardrailAPIInputs] | Unset = UNSET
        if _inputs_list is not UNSET:
            inputs_list = []
            for inputs_list_item_data in _inputs_list:
                inputs_list_item = GenericGuardrailAPIInputs.from_dict(inputs_list_item_data)



                inputs_list.append(inputs_list_item)


        _request_data = d.pop("request_data", UNSET)
        request_data: TestPoliciesAndGuardrailsRequestRequestData | Unset
        if isinstance(_request_data,  Unset):
            request_data = UNSET
        else:
            request_data = TestPoliciesAndGuardrailsRequestRequestData.from_dict(_request_data)




        _input_type = d.pop("input_type", UNSET)
        input_type: TestPoliciesAndGuardrailsRequestInputType | Unset
        if isinstance(_input_type,  Unset):
            input_type = UNSET
        else:
            input_type = TestPoliciesAndGuardrailsRequestInputType(_input_type)




        def _parse_agent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_id = _parse_agent_id(d.pop("agent_id", UNSET))


        test_policies_and_guardrails_request = cls(
            policy_names=policy_names,
            guardrail_names=guardrail_names,
            inputs_list=inputs_list,
            request_data=request_data,
            input_type=input_type,
            agent_id=agent_id,
        )


        test_policies_and_guardrails_request.additional_properties = d
        return test_policies_and_guardrails_request

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
