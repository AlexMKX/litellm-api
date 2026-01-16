from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PassThroughGuardrailSettings")



@_attrs_define
class PassThroughGuardrailSettings:
    """ Settings for a specific guardrail on a passthrough endpoint.

    Allows field-level targeting for guardrail execution.

        Attributes:
            request_fields (list[str] | None | Unset): JSONPath expressions for input field targeting (pre_call). Examples:
                'query', 'documents[*].text', 'messages[*].content'. If not specified, guardrail runs on entire request payload.
            response_fields (list[str] | None | Unset): JSONPath expressions for output field targeting (post_call).
                Examples: 'results[*].text', 'output'. If not specified, guardrail runs on entire response payload.
     """

    request_fields: list[str] | None | Unset = UNSET
    response_fields: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        request_fields: list[str] | None | Unset
        if isinstance(self.request_fields, Unset):
            request_fields = UNSET
        elif isinstance(self.request_fields, list):
            request_fields = self.request_fields


        else:
            request_fields = self.request_fields

        response_fields: list[str] | None | Unset
        if isinstance(self.response_fields, Unset):
            response_fields = UNSET
        elif isinstance(self.response_fields, list):
            response_fields = self.response_fields


        else:
            response_fields = self.response_fields


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if request_fields is not UNSET:
            field_dict["request_fields"] = request_fields
        if response_fields is not UNSET:
            field_dict["response_fields"] = response_fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_request_fields(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                request_fields_type_0 = cast(list[str], data)

                return request_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        request_fields = _parse_request_fields(d.pop("request_fields", UNSET))


        def _parse_response_fields(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_fields_type_0 = cast(list[str], data)

                return response_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        response_fields = _parse_response_fields(d.pop("response_fields", UNSET))


        pass_through_guardrail_settings = cls(
            request_fields=request_fields,
            response_fields=response_fields,
        )


        pass_through_guardrail_settings.additional_properties = d
        return pass_through_guardrail_settings

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
