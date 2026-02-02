from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.message_role import MessageRole
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chat_completion_annotation import ChatCompletionAnnotation
  from ..models.chat_completion_audio_response import ChatCompletionAudioResponse
  from ..models.chat_completion_message_tool_call import ChatCompletionMessageToolCall
  from ..models.chat_completion_redacted_thinking_block import ChatCompletionRedactedThinkingBlock
  from ..models.chat_completion_thinking_block import ChatCompletionThinkingBlock
  from ..models.function_call import FunctionCall
  from ..models.image_url_list_item import ImageURLListItem
  from ..models.message_provider_specific_fields_type_0 import MessageProviderSpecificFieldsType0





T = TypeVar("T", bound="Message")



@_attrs_define
class Message:
    """ 
        Attributes:
            content (None | str):
            role (MessageRole):
            tool_calls (list[ChatCompletionMessageToolCall] | None):
            function_call (FunctionCall | None):
            audio (ChatCompletionAudioResponse | None | Unset):
            images (list[ImageURLListItem] | None | Unset):
            reasoning_content (None | str | Unset):
            thinking_blocks (list[ChatCompletionRedactedThinkingBlock | ChatCompletionThinkingBlock] | None | Unset):
            provider_specific_fields (MessageProviderSpecificFieldsType0 | None | Unset):
            annotations (list[ChatCompletionAnnotation] | None | Unset):
     """

    content: None | str
    role: MessageRole
    tool_calls: list[ChatCompletionMessageToolCall] | None
    function_call: FunctionCall | None
    audio: ChatCompletionAudioResponse | None | Unset = UNSET
    images: list[ImageURLListItem] | None | Unset = UNSET
    reasoning_content: None | str | Unset = UNSET
    thinking_blocks: list[ChatCompletionRedactedThinkingBlock | ChatCompletionThinkingBlock] | None | Unset = UNSET
    provider_specific_fields: MessageProviderSpecificFieldsType0 | None | Unset = UNSET
    annotations: list[ChatCompletionAnnotation] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_annotation import ChatCompletionAnnotation
        from ..models.chat_completion_message_tool_call import ChatCompletionMessageToolCall
        from ..models.message_provider_specific_fields_type_0 import MessageProviderSpecificFieldsType0
        from ..models.chat_completion_thinking_block import ChatCompletionThinkingBlock
        from ..models.image_url_list_item import ImageURLListItem
        from ..models.function_call import FunctionCall
        from ..models.chat_completion_redacted_thinking_block import ChatCompletionRedactedThinkingBlock
        from ..models.chat_completion_audio_response import ChatCompletionAudioResponse
        content: None | str
        content = self.content

        role = self.role.value

        tool_calls: list[dict[str, Any]] | None
        if isinstance(self.tool_calls, list):
            tool_calls = []
            for tool_calls_type_0_item_data in self.tool_calls:
                tool_calls_type_0_item = tool_calls_type_0_item_data.to_dict()
                tool_calls.append(tool_calls_type_0_item)


        else:
            tool_calls = self.tool_calls

        function_call: dict[str, Any] | None
        if isinstance(self.function_call, FunctionCall):
            function_call = self.function_call.to_dict()
        else:
            function_call = self.function_call

        audio: dict[str, Any] | None | Unset
        if isinstance(self.audio, Unset):
            audio = UNSET
        elif isinstance(self.audio, ChatCompletionAudioResponse):
            audio = self.audio.to_dict()
        else:
            audio = self.audio

        images: list[dict[str, Any]] | None | Unset
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item = images_type_0_item_data.to_dict()
                images.append(images_type_0_item)


        else:
            images = self.images

        reasoning_content: None | str | Unset
        if isinstance(self.reasoning_content, Unset):
            reasoning_content = UNSET
        else:
            reasoning_content = self.reasoning_content

        thinking_blocks: list[dict[str, Any]] | None | Unset
        if isinstance(self.thinking_blocks, Unset):
            thinking_blocks = UNSET
        elif isinstance(self.thinking_blocks, list):
            thinking_blocks = []
            for thinking_blocks_type_0_item_data in self.thinking_blocks:
                thinking_blocks_type_0_item: dict[str, Any]
                if isinstance(thinking_blocks_type_0_item_data, ChatCompletionThinkingBlock):
                    thinking_blocks_type_0_item = thinking_blocks_type_0_item_data.to_dict()
                else:
                    thinking_blocks_type_0_item = thinking_blocks_type_0_item_data.to_dict()

                thinking_blocks.append(thinking_blocks_type_0_item)


        else:
            thinking_blocks = self.thinking_blocks

        provider_specific_fields: dict[str, Any] | None | Unset
        if isinstance(self.provider_specific_fields, Unset):
            provider_specific_fields = UNSET
        elif isinstance(self.provider_specific_fields, MessageProviderSpecificFieldsType0):
            provider_specific_fields = self.provider_specific_fields.to_dict()
        else:
            provider_specific_fields = self.provider_specific_fields

        annotations: list[dict[str, Any]] | None | Unset
        if isinstance(self.annotations, Unset):
            annotations = UNSET
        elif isinstance(self.annotations, list):
            annotations = []
            for annotations_type_0_item_data in self.annotations:
                annotations_type_0_item = annotations_type_0_item_data.to_dict()
                annotations.append(annotations_type_0_item)


        else:
            annotations = self.annotations


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "content": content,
            "role": role,
            "tool_calls": tool_calls,
            "function_call": function_call,
        })
        if audio is not UNSET:
            field_dict["audio"] = audio
        if images is not UNSET:
            field_dict["images"] = images
        if reasoning_content is not UNSET:
            field_dict["reasoning_content"] = reasoning_content
        if thinking_blocks is not UNSET:
            field_dict["thinking_blocks"] = thinking_blocks
        if provider_specific_fields is not UNSET:
            field_dict["provider_specific_fields"] = provider_specific_fields
        if annotations is not UNSET:
            field_dict["annotations"] = annotations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_annotation import ChatCompletionAnnotation
        from ..models.chat_completion_audio_response import ChatCompletionAudioResponse
        from ..models.chat_completion_message_tool_call import ChatCompletionMessageToolCall
        from ..models.chat_completion_redacted_thinking_block import ChatCompletionRedactedThinkingBlock
        from ..models.chat_completion_thinking_block import ChatCompletionThinkingBlock
        from ..models.function_call import FunctionCall
        from ..models.image_url_list_item import ImageURLListItem
        from ..models.message_provider_specific_fields_type_0 import MessageProviderSpecificFieldsType0
        d = dict(src_dict)
        def _parse_content(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content = _parse_content(d.pop("content"))


        role = MessageRole(d.pop("role"))




        def _parse_tool_calls(data: object) -> list[ChatCompletionMessageToolCall] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tool_calls_type_0 = []
                _tool_calls_type_0 = data
                for tool_calls_type_0_item_data in (_tool_calls_type_0):
                    tool_calls_type_0_item = ChatCompletionMessageToolCall.from_dict(tool_calls_type_0_item_data)



                    tool_calls_type_0.append(tool_calls_type_0_item)

                return tool_calls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ChatCompletionMessageToolCall] | None, data)

        tool_calls = _parse_tool_calls(d.pop("tool_calls"))


        def _parse_function_call(data: object) -> FunctionCall | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                function_call_type_0 = FunctionCall.from_dict(data)



                return function_call_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FunctionCall | None, data)

        function_call = _parse_function_call(d.pop("function_call"))


        def _parse_audio(data: object) -> ChatCompletionAudioResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                audio_type_0 = ChatCompletionAudioResponse.from_dict(data)



                return audio_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatCompletionAudioResponse | None | Unset, data)

        audio = _parse_audio(d.pop("audio", UNSET))


        def _parse_images(data: object) -> list[ImageURLListItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = []
                _images_type_0 = data
                for images_type_0_item_data in (_images_type_0):
                    images_type_0_item = ImageURLListItem.from_dict(images_type_0_item_data)



                    images_type_0.append(images_type_0_item)

                return images_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImageURLListItem] | None | Unset, data)

        images = _parse_images(d.pop("images", UNSET))


        def _parse_reasoning_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reasoning_content = _parse_reasoning_content(d.pop("reasoning_content", UNSET))


        def _parse_thinking_blocks(data: object) -> list[ChatCompletionRedactedThinkingBlock | ChatCompletionThinkingBlock] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                thinking_blocks_type_0 = []
                _thinking_blocks_type_0 = data
                for thinking_blocks_type_0_item_data in (_thinking_blocks_type_0):
                    def _parse_thinking_blocks_type_0_item(data: object) -> ChatCompletionRedactedThinkingBlock | ChatCompletionThinkingBlock:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            thinking_blocks_type_0_item_type_0 = ChatCompletionThinkingBlock.from_dict(data)



                            return thinking_blocks_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        thinking_blocks_type_0_item_type_1 = ChatCompletionRedactedThinkingBlock.from_dict(data)



                        return thinking_blocks_type_0_item_type_1

                    thinking_blocks_type_0_item = _parse_thinking_blocks_type_0_item(thinking_blocks_type_0_item_data)

                    thinking_blocks_type_0.append(thinking_blocks_type_0_item)

                return thinking_blocks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ChatCompletionRedactedThinkingBlock | ChatCompletionThinkingBlock] | None | Unset, data)

        thinking_blocks = _parse_thinking_blocks(d.pop("thinking_blocks", UNSET))


        def _parse_provider_specific_fields(data: object) -> MessageProviderSpecificFieldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_specific_fields_type_0 = MessageProviderSpecificFieldsType0.from_dict(data)



                return provider_specific_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MessageProviderSpecificFieldsType0 | None | Unset, data)

        provider_specific_fields = _parse_provider_specific_fields(d.pop("provider_specific_fields", UNSET))


        def _parse_annotations(data: object) -> list[ChatCompletionAnnotation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                annotations_type_0 = []
                _annotations_type_0 = data
                for annotations_type_0_item_data in (_annotations_type_0):
                    annotations_type_0_item = ChatCompletionAnnotation.from_dict(annotations_type_0_item_data)



                    annotations_type_0.append(annotations_type_0_item)

                return annotations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ChatCompletionAnnotation] | None | Unset, data)

        annotations = _parse_annotations(d.pop("annotations", UNSET))


        message = cls(
            content=content,
            role=role,
            tool_calls=tool_calls,
            function_call=function_call,
            audio=audio,
            images=images,
            reasoning_content=reasoning_content,
            thinking_blocks=thinking_blocks,
            provider_specific_fields=provider_specific_fields,
            annotations=annotations,
        )


        message.additional_properties = d
        return message

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
