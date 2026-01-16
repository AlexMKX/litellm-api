from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.public_model_hub_info_useful_links_type_0 import PublicModelHubInfoUsefulLinksType0





T = TypeVar("T", bound="PublicModelHubInfo")



@_attrs_define
class PublicModelHubInfo:
    """ 
        Attributes:
            docs_title (str):
            custom_docs_description (None | str):
            litellm_version (str):
            useful_links (None | PublicModelHubInfoUsefulLinksType0):
     """

    docs_title: str
    custom_docs_description: None | str
    litellm_version: str
    useful_links: None | PublicModelHubInfoUsefulLinksType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.public_model_hub_info_useful_links_type_0 import PublicModelHubInfoUsefulLinksType0
        docs_title = self.docs_title

        custom_docs_description: None | str
        custom_docs_description = self.custom_docs_description

        litellm_version = self.litellm_version

        useful_links: dict[str, Any] | None
        if isinstance(self.useful_links, PublicModelHubInfoUsefulLinksType0):
            useful_links = self.useful_links.to_dict()
        else:
            useful_links = self.useful_links


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "docs_title": docs_title,
            "custom_docs_description": custom_docs_description,
            "litellm_version": litellm_version,
            "useful_links": useful_links,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_model_hub_info_useful_links_type_0 import PublicModelHubInfoUsefulLinksType0
        d = dict(src_dict)
        docs_title = d.pop("docs_title")

        def _parse_custom_docs_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        custom_docs_description = _parse_custom_docs_description(d.pop("custom_docs_description"))


        litellm_version = d.pop("litellm_version")

        def _parse_useful_links(data: object) -> None | PublicModelHubInfoUsefulLinksType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                useful_links_type_0 = PublicModelHubInfoUsefulLinksType0.from_dict(data)



                return useful_links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublicModelHubInfoUsefulLinksType0, data)

        useful_links = _parse_useful_links(d.pop("useful_links"))


        public_model_hub_info = cls(
            docs_title=docs_title,
            custom_docs_description=custom_docs_description,
            litellm_version=litellm_version,
            useful_links=useful_links,
        )


        public_model_hub_info.additional_properties = d
        return public_model_hub_info

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
