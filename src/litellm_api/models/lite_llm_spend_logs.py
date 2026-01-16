from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.lite_llm_spend_logs_messages_type_2 import LiteLLMSpendLogsMessagesType2
  from ..models.lite_llm_spend_logs_response_type_2 import LiteLLMSpendLogsResponseType2





T = TypeVar("T", bound="LiteLLMSpendLogs")



@_attrs_define
class LiteLLMSpendLogs:
    """ 
        Attributes:
            request_id (str):
            api_key (str):
            call_type (str):
            start_time (datetime.datetime | None | str):
            end_time (datetime.datetime | None | str):
            messages (list[Any] | LiteLLMSpendLogsMessagesType2 | None | str):
            response (list[Any] | LiteLLMSpendLogsResponseType2 | None | str):
            model (None | str | Unset):  Default: ''.
            api_base (None | str | Unset):  Default: ''.
            spend (float | None | Unset):  Default: 0.0.
            total_tokens (int | None | Unset):  Default: 0.
            prompt_tokens (int | None | Unset):  Default: 0.
            completion_tokens (int | None | Unset):  Default: 0.
            user (None | str | Unset):  Default: ''.
            metadata (Any | None | Unset):  Default: {}.
            cache_hit (None | str | Unset):  Default: 'False'.
            cache_key (None | str | Unset):
            request_tags (Any | None | Unset):
            requester_ip_address (None | str | Unset):
     """

    request_id: str
    api_key: str
    call_type: str
    start_time: datetime.datetime | None | str
    end_time: datetime.datetime | None | str
    messages: list[Any] | LiteLLMSpendLogsMessagesType2 | None | str
    response: list[Any] | LiteLLMSpendLogsResponseType2 | None | str
    model: None | str | Unset = ''
    api_base: None | str | Unset = ''
    spend: float | None | Unset = 0.0
    total_tokens: int | None | Unset = 0
    prompt_tokens: int | None | Unset = 0
    completion_tokens: int | None | Unset = 0
    user: None | str | Unset = ''
    metadata: Any | None | Unset = {}
    cache_hit: None | str | Unset = 'False'
    cache_key: None | str | Unset = UNSET
    request_tags: Any | None | Unset = UNSET
    requester_ip_address: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_spend_logs_response_type_2 import LiteLLMSpendLogsResponseType2
        from ..models.lite_llm_spend_logs_messages_type_2 import LiteLLMSpendLogsMessagesType2
        request_id = self.request_id

        api_key = self.api_key

        call_type = self.call_type

        start_time: None | str
        if isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: None | str
        if isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        messages: dict[str, Any] | list[Any] | None | str
        if isinstance(self.messages, list):
            messages = self.messages


        elif isinstance(self.messages, LiteLLMSpendLogsMessagesType2):
            messages = self.messages.to_dict()
        else:
            messages = self.messages

        response: dict[str, Any] | list[Any] | None | str
        if isinstance(self.response, list):
            response = self.response


        elif isinstance(self.response, LiteLLMSpendLogsResponseType2):
            response = self.response.to_dict()
        else:
            response = self.response

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        api_base: None | str | Unset
        if isinstance(self.api_base, Unset):
            api_base = UNSET
        else:
            api_base = self.api_base

        spend: float | None | Unset
        if isinstance(self.spend, Unset):
            spend = UNSET
        else:
            spend = self.spend

        total_tokens: int | None | Unset
        if isinstance(self.total_tokens, Unset):
            total_tokens = UNSET
        else:
            total_tokens = self.total_tokens

        prompt_tokens: int | None | Unset
        if isinstance(self.prompt_tokens, Unset):
            prompt_tokens = UNSET
        else:
            prompt_tokens = self.prompt_tokens

        completion_tokens: int | None | Unset
        if isinstance(self.completion_tokens, Unset):
            completion_tokens = UNSET
        else:
            completion_tokens = self.completion_tokens

        user: None | str | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        metadata: Any | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        else:
            metadata = self.metadata

        cache_hit: None | str | Unset
        if isinstance(self.cache_hit, Unset):
            cache_hit = UNSET
        else:
            cache_hit = self.cache_hit

        cache_key: None | str | Unset
        if isinstance(self.cache_key, Unset):
            cache_key = UNSET
        else:
            cache_key = self.cache_key

        request_tags: Any | None | Unset
        if isinstance(self.request_tags, Unset):
            request_tags = UNSET
        else:
            request_tags = self.request_tags

        requester_ip_address: None | str | Unset
        if isinstance(self.requester_ip_address, Unset):
            requester_ip_address = UNSET
        else:
            requester_ip_address = self.requester_ip_address


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "request_id": request_id,
            "api_key": api_key,
            "call_type": call_type,
            "startTime": start_time,
            "endTime": end_time,
            "messages": messages,
            "response": response,
        })
        if model is not UNSET:
            field_dict["model"] = model
        if api_base is not UNSET:
            field_dict["api_base"] = api_base
        if spend is not UNSET:
            field_dict["spend"] = spend
        if total_tokens is not UNSET:
            field_dict["total_tokens"] = total_tokens
        if prompt_tokens is not UNSET:
            field_dict["prompt_tokens"] = prompt_tokens
        if completion_tokens is not UNSET:
            field_dict["completion_tokens"] = completion_tokens
        if user is not UNSET:
            field_dict["user"] = user
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if cache_hit is not UNSET:
            field_dict["cache_hit"] = cache_hit
        if cache_key is not UNSET:
            field_dict["cache_key"] = cache_key
        if request_tags is not UNSET:
            field_dict["request_tags"] = request_tags
        if requester_ip_address is not UNSET:
            field_dict["requester_ip_address"] = requester_ip_address

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_spend_logs_messages_type_2 import LiteLLMSpendLogsMessagesType2
        from ..models.lite_llm_spend_logs_response_type_2 import LiteLLMSpendLogsResponseType2
        d = dict(src_dict)
        request_id = d.pop("request_id")

        api_key = d.pop("api_key")

        call_type = d.pop("call_type")

        def _parse_start_time(data: object) -> datetime.datetime | None | str:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_1 = isoparse(data)



                return start_time_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | str, data)

        start_time = _parse_start_time(d.pop("startTime"))


        def _parse_end_time(data: object) -> datetime.datetime | None | str:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_1 = isoparse(data)



                return end_time_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | str, data)

        end_time = _parse_end_time(d.pop("endTime"))


        def _parse_messages(data: object) -> list[Any] | LiteLLMSpendLogsMessagesType2 | None | str:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                messages_type_1 = cast(list[Any], data)

                return messages_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                messages_type_2 = LiteLLMSpendLogsMessagesType2.from_dict(data)



                return messages_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | LiteLLMSpendLogsMessagesType2 | None | str, data)

        messages = _parse_messages(d.pop("messages"))


        def _parse_response(data: object) -> list[Any] | LiteLLMSpendLogsResponseType2 | None | str:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_type_1 = cast(list[Any], data)

                return response_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_type_2 = LiteLLMSpendLogsResponseType2.from_dict(data)



                return response_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | LiteLLMSpendLogsResponseType2 | None | str, data)

        response = _parse_response(d.pop("response"))


        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        def _parse_api_base(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_base = _parse_api_base(d.pop("api_base", UNSET))


        def _parse_spend(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        spend = _parse_spend(d.pop("spend", UNSET))


        def _parse_total_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_tokens = _parse_total_tokens(d.pop("total_tokens", UNSET))


        def _parse_prompt_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prompt_tokens = _parse_prompt_tokens(d.pop("prompt_tokens", UNSET))


        def _parse_completion_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        completion_tokens = _parse_completion_tokens(d.pop("completion_tokens", UNSET))


        def _parse_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user = _parse_user(d.pop("user", UNSET))


        def _parse_metadata(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        def _parse_cache_hit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cache_hit = _parse_cache_hit(d.pop("cache_hit", UNSET))


        def _parse_cache_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cache_key = _parse_cache_key(d.pop("cache_key", UNSET))


        def _parse_request_tags(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        request_tags = _parse_request_tags(d.pop("request_tags", UNSET))


        def _parse_requester_ip_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requester_ip_address = _parse_requester_ip_address(d.pop("requester_ip_address", UNSET))


        lite_llm_spend_logs = cls(
            request_id=request_id,
            api_key=api_key,
            call_type=call_type,
            start_time=start_time,
            end_time=end_time,
            messages=messages,
            response=response,
            model=model,
            api_base=api_base,
            spend=spend,
            total_tokens=total_tokens,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            user=user,
            metadata=metadata,
            cache_hit=cache_hit,
            cache_key=cache_key,
            request_tags=request_tags,
            requester_ip_address=requester_ip_address,
        )


        lite_llm_spend_logs.additional_properties = d
        return lite_llm_spend_logs

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
