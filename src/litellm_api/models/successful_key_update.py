from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.successful_key_update_key_info import SuccessfulKeyUpdateKeyInfo





T = TypeVar("T", bound="SuccessfulKeyUpdate")



@_attrs_define
class SuccessfulKeyUpdate:
    """ Successfully updated key with its updated information

        Attributes:
            key (str):
            key_info (SuccessfulKeyUpdateKeyInfo):
     """

    key: str
    key_info: SuccessfulKeyUpdateKeyInfo
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.successful_key_update_key_info import SuccessfulKeyUpdateKeyInfo
        key = self.key

        key_info = self.key_info.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
            "key_info": key_info,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.successful_key_update_key_info import SuccessfulKeyUpdateKeyInfo
        d = dict(src_dict)
        key = d.pop("key")

        key_info = SuccessfulKeyUpdateKeyInfo.from_dict(d.pop("key_info"))




        successful_key_update = cls(
            key=key,
            key_info=key_info,
        )


        successful_key_update.additional_properties = d
        return successful_key_update

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
