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
  from ..models.chat_completion_redacted_thinking_block_cache_control_type_0 import ChatCompletionRedactedThinkingBlockCacheControlType0





T = TypeVar("T", bound="ChatCompletionRedactedThinkingBlock")



@_attrs_define
class ChatCompletionRedactedThinkingBlock:
    """ 
        Attributes:
            type_ (Literal['redacted_thinking']):
            data (str | Unset):
            cache_control (ChatCompletionCachedContent | ChatCompletionRedactedThinkingBlockCacheControlType0 | None |
                Unset):
     """

    type_: Literal['redacted_thinking']
    data: str | Unset = UNSET
    cache_control: ChatCompletionCachedContent | ChatCompletionRedactedThinkingBlockCacheControlType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_cached_content import ChatCompletionCachedContent
        from ..models.chat_completion_redacted_thinking_block_cache_control_type_0 import ChatCompletionRedactedThinkingBlockCacheControlType0
        type_ = self.type_

        data = self.data

        cache_control: dict[str, Any] | None | Unset
        if isinstance(self.cache_control, Unset):
            cache_control = UNSET
        elif isinstance(self.cache_control, ChatCompletionRedactedThinkingBlockCacheControlType0):
            cache_control = self.cache_control.to_dict()
        elif isinstance(self.cache_control, ChatCompletionCachedContent):
            cache_control = self.cache_control.to_dict()
        else:
            cache_control = self.cache_control


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if data is not UNSET:
            field_dict["data"] = data
        if cache_control is not UNSET:
            field_dict["cache_control"] = cache_control

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_cached_content import ChatCompletionCachedContent
        from ..models.chat_completion_redacted_thinking_block_cache_control_type_0 import ChatCompletionRedactedThinkingBlockCacheControlType0
        d = dict(src_dict)
        type_ = cast(Literal['redacted_thinking'] , d.pop("type"))
        if type_ != 'redacted_thinking':
            raise ValueError(f"type must match const 'redacted_thinking', got '{type_}'")

        data = d.pop("data", UNSET)

        def _parse_cache_control(data: object) -> ChatCompletionCachedContent | ChatCompletionRedactedThinkingBlockCacheControlType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cache_control_type_0 = ChatCompletionRedactedThinkingBlockCacheControlType0.from_dict(data)



                return cache_control_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cache_control_type_1 = ChatCompletionCachedContent.from_dict(data)



                return cache_control_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatCompletionCachedContent | ChatCompletionRedactedThinkingBlockCacheControlType0 | None | Unset, data)

        cache_control = _parse_cache_control(d.pop("cache_control", UNSET))


        chat_completion_redacted_thinking_block = cls(
            type_=type_,
            data=data,
            cache_control=cache_control,
        )


        chat_completion_redacted_thinking_block.additional_properties = d
        return chat_completion_redacted_thinking_block

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
