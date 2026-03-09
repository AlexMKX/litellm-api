from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.test_custom_code_guardrail_request_request_data_type_0 import TestCustomCodeGuardrailRequestRequestDataType0
  from ..models.test_custom_code_guardrail_request_test_input import TestCustomCodeGuardrailRequestTestInput





T = TypeVar("T", bound="TestCustomCodeGuardrailRequest")



@_attrs_define
class TestCustomCodeGuardrailRequest:
    """ Request model for testing custom code guardrails.

        Attributes:
            custom_code (str):
            test_input (TestCustomCodeGuardrailRequestTestInput):
            input_type (str | Unset):  Default: 'request'.
            request_data (None | TestCustomCodeGuardrailRequestRequestDataType0 | Unset):
     """

    custom_code: str
    test_input: TestCustomCodeGuardrailRequestTestInput
    input_type: str | Unset = 'request'
    request_data: None | TestCustomCodeGuardrailRequestRequestDataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.test_custom_code_guardrail_request_request_data_type_0 import TestCustomCodeGuardrailRequestRequestDataType0
        from ..models.test_custom_code_guardrail_request_test_input import TestCustomCodeGuardrailRequestTestInput
        custom_code = self.custom_code

        test_input = self.test_input.to_dict()

        input_type = self.input_type

        request_data: dict[str, Any] | None | Unset
        if isinstance(self.request_data, Unset):
            request_data = UNSET
        elif isinstance(self.request_data, TestCustomCodeGuardrailRequestRequestDataType0):
            request_data = self.request_data.to_dict()
        else:
            request_data = self.request_data


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "custom_code": custom_code,
            "test_input": test_input,
        })
        if input_type is not UNSET:
            field_dict["input_type"] = input_type
        if request_data is not UNSET:
            field_dict["request_data"] = request_data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_custom_code_guardrail_request_request_data_type_0 import TestCustomCodeGuardrailRequestRequestDataType0
        from ..models.test_custom_code_guardrail_request_test_input import TestCustomCodeGuardrailRequestTestInput
        d = dict(src_dict)
        custom_code = d.pop("custom_code")

        test_input = TestCustomCodeGuardrailRequestTestInput.from_dict(d.pop("test_input"))




        input_type = d.pop("input_type", UNSET)

        def _parse_request_data(data: object) -> None | TestCustomCodeGuardrailRequestRequestDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                request_data_type_0 = TestCustomCodeGuardrailRequestRequestDataType0.from_dict(data)



                return request_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TestCustomCodeGuardrailRequestRequestDataType0 | Unset, data)

        request_data = _parse_request_data(d.pop("request_data", UNSET))


        test_custom_code_guardrail_request = cls(
            custom_code=custom_code,
            test_input=test_input,
            input_type=input_type,
            request_data=request_data,
        )


        test_custom_code_guardrail_request.additional_properties = d
        return test_custom_code_guardrail_request

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
