from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SCIMUserName")



@_attrs_define
class SCIMUserName:
    """ 
        Attributes:
            family_name (None | str | Unset):
            given_name (None | str | Unset):
            formatted (None | str | Unset):
            middle_name (None | str | Unset):
            honorific_prefix (None | str | Unset):
            honorific_suffix (None | str | Unset):
     """

    family_name: None | str | Unset = UNSET
    given_name: None | str | Unset = UNSET
    formatted: None | str | Unset = UNSET
    middle_name: None | str | Unset = UNSET
    honorific_prefix: None | str | Unset = UNSET
    honorific_suffix: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        family_name: None | str | Unset
        if isinstance(self.family_name, Unset):
            family_name = UNSET
        else:
            family_name = self.family_name

        given_name: None | str | Unset
        if isinstance(self.given_name, Unset):
            given_name = UNSET
        else:
            given_name = self.given_name

        formatted: None | str | Unset
        if isinstance(self.formatted, Unset):
            formatted = UNSET
        else:
            formatted = self.formatted

        middle_name: None | str | Unset
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        honorific_prefix: None | str | Unset
        if isinstance(self.honorific_prefix, Unset):
            honorific_prefix = UNSET
        else:
            honorific_prefix = self.honorific_prefix

        honorific_suffix: None | str | Unset
        if isinstance(self.honorific_suffix, Unset):
            honorific_suffix = UNSET
        else:
            honorific_suffix = self.honorific_suffix


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if given_name is not UNSET:
            field_dict["givenName"] = given_name
        if formatted is not UNSET:
            field_dict["formatted"] = formatted
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if honorific_prefix is not UNSET:
            field_dict["honorificPrefix"] = honorific_prefix
        if honorific_suffix is not UNSET:
            field_dict["honorificSuffix"] = honorific_suffix

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_family_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        family_name = _parse_family_name(d.pop("familyName", UNSET))


        def _parse_given_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        given_name = _parse_given_name(d.pop("givenName", UNSET))


        def _parse_formatted(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        formatted = _parse_formatted(d.pop("formatted", UNSET))


        def _parse_middle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        middle_name = _parse_middle_name(d.pop("middleName", UNSET))


        def _parse_honorific_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        honorific_prefix = _parse_honorific_prefix(d.pop("honorificPrefix", UNSET))


        def _parse_honorific_suffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        honorific_suffix = _parse_honorific_suffix(d.pop("honorificSuffix", UNSET))


        scim_user_name = cls(
            family_name=family_name,
            given_name=given_name,
            formatted=formatted,
            middle_name=middle_name,
            honorific_prefix=honorific_prefix,
            honorific_suffix=honorific_suffix,
        )


        scim_user_name.additional_properties = d
        return scim_user_name

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
