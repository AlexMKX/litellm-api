from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.cache_test_request_cache_settings import CacheTestRequestCacheSettings





T = TypeVar("T", bound="CacheTestRequest")



@_attrs_define
class CacheTestRequest:
    """ 
        Attributes:
            cache_settings (CacheTestRequestCacheSettings): Cache settings to test connection with
     """

    cache_settings: CacheTestRequestCacheSettings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cache_test_request_cache_settings import CacheTestRequestCacheSettings
        cache_settings = self.cache_settings.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cache_settings": cache_settings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cache_test_request_cache_settings import CacheTestRequestCacheSettings
        d = dict(src_dict)
        cache_settings = CacheTestRequestCacheSettings.from_dict(d.pop("cache_settings"))




        cache_test_request = cls(
            cache_settings=cache_settings,
        )


        cache_test_request.additional_properties = d
        return cache_test_request

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
