from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="AccessControlUIAccessMode")



@_attrs_define
class AccessControlUIAccessMode:
    """ Model for Controlling UI Access Mode via SSO Groups

        Attributes:
            type_ (Literal['restricted_sso_group']):
            restricted_sso_group (str):
            sso_group_jwt_field (str):
     """

    type_: Literal['restricted_sso_group']
    restricted_sso_group: str
    sso_group_jwt_field: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        restricted_sso_group = self.restricted_sso_group

        sso_group_jwt_field = self.sso_group_jwt_field


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "restricted_sso_group": restricted_sso_group,
            "sso_group_jwt_field": sso_group_jwt_field,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal['restricted_sso_group'] , d.pop("type"))
        if type_ != 'restricted_sso_group':
            raise ValueError(f"type must match const 'restricted_sso_group', got '{type_}'")

        restricted_sso_group = d.pop("restricted_sso_group")

        sso_group_jwt_field = d.pop("sso_group_jwt_field")

        access_control_ui_access_mode = cls(
            type_=type_,
            restricted_sso_group=restricted_sso_group,
            sso_group_jwt_field=sso_group_jwt_field,
        )


        access_control_ui_access_mode.additional_properties = d
        return access_control_ui_access_mode

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
