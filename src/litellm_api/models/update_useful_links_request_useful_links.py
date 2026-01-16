from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.update_useful_links_request_useful_links_additional_property_type_1 import UpdateUsefulLinksRequestUsefulLinksAdditionalPropertyType1





T = TypeVar("T", bound="UpdateUsefulLinksRequestUsefulLinks")



@_attrs_define
class UpdateUsefulLinksRequestUsefulLinks:
    """ 
     """

    additional_properties: dict[str, str | UpdateUsefulLinksRequestUsefulLinksAdditionalPropertyType1] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_useful_links_request_useful_links_additional_property_type_1 import UpdateUsefulLinksRequestUsefulLinksAdditionalPropertyType1
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            
            if isinstance(prop, UpdateUsefulLinksRequestUsefulLinksAdditionalPropertyType1):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_useful_links_request_useful_links_additional_property_type_1 import UpdateUsefulLinksRequestUsefulLinksAdditionalPropertyType1
        d = dict(src_dict)
        update_useful_links_request_useful_links = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            def _parse_additional_property(data: object) -> str | UpdateUsefulLinksRequestUsefulLinksAdditionalPropertyType1:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_1 = UpdateUsefulLinksRequestUsefulLinksAdditionalPropertyType1.from_dict(data)



                    return additional_property_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(str | UpdateUsefulLinksRequestUsefulLinksAdditionalPropertyType1, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        update_useful_links_request_useful_links.additional_properties = additional_properties
        return update_useful_links_request_useful_links

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str | UpdateUsefulLinksRequestUsefulLinksAdditionalPropertyType1:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str | UpdateUsefulLinksRequestUsefulLinksAdditionalPropertyType1) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
