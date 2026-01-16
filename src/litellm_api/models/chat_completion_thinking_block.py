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
  from ..models.chat_completion_thinking_block_cache_control_type_0 import ChatCompletionThinkingBlockCacheControlType0





T = TypeVar("T", bound="ChatCompletionThinkingBlock")



@_attrs_define
class ChatCompletionThinkingBlock:
    """ 
        Attributes:
            type_ (Literal['thinking']):
            thinking (str | Unset):
            signature (str | Unset):
            cache_control (ChatCompletionCachedContent | ChatCompletionThinkingBlockCacheControlType0 | None | Unset):
     """

    type_: Literal['thinking']
    thinking: str | Unset = UNSET
    signature: str | Unset = UNSET
    cache_control: ChatCompletionCachedContent | ChatCompletionThinkingBlockCacheControlType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_cached_content import ChatCompletionCachedContent
        from ..models.chat_completion_thinking_block_cache_control_type_0 import ChatCompletionThinkingBlockCacheControlType0
        type_ = self.type_

        thinking = self.thinking

        signature = self.signature

        cache_control: dict[str, Any] | None | Unset
        if isinstance(self.cache_control, Unset):
            cache_control = UNSET
        elif isinstance(self.cache_control, ChatCompletionThinkingBlockCacheControlType0):
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
        if thinking is not UNSET:
            field_dict["thinking"] = thinking
        if signature is not UNSET:
            field_dict["signature"] = signature
        if cache_control is not UNSET:
            field_dict["cache_control"] = cache_control

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_cached_content import ChatCompletionCachedContent
        from ..models.chat_completion_thinking_block_cache_control_type_0 import ChatCompletionThinkingBlockCacheControlType0
        d = dict(src_dict)
        type_ = cast(Literal['thinking'] , d.pop("type"))
        if type_ != 'thinking':
            raise ValueError(f"type must match const 'thinking', got '{type_}'")

        thinking = d.pop("thinking", UNSET)

        signature = d.pop("signature", UNSET)

        def _parse_cache_control(data: object) -> ChatCompletionCachedContent | ChatCompletionThinkingBlockCacheControlType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cache_control_type_0 = ChatCompletionThinkingBlockCacheControlType0.from_dict(data)



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
            return cast(ChatCompletionCachedContent | ChatCompletionThinkingBlockCacheControlType0 | None | Unset, data)

        cache_control = _parse_cache_control(d.pop("cache_control", UNSET))


        chat_completion_thinking_block = cls(
            type_=type_,
            thinking=thinking,
            signature=signature,
            cache_control=cache_control,
        )


        chat_completion_thinking_block.additional_properties = d
        return chat_completion_thinking_block

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
