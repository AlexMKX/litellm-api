from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.test_custom_code_guardrail_response_result_type_0 import TestCustomCodeGuardrailResponseResultType0





T = TypeVar("T", bound="TestCustomCodeGuardrailResponse")



@_attrs_define
class TestCustomCodeGuardrailResponse:
    """ Response model for testing custom code guardrails.

        Attributes:
            success (bool):
            result (None | TestCustomCodeGuardrailResponseResultType0 | Unset):
            error (None | str | Unset):
            error_type (None | str | Unset):
     """

    success: bool
    result: None | TestCustomCodeGuardrailResponseResultType0 | Unset = UNSET
    error: None | str | Unset = UNSET
    error_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.test_custom_code_guardrail_response_result_type_0 import TestCustomCodeGuardrailResponseResultType0
        success = self.success

        result: dict[str, Any] | None | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        elif isinstance(self.result, TestCustomCodeGuardrailResponseResultType0):
            result = self.result.to_dict()
        else:
            result = self.result

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        error_type: None | str | Unset
        if isinstance(self.error_type, Unset):
            error_type = UNSET
        else:
            error_type = self.error_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "success": success,
        })
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error
        if error_type is not UNSET:
            field_dict["error_type"] = error_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_custom_code_guardrail_response_result_type_0 import TestCustomCodeGuardrailResponseResultType0
        d = dict(src_dict)
        success = d.pop("success")

        def _parse_result(data: object) -> None | TestCustomCodeGuardrailResponseResultType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_0 = TestCustomCodeGuardrailResponseResultType0.from_dict(data)



                return result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TestCustomCodeGuardrailResponseResultType0 | Unset, data)

        result = _parse_result(d.pop("result", UNSET))


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        def _parse_error_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_type = _parse_error_type(d.pop("error_type", UNSET))


        test_custom_code_guardrail_response = cls(
            success=success,
            result=result,
            error=error,
            error_type=error_type,
        )


        test_custom_code_guardrail_response.additional_properties = d
        return test_custom_code_guardrail_response

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
