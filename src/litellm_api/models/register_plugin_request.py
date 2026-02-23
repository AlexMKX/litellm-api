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
  from ..models.register_plugin_request_source import RegisterPluginRequestSource





T = TypeVar("T", bound="RegisterPluginRequest")



@_attrs_define
class RegisterPluginRequest:
    """ Request body for registering a plugin in the marketplace.

    LiteLLM acts as a registry/discovery layer. Plugins are hosted on
    GitHub/GitLab/Bitbucket and referenced by their git source.

        Attributes:
            name (str): Plugin name (kebab-case, e.g., 'my-plugin')
            source (RegisterPluginRequestSource): Git source reference. Supported formats:
                - GitHub: {'source': 'github', 'repo': 'org/repo'}
                - Git URL: {'source': 'url', 'url': 'https://github.com/org/repo.git'}
            version (None | str | Unset): Semantic version Default: '1.0.0'.
            description (None | str | Unset): Plugin description
            author (None | PluginAuthor | Unset): Plugin author
            homepage (None | str | Unset): Plugin homepage URL
            keywords (list[str] | None | Unset): Search keywords
            category (None | str | Unset): Plugin category
     """

    name: str
    source: RegisterPluginRequestSource
    version: None | str | Unset = '1.0.0'
    description: None | str | Unset = UNSET
    author: None | PluginAuthor | Unset = UNSET
    homepage: None | str | Unset = UNSET
    keywords: list[str] | None | Unset = UNSET
    category: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.register_plugin_request_source import RegisterPluginRequestSource
        from ..models.plugin_author import PluginAuthor
        name = self.name

        source = self.source.to_dict()

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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
            "name": name,
            "source": source,
        })
        if version is not UNSET:
            field_dict["version"] = version
        if description is not UNSET:
            field_dict["description"] = description
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
        from ..models.register_plugin_request_source import RegisterPluginRequestSource
        d = dict(src_dict)
        name = d.pop("name")

        source = RegisterPluginRequestSource.from_dict(d.pop("source"))




        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


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


        register_plugin_request = cls(
            name=name,
            source=source,
            version=version,
            description=description,
            author=author,
            homepage=homepage,
            keywords=keywords,
            category=category,
        )


        register_plugin_request.additional_properties = d
        return register_plugin_request

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
