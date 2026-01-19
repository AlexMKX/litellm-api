from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.scim_group import SCIMGroup
  from ..models.scim_user import SCIMUser





T = TypeVar("T", bound="SCIMListResponse")



@_attrs_define
class SCIMListResponse:
    """ 
        Attributes:
            total_results (int):
            resources (list[SCIMGroup] | list[SCIMUser]):
            schemas (list[str] | Unset):
            start_index (int | None | Unset):  Default: 1.
            items_per_page (int | None | Unset):  Default: 10.
     """

    total_results: int
    resources: list[SCIMGroup] | list[SCIMUser]
    schemas: list[str] | Unset = UNSET
    start_index: int | None | Unset = 1
    items_per_page: int | None | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.scim_user import SCIMUser
        from ..models.scim_group import SCIMGroup
        total_results = self.total_results

        resources: list[dict[str, Any]]
        if isinstance(self.resources, list):
            resources = []
            for resources_type_0_item_data in self.resources:
                resources_type_0_item = resources_type_0_item_data.to_dict()
                resources.append(resources_type_0_item)


        else:
            resources = []
            for resources_type_1_item_data in self.resources:
                resources_type_1_item = resources_type_1_item_data.to_dict()
                resources.append(resources_type_1_item)




        schemas: list[str] | Unset = UNSET
        if not isinstance(self.schemas, Unset):
            schemas = self.schemas



        start_index: int | None | Unset
        if isinstance(self.start_index, Unset):
            start_index = UNSET
        else:
            start_index = self.start_index

        items_per_page: int | None | Unset
        if isinstance(self.items_per_page, Unset):
            items_per_page = UNSET
        else:
            items_per_page = self.items_per_page


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "totalResults": total_results,
            "Resources": resources,
        })
        if schemas is not UNSET:
            field_dict["schemas"] = schemas
        if start_index is not UNSET:
            field_dict["startIndex"] = start_index
        if items_per_page is not UNSET:
            field_dict["itemsPerPage"] = items_per_page

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scim_group import SCIMGroup
        from ..models.scim_user import SCIMUser
        d = dict(src_dict)
        total_results = d.pop("totalResults")

        def _parse_resources(data: object) -> list[SCIMGroup] | list[SCIMUser]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resources_type_0 = []
                _resources_type_0 = data
                for resources_type_0_item_data in (_resources_type_0):
                    resources_type_0_item = SCIMUser.from_dict(resources_type_0_item_data)



                    resources_type_0.append(resources_type_0_item)

                return resources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            resources_type_1 = []
            _resources_type_1 = data
            for resources_type_1_item_data in (_resources_type_1):
                resources_type_1_item = SCIMGroup.from_dict(resources_type_1_item_data)



                resources_type_1.append(resources_type_1_item)

            return resources_type_1

        resources = _parse_resources(d.pop("Resources"))


        schemas = cast(list[str], d.pop("schemas", UNSET))


        def _parse_start_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        start_index = _parse_start_index(d.pop("startIndex", UNSET))


        def _parse_items_per_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        items_per_page = _parse_items_per_page(d.pop("itemsPerPage", UNSET))


        scim_list_response = cls(
            total_results=total_results,
            resources=resources,
            schemas=schemas,
            start_index=start_index,
            items_per_page=items_per_page,
        )


        scim_list_response.additional_properties = d
        return scim_list_response

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
