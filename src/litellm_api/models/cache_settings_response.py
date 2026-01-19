from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.cache_settings_field import CacheSettingsField
  from ..models.cache_settings_response_current_values import CacheSettingsResponseCurrentValues
  from ..models.cache_settings_response_redis_type_descriptions import CacheSettingsResponseRedisTypeDescriptions





T = TypeVar("T", bound="CacheSettingsResponse")



@_attrs_define
class CacheSettingsResponse:
    """ 
        Attributes:
            fields (list[CacheSettingsField]): List of all configurable cache settings with metadata
            current_values (CacheSettingsResponseCurrentValues): Current values of cache settings
            redis_type_descriptions (CacheSettingsResponseRedisTypeDescriptions): Descriptions for each Redis type option
     """

    fields: list[CacheSettingsField]
    current_values: CacheSettingsResponseCurrentValues
    redis_type_descriptions: CacheSettingsResponseRedisTypeDescriptions
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cache_settings_field import CacheSettingsField
        from ..models.cache_settings_response_redis_type_descriptions import CacheSettingsResponseRedisTypeDescriptions
        from ..models.cache_settings_response_current_values import CacheSettingsResponseCurrentValues
        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)



        current_values = self.current_values.to_dict()

        redis_type_descriptions = self.redis_type_descriptions.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "fields": fields,
            "current_values": current_values,
            "redis_type_descriptions": redis_type_descriptions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cache_settings_field import CacheSettingsField
        from ..models.cache_settings_response_current_values import CacheSettingsResponseCurrentValues
        from ..models.cache_settings_response_redis_type_descriptions import CacheSettingsResponseRedisTypeDescriptions
        d = dict(src_dict)
        fields = []
        _fields = d.pop("fields")
        for fields_item_data in (_fields):
            fields_item = CacheSettingsField.from_dict(fields_item_data)



            fields.append(fields_item)


        current_values = CacheSettingsResponseCurrentValues.from_dict(d.pop("current_values"))




        redis_type_descriptions = CacheSettingsResponseRedisTypeDescriptions.from_dict(d.pop("redis_type_descriptions"))




        cache_settings_response = cls(
            fields=fields,
            current_values=current_values,
            redis_type_descriptions=redis_type_descriptions,
        )


        cache_settings_response.additional_properties = d
        return cache_settings_response

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
