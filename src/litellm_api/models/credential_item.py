from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.credential_item_credential_info import CredentialItemCredentialInfo
  from ..models.credential_item_credential_values import CredentialItemCredentialValues





T = TypeVar("T", bound="CredentialItem")



@_attrs_define
class CredentialItem:
    """ 
        Attributes:
            credential_name (str):
            credential_info (CredentialItemCredentialInfo):
            credential_values (CredentialItemCredentialValues):
     """

    credential_name: str
    credential_info: CredentialItemCredentialInfo
    credential_values: CredentialItemCredentialValues
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.credential_item_credential_values import CredentialItemCredentialValues
        from ..models.credential_item_credential_info import CredentialItemCredentialInfo
        credential_name = self.credential_name

        credential_info = self.credential_info.to_dict()

        credential_values = self.credential_values.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "credential_name": credential_name,
            "credential_info": credential_info,
            "credential_values": credential_values,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_item_credential_info import CredentialItemCredentialInfo
        from ..models.credential_item_credential_values import CredentialItemCredentialValues
        d = dict(src_dict)
        credential_name = d.pop("credential_name")

        credential_info = CredentialItemCredentialInfo.from_dict(d.pop("credential_info"))




        credential_values = CredentialItemCredentialValues.from_dict(d.pop("credential_values"))




        credential_item = cls(
            credential_name=credential_name,
            credential_info=credential_info,
            credential_values=credential_values,
        )


        credential_item.additional_properties = d
        return credential_item

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
