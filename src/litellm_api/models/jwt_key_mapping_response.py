from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="JWTKeyMappingResponse")



@_attrs_define
class JWTKeyMappingResponse:
    """ 
        Attributes:
            created_at (datetime.datetime):
            id (str):
            is_active (bool):
            jwt_claim_name (str):
            jwt_claim_value (str):
            updated_at (datetime.datetime):
            created_by (None | str | Unset):
            description (None | str | Unset):
            updated_by (None | str | Unset):
     """

    created_at: datetime.datetime
    id: str
    is_active: bool
    jwt_claim_name: str
    jwt_claim_value: str
    updated_at: datetime.datetime
    created_by: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        is_active = self.is_active

        jwt_claim_name = self.jwt_claim_name

        jwt_claim_value = self.jwt_claim_value

        updated_at = self.updated_at.isoformat()

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "id": id,
            "is_active": is_active,
            "jwt_claim_name": jwt_claim_name,
            "jwt_claim_value": jwt_claim_value,
            "updated_at": updated_at,
        })
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        id = d.pop("id")

        is_active = d.pop("is_active")

        jwt_claim_name = d.pop("jwt_claim_name")

        jwt_claim_value = d.pop("jwt_claim_value")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))




        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))


        jwt_key_mapping_response = cls(
            created_at=created_at,
            id=id,
            is_active=is_active,
            jwt_claim_name=jwt_claim_name,
            jwt_claim_value=jwt_claim_value,
            updated_at=updated_at,
            created_by=created_by,
            description=description,
            updated_by=updated_by,
        )


        jwt_key_mapping_response.additional_properties = d
        return jwt_key_mapping_response

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
