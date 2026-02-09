from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.internal_user_settings_response_field_schema import InternalUserSettingsResponseFieldSchema
  from ..models.internal_user_settings_response_values import InternalUserSettingsResponseValues





T = TypeVar("T", bound="InternalUserSettingsResponse")



@_attrs_define
class InternalUserSettingsResponse:
    """ Response model for internal user settings

        Attributes:
            values (InternalUserSettingsResponseValues):
            field_schema (InternalUserSettingsResponseFieldSchema):
     """

    values: InternalUserSettingsResponseValues
    field_schema: InternalUserSettingsResponseFieldSchema
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.internal_user_settings_response_field_schema import InternalUserSettingsResponseFieldSchema
        from ..models.internal_user_settings_response_values import InternalUserSettingsResponseValues
        values = self.values.to_dict()

        field_schema = self.field_schema.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "values": values,
            "field_schema": field_schema,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_user_settings_response_field_schema import InternalUserSettingsResponseFieldSchema
        from ..models.internal_user_settings_response_values import InternalUserSettingsResponseValues
        d = dict(src_dict)
        values = InternalUserSettingsResponseValues.from_dict(d.pop("values"))




        field_schema = InternalUserSettingsResponseFieldSchema.from_dict(d.pop("field_schema"))




        internal_user_settings_response = cls(
            values=values,
            field_schema=field_schema,
        )


        internal_user_settings_response.additional_properties = d
        return internal_user_settings_response

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
