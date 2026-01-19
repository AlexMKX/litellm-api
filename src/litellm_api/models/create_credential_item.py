from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_credential_item_credential_info import CreateCredentialItemCredentialInfo
  from ..models.create_credential_item_credential_values_type_0 import CreateCredentialItemCredentialValuesType0





T = TypeVar("T", bound="CreateCredentialItem")



@_attrs_define
class CreateCredentialItem:
    """ 
        Attributes:
            credential_name (str):
            credential_info (CreateCredentialItemCredentialInfo):
            credential_values (CreateCredentialItemCredentialValuesType0 | None | Unset):
            model_id (None | str | Unset):
     """

    credential_name: str
    credential_info: CreateCredentialItemCredentialInfo
    credential_values: CreateCredentialItemCredentialValuesType0 | None | Unset = UNSET
    model_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_credential_item_credential_values_type_0 import CreateCredentialItemCredentialValuesType0
        from ..models.create_credential_item_credential_info import CreateCredentialItemCredentialInfo
        credential_name = self.credential_name

        credential_info = self.credential_info.to_dict()

        credential_values: dict[str, Any] | None | Unset
        if isinstance(self.credential_values, Unset):
            credential_values = UNSET
        elif isinstance(self.credential_values, CreateCredentialItemCredentialValuesType0):
            credential_values = self.credential_values.to_dict()
        else:
            credential_values = self.credential_values

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "credential_name": credential_name,
            "credential_info": credential_info,
        })
        if credential_values is not UNSET:
            field_dict["credential_values"] = credential_values
        if model_id is not UNSET:
            field_dict["model_id"] = model_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_credential_item_credential_info import CreateCredentialItemCredentialInfo
        from ..models.create_credential_item_credential_values_type_0 import CreateCredentialItemCredentialValuesType0
        d = dict(src_dict)
        credential_name = d.pop("credential_name")

        credential_info = CreateCredentialItemCredentialInfo.from_dict(d.pop("credential_info"))




        def _parse_credential_values(data: object) -> CreateCredentialItemCredentialValuesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credential_values_type_0 = CreateCredentialItemCredentialValuesType0.from_dict(data)



                return credential_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateCredentialItemCredentialValuesType0 | None | Unset, data)

        credential_values = _parse_credential_values(d.pop("credential_values", UNSET))


        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))


        create_credential_item = cls(
            credential_name=credential_name,
            credential_info=credential_info,
            credential_values=credential_values,
            model_id=model_id,
        )


        create_credential_item.additional_properties = d
        return create_credential_item

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
