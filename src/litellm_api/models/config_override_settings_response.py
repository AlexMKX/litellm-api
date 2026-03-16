from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.config_override_settings_response_field_schema import ConfigOverrideSettingsResponseFieldSchema
  from ..models.config_override_settings_response_values import ConfigOverrideSettingsResponseValues





T = TypeVar("T", bound="ConfigOverrideSettingsResponse")



@_attrs_define
class ConfigOverrideSettingsResponse:
    """ Response model for config override settings GET endpoints.

        Attributes:
            config_type (str): The type of config override
            values (ConfigOverrideSettingsResponseValues): Current configuration values (sensitive fields decrypted)
            field_schema (ConfigOverrideSettingsResponseFieldSchema): Schema information for UI rendering
     """

    config_type: str
    values: ConfigOverrideSettingsResponseValues
    field_schema: ConfigOverrideSettingsResponseFieldSchema
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_override_settings_response_field_schema import ConfigOverrideSettingsResponseFieldSchema
        from ..models.config_override_settings_response_values import ConfigOverrideSettingsResponseValues
        config_type = self.config_type

        values = self.values.to_dict()

        field_schema = self.field_schema.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "config_type": config_type,
            "values": values,
            "field_schema": field_schema,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_override_settings_response_field_schema import ConfigOverrideSettingsResponseFieldSchema
        from ..models.config_override_settings_response_values import ConfigOverrideSettingsResponseValues
        d = dict(src_dict)
        config_type = d.pop("config_type")

        values = ConfigOverrideSettingsResponseValues.from_dict(d.pop("values"))




        field_schema = ConfigOverrideSettingsResponseFieldSchema.from_dict(d.pop("field_schema"))




        config_override_settings_response = cls(
            config_type=config_type,
            values=values,
            field_schema=field_schema,
        )


        config_override_settings_response.additional_properties = d
        return config_override_settings_response

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
