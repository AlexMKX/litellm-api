from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.scim_user_email import SCIMUserEmail
  from ..models.scim_user_group import SCIMUserGroup
  from ..models.scim_user_meta_type_0 import SCIMUserMetaType0
  from ..models.scim_user_name import SCIMUserName





T = TypeVar("T", bound="SCIMUser")



@_attrs_define
class SCIMUser:
    """ 
        Attributes:
            schemas (list[str]):
            id (None | str | Unset):
            external_id (None | str | Unset):
            meta (None | SCIMUserMetaType0 | Unset):
            user_name (None | str | Unset):
            name (None | SCIMUserName | Unset):
            display_name (None | str | Unset):
            active (bool | Unset):  Default: True.
            emails (list[SCIMUserEmail] | None | Unset):
            groups (list[SCIMUserGroup] | None | Unset):
     """

    schemas: list[str]
    id: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    meta: None | SCIMUserMetaType0 | Unset = UNSET
    user_name: None | str | Unset = UNSET
    name: None | SCIMUserName | Unset = UNSET
    display_name: None | str | Unset = UNSET
    active: bool | Unset = True
    emails: list[SCIMUserEmail] | None | Unset = UNSET
    groups: list[SCIMUserGroup] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.scim_user_name import SCIMUserName
        from ..models.scim_user_meta_type_0 import SCIMUserMetaType0
        from ..models.scim_user_email import SCIMUserEmail
        from ..models.scim_user_group import SCIMUserGroup
        schemas = self.schemas



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
        elif isinstance(self.meta, SCIMUserMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        name: dict[str, Any] | None | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        elif isinstance(self.name, SCIMUserName):
            name = self.name.to_dict()
        else:
            name = self.name

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        active = self.active

        emails: list[dict[str, Any]] | None | Unset
        if isinstance(self.emails, Unset):
            emails = UNSET
        elif isinstance(self.emails, list):
            emails = []
            for emails_type_0_item_data in self.emails:
                emails_type_0_item = emails_type_0_item_data.to_dict()
                emails.append(emails_type_0_item)


        else:
            emails = self.emails

        groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = groups_type_0_item_data.to_dict()
                groups.append(groups_type_0_item)


        else:
            groups = self.groups


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "schemas": schemas,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if meta is not UNSET:
            field_dict["meta"] = meta
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if active is not UNSET:
            field_dict["active"] = active
        if emails is not UNSET:
            field_dict["emails"] = emails
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scim_user_email import SCIMUserEmail
        from ..models.scim_user_group import SCIMUserGroup
        from ..models.scim_user_meta_type_0 import SCIMUserMetaType0
        from ..models.scim_user_name import SCIMUserName
        d = dict(src_dict)
        schemas = cast(list[str], d.pop("schemas"))


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


        def _parse_meta(data: object) -> None | SCIMUserMetaType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = SCIMUserMetaType0.from_dict(data)



                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SCIMUserMetaType0 | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))


        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("userName", UNSET))


        def _parse_name(data: object) -> None | SCIMUserName | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                name_type_0 = SCIMUserName.from_dict(data)



                return name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SCIMUserName | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))


        active = d.pop("active", UNSET)

        def _parse_emails(data: object) -> list[SCIMUserEmail] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                emails_type_0 = []
                _emails_type_0 = data
                for emails_type_0_item_data in (_emails_type_0):
                    emails_type_0_item = SCIMUserEmail.from_dict(emails_type_0_item_data)



                    emails_type_0.append(emails_type_0_item)

                return emails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SCIMUserEmail] | None | Unset, data)

        emails = _parse_emails(d.pop("emails", UNSET))


        def _parse_groups(data: object) -> list[SCIMUserGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in (_groups_type_0):
                    groups_type_0_item = SCIMUserGroup.from_dict(groups_type_0_item_data)



                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SCIMUserGroup] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))


        scim_user = cls(
            schemas=schemas,
            id=id,
            external_id=external_id,
            meta=meta,
            user_name=user_name,
            name=name,
            display_name=display_name,
            active=active,
            emails=emails,
            groups=groups,
        )


        scim_user.additional_properties = d
        return scim_user

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
