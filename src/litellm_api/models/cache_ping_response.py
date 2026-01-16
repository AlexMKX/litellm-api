from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cache_ping_response_health_check_cache_params_type_0 import CachePingResponseHealthCheckCacheParamsType0





T = TypeVar("T", bound="CachePingResponse")



@_attrs_define
class CachePingResponse:
    """ 
        Attributes:
            status (str):
            cache_type (str):
            ping_response (bool | None | Unset):
            set_cache_response (None | str | Unset):
            litellm_cache_params (None | str | Unset):
            health_check_cache_params (CachePingResponseHealthCheckCacheParamsType0 | None | Unset):
     """

    status: str
    cache_type: str
    ping_response: bool | None | Unset = UNSET
    set_cache_response: None | str | Unset = UNSET
    litellm_cache_params: None | str | Unset = UNSET
    health_check_cache_params: CachePingResponseHealthCheckCacheParamsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cache_ping_response_health_check_cache_params_type_0 import CachePingResponseHealthCheckCacheParamsType0
        status = self.status

        cache_type = self.cache_type

        ping_response: bool | None | Unset
        if isinstance(self.ping_response, Unset):
            ping_response = UNSET
        else:
            ping_response = self.ping_response

        set_cache_response: None | str | Unset
        if isinstance(self.set_cache_response, Unset):
            set_cache_response = UNSET
        else:
            set_cache_response = self.set_cache_response

        litellm_cache_params: None | str | Unset
        if isinstance(self.litellm_cache_params, Unset):
            litellm_cache_params = UNSET
        else:
            litellm_cache_params = self.litellm_cache_params

        health_check_cache_params: dict[str, Any] | None | Unset
        if isinstance(self.health_check_cache_params, Unset):
            health_check_cache_params = UNSET
        elif isinstance(self.health_check_cache_params, CachePingResponseHealthCheckCacheParamsType0):
            health_check_cache_params = self.health_check_cache_params.to_dict()
        else:
            health_check_cache_params = self.health_check_cache_params


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "cache_type": cache_type,
        })
        if ping_response is not UNSET:
            field_dict["ping_response"] = ping_response
        if set_cache_response is not UNSET:
            field_dict["set_cache_response"] = set_cache_response
        if litellm_cache_params is not UNSET:
            field_dict["litellm_cache_params"] = litellm_cache_params
        if health_check_cache_params is not UNSET:
            field_dict["health_check_cache_params"] = health_check_cache_params

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cache_ping_response_health_check_cache_params_type_0 import CachePingResponseHealthCheckCacheParamsType0
        d = dict(src_dict)
        status = d.pop("status")

        cache_type = d.pop("cache_type")

        def _parse_ping_response(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ping_response = _parse_ping_response(d.pop("ping_response", UNSET))


        def _parse_set_cache_response(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        set_cache_response = _parse_set_cache_response(d.pop("set_cache_response", UNSET))


        def _parse_litellm_cache_params(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        litellm_cache_params = _parse_litellm_cache_params(d.pop("litellm_cache_params", UNSET))


        def _parse_health_check_cache_params(data: object) -> CachePingResponseHealthCheckCacheParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                health_check_cache_params_type_0 = CachePingResponseHealthCheckCacheParamsType0.from_dict(data)



                return health_check_cache_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CachePingResponseHealthCheckCacheParamsType0 | None | Unset, data)

        health_check_cache_params = _parse_health_check_cache_params(d.pop("health_check_cache_params", UNSET))


        cache_ping_response = cls(
            status=status,
            cache_type=cache_type,
            ping_response=ping_response,
            set_cache_response=set_cache_response,
            litellm_cache_params=litellm_cache_params,
            health_check_cache_params=health_check_cache_params,
        )


        cache_ping_response.additional_properties = d
        return cache_ping_response

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
