from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.chat_completion_text_object import ChatCompletionTextObject





T = TypeVar("T", bound="ChatCompletionFunctionMessage")



@_attrs_define
class ChatCompletionFunctionMessage:
    """ 
        Attributes:
            role (Literal['function']):
            content (list[ChatCompletionTextObject] | None | str):
            name (str):
            tool_call_id (None | str):
     """

    role: Literal['function']
    content: list[ChatCompletionTextObject] | None | str
    name: str
    tool_call_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_text_object import ChatCompletionTextObject
        role = self.role

        content: list[dict[str, Any]] | None | str
        if isinstance(self.content, list):
            content = []
            for content_type_1_item_data in self.content:
                content_type_1_item = content_type_1_item_data.to_dict()
                content.append(content_type_1_item)


        else:
            content = self.content

        name = self.name

        tool_call_id: None | str
        tool_call_id = self.tool_call_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "role": role,
            "content": content,
            "name": name,
            "tool_call_id": tool_call_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_text_object import ChatCompletionTextObject
        d = dict(src_dict)
        role = cast(Literal['function'] , d.pop("role"))
        if role != 'function':
            raise ValueError(f"role must match const 'function', got '{role}'")

        def _parse_content(data: object) -> list[ChatCompletionTextObject] | None | str:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_type_1 = []
                _content_type_1 = data
                for content_type_1_item_data in (_content_type_1):
                    content_type_1_item = ChatCompletionTextObject.from_dict(content_type_1_item_data)



                    content_type_1.append(content_type_1_item)

                return content_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ChatCompletionTextObject] | None | str, data)

        content = _parse_content(d.pop("content"))


        name = d.pop("name")

        def _parse_tool_call_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tool_call_id = _parse_tool_call_id(d.pop("tool_call_id"))


        chat_completion_function_message = cls(
            role=role,
            content=content,
            name=name,
            tool_call_id=tool_call_id,
        )


        chat_completion_function_message.additional_properties = d
        return chat_completion_function_message

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
