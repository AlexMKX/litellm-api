from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChatCompletionAnnotationURLCitation")



@_attrs_define
class ChatCompletionAnnotationURLCitation:
    """ 
        Attributes:
            end_index (int | Unset):
            start_index (int | Unset):
            title (str | Unset):
            url (str | Unset):
     """

    end_index: int | Unset = UNSET
    start_index: int | Unset = UNSET
    title: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        end_index = self.end_index

        start_index = self.start_index

        title = self.title

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end_index is not UNSET:
            field_dict["end_index"] = end_index
        if start_index is not UNSET:
            field_dict["start_index"] = start_index
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_index = d.pop("end_index", UNSET)

        start_index = d.pop("start_index", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        chat_completion_annotation_url_citation = cls(
            end_index=end_index,
            start_index=start_index,
            title=title,
            url=url,
        )


        chat_completion_annotation_url_citation.additional_properties = d
        return chat_completion_annotation_url_citation

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
