from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chat_completion_assistant_message import ChatCompletionAssistantMessage
  from ..models.chat_completion_developer_message import ChatCompletionDeveloperMessage
  from ..models.chat_completion_function_message import ChatCompletionFunctionMessage
  from ..models.chat_completion_message_tool_call import ChatCompletionMessageToolCall
  from ..models.chat_completion_system_message import ChatCompletionSystemMessage
  from ..models.chat_completion_tool_call_chunk import ChatCompletionToolCallChunk
  from ..models.chat_completion_tool_message import ChatCompletionToolMessage
  from ..models.chat_completion_tool_param import ChatCompletionToolParam
  from ..models.chat_completion_user_message import ChatCompletionUserMessage





T = TypeVar("T", bound="GenericGuardrailAPIInputs")



@_attrs_define
class GenericGuardrailAPIInputs:
    """ 
        Attributes:
            texts (list[str] | Unset):
            images (list[str] | Unset):
            tools (list[ChatCompletionToolParam] | Unset):
            tool_calls (list[ChatCompletionMessageToolCall] | list[ChatCompletionToolCallChunk] | Unset):
            structured_messages (list[ChatCompletionAssistantMessage | ChatCompletionDeveloperMessage |
                ChatCompletionFunctionMessage | ChatCompletionSystemMessage | ChatCompletionToolMessage |
                ChatCompletionUserMessage] | Unset):
            model (None | str | Unset):
     """

    texts: list[str] | Unset = UNSET
    images: list[str] | Unset = UNSET
    tools: list[ChatCompletionToolParam] | Unset = UNSET
    tool_calls: list[ChatCompletionMessageToolCall] | list[ChatCompletionToolCallChunk] | Unset = UNSET
    structured_messages: list[ChatCompletionAssistantMessage | ChatCompletionDeveloperMessage | ChatCompletionFunctionMessage | ChatCompletionSystemMessage | ChatCompletionToolMessage | ChatCompletionUserMessage] | Unset = UNSET
    model: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_tool_message import ChatCompletionToolMessage
        from ..models.chat_completion_system_message import ChatCompletionSystemMessage
        from ..models.chat_completion_tool_call_chunk import ChatCompletionToolCallChunk
        from ..models.chat_completion_message_tool_call import ChatCompletionMessageToolCall
        from ..models.chat_completion_tool_param import ChatCompletionToolParam
        from ..models.chat_completion_assistant_message import ChatCompletionAssistantMessage
        from ..models.chat_completion_developer_message import ChatCompletionDeveloperMessage
        from ..models.chat_completion_user_message import ChatCompletionUserMessage
        from ..models.chat_completion_function_message import ChatCompletionFunctionMessage
        texts: list[str] | Unset = UNSET
        if not isinstance(self.texts, Unset):
            texts = self.texts



        images: list[str] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images



        tools: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tools, Unset):
            tools = []
            for tools_item_data in self.tools:
                tools_item = tools_item_data.to_dict()
                tools.append(tools_item)



        tool_calls: list[dict[str, Any]] | Unset
        if isinstance(self.tool_calls, Unset):
            tool_calls = UNSET
        elif isinstance(self.tool_calls, list):
            tool_calls = []
            for tool_calls_type_0_item_data in self.tool_calls:
                tool_calls_type_0_item = tool_calls_type_0_item_data.to_dict()
                tool_calls.append(tool_calls_type_0_item)


        else:
            tool_calls = []
            for tool_calls_type_1_item_data in self.tool_calls:
                tool_calls_type_1_item = tool_calls_type_1_item_data.to_dict()
                tool_calls.append(tool_calls_type_1_item)




        structured_messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.structured_messages, Unset):
            structured_messages = []
            for structured_messages_item_data in self.structured_messages:
                structured_messages_item: dict[str, Any]
                if isinstance(structured_messages_item_data, ChatCompletionUserMessage):
                    structured_messages_item = structured_messages_item_data.to_dict()
                elif isinstance(structured_messages_item_data, ChatCompletionAssistantMessage):
                    structured_messages_item = structured_messages_item_data.to_dict()
                elif isinstance(structured_messages_item_data, ChatCompletionToolMessage):
                    structured_messages_item = structured_messages_item_data.to_dict()
                elif isinstance(structured_messages_item_data, ChatCompletionSystemMessage):
                    structured_messages_item = structured_messages_item_data.to_dict()
                elif isinstance(structured_messages_item_data, ChatCompletionFunctionMessage):
                    structured_messages_item = structured_messages_item_data.to_dict()
                else:
                    structured_messages_item = structured_messages_item_data.to_dict()

                structured_messages.append(structured_messages_item)



        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if texts is not UNSET:
            field_dict["texts"] = texts
        if images is not UNSET:
            field_dict["images"] = images
        if tools is not UNSET:
            field_dict["tools"] = tools
        if tool_calls is not UNSET:
            field_dict["tool_calls"] = tool_calls
        if structured_messages is not UNSET:
            field_dict["structured_messages"] = structured_messages
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_assistant_message import ChatCompletionAssistantMessage
        from ..models.chat_completion_developer_message import ChatCompletionDeveloperMessage
        from ..models.chat_completion_function_message import ChatCompletionFunctionMessage
        from ..models.chat_completion_message_tool_call import ChatCompletionMessageToolCall
        from ..models.chat_completion_system_message import ChatCompletionSystemMessage
        from ..models.chat_completion_tool_call_chunk import ChatCompletionToolCallChunk
        from ..models.chat_completion_tool_message import ChatCompletionToolMessage
        from ..models.chat_completion_tool_param import ChatCompletionToolParam
        from ..models.chat_completion_user_message import ChatCompletionUserMessage
        d = dict(src_dict)
        texts = cast(list[str], d.pop("texts", UNSET))


        images = cast(list[str], d.pop("images", UNSET))


        _tools = d.pop("tools", UNSET)
        tools: list[ChatCompletionToolParam] | Unset = UNSET
        if _tools is not UNSET:
            tools = []
            for tools_item_data in _tools:
                tools_item = ChatCompletionToolParam.from_dict(tools_item_data)



                tools.append(tools_item)


        def _parse_tool_calls(data: object) -> list[ChatCompletionMessageToolCall] | list[ChatCompletionToolCallChunk] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tool_calls_type_0 = []
                _tool_calls_type_0 = data
                for tool_calls_type_0_item_data in (_tool_calls_type_0):
                    tool_calls_type_0_item = ChatCompletionToolCallChunk.from_dict(tool_calls_type_0_item_data)



                    tool_calls_type_0.append(tool_calls_type_0_item)

                return tool_calls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            tool_calls_type_1 = []
            _tool_calls_type_1 = data
            for tool_calls_type_1_item_data in (_tool_calls_type_1):
                tool_calls_type_1_item = ChatCompletionMessageToolCall.from_dict(tool_calls_type_1_item_data)



                tool_calls_type_1.append(tool_calls_type_1_item)

            return tool_calls_type_1

        tool_calls = _parse_tool_calls(d.pop("tool_calls", UNSET))


        _structured_messages = d.pop("structured_messages", UNSET)
        structured_messages: list[ChatCompletionAssistantMessage | ChatCompletionDeveloperMessage | ChatCompletionFunctionMessage | ChatCompletionSystemMessage | ChatCompletionToolMessage | ChatCompletionUserMessage] | Unset = UNSET
        if _structured_messages is not UNSET:
            structured_messages = []
            for structured_messages_item_data in _structured_messages:
                def _parse_structured_messages_item(data: object) -> ChatCompletionAssistantMessage | ChatCompletionDeveloperMessage | ChatCompletionFunctionMessage | ChatCompletionSystemMessage | ChatCompletionToolMessage | ChatCompletionUserMessage:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        structured_messages_item_type_0 = ChatCompletionUserMessage.from_dict(data)



                        return structured_messages_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        structured_messages_item_type_1 = ChatCompletionAssistantMessage.from_dict(data)



                        return structured_messages_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        structured_messages_item_type_2 = ChatCompletionToolMessage.from_dict(data)



                        return structured_messages_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        structured_messages_item_type_3 = ChatCompletionSystemMessage.from_dict(data)



                        return structured_messages_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        structured_messages_item_type_4 = ChatCompletionFunctionMessage.from_dict(data)



                        return structured_messages_item_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    structured_messages_item_type_5 = ChatCompletionDeveloperMessage.from_dict(data)



                    return structured_messages_item_type_5

                structured_messages_item = _parse_structured_messages_item(structured_messages_item_data)

                structured_messages.append(structured_messages_item)


        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        generic_guardrail_api_inputs = cls(
            texts=texts,
            images=images,
            tools=tools,
            tool_calls=tool_calls,
            structured_messages=structured_messages,
            model=model,
        )


        generic_guardrail_api_inputs.additional_properties = d
        return generic_guardrail_api_inputs

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
