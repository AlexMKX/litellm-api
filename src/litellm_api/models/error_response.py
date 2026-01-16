from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.error_response_detail import ErrorResponseDetail





T = TypeVar("T", bound="ErrorResponse")



@_attrs_define
class ErrorResponse:
    """ 
        Attributes:
            detail (ErrorResponseDetail):  Example: {'error': {'code': 'error_code', 'message': 'Error message', 'param':
                'error_param', 'type': 'error_type'}}.
     """

    detail: ErrorResponseDetail
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.error_response_detail import ErrorResponseDetail
        detail = self.detail.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "detail": detail,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_response_detail import ErrorResponseDetail
        d = dict(src_dict)
        detail = ErrorResponseDetail.from_dict(d.pop("detail"))




        error_response = cls(
            detail=detail,
        )


        error_response.additional_properties = d
        return error_response

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
