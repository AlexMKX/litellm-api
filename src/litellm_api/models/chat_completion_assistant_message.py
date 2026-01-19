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
  from ..models.chat_completion_assistant_tool_call import ChatCompletionAssistantToolCall
  from ..models.chat_completion_cached_content import ChatCompletionCachedContent
  from ..models.chat_completion_redacted_thinking_block import ChatCompletionRedactedThinkingBlock
  from ..models.chat_completion_text_object import ChatCompletionTextObject
  from ..models.chat_completion_thinking_block import ChatCompletionThinkingBlock
  from ..models.chat_completion_tool_call_function_chunk import ChatCompletionToolCallFunctionChunk





T = TypeVar("T", bound="ChatCompletionAssistantMessage")



@_attrs_define
class ChatCompletionAssistantMessage:
    """ 
        Attributes:
            role (Literal['assistant']):
            content (list[ChatCompletionTextObject | ChatCompletionThinkingBlock] | None | str | Unset):
            name (None | str | Unset):
            tool_calls (list[ChatCompletionAssistantToolCall] | None | Unset):
            function_call (ChatCompletionToolCallFunctionChunk | None | Unset):
            reasoning_content (None | str | Unset):
            cache_control (ChatCompletionCachedContent | Unset):
            thinking_blocks (list[ChatCompletionRedactedThinkingBlock | ChatCompletionThinkingBlock] | None | Unset):
     """

    role: Literal['assistant']
    content: list[ChatCompletionTextObject | ChatCompletionThinkingBlock] | None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    tool_calls: list[ChatCompletionAssistantToolCall] | None | Unset = UNSET
    function_call: ChatCompletionToolCallFunctionChunk | None | Unset = UNSET
    reasoning_content: None | str | Unset = UNSET
    cache_control: ChatCompletionCachedContent | Unset = UNSET
    thinking_blocks: list[ChatCompletionRedactedThinkingBlock | ChatCompletionThinkingBlock] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_text_object import ChatCompletionTextObject
        from ..models.chat_completion_thinking_block import ChatCompletionThinkingBlock
        from ..models.chat_completion_redacted_thinking_block import ChatCompletionRedactedThinkingBlock
        from ..models.chat_completion_assistant_tool_call import ChatCompletionAssistantToolCall
        from ..models.chat_completion_cached_content import ChatCompletionCachedContent
        from ..models.chat_completion_tool_call_function_chunk import ChatCompletionToolCallFunctionChunk
        role = self.role

        content: list[dict[str, Any]] | None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, list):
            content = []
            for content_type_1_item_data in self.content:
                content_type_1_item: dict[str, Any]
                if isinstance(content_type_1_item_data, ChatCompletionTextObject):
                    content_type_1_item = content_type_1_item_data.to_dict()
                else:
                    content_type_1_item = content_type_1_item_data.to_dict()

                content.append(content_type_1_item)


        else:
            content = self.content

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        tool_calls: list[dict[str, Any]] | None | Unset
        if isinstance(self.tool_calls, Unset):
            tool_calls = UNSET
        elif isinstance(self.tool_calls, list):
            tool_calls = []
            for tool_calls_type_0_item_data in self.tool_calls:
                tool_calls_type_0_item = tool_calls_type_0_item_data.to_dict()
                tool_calls.append(tool_calls_type_0_item)


        else:
            tool_calls = self.tool_calls

        function_call: dict[str, Any] | None | Unset
        if isinstance(self.function_call, Unset):
            function_call = UNSET
        elif isinstance(self.function_call, ChatCompletionToolCallFunctionChunk):
            function_call = self.function_call.to_dict()
        else:
            function_call = self.function_call

        reasoning_content: None | str | Unset
        if isinstance(self.reasoning_content, Unset):
            reasoning_content = UNSET
        else:
            reasoning_content = self.reasoning_content

        cache_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cache_control, Unset):
            cache_control = self.cache_control.to_dict()

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "role": role,
        })
        if content is not UNSET:
            field_dict["content"] = content
        if name is not UNSET:
            field_dict["name"] = name
        if tool_calls is not UNSET:
            field_dict["tool_calls"] = tool_calls
        if function_call is not UNSET:
            field_dict["function_call"] = function_call
        if reasoning_content is not UNSET:
            field_dict["reasoning_content"] = reasoning_content
        if cache_control is not UNSET:
            field_dict["cache_control"] = cache_control
        if thinking_blocks is not UNSET:
            field_dict["thinking_blocks"] = thinking_blocks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_assistant_tool_call import ChatCompletionAssistantToolCall
        from ..models.chat_completion_cached_content import ChatCompletionCachedContent
        from ..models.chat_completion_redacted_thinking_block import ChatCompletionRedactedThinkingBlock
        from ..models.chat_completion_text_object import ChatCompletionTextObject
        from ..models.chat_completion_thinking_block import ChatCompletionThinkingBlock
        from ..models.chat_completion_tool_call_function_chunk import ChatCompletionToolCallFunctionChunk
        d = dict(src_dict)
        role = cast(Literal['assistant'] , d.pop("role"))
        if role != 'assistant':
            raise ValueError(f"role must match const 'assistant', got '{role}'")

        def _parse_content(data: object) -> list[ChatCompletionTextObject | ChatCompletionThinkingBlock] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_type_1 = []
                _content_type_1 = data
                for content_type_1_item_data in (_content_type_1):
                    def _parse_content_type_1_item(data: object) -> ChatCompletionTextObject | ChatCompletionThinkingBlock:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            content_type_1_item_type_0 = ChatCompletionTextObject.from_dict(data)



                            return content_type_1_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        content_type_1_item_type_1 = ChatCompletionThinkingBlock.from_dict(data)



                        return content_type_1_item_type_1

                    content_type_1_item = _parse_content_type_1_item(content_type_1_item_data)

                    content_type_1.append(content_type_1_item)

                return content_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ChatCompletionTextObject | ChatCompletionThinkingBlock] | None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_tool_calls(data: object) -> list[ChatCompletionAssistantToolCall] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tool_calls_type_0 = []
                _tool_calls_type_0 = data
                for tool_calls_type_0_item_data in (_tool_calls_type_0):
                    tool_calls_type_0_item = ChatCompletionAssistantToolCall.from_dict(tool_calls_type_0_item_data)



                    tool_calls_type_0.append(tool_calls_type_0_item)

                return tool_calls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ChatCompletionAssistantToolCall] | None | Unset, data)

        tool_calls = _parse_tool_calls(d.pop("tool_calls", UNSET))


        def _parse_function_call(data: object) -> ChatCompletionToolCallFunctionChunk | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                function_call_type_0 = ChatCompletionToolCallFunctionChunk.from_dict(data)



                return function_call_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatCompletionToolCallFunctionChunk | None | Unset, data)

        function_call = _parse_function_call(d.pop("function_call", UNSET))


        def _parse_reasoning_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reasoning_content = _parse_reasoning_content(d.pop("reasoning_content", UNSET))


        _cache_control = d.pop("cache_control", UNSET)
        cache_control: ChatCompletionCachedContent | Unset
        if isinstance(_cache_control,  Unset):
            cache_control = UNSET
        else:
            cache_control = ChatCompletionCachedContent.from_dict(_cache_control)




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


        chat_completion_assistant_message = cls(
            role=role,
            content=content,
            name=name,
            tool_calls=tool_calls,
            function_call=function_call,
            reasoning_content=reasoning_content,
            cache_control=cache_control,
            thinking_blocks=thinking_blocks,
        )


        chat_completion_assistant_message.additional_properties = d
        return chat_completion_assistant_message

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
