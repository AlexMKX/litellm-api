from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.chat_completion_tool_call_function_chunk import ChatCompletionToolCallFunctionChunk





T = TypeVar("T", bound="ChatCompletionAssistantToolCall")



@_attrs_define
class ChatCompletionAssistantToolCall:
    """ 
        Attributes:
            id (None | str):
            type_ (Literal['function']):
            function (ChatCompletionToolCallFunctionChunk):
     """

    id: None | str
    type_: Literal['function']
    function: ChatCompletionToolCallFunctionChunk
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_tool_call_function_chunk import ChatCompletionToolCallFunctionChunk
        id: None | str
        id = self.id

        type_ = self.type_

        function = self.function.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "type": type_,
            "function": function,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_tool_call_function_chunk import ChatCompletionToolCallFunctionChunk
        d = dict(src_dict)
        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))


        type_ = cast(Literal['function'] , d.pop("type"))
        if type_ != 'function':
            raise ValueError(f"type must match const 'function', got '{type_}'")

        function = ChatCompletionToolCallFunctionChunk.from_dict(d.pop("function"))




        chat_completion_assistant_tool_call = cls(
            id=id,
            type_=type_,
            function=function,
        )


        chat_completion_assistant_tool_call.additional_properties = d
        return chat_completion_assistant_tool_call

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
