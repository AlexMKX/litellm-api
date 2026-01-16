from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.chat_completion_annotation_url_citation import ChatCompletionAnnotationURLCitation





T = TypeVar("T", bound="ChatCompletionAnnotation")



@_attrs_define
class ChatCompletionAnnotation:
    """ 
        Attributes:
            type_ (Literal['url_citation'] | Unset):
            url_citation (ChatCompletionAnnotationURLCitation | Unset):
     """

    type_: Literal['url_citation'] | Unset = UNSET
    url_citation: ChatCompletionAnnotationURLCitation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_annotation_url_citation import ChatCompletionAnnotationURLCitation
        type_ = self.type_

        url_citation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.url_citation, Unset):
            url_citation = self.url_citation.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url_citation is not UNSET:
            field_dict["url_citation"] = url_citation

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_annotation_url_citation import ChatCompletionAnnotationURLCitation
        d = dict(src_dict)
        type_ = cast(Literal['url_citation'] | Unset , d.pop("type", UNSET))
        if type_ != 'url_citation'and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'url_citation', got '{type_}'")

        _url_citation = d.pop("url_citation", UNSET)
        url_citation: ChatCompletionAnnotationURLCitation | Unset
        if isinstance(_url_citation,  Unset):
            url_citation = UNSET
        else:
            url_citation = ChatCompletionAnnotationURLCitation.from_dict(_url_citation)




        chat_completion_annotation = cls(
            type_=type_,
            url_citation=url_citation,
        )


        chat_completion_annotation.additional_properties = d
        return chat_completion_annotation

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
