from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.chat_completion_image_url_object import ChatCompletionImageUrlObject





T = TypeVar("T", bound="ChatCompletionImageObject")



@_attrs_define
class ChatCompletionImageObject:
    """ 
        Attributes:
            type_ (Literal['image_url']):
            image_url (ChatCompletionImageUrlObject | str):
     """

    type_: Literal['image_url']
    image_url: ChatCompletionImageUrlObject | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_image_url_object import ChatCompletionImageUrlObject
        type_ = self.type_

        image_url: dict[str, Any] | str
        if isinstance(self.image_url, ChatCompletionImageUrlObject):
            image_url = self.image_url.to_dict()
        else:
            image_url = self.image_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "image_url": image_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_image_url_object import ChatCompletionImageUrlObject
        d = dict(src_dict)
        type_ = cast(Literal['image_url'] , d.pop("type"))
        if type_ != 'image_url':
            raise ValueError(f"type must match const 'image_url', got '{type_}'")

        def _parse_image_url(data: object) -> ChatCompletionImageUrlObject | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_url_type_1 = ChatCompletionImageUrlObject.from_dict(data)



                return image_url_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatCompletionImageUrlObject | str, data)

        image_url = _parse_image_url(d.pop("image_url"))


        chat_completion_image_object = cls(
            type_=type_,
            image_url=image_url,
        )


        chat_completion_image_object.additional_properties = d
        return chat_completion_image_object

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
