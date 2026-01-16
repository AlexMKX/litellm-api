from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Skill")



@_attrs_define
class Skill:
    """ Represents a skill from the Anthropic Skills API

        Attributes:
            id (str):
            created_at (str):
            source (str):
            updated_at (str):
            display_title (None | str | Unset):
            latest_version (None | str | Unset):
            type_ (str | Unset):  Default: 'skill'.
     """

    id: str
    created_at: str
    source: str
    updated_at: str
    display_title: None | str | Unset = UNSET
    latest_version: None | str | Unset = UNSET
    type_: str | Unset = 'skill'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at

        source = self.source

        updated_at = self.updated_at

        display_title: None | str | Unset
        if isinstance(self.display_title, Unset):
            display_title = UNSET
        else:
            display_title = self.display_title

        latest_version: None | str | Unset
        if isinstance(self.latest_version, Unset):
            latest_version = UNSET
        else:
            latest_version = self.latest_version

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "created_at": created_at,
            "source": source,
            "updated_at": updated_at,
        })
        if display_title is not UNSET:
            field_dict["display_title"] = display_title
        if latest_version is not UNSET:
            field_dict["latest_version"] = latest_version
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("created_at")

        source = d.pop("source")

        updated_at = d.pop("updated_at")

        def _parse_display_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_title = _parse_display_title(d.pop("display_title", UNSET))


        def _parse_latest_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_version = _parse_latest_version(d.pop("latest_version", UNSET))


        type_ = d.pop("type", UNSET)

        skill = cls(
            id=id,
            created_at=created_at,
            source=source,
            updated_at=updated_at,
            display_title=display_title,
            latest_version=latest_version,
            type_=type_,
        )


        skill.additional_properties = d
        return skill

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
