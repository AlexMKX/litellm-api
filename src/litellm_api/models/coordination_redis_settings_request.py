from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.coordination_redis_settings_request_settings import CoordinationRedisSettingsRequestSettings





T = TypeVar("T", bound="CoordinationRedisSettingsRequest")



@_attrs_define
class CoordinationRedisSettingsRequest:
    """ 
        Attributes:
            settings (CoordinationRedisSettingsRequestSettings): Coordination Redis connection params
     """

    settings: CoordinationRedisSettingsRequestSettings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.coordination_redis_settings_request_settings import CoordinationRedisSettingsRequestSettings
        settings = self.settings.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "settings": settings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coordination_redis_settings_request_settings import CoordinationRedisSettingsRequestSettings
        d = dict(src_dict)
        settings = CoordinationRedisSettingsRequestSettings.from_dict(d.pop("settings"))




        coordination_redis_settings_request = cls(
            settings=settings,
        )


        coordination_redis_settings_request.additional_properties = d
        return coordination_redis_settings_request

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
