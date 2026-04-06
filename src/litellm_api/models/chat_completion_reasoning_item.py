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
  from ..models.chat_completion_reasoning_summary_text_block import ChatCompletionReasoningSummaryTextBlock





T = TypeVar("T", bound="ChatCompletionReasoningItem")



@_attrs_define
class ChatCompletionReasoningItem:
    """ Represents an OpenAI Responses API reasoning item for round-tripping in conversation history.

        Attributes:
            type_ (Literal['reasoning']):
            id (str | Unset):
            encrypted_content (None | str | Unset):
            summary (list[ChatCompletionReasoningSummaryTextBlock] | Unset):
     """

    type_: Literal['reasoning']
    id: str | Unset = UNSET
    encrypted_content: None | str | Unset = UNSET
    summary: list[ChatCompletionReasoningSummaryTextBlock] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_reasoning_summary_text_block import ChatCompletionReasoningSummaryTextBlock
        type_ = self.type_

        id = self.id

        encrypted_content: None | str | Unset
        if isinstance(self.encrypted_content, Unset):
            encrypted_content = UNSET
        else:
            encrypted_content = self.encrypted_content

        summary: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = []
            for summary_item_data in self.summary:
                summary_item = summary_item_data.to_dict()
                summary.append(summary_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if encrypted_content is not UNSET:
            field_dict["encrypted_content"] = encrypted_content
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_reasoning_summary_text_block import ChatCompletionReasoningSummaryTextBlock
        d = dict(src_dict)
        type_ = cast(Literal['reasoning'] , d.pop("type"))
        if type_ != 'reasoning':
            raise ValueError(f"type must match const 'reasoning', got '{type_}'")

        id = d.pop("id", UNSET)

        def _parse_encrypted_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        encrypted_content = _parse_encrypted_content(d.pop("encrypted_content", UNSET))


        _summary = d.pop("summary", UNSET)
        summary: list[ChatCompletionReasoningSummaryTextBlock] | Unset = UNSET
        if _summary is not UNSET:
            summary = []
            for summary_item_data in _summary:
                summary_item = ChatCompletionReasoningSummaryTextBlock.from_dict(summary_item_data)



                summary.append(summary_item)


        chat_completion_reasoning_item = cls(
            type_=type_,
            id=id,
            encrypted_content=encrypted_content,
            summary=summary,
        )


        chat_completion_reasoning_item.additional_properties = d
        return chat_completion_reasoning_item

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
