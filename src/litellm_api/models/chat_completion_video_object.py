from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.chat_completion_video_url_object import ChatCompletionVideoUrlObject





T = TypeVar("T", bound="ChatCompletionVideoObject")



@_attrs_define
class ChatCompletionVideoObject:
    """ 
        Attributes:
            type_ (Literal['video_url']):
            video_url (ChatCompletionVideoUrlObject | str):
     """

    type_: Literal['video_url']
    video_url: ChatCompletionVideoUrlObject | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_video_url_object import ChatCompletionVideoUrlObject
        type_ = self.type_

        video_url: dict[str, Any] | str
        if isinstance(self.video_url, ChatCompletionVideoUrlObject):
            video_url = self.video_url.to_dict()
        else:
            video_url = self.video_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "video_url": video_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_video_url_object import ChatCompletionVideoUrlObject
        d = dict(src_dict)
        type_ = cast(Literal['video_url'] , d.pop("type"))
        if type_ != 'video_url':
            raise ValueError(f"type must match const 'video_url', got '{type_}'")

        def _parse_video_url(data: object) -> ChatCompletionVideoUrlObject | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                video_url_type_1 = ChatCompletionVideoUrlObject.from_dict(data)



                return video_url_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatCompletionVideoUrlObject | str, data)

        video_url = _parse_video_url(d.pop("video_url"))


        chat_completion_video_object = cls(
            type_=type_,
            video_url=video_url,
        )


        chat_completion_video_object.additional_properties = d
        return chat_completion_video_object

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
