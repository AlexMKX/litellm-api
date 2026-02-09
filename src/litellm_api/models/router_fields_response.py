from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.router_fields_response_routing_strategy_descriptions import RouterFieldsResponseRoutingStrategyDescriptions
  from ..models.router_settings_field import RouterSettingsField





T = TypeVar("T", bound="RouterFieldsResponse")



@_attrs_define
class RouterFieldsResponse:
    """ 
        Attributes:
            fields (list[RouterSettingsField]): List of all configurable router settings with metadata (without field
                values)
            routing_strategy_descriptions (RouterFieldsResponseRoutingStrategyDescriptions): Descriptions for each routing
                strategy option
     """

    fields: list[RouterSettingsField]
    routing_strategy_descriptions: RouterFieldsResponseRoutingStrategyDescriptions
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.router_settings_field import RouterSettingsField
        from ..models.router_fields_response_routing_strategy_descriptions import RouterFieldsResponseRoutingStrategyDescriptions
        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)



        routing_strategy_descriptions = self.routing_strategy_descriptions.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "fields": fields,
            "routing_strategy_descriptions": routing_strategy_descriptions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.router_fields_response_routing_strategy_descriptions import RouterFieldsResponseRoutingStrategyDescriptions
        from ..models.router_settings_field import RouterSettingsField
        d = dict(src_dict)
        fields = []
        _fields = d.pop("fields")
        for fields_item_data in (_fields):
            fields_item = RouterSettingsField.from_dict(fields_item_data)



            fields.append(fields_item)


        routing_strategy_descriptions = RouterFieldsResponseRoutingStrategyDescriptions.from_dict(d.pop("routing_strategy_descriptions"))




        router_fields_response = cls(
            fields=fields,
            routing_strategy_descriptions=routing_strategy_descriptions,
        )


        router_fields_response.additional_properties = d
        return router_fields_response

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
