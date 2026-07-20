from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.coordination_redis_settings_response_source_type_0 import CoordinationRedisSettingsResponseSourceType0
from typing import cast

if TYPE_CHECKING:
  from ..models.coordination_redis_settings_field import CoordinationRedisSettingsField
  from ..models.coordination_redis_settings_response_values import CoordinationRedisSettingsResponseValues





T = TypeVar("T", bound="CoordinationRedisSettingsResponse")



@_attrs_define
class CoordinationRedisSettingsResponse:
    """ 
        Attributes:
            values (CoordinationRedisSettingsResponseValues): Current coordination Redis settings, with credentials redacted
            fields (list[CoordinationRedisSettingsField]): List of all configurable coordination Redis settings with
                metadata
            source (CoordinationRedisSettingsResponseSourceType0 | None): Where the proxy's coordination Redis comes from;
                null when it has none
     """

    values: CoordinationRedisSettingsResponseValues
    fields: list[CoordinationRedisSettingsField]
    source: CoordinationRedisSettingsResponseSourceType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.coordination_redis_settings_field import CoordinationRedisSettingsField
        from ..models.coordination_redis_settings_response_values import CoordinationRedisSettingsResponseValues
        values = self.values.to_dict()

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)



        source: None | str
        if isinstance(self.source, CoordinationRedisSettingsResponseSourceType0):
            source = self.source.value
        else:
            source = self.source


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "values": values,
            "fields": fields,
            "source": source,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coordination_redis_settings_field import CoordinationRedisSettingsField
        from ..models.coordination_redis_settings_response_values import CoordinationRedisSettingsResponseValues
        d = dict(src_dict)
        values = CoordinationRedisSettingsResponseValues.from_dict(d.pop("values"))




        fields = []
        _fields = d.pop("fields")
        for fields_item_data in (_fields):
            fields_item = CoordinationRedisSettingsField.from_dict(fields_item_data)



            fields.append(fields_item)


        def _parse_source(data: object) -> CoordinationRedisSettingsResponseSourceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_0 = CoordinationRedisSettingsResponseSourceType0(data)



                return source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CoordinationRedisSettingsResponseSourceType0 | None, data)

        source = _parse_source(d.pop("source"))


        coordination_redis_settings_response = cls(
            values=values,
            fields=fields,
            source=source,
        )


        coordination_redis_settings_response.additional_properties = d
        return coordination_redis_settings_response

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
