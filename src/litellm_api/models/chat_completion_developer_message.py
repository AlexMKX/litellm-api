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





T = TypeVar("T", bound="ChatCompletionDeveloperMessage")



@_attrs_define
class ChatCompletionDeveloperMessage:
    """ 
        Attributes:
            role (Literal['developer']):
            content (list[Any] | str):
            name (str | Unset):
            cache_control (ChatCompletionCachedContent | Unset):
     """

    role: Literal['developer']
    content: list[Any] | str
    name: str | Unset = UNSET
    cache_control: ChatCompletionCachedContent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_cached_content import ChatCompletionCachedContent
        role = self.role

        content: list[Any] | str
        if isinstance(self.content, list):
            content = self.content


        else:
            content = self.content

        name = self.name

        cache_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cache_control, Unset):
            cache_control = self.cache_control.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "role": role,
            "content": content,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if cache_control is not UNSET:
            field_dict["cache_control"] = cache_control

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_cached_content import ChatCompletionCachedContent
        d = dict(src_dict)
        role = cast(Literal['developer'] , d.pop("role"))
        if role != 'developer':
            raise ValueError(f"role must match const 'developer', got '{role}'")

        def _parse_content(data: object) -> list[Any] | str:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_type_1 = cast(list[Any], data)

                return content_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | str, data)

        content = _parse_content(d.pop("content"))


        name = d.pop("name", UNSET)

        _cache_control = d.pop("cache_control", UNSET)
        cache_control: ChatCompletionCachedContent | Unset
        if isinstance(_cache_control,  Unset):
            cache_control = UNSET
        else:
            cache_control = ChatCompletionCachedContent.from_dict(_cache_control)




        chat_completion_developer_message = cls(
            role=role,
            content=content,
            name=name,
            cache_control=cache_control,
        )


        chat_completion_developer_message.additional_properties = d
        return chat_completion_developer_message

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
