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
  from ..models.chat_completion_cached_content import ChatCompletionCachedContent





T = TypeVar("T", bound="ChatCompletionTextObject")



@_attrs_define
class ChatCompletionTextObject:
    """ 
        Attributes:
            type_ (Literal['text']):
            text (str):
            cache_control (ChatCompletionCachedContent | Unset):
     """

    type_: Literal['text']
    text: str
    cache_control: ChatCompletionCachedContent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_cached_content import ChatCompletionCachedContent
        type_ = self.type_

        text = self.text

        cache_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cache_control, Unset):
            cache_control = self.cache_control.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "text": text,
        })
        if cache_control is not UNSET:
            field_dict["cache_control"] = cache_control

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_cached_content import ChatCompletionCachedContent
        d = dict(src_dict)
        type_ = cast(Literal['text'] , d.pop("type"))
        if type_ != 'text':
            raise ValueError(f"type must match const 'text', got '{type_}'")

        text = d.pop("text")

        _cache_control = d.pop("cache_control", UNSET)
        cache_control: ChatCompletionCachedContent | Unset
        if isinstance(_cache_control,  Unset):
            cache_control = UNSET
        else:
            cache_control = ChatCompletionCachedContent.from_dict(_cache_control)




        chat_completion_text_object = cls(
            type_=type_,
            text=text,
            cache_control=cache_control,
        )


        chat_completion_text_object.additional_properties = d
        return chat_completion_text_object

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
