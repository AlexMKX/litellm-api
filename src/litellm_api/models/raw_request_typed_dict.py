from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.raw_request_typed_dict_raw_request_body_type_0 import RawRequestTypedDictRawRequestBodyType0
  from ..models.raw_request_typed_dict_raw_request_headers_type_0 import RawRequestTypedDictRawRequestHeadersType0





T = TypeVar("T", bound="RawRequestTypedDict")



@_attrs_define
class RawRequestTypedDict:
    """ 
        Attributes:
            raw_request_api_base (None | str | Unset):
            raw_request_body (None | RawRequestTypedDictRawRequestBodyType0 | Unset):
            raw_request_headers (None | RawRequestTypedDictRawRequestHeadersType0 | Unset):
            error (None | str | Unset):
     """

    raw_request_api_base: None | str | Unset = UNSET
    raw_request_body: None | RawRequestTypedDictRawRequestBodyType0 | Unset = UNSET
    raw_request_headers: None | RawRequestTypedDictRawRequestHeadersType0 | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.raw_request_typed_dict_raw_request_body_type_0 import RawRequestTypedDictRawRequestBodyType0
        from ..models.raw_request_typed_dict_raw_request_headers_type_0 import RawRequestTypedDictRawRequestHeadersType0
        raw_request_api_base: None | str | Unset
        if isinstance(self.raw_request_api_base, Unset):
            raw_request_api_base = UNSET
        else:
            raw_request_api_base = self.raw_request_api_base

        raw_request_body: dict[str, Any] | None | Unset
        if isinstance(self.raw_request_body, Unset):
            raw_request_body = UNSET
        elif isinstance(self.raw_request_body, RawRequestTypedDictRawRequestBodyType0):
            raw_request_body = self.raw_request_body.to_dict()
        else:
            raw_request_body = self.raw_request_body

        raw_request_headers: dict[str, Any] | None | Unset
        if isinstance(self.raw_request_headers, Unset):
            raw_request_headers = UNSET
        elif isinstance(self.raw_request_headers, RawRequestTypedDictRawRequestHeadersType0):
            raw_request_headers = self.raw_request_headers.to_dict()
        else:
            raw_request_headers = self.raw_request_headers

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if raw_request_api_base is not UNSET:
            field_dict["raw_request_api_base"] = raw_request_api_base
        if raw_request_body is not UNSET:
            field_dict["raw_request_body"] = raw_request_body
        if raw_request_headers is not UNSET:
            field_dict["raw_request_headers"] = raw_request_headers
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_request_typed_dict_raw_request_body_type_0 import RawRequestTypedDictRawRequestBodyType0
        from ..models.raw_request_typed_dict_raw_request_headers_type_0 import RawRequestTypedDictRawRequestHeadersType0
        d = dict(src_dict)
        def _parse_raw_request_api_base(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        raw_request_api_base = _parse_raw_request_api_base(d.pop("raw_request_api_base", UNSET))


        def _parse_raw_request_body(data: object) -> None | RawRequestTypedDictRawRequestBodyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                raw_request_body_type_0 = RawRequestTypedDictRawRequestBodyType0.from_dict(data)



                return raw_request_body_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RawRequestTypedDictRawRequestBodyType0 | Unset, data)

        raw_request_body = _parse_raw_request_body(d.pop("raw_request_body", UNSET))


        def _parse_raw_request_headers(data: object) -> None | RawRequestTypedDictRawRequestHeadersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                raw_request_headers_type_0 = RawRequestTypedDictRawRequestHeadersType0.from_dict(data)



                return raw_request_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RawRequestTypedDictRawRequestHeadersType0 | Unset, data)

        raw_request_headers = _parse_raw_request_headers(d.pop("raw_request_headers", UNSET))


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        raw_request_typed_dict = cls(
            raw_request_api_base=raw_request_api_base,
            raw_request_body=raw_request_body,
            raw_request_headers=raw_request_headers,
            error=error,
        )


        raw_request_typed_dict.additional_properties = d
        return raw_request_typed_dict

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
