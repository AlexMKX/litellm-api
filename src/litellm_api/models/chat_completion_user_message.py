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
  from ..models.chat_completion_audio_object import ChatCompletionAudioObject
  from ..models.chat_completion_cached_content import ChatCompletionCachedContent
  from ..models.chat_completion_document_object import ChatCompletionDocumentObject
  from ..models.chat_completion_file_object import ChatCompletionFileObject
  from ..models.chat_completion_image_object import ChatCompletionImageObject
  from ..models.chat_completion_text_object import ChatCompletionTextObject
  from ..models.chat_completion_video_object import ChatCompletionVideoObject





T = TypeVar("T", bound="ChatCompletionUserMessage")



@_attrs_define
class ChatCompletionUserMessage:
    """ 
        Attributes:
            role (Literal['user']):
            content (list[ChatCompletionAudioObject | ChatCompletionDocumentObject | ChatCompletionFileObject |
                ChatCompletionImageObject | ChatCompletionTextObject | ChatCompletionVideoObject] | str):
            cache_control (ChatCompletionCachedContent | Unset):
     """

    role: Literal['user']
    content: list[ChatCompletionAudioObject | ChatCompletionDocumentObject | ChatCompletionFileObject | ChatCompletionImageObject | ChatCompletionTextObject | ChatCompletionVideoObject] | str
    cache_control: ChatCompletionCachedContent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_text_object import ChatCompletionTextObject
        from ..models.chat_completion_cached_content import ChatCompletionCachedContent
        from ..models.chat_completion_document_object import ChatCompletionDocumentObject
        from ..models.chat_completion_audio_object import ChatCompletionAudioObject
        from ..models.chat_completion_image_object import ChatCompletionImageObject
        from ..models.chat_completion_file_object import ChatCompletionFileObject
        from ..models.chat_completion_video_object import ChatCompletionVideoObject
        role = self.role

        content: list[dict[str, Any]] | str
        if isinstance(self.content, list):
            content = []
            for content_type_1_item_data in self.content:
                content_type_1_item: dict[str, Any]
                if isinstance(content_type_1_item_data, ChatCompletionTextObject):
                    content_type_1_item = content_type_1_item_data.to_dict()
                elif isinstance(content_type_1_item_data, ChatCompletionImageObject):
                    content_type_1_item = content_type_1_item_data.to_dict()
                elif isinstance(content_type_1_item_data, ChatCompletionAudioObject):
                    content_type_1_item = content_type_1_item_data.to_dict()
                elif isinstance(content_type_1_item_data, ChatCompletionDocumentObject):
                    content_type_1_item = content_type_1_item_data.to_dict()
                elif isinstance(content_type_1_item_data, ChatCompletionVideoObject):
                    content_type_1_item = content_type_1_item_data.to_dict()
                else:
                    content_type_1_item = content_type_1_item_data.to_dict()

                content.append(content_type_1_item)


        else:
            content = self.content

        cache_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cache_control, Unset):
            cache_control = self.cache_control.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "role": role,
            "content": content,
        })
        if cache_control is not UNSET:
            field_dict["cache_control"] = cache_control

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_audio_object import ChatCompletionAudioObject
        from ..models.chat_completion_cached_content import ChatCompletionCachedContent
        from ..models.chat_completion_document_object import ChatCompletionDocumentObject
        from ..models.chat_completion_file_object import ChatCompletionFileObject
        from ..models.chat_completion_image_object import ChatCompletionImageObject
        from ..models.chat_completion_text_object import ChatCompletionTextObject
        from ..models.chat_completion_video_object import ChatCompletionVideoObject
        d = dict(src_dict)
        role = cast(Literal['user'] , d.pop("role"))
        if role != 'user':
            raise ValueError(f"role must match const 'user', got '{role}'")

        def _parse_content(data: object) -> list[ChatCompletionAudioObject | ChatCompletionDocumentObject | ChatCompletionFileObject | ChatCompletionImageObject | ChatCompletionTextObject | ChatCompletionVideoObject] | str:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_type_1 = []
                _content_type_1 = data
                for content_type_1_item_data in (_content_type_1):
                    def _parse_content_type_1_item(data: object) -> ChatCompletionAudioObject | ChatCompletionDocumentObject | ChatCompletionFileObject | ChatCompletionImageObject | ChatCompletionTextObject | ChatCompletionVideoObject:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            content_type_1_item_type_0 = ChatCompletionTextObject.from_dict(data)



                            return content_type_1_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            content_type_1_item_type_1 = ChatCompletionImageObject.from_dict(data)



                            return content_type_1_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            content_type_1_item_type_2 = ChatCompletionAudioObject.from_dict(data)



                            return content_type_1_item_type_2
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            content_type_1_item_type_3 = ChatCompletionDocumentObject.from_dict(data)



                            return content_type_1_item_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            content_type_1_item_type_4 = ChatCompletionVideoObject.from_dict(data)



                            return content_type_1_item_type_4
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        content_type_1_item_type_5 = ChatCompletionFileObject.from_dict(data)



                        return content_type_1_item_type_5

                    content_type_1_item = _parse_content_type_1_item(content_type_1_item_data)

                    content_type_1.append(content_type_1_item)

                return content_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ChatCompletionAudioObject | ChatCompletionDocumentObject | ChatCompletionFileObject | ChatCompletionImageObject | ChatCompletionTextObject | ChatCompletionVideoObject] | str, data)

        content = _parse_content(d.pop("content"))


        _cache_control = d.pop("cache_control", UNSET)
        cache_control: ChatCompletionCachedContent | Unset
        if isinstance(_cache_control,  Unset):
            cache_control = UNSET
        else:
            cache_control = ChatCompletionCachedContent.from_dict(_cache_control)




        chat_completion_user_message = cls(
            role=role,
            content=content,
            cache_control=cache_control,
        )


        chat_completion_user_message.additional_properties = d
        return chat_completion_user_message

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
