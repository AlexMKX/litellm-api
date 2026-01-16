from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="OpenIdConnectSecurityScheme")



@_attrs_define
class OpenIdConnectSecurityScheme:
    """ Defines a security scheme using OpenID Connect.

        Attributes:
            type_ (Literal['openIdConnect']):
            open_id_connect_url (str):
            description (None | str | Unset):
     """

    type_: Literal['openIdConnect']
    open_id_connect_url: str
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        open_id_connect_url = self.open_id_connect_url

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "openIdConnectUrl": open_id_connect_url,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal['openIdConnect'] , d.pop("type"))
        if type_ != 'openIdConnect':
            raise ValueError(f"type must match const 'openIdConnect', got '{type_}'")

        open_id_connect_url = d.pop("openIdConnectUrl")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        open_id_connect_security_scheme = cls(
            type_=type_,
            open_id_connect_url=open_id_connect_url,
            description=description,
        )


        open_id_connect_security_scheme.additional_properties = d
        return open_id_connect_security_scheme

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
