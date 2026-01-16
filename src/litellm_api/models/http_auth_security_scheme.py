from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="HTTPAuthSecurityScheme")



@_attrs_define
class HTTPAuthSecurityScheme:
    """ Defines a security scheme using HTTP authentication.

        Attributes:
            type_ (Literal['http']):
            scheme (str):
            bearer_format (None | str):
            description (None | str | Unset):
     """

    type_: Literal['http']
    scheme: str
    bearer_format: None | str
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        scheme = self.scheme

        bearer_format: None | str
        bearer_format = self.bearer_format

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "scheme": scheme,
            "bearerFormat": bearer_format,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal['http'] , d.pop("type"))
        if type_ != 'http':
            raise ValueError(f"type must match const 'http', got '{type_}'")

        scheme = d.pop("scheme")

        def _parse_bearer_format(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bearer_format = _parse_bearer_format(d.pop("bearerFormat"))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        http_auth_security_scheme = cls(
            type_=type_,
            scheme=scheme,
            bearer_format=bearer_format,
            description=description,
        )


        http_auth_security_scheme.additional_properties = d
        return http_auth_security_scheme

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
