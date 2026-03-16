from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CreateJWTKeyMappingRequest")



@_attrs_define
class CreateJWTKeyMappingRequest:
    """ 
        Attributes:
            jwt_claim_name (str):
            jwt_claim_value (str):
            key (str):
            description (None | str | Unset):
     """

    jwt_claim_name: str
    jwt_claim_value: str
    key: str
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        jwt_claim_name = self.jwt_claim_name

        jwt_claim_value = self.jwt_claim_value

        key = self.key

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "jwt_claim_name": jwt_claim_name,
            "jwt_claim_value": jwt_claim_value,
            "key": key,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        jwt_claim_name = d.pop("jwt_claim_name")

        jwt_claim_value = d.pop("jwt_claim_value")

        key = d.pop("key")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        create_jwt_key_mapping_request = cls(
            jwt_claim_name=jwt_claim_name,
            jwt_claim_value=jwt_claim_value,
            key=key,
            description=description,
        )


        create_jwt_key_mapping_request.additional_properties = d
        return create_jwt_key_mapping_request

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
