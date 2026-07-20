from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.coordination_redis_settings_field_section import CoordinationRedisSettingsFieldSection
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CoordinationRedisSettingsField")



@_attrs_define
class CoordinationRedisSettingsField:
    """ 
        Attributes:
            field_name (str):
            field_type (str):
            field_description (str):
            ui_field_name (str):
            section (CoordinationRedisSettingsFieldSection):
            field_value (Any | None | Unset):
            field_default (Any | None | Unset):
     """

    field_name: str
    field_type: str
    field_description: str
    ui_field_name: str
    section: CoordinationRedisSettingsFieldSection
    field_value: Any | None | Unset = UNSET
    field_default: Any | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        field_type = self.field_type

        field_description = self.field_description

        ui_field_name = self.ui_field_name

        section = self.section.value

        field_value: Any | None | Unset
        if isinstance(self.field_value, Unset):
            field_value = UNSET
        else:
            field_value = self.field_value

        field_default: Any | None | Unset
        if isinstance(self.field_default, Unset):
            field_default = UNSET
        else:
            field_default = self.field_default


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "field_name": field_name,
            "field_type": field_type,
            "field_description": field_description,
            "ui_field_name": ui_field_name,
            "section": section,
        })
        if field_value is not UNSET:
            field_dict["field_value"] = field_value
        if field_default is not UNSET:
            field_dict["field_default"] = field_default

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("field_name")

        field_type = d.pop("field_type")

        field_description = d.pop("field_description")

        ui_field_name = d.pop("ui_field_name")

        section = CoordinationRedisSettingsFieldSection(d.pop("section"))




        def _parse_field_value(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        field_value = _parse_field_value(d.pop("field_value", UNSET))


        def _parse_field_default(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        field_default = _parse_field_default(d.pop("field_default", UNSET))


        coordination_redis_settings_field = cls(
            field_name=field_name,
            field_type=field_type,
            field_description=field_description,
            ui_field_name=ui_field_name,
            section=section,
            field_value=field_value,
            field_default=field_default,
        )


        coordination_redis_settings_field.additional_properties = d
        return coordination_redis_settings_field

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
