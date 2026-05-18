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





T = TypeVar("T", bound="ChatCompletionToolCallChunk")



@_attrs_define
class ChatCompletionToolCallChunk:
    """ 
        Attributes:
            function (ChatCompletionToolCallFunctionChunk):
            id (None | str):
            index (int):
            type_ (Literal['function']):
     """

    function: ChatCompletionToolCallFunctionChunk
    id: None | str
    index: int
    type_: Literal['function']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_tool_call_function_chunk import ChatCompletionToolCallFunctionChunk
        function = self.function.to_dict()

        id: None | str
        id = self.id

        index = self.index

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "function": function,
            "id": id,
            "index": index,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_tool_call_function_chunk import ChatCompletionToolCallFunctionChunk
        d = dict(src_dict)
        function = ChatCompletionToolCallFunctionChunk.from_dict(d.pop("function"))




        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))


        index = d.pop("index")

        type_ = cast(Literal['function'] , d.pop("type"))
        if type_ != 'function':
            raise ValueError(f"type must match const 'function', got '{type_}'")

        chat_completion_tool_call_chunk = cls(
            function=function,
            id=id,
            index=index,
            type_=type_,
        )


        chat_completion_tool_call_chunk.additional_properties = d
        return chat_completion_tool_call_chunk

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
