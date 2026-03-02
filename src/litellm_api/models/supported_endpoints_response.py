from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.supported_endpoint import SupportedEndpoint





T = TypeVar("T", bound="SupportedEndpointsResponse")



@_attrs_define
class SupportedEndpointsResponse:
    """ 
        Attributes:
            endpoints (list[SupportedEndpoint]):
     """

    endpoints: list[SupportedEndpoint]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.supported_endpoint import SupportedEndpoint
        endpoints = []
        for endpoints_item_data in self.endpoints:
            endpoints_item = endpoints_item_data.to_dict()
            endpoints.append(endpoints_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "endpoints": endpoints,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.supported_endpoint import SupportedEndpoint
        d = dict(src_dict)
        endpoints = []
        _endpoints = d.pop("endpoints")
        for endpoints_item_data in (_endpoints):
            endpoints_item = SupportedEndpoint.from_dict(endpoints_item_data)



            endpoints.append(endpoints_item)


        supported_endpoints_response = cls(
            endpoints=endpoints,
        )


        supported_endpoints_response.additional_properties = d
        return supported_endpoints_response

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
