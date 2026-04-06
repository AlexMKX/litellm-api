from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, cast






T = TypeVar("T", bound="ChatCompletionReasoningSummaryTextBlock")



@_attrs_define
class ChatCompletionReasoningSummaryTextBlock:
    """ 
        Attributes:
            type_ (Literal['summary_text']):
            text (str | Unset):
     """

    type_: Literal['summary_text']
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal['summary_text'] , d.pop("type"))
        if type_ != 'summary_text':
            raise ValueError(f"type must match const 'summary_text', got '{type_}'")

        text = d.pop("text", UNSET)

        chat_completion_reasoning_summary_text_block = cls(
            type_=type_,
            text=text,
        )


        chat_completion_reasoning_summary_text_block.additional_properties = d
        return chat_completion_reasoning_summary_text_block

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
