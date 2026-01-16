from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CacheSettingsField")



@_attrs_define
class CacheSettingsField:
    """ 
        Attributes:
            field_name (str):
            field_type (str):
            field_value (Any):
            field_description (str):
            ui_field_name (str):
            field_default (Any | Unset):
            options (list[str] | None | Unset):
            link (None | str | Unset):
            redis_type (None | str | Unset):
     """

    field_name: str
    field_type: str
    field_value: Any
    field_description: str
    ui_field_name: str
    field_default: Any | Unset = UNSET
    options: list[str] | None | Unset = UNSET
    link: None | str | Unset = UNSET
    redis_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        field_type = self.field_type

        field_value = self.field_value

        field_description = self.field_description

        ui_field_name = self.ui_field_name

        field_default = self.field_default

        options: list[str] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = self.options


        else:
            options = self.options

        link: None | str | Unset
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

        redis_type: None | str | Unset
        if isinstance(self.redis_type, Unset):
            redis_type = UNSET
        else:
            redis_type = self.redis_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "field_name": field_name,
            "field_type": field_type,
            "field_value": field_value,
            "field_description": field_description,
            "ui_field_name": ui_field_name,
        })
        if field_default is not UNSET:
            field_dict["field_default"] = field_default
        if options is not UNSET:
            field_dict["options"] = options
        if link is not UNSET:
            field_dict["link"] = link
        if redis_type is not UNSET:
            field_dict["redis_type"] = redis_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("field_name")

        field_type = d.pop("field_type")

        field_value = d.pop("field_value")

        field_description = d.pop("field_description")

        ui_field_name = d.pop("ui_field_name")

        field_default = d.pop("field_default", UNSET)

        def _parse_options(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = cast(list[str], data)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))


        def _parse_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        link = _parse_link(d.pop("link", UNSET))


        def _parse_redis_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        redis_type = _parse_redis_type(d.pop("redis_type", UNSET))


        cache_settings_field = cls(
            field_name=field_name,
            field_type=field_type,
            field_value=field_value,
            field_description=field_description,
            ui_field_name=ui_field_name,
            field_default=field_default,
            options=options,
            link=link,
            redis_type=redis_type,
        )


        cache_settings_field.additional_properties = d
        return cache_settings_field

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
