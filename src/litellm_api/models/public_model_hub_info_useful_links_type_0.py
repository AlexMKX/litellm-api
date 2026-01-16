from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.public_model_hub_info_useful_links_type_0_additional_property_type_1 import PublicModelHubInfoUsefulLinksType0AdditionalPropertyType1





T = TypeVar("T", bound="PublicModelHubInfoUsefulLinksType0")



@_attrs_define
class PublicModelHubInfoUsefulLinksType0:
    """ 
     """

    additional_properties: dict[str, PublicModelHubInfoUsefulLinksType0AdditionalPropertyType1 | str] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.public_model_hub_info_useful_links_type_0_additional_property_type_1 import PublicModelHubInfoUsefulLinksType0AdditionalPropertyType1
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            
            if isinstance(prop, PublicModelHubInfoUsefulLinksType0AdditionalPropertyType1):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_model_hub_info_useful_links_type_0_additional_property_type_1 import PublicModelHubInfoUsefulLinksType0AdditionalPropertyType1
        d = dict(src_dict)
        public_model_hub_info_useful_links_type_0 = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            def _parse_additional_property(data: object) -> PublicModelHubInfoUsefulLinksType0AdditionalPropertyType1 | str:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_1 = PublicModelHubInfoUsefulLinksType0AdditionalPropertyType1.from_dict(data)



                    return additional_property_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(PublicModelHubInfoUsefulLinksType0AdditionalPropertyType1 | str, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        public_model_hub_info_useful_links_type_0.additional_properties = additional_properties
        return public_model_hub_info_useful_links_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> PublicModelHubInfoUsefulLinksType0AdditionalPropertyType1 | str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: PublicModelHubInfoUsefulLinksType0AdditionalPropertyType1 | str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
