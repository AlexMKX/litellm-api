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
  from ..models.chat_completion_system_message import ChatCompletionSystemMessage
  from ..models.chat_completion_tool_message import ChatCompletionToolMessage
  from ..models.chat_completion_user_message import ChatCompletionUserMessage
  from ..models.chat_completion_v1_chat_completions_post_body_context_window_fallback_dict_type_0 import ChatCompletionV1ChatCompletionsPostBodyContextWindowFallbackDictType0
  from ..models.chat_completion_v1_chat_completions_post_body_function_call_type_1 import ChatCompletionV1ChatCompletionsPostBodyFunctionCallType1
  from ..models.chat_completion_v1_chat_completions_post_body_functions_type_0_item import ChatCompletionV1ChatCompletionsPostBodyFunctionsType0Item
  from ..models.chat_completion_v1_chat_completions_post_body_logit_bias_type_0 import ChatCompletionV1ChatCompletionsPostBodyLogitBiasType0
  from ..models.chat_completion_v1_chat_completions_post_body_metadata_type_0 import ChatCompletionV1ChatCompletionsPostBodyMetadataType0
  from ..models.chat_completion_v1_chat_completions_post_body_response_format_type_0 import ChatCompletionV1ChatCompletionsPostBodyResponseFormatType0
  from ..models.chat_completion_v1_chat_completions_post_body_stream_options_type_0 import ChatCompletionV1ChatCompletionsPostBodyStreamOptionsType0
  from ..models.chat_completion_v1_chat_completions_post_body_tool_choice_type_1 import ChatCompletionV1ChatCompletionsPostBodyToolChoiceType1
  from ..models.chat_completion_v1_chat_completions_post_body_tools_type_0_item import ChatCompletionV1ChatCompletionsPostBodyToolsType0Item





T = TypeVar("T", bound="ChatCompletionV1ChatCompletionsPostBody")



@_attrs_define
class ChatCompletionV1ChatCompletionsPostBody:
    """ 
        Attributes:
            model (str):
            messages (list[ChatCompletionAssistantMessage | ChatCompletionDeveloperMessage | ChatCompletionFunctionMessage |
                ChatCompletionSystemMessage | ChatCompletionToolMessage | ChatCompletionUserMessage]):  Example: [{'role':
                'user', 'content': 'Hello, how are you?'}].
            frequency_penalty (float | None | Unset):
            logit_bias (ChatCompletionV1ChatCompletionsPostBodyLogitBiasType0 | None | Unset):
            logprobs (bool | None | Unset):
            top_logprobs (int | None | Unset):
            max_tokens (int | None | Unset):
            n (int | None | Unset):
            presence_penalty (float | None | Unset):
            response_format (ChatCompletionV1ChatCompletionsPostBodyResponseFormatType0 | None | Unset):
            seed (int | None | Unset):
            service_tier (None | str | Unset):
            stop (list[str] | None | str | Unset):
            stream_options (ChatCompletionV1ChatCompletionsPostBodyStreamOptionsType0 | None | Unset):
            temperature (float | None | Unset):
            top_p (float | None | Unset):
            tools (list[ChatCompletionV1ChatCompletionsPostBodyToolsType0Item] | None | Unset):
            tool_choice (ChatCompletionV1ChatCompletionsPostBodyToolChoiceType1 | None | str | Unset):
            parallel_tool_calls (bool | None | Unset):
            function_call (ChatCompletionV1ChatCompletionsPostBodyFunctionCallType1 | None | str | Unset):
            functions (list[ChatCompletionV1ChatCompletionsPostBodyFunctionsType0Item] | None | Unset):
            user (None | str | Unset):
            stream (bool | None | Unset):
            metadata (ChatCompletionV1ChatCompletionsPostBodyMetadataType0 | None | Unset):
            guardrails (list[str] | None | Unset):
            caching (bool | None | Unset):
            num_retries (int | None | Unset):
            context_window_fallback_dict (ChatCompletionV1ChatCompletionsPostBodyContextWindowFallbackDictType0 | None |
                Unset):
            fallbacks (list[str] | None | Unset):
     """

    model: str
    messages: list[ChatCompletionAssistantMessage | ChatCompletionDeveloperMessage | ChatCompletionFunctionMessage | ChatCompletionSystemMessage | ChatCompletionToolMessage | ChatCompletionUserMessage]
    frequency_penalty: float | None | Unset = UNSET
    logit_bias: ChatCompletionV1ChatCompletionsPostBodyLogitBiasType0 | None | Unset = UNSET
    logprobs: bool | None | Unset = UNSET
    top_logprobs: int | None | Unset = UNSET
    max_tokens: int | None | Unset = UNSET
    n: int | None | Unset = UNSET
    presence_penalty: float | None | Unset = UNSET
    response_format: ChatCompletionV1ChatCompletionsPostBodyResponseFormatType0 | None | Unset = UNSET
    seed: int | None | Unset = UNSET
    service_tier: None | str | Unset = UNSET
    stop: list[str] | None | str | Unset = UNSET
    stream_options: ChatCompletionV1ChatCompletionsPostBodyStreamOptionsType0 | None | Unset = UNSET
    temperature: float | None | Unset = UNSET
    top_p: float | None | Unset = UNSET
    tools: list[ChatCompletionV1ChatCompletionsPostBodyToolsType0Item] | None | Unset = UNSET
    tool_choice: ChatCompletionV1ChatCompletionsPostBodyToolChoiceType1 | None | str | Unset = UNSET
    parallel_tool_calls: bool | None | Unset = UNSET
    function_call: ChatCompletionV1ChatCompletionsPostBodyFunctionCallType1 | None | str | Unset = UNSET
    functions: list[ChatCompletionV1ChatCompletionsPostBodyFunctionsType0Item] | None | Unset = UNSET
    user: None | str | Unset = UNSET
    stream: bool | None | Unset = UNSET
    metadata: ChatCompletionV1ChatCompletionsPostBodyMetadataType0 | None | Unset = UNSET
    guardrails: list[str] | None | Unset = UNSET
    caching: bool | None | Unset = UNSET
    num_retries: int | None | Unset = UNSET
    context_window_fallback_dict: ChatCompletionV1ChatCompletionsPostBodyContextWindowFallbackDictType0 | None | Unset = UNSET
    fallbacks: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_v1_chat_completions_post_body_metadata_type_0 import ChatCompletionV1ChatCompletionsPostBodyMetadataType0
        from ..models.chat_completion_v1_chat_completions_post_body_logit_bias_type_0 import ChatCompletionV1ChatCompletionsPostBodyLogitBiasType0
        from ..models.chat_completion_assistant_message import ChatCompletionAssistantMessage
        from ..models.chat_completion_tool_message import ChatCompletionToolMessage
        from ..models.chat_completion_system_message import ChatCompletionSystemMessage
        from ..models.chat_completion_v1_chat_completions_post_body_tools_type_0_item import ChatCompletionV1ChatCompletionsPostBodyToolsType0Item
        from ..models.chat_completion_v1_chat_completions_post_body_function_call_type_1 import ChatCompletionV1ChatCompletionsPostBodyFunctionCallType1
        from ..models.chat_completion_v1_chat_completions_post_body_functions_type_0_item import ChatCompletionV1ChatCompletionsPostBodyFunctionsType0Item
        from ..models.chat_completion_v1_chat_completions_post_body_response_format_type_0 import ChatCompletionV1ChatCompletionsPostBodyResponseFormatType0
        from ..models.chat_completion_function_message import ChatCompletionFunctionMessage
        from ..models.chat_completion_v1_chat_completions_post_body_stream_options_type_0 import ChatCompletionV1ChatCompletionsPostBodyStreamOptionsType0
        from ..models.chat_completion_user_message import ChatCompletionUserMessage
        from ..models.chat_completion_v1_chat_completions_post_body_context_window_fallback_dict_type_0 import ChatCompletionV1ChatCompletionsPostBodyContextWindowFallbackDictType0
        from ..models.chat_completion_v1_chat_completions_post_body_tool_choice_type_1 import ChatCompletionV1ChatCompletionsPostBodyToolChoiceType1
        from ..models.chat_completion_developer_message import ChatCompletionDeveloperMessage
        model = self.model

        messages = []
        for messages_item_data in self.messages:
            messages_item: dict[str, Any]
            if isinstance(messages_item_data, ChatCompletionUserMessage):
                messages_item = messages_item_data.to_dict()
            elif isinstance(messages_item_data, ChatCompletionAssistantMessage):
                messages_item = messages_item_data.to_dict()
            elif isinstance(messages_item_data, ChatCompletionToolMessage):
                messages_item = messages_item_data.to_dict()
            elif isinstance(messages_item_data, ChatCompletionSystemMessage):
                messages_item = messages_item_data.to_dict()
            elif isinstance(messages_item_data, ChatCompletionFunctionMessage):
                messages_item = messages_item_data.to_dict()
            else:
                messages_item = messages_item_data.to_dict()

            messages.append(messages_item)



        frequency_penalty: float | None | Unset
        if isinstance(self.frequency_penalty, Unset):
            frequency_penalty = UNSET
        else:
            frequency_penalty = self.frequency_penalty

        logit_bias: dict[str, Any] | None | Unset
        if isinstance(self.logit_bias, Unset):
            logit_bias = UNSET
        elif isinstance(self.logit_bias, ChatCompletionV1ChatCompletionsPostBodyLogitBiasType0):
            logit_bias = self.logit_bias.to_dict()
        else:
            logit_bias = self.logit_bias

        logprobs: bool | None | Unset
        if isinstance(self.logprobs, Unset):
            logprobs = UNSET
        else:
            logprobs = self.logprobs

        top_logprobs: int | None | Unset
        if isinstance(self.top_logprobs, Unset):
            top_logprobs = UNSET
        else:
            top_logprobs = self.top_logprobs

        max_tokens: int | None | Unset
        if isinstance(self.max_tokens, Unset):
            max_tokens = UNSET
        else:
            max_tokens = self.max_tokens

        n: int | None | Unset
        if isinstance(self.n, Unset):
            n = UNSET
        else:
            n = self.n

        presence_penalty: float | None | Unset
        if isinstance(self.presence_penalty, Unset):
            presence_penalty = UNSET
        else:
            presence_penalty = self.presence_penalty

        response_format: dict[str, Any] | None | Unset
        if isinstance(self.response_format, Unset):
            response_format = UNSET
        elif isinstance(self.response_format, ChatCompletionV1ChatCompletionsPostBodyResponseFormatType0):
            response_format = self.response_format.to_dict()
        else:
            response_format = self.response_format

        seed: int | None | Unset
        if isinstance(self.seed, Unset):
            seed = UNSET
        else:
            seed = self.seed

        service_tier: None | str | Unset
        if isinstance(self.service_tier, Unset):
            service_tier = UNSET
        else:
            service_tier = self.service_tier

        stop: list[str] | None | str | Unset
        if isinstance(self.stop, Unset):
            stop = UNSET
        elif isinstance(self.stop, list):
            stop = self.stop


        else:
            stop = self.stop

        stream_options: dict[str, Any] | None | Unset
        if isinstance(self.stream_options, Unset):
            stream_options = UNSET
        elif isinstance(self.stream_options, ChatCompletionV1ChatCompletionsPostBodyStreamOptionsType0):
            stream_options = self.stream_options.to_dict()
        else:
            stream_options = self.stream_options

        temperature: float | None | Unset
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        top_p: float | None | Unset
        if isinstance(self.top_p, Unset):
            top_p = UNSET
        else:
            top_p = self.top_p

        tools: list[dict[str, Any]] | None | Unset
        if isinstance(self.tools, Unset):
            tools = UNSET
        elif isinstance(self.tools, list):
            tools = []
            for tools_type_0_item_data in self.tools:
                tools_type_0_item = tools_type_0_item_data.to_dict()
                tools.append(tools_type_0_item)


        else:
            tools = self.tools

        tool_choice: dict[str, Any] | None | str | Unset
        if isinstance(self.tool_choice, Unset):
            tool_choice = UNSET
        elif isinstance(self.tool_choice, ChatCompletionV1ChatCompletionsPostBodyToolChoiceType1):
            tool_choice = self.tool_choice.to_dict()
        else:
            tool_choice = self.tool_choice

        parallel_tool_calls: bool | None | Unset
        if isinstance(self.parallel_tool_calls, Unset):
            parallel_tool_calls = UNSET
        else:
            parallel_tool_calls = self.parallel_tool_calls

        function_call: dict[str, Any] | None | str | Unset
        if isinstance(self.function_call, Unset):
            function_call = UNSET
        elif isinstance(self.function_call, ChatCompletionV1ChatCompletionsPostBodyFunctionCallType1):
            function_call = self.function_call.to_dict()
        else:
            function_call = self.function_call

        functions: list[dict[str, Any]] | None | Unset
        if isinstance(self.functions, Unset):
            functions = UNSET
        elif isinstance(self.functions, list):
            functions = []
            for functions_type_0_item_data in self.functions:
                functions_type_0_item = functions_type_0_item_data.to_dict()
                functions.append(functions_type_0_item)


        else:
            functions = self.functions

        user: None | str | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        stream: bool | None | Unset
        if isinstance(self.stream, Unset):
            stream = UNSET
        else:
            stream = self.stream

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, ChatCompletionV1ChatCompletionsPostBodyMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        guardrails: list[str] | None | Unset
        if isinstance(self.guardrails, Unset):
            guardrails = UNSET
        elif isinstance(self.guardrails, list):
            guardrails = self.guardrails


        else:
            guardrails = self.guardrails

        caching: bool | None | Unset
        if isinstance(self.caching, Unset):
            caching = UNSET
        else:
            caching = self.caching

        num_retries: int | None | Unset
        if isinstance(self.num_retries, Unset):
            num_retries = UNSET
        else:
            num_retries = self.num_retries

        context_window_fallback_dict: dict[str, Any] | None | Unset
        if isinstance(self.context_window_fallback_dict, Unset):
            context_window_fallback_dict = UNSET
        elif isinstance(self.context_window_fallback_dict, ChatCompletionV1ChatCompletionsPostBodyContextWindowFallbackDictType0):
            context_window_fallback_dict = self.context_window_fallback_dict.to_dict()
        else:
            context_window_fallback_dict = self.context_window_fallback_dict

        fallbacks: list[str] | None | Unset
        if isinstance(self.fallbacks, Unset):
            fallbacks = UNSET
        elif isinstance(self.fallbacks, list):
            fallbacks = self.fallbacks


        else:
            fallbacks = self.fallbacks


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "model": model,
            "messages": messages,
        })
        if frequency_penalty is not UNSET:
            field_dict["frequency_penalty"] = frequency_penalty
        if logit_bias is not UNSET:
            field_dict["logit_bias"] = logit_bias
        if logprobs is not UNSET:
            field_dict["logprobs"] = logprobs
        if top_logprobs is not UNSET:
            field_dict["top_logprobs"] = top_logprobs
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if n is not UNSET:
            field_dict["n"] = n
        if presence_penalty is not UNSET:
            field_dict["presence_penalty"] = presence_penalty
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if seed is not UNSET:
            field_dict["seed"] = seed
        if service_tier is not UNSET:
            field_dict["service_tier"] = service_tier
        if stop is not UNSET:
            field_dict["stop"] = stop
        if stream_options is not UNSET:
            field_dict["stream_options"] = stream_options
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if top_p is not UNSET:
            field_dict["top_p"] = top_p
        if tools is not UNSET:
            field_dict["tools"] = tools
        if tool_choice is not UNSET:
            field_dict["tool_choice"] = tool_choice
        if parallel_tool_calls is not UNSET:
            field_dict["parallel_tool_calls"] = parallel_tool_calls
        if function_call is not UNSET:
            field_dict["function_call"] = function_call
        if functions is not UNSET:
            field_dict["functions"] = functions
        if user is not UNSET:
            field_dict["user"] = user
        if stream is not UNSET:
            field_dict["stream"] = stream
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if guardrails is not UNSET:
            field_dict["guardrails"] = guardrails
        if caching is not UNSET:
            field_dict["caching"] = caching
        if num_retries is not UNSET:
            field_dict["num_retries"] = num_retries
        if context_window_fallback_dict is not UNSET:
            field_dict["context_window_fallback_dict"] = context_window_fallback_dict
        if fallbacks is not UNSET:
            field_dict["fallbacks"] = fallbacks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_assistant_message import ChatCompletionAssistantMessage
        from ..models.chat_completion_developer_message import ChatCompletionDeveloperMessage
        from ..models.chat_completion_function_message import ChatCompletionFunctionMessage
        from ..models.chat_completion_system_message import ChatCompletionSystemMessage
        from ..models.chat_completion_tool_message import ChatCompletionToolMessage
        from ..models.chat_completion_user_message import ChatCompletionUserMessage
        from ..models.chat_completion_v1_chat_completions_post_body_context_window_fallback_dict_type_0 import ChatCompletionV1ChatCompletionsPostBodyContextWindowFallbackDictType0
        from ..models.chat_completion_v1_chat_completions_post_body_function_call_type_1 import ChatCompletionV1ChatCompletionsPostBodyFunctionCallType1
        from ..models.chat_completion_v1_chat_completions_post_body_functions_type_0_item import ChatCompletionV1ChatCompletionsPostBodyFunctionsType0Item
        from ..models.chat_completion_v1_chat_completions_post_body_logit_bias_type_0 import ChatCompletionV1ChatCompletionsPostBodyLogitBiasType0
        from ..models.chat_completion_v1_chat_completions_post_body_metadata_type_0 import ChatCompletionV1ChatCompletionsPostBodyMetadataType0
        from ..models.chat_completion_v1_chat_completions_post_body_response_format_type_0 import ChatCompletionV1ChatCompletionsPostBodyResponseFormatType0
        from ..models.chat_completion_v1_chat_completions_post_body_stream_options_type_0 import ChatCompletionV1ChatCompletionsPostBodyStreamOptionsType0
        from ..models.chat_completion_v1_chat_completions_post_body_tool_choice_type_1 import ChatCompletionV1ChatCompletionsPostBodyToolChoiceType1
        from ..models.chat_completion_v1_chat_completions_post_body_tools_type_0_item import ChatCompletionV1ChatCompletionsPostBodyToolsType0Item
        d = dict(src_dict)
        model = d.pop("model")

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in (_messages):
            def _parse_messages_item(data: object) -> ChatCompletionAssistantMessage | ChatCompletionDeveloperMessage | ChatCompletionFunctionMessage | ChatCompletionSystemMessage | ChatCompletionToolMessage | ChatCompletionUserMessage:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_0 = ChatCompletionUserMessage.from_dict(data)



                    return messages_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_1 = ChatCompletionAssistantMessage.from_dict(data)



                    return messages_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_2 = ChatCompletionToolMessage.from_dict(data)



                    return messages_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_3 = ChatCompletionSystemMessage.from_dict(data)



                    return messages_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_4 = ChatCompletionFunctionMessage.from_dict(data)



                    return messages_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                messages_item_type_5 = ChatCompletionDeveloperMessage.from_dict(data)



                return messages_item_type_5

            messages_item = _parse_messages_item(messages_item_data)

            messages.append(messages_item)


        def _parse_frequency_penalty(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        frequency_penalty = _parse_frequency_penalty(d.pop("frequency_penalty", UNSET))


        def _parse_logit_bias(data: object) -> ChatCompletionV1ChatCompletionsPostBodyLogitBiasType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                logit_bias_type_0 = ChatCompletionV1ChatCompletionsPostBodyLogitBiasType0.from_dict(data)



                return logit_bias_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatCompletionV1ChatCompletionsPostBodyLogitBiasType0 | None | Unset, data)

        logit_bias = _parse_logit_bias(d.pop("logit_bias", UNSET))


        def _parse_logprobs(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        logprobs = _parse_logprobs(d.pop("logprobs", UNSET))


        def _parse_top_logprobs(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        top_logprobs = _parse_top_logprobs(d.pop("top_logprobs", UNSET))


        def _parse_max_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_tokens = _parse_max_tokens(d.pop("max_tokens", UNSET))


        def _parse_n(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        n = _parse_n(d.pop("n", UNSET))


        def _parse_presence_penalty(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        presence_penalty = _parse_presence_penalty(d.pop("presence_penalty", UNSET))


        def _parse_response_format(data: object) -> ChatCompletionV1ChatCompletionsPostBodyResponseFormatType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_format_type_0 = ChatCompletionV1ChatCompletionsPostBodyResponseFormatType0.from_dict(data)



                return response_format_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatCompletionV1ChatCompletionsPostBodyResponseFormatType0 | None | Unset, data)

        response_format = _parse_response_format(d.pop("response_format", UNSET))


        def _parse_seed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        seed = _parse_seed(d.pop("seed", UNSET))


        def _parse_service_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_tier = _parse_service_tier(d.pop("service_tier", UNSET))


        def _parse_stop(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stop_type_1 = cast(list[str], data)

                return stop_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | str | Unset, data)

        stop = _parse_stop(d.pop("stop", UNSET))


        def _parse_stream_options(data: object) -> ChatCompletionV1ChatCompletionsPostBodyStreamOptionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stream_options_type_0 = ChatCompletionV1ChatCompletionsPostBodyStreamOptionsType0.from_dict(data)



                return stream_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatCompletionV1ChatCompletionsPostBodyStreamOptionsType0 | None | Unset, data)

        stream_options = _parse_stream_options(d.pop("stream_options", UNSET))


        def _parse_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))


        def _parse_top_p(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        top_p = _parse_top_p(d.pop("top_p", UNSET))


        def _parse_tools(data: object) -> list[ChatCompletionV1ChatCompletionsPostBodyToolsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tools_type_0 = []
                _tools_type_0 = data
                for tools_type_0_item_data in (_tools_type_0):
                    tools_type_0_item = ChatCompletionV1ChatCompletionsPostBodyToolsType0Item.from_dict(tools_type_0_item_data)



                    tools_type_0.append(tools_type_0_item)

                return tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ChatCompletionV1ChatCompletionsPostBodyToolsType0Item] | None | Unset, data)

        tools = _parse_tools(d.pop("tools", UNSET))


        def _parse_tool_choice(data: object) -> ChatCompletionV1ChatCompletionsPostBodyToolChoiceType1 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tool_choice_type_1 = ChatCompletionV1ChatCompletionsPostBodyToolChoiceType1.from_dict(data)



                return tool_choice_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatCompletionV1ChatCompletionsPostBodyToolChoiceType1 | None | str | Unset, data)

        tool_choice = _parse_tool_choice(d.pop("tool_choice", UNSET))


        def _parse_parallel_tool_calls(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        parallel_tool_calls = _parse_parallel_tool_calls(d.pop("parallel_tool_calls", UNSET))


        def _parse_function_call(data: object) -> ChatCompletionV1ChatCompletionsPostBodyFunctionCallType1 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                function_call_type_1 = ChatCompletionV1ChatCompletionsPostBodyFunctionCallType1.from_dict(data)



                return function_call_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatCompletionV1ChatCompletionsPostBodyFunctionCallType1 | None | str | Unset, data)

        function_call = _parse_function_call(d.pop("function_call", UNSET))


        def _parse_functions(data: object) -> list[ChatCompletionV1ChatCompletionsPostBodyFunctionsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                functions_type_0 = []
                _functions_type_0 = data
                for functions_type_0_item_data in (_functions_type_0):
                    functions_type_0_item = ChatCompletionV1ChatCompletionsPostBodyFunctionsType0Item.from_dict(functions_type_0_item_data)



                    functions_type_0.append(functions_type_0_item)

                return functions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ChatCompletionV1ChatCompletionsPostBodyFunctionsType0Item] | None | Unset, data)

        functions = _parse_functions(d.pop("functions", UNSET))


        def _parse_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user = _parse_user(d.pop("user", UNSET))


        def _parse_stream(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        stream = _parse_stream(d.pop("stream", UNSET))


        def _parse_metadata(data: object) -> ChatCompletionV1ChatCompletionsPostBodyMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = ChatCompletionV1ChatCompletionsPostBodyMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatCompletionV1ChatCompletionsPostBodyMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        def _parse_guardrails(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                guardrails_type_0 = cast(list[str], data)

                return guardrails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        guardrails = _parse_guardrails(d.pop("guardrails", UNSET))


        def _parse_caching(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        caching = _parse_caching(d.pop("caching", UNSET))


        def _parse_num_retries(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_retries = _parse_num_retries(d.pop("num_retries", UNSET))


        def _parse_context_window_fallback_dict(data: object) -> ChatCompletionV1ChatCompletionsPostBodyContextWindowFallbackDictType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_window_fallback_dict_type_0 = ChatCompletionV1ChatCompletionsPostBodyContextWindowFallbackDictType0.from_dict(data)



                return context_window_fallback_dict_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatCompletionV1ChatCompletionsPostBodyContextWindowFallbackDictType0 | None | Unset, data)

        context_window_fallback_dict = _parse_context_window_fallback_dict(d.pop("context_window_fallback_dict", UNSET))


        def _parse_fallbacks(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fallbacks_type_0 = cast(list[str], data)

                return fallbacks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        fallbacks = _parse_fallbacks(d.pop("fallbacks", UNSET))


        chat_completion_v1_chat_completions_post_body = cls(
            model=model,
            messages=messages,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            logprobs=logprobs,
            top_logprobs=top_logprobs,
            max_tokens=max_tokens,
            n=n,
            presence_penalty=presence_penalty,
            response_format=response_format,
            seed=seed,
            service_tier=service_tier,
            stop=stop,
            stream_options=stream_options,
            temperature=temperature,
            top_p=top_p,
            tools=tools,
            tool_choice=tool_choice,
            parallel_tool_calls=parallel_tool_calls,
            function_call=function_call,
            functions=functions,
            user=user,
            stream=stream,
            metadata=metadata,
            guardrails=guardrails,
            caching=caching,
            num_retries=num_retries,
            context_window_fallback_dict=context_window_fallback_dict,
            fallbacks=fallbacks,
        )


        chat_completion_v1_chat_completions_post_body.additional_properties = d
        return chat_completion_v1_chat_completions_post_body

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
