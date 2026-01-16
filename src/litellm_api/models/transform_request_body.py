from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.call_types import CallTypes
from typing import cast

if TYPE_CHECKING:
  from ..models.transform_request_body_request_body import TransformRequestBodyRequestBody





T = TypeVar("T", bound="TransformRequestBody")



@_attrs_define
class TransformRequestBody:
    """ 
        Attributes:
            call_type (CallTypes):
            request_body (TransformRequestBodyRequestBody):
     """

    call_type: CallTypes
    request_body: TransformRequestBodyRequestBody
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.transform_request_body_request_body import TransformRequestBodyRequestBody
        call_type = self.call_type.value

        request_body = self.request_body.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "call_type": call_type,
            "request_body": request_body,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transform_request_body_request_body import TransformRequestBodyRequestBody
        d = dict(src_dict)
        call_type = CallTypes(d.pop("call_type"))




        request_body = TransformRequestBodyRequestBody.from_dict(d.pop("request_body"))




        transform_request_body = cls(
            call_type=call_type,
            request_body=request_body,
        )


        transform_request_body.additional_properties = d
        return transform_request_body

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
