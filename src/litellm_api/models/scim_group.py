from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.scim_group_meta_type_0 import SCIMGroupMetaType0
  from ..models.scim_member import SCIMMember





T = TypeVar("T", bound="SCIMGroup")



@_attrs_define
class SCIMGroup:
    """ 
        Attributes:
            schemas (list[str]):
            display_name (str):
            id (None | str | Unset):
            external_id (None | str | Unset):
            meta (None | SCIMGroupMetaType0 | Unset):
            members (list[SCIMMember] | None | Unset):
     """

    schemas: list[str]
    display_name: str
    id: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    meta: None | SCIMGroupMetaType0 | Unset = UNSET
    members: list[SCIMMember] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.scim_member import SCIMMember
        from ..models.scim_group_meta_type_0 import SCIMGroupMetaType0
        schemas = self.schemas



        display_name = self.display_name

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, SCIMGroupMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        members: list[dict[str, Any]] | None | Unset
        if isinstance(self.members, Unset):
            members = UNSET
        elif isinstance(self.members, list):
            members = []
            for members_type_0_item_data in self.members:
                members_type_0_item = members_type_0_item_data.to_dict()
                members.append(members_type_0_item)


        else:
            members = self.members


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "schemas": schemas,
            "displayName": display_name,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if meta is not UNSET:
            field_dict["meta"] = meta
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scim_group_meta_type_0 import SCIMGroupMetaType0
        from ..models.scim_member import SCIMMember
        d = dict(src_dict)
        schemas = cast(list[str], d.pop("schemas"))


        display_name = d.pop("displayName")

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))


        def _parse_meta(data: object) -> None | SCIMGroupMetaType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = SCIMGroupMetaType0.from_dict(data)



                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SCIMGroupMetaType0 | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))


        def _parse_members(data: object) -> list[SCIMMember] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                members_type_0 = []
                _members_type_0 = data
                for members_type_0_item_data in (_members_type_0):
                    members_type_0_item = SCIMMember.from_dict(members_type_0_item_data)



                    members_type_0.append(members_type_0_item)

                return members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SCIMMember] | None | Unset, data)

        members = _parse_members(d.pop("members", UNSET))


        scim_group = cls(
            schemas=schemas,
            display_name=display_name,
            id=id,
            external_id=external_id,
            meta=meta,
            members=members,
        )


        scim_group.additional_properties = d
        return scim_group

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
