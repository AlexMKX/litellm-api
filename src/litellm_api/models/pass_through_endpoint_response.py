from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.pass_through_generic_endpoint import PassThroughGenericEndpoint





T = TypeVar("T", bound="PassThroughEndpointResponse")



@_attrs_define
class PassThroughEndpointResponse:
    """ 
        Attributes:
            endpoints (list[PassThroughGenericEndpoint]):
     """

    endpoints: list[PassThroughGenericEndpoint]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.pass_through_generic_endpoint import PassThroughGenericEndpoint
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
        from ..models.pass_through_generic_endpoint import PassThroughGenericEndpoint
        d = dict(src_dict)
        endpoints = []
        _endpoints = d.pop("endpoints")
        for endpoints_item_data in (_endpoints):
            endpoints_item = PassThroughGenericEndpoint.from_dict(endpoints_item_data)



            endpoints.append(endpoints_item)


        pass_through_endpoint_response = cls(
            endpoints=endpoints,
        )


        pass_through_endpoint_response.additional_properties = d
        return pass_through_endpoint_response

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
