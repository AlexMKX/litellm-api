from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.plugin_author import PluginAuthor
  from ..models.plugin_list_item_source import PluginListItemSource





T = TypeVar("T", bound="PluginListItem")



@_attrs_define
class PluginListItem:
    """ Plugin item in list responses.

        Attributes:
            id (str):
            name (str):
            version (None | str):
            description (None | str):
            source (PluginListItemSource):
            enabled (bool):
            created_at (None | str):
            updated_at (None | str):
            author (None | PluginAuthor | Unset):
            homepage (None | str | Unset):
            keywords (list[str] | None | Unset):
            category (None | str | Unset):
     """

    id: str
    name: str
    version: None | str
    description: None | str
    source: PluginListItemSource
    enabled: bool
    created_at: None | str
    updated_at: None | str
    author: None | PluginAuthor | Unset = UNSET
    homepage: None | str | Unset = UNSET
    keywords: list[str] | None | Unset = UNSET
    category: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.plugin_author import PluginAuthor
        from ..models.plugin_list_item_source import PluginListItemSource
        id = self.id

        name = self.name

        version: None | str
        version = self.version

        description: None | str
        description = self.description

        source = self.source.to_dict()

        enabled = self.enabled

        created_at: None | str
        created_at = self.created_at

        updated_at: None | str
        updated_at = self.updated_at

        author: dict[str, Any] | None | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(self.author, PluginAuthor):
            author = self.author.to_dict()
        else:
            author = self.author

        homepage: None | str | Unset
        if isinstance(self.homepage, Unset):
            homepage = UNSET
        else:
            homepage = self.homepage

        keywords: list[str] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords


        else:
            keywords = self.keywords

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "version": version,
            "description": description,
            "source": source,
            "enabled": enabled,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if author is not UNSET:
            field_dict["author"] = author
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_author import PluginAuthor
        from ..models.plugin_list_item_source import PluginListItemSource
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        version = _parse_version(d.pop("version"))


        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        source = PluginListItemSource.from_dict(d.pop("source"))




        enabled = d.pop("enabled")

        def _parse_created_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_at = _parse_created_at(d.pop("created_at"))


        def _parse_updated_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))


        def _parse_author(data: object) -> None | PluginAuthor | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                author_type_0 = PluginAuthor.from_dict(data)



                return author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PluginAuthor | Unset, data)

        author = _parse_author(d.pop("author", UNSET))


        def _parse_homepage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        homepage = _parse_homepage(d.pop("homepage", UNSET))


        def _parse_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = cast(list[str], data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))


        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        plugin_list_item = cls(
            id=id,
            name=name,
            version=version,
            description=description,
            source=source,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
            author=author,
            homepage=homepage,
            keywords=keywords,
            category=category,
        )


        plugin_list_item.additional_properties = d
        return plugin_list_item

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
