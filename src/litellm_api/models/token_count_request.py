from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.token_count_request_contents_type_0_item import TokenCountRequestContentsType0Item
  from ..models.token_count_request_messages_type_0_item import TokenCountRequestMessagesType0Item





T = TypeVar("T", bound="TokenCountRequest")



@_attrs_define
class TokenCountRequest:
    """ 
        Attributes:
            model (str):
            prompt (None | str | Unset):
            messages (list[TokenCountRequestMessagesType0Item] | None | Unset):
            contents (list[TokenCountRequestContentsType0Item] | None | Unset):
     """

    model: str
    prompt: None | str | Unset = UNSET
    messages: list[TokenCountRequestMessagesType0Item] | None | Unset = UNSET
    contents: list[TokenCountRequestContentsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.token_count_request_contents_type_0_item import TokenCountRequestContentsType0Item
        from ..models.token_count_request_messages_type_0_item import TokenCountRequestMessagesType0Item
        model = self.model

        prompt: None | str | Unset
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

        messages: list[dict[str, Any]] | None | Unset
        if isinstance(self.messages, Unset):
            messages = UNSET
        elif isinstance(self.messages, list):
            messages = []
            for messages_type_0_item_data in self.messages:
                messages_type_0_item = messages_type_0_item_data.to_dict()
                messages.append(messages_type_0_item)


        else:
            messages = self.messages

        contents: list[dict[str, Any]] | None | Unset
        if isinstance(self.contents, Unset):
            contents = UNSET
        elif isinstance(self.contents, list):
            contents = []
            for contents_type_0_item_data in self.contents:
                contents_type_0_item = contents_type_0_item_data.to_dict()
                contents.append(contents_type_0_item)


        else:
            contents = self.contents


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "model": model,
        })
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if messages is not UNSET:
            field_dict["messages"] = messages
        if contents is not UNSET:
            field_dict["contents"] = contents

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_count_request_contents_type_0_item import TokenCountRequestContentsType0Item
        from ..models.token_count_request_messages_type_0_item import TokenCountRequestMessagesType0Item
        d = dict(src_dict)
        model = d.pop("model")

        def _parse_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))


        def _parse_messages(data: object) -> list[TokenCountRequestMessagesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                messages_type_0 = []
                _messages_type_0 = data
                for messages_type_0_item_data in (_messages_type_0):
                    messages_type_0_item = TokenCountRequestMessagesType0Item.from_dict(messages_type_0_item_data)



                    messages_type_0.append(messages_type_0_item)

                return messages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TokenCountRequestMessagesType0Item] | None | Unset, data)

        messages = _parse_messages(d.pop("messages", UNSET))


        def _parse_contents(data: object) -> list[TokenCountRequestContentsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                contents_type_0 = []
                _contents_type_0 = data
                for contents_type_0_item_data in (_contents_type_0):
                    contents_type_0_item = TokenCountRequestContentsType0Item.from_dict(contents_type_0_item_data)



                    contents_type_0.append(contents_type_0_item)

                return contents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TokenCountRequestContentsType0Item] | None | Unset, data)

        contents = _parse_contents(d.pop("contents", UNSET))


        token_count_request = cls(
            model=model,
            prompt=prompt,
            messages=messages,
            contents=contents,
        )


        token_count_request.additional_properties = d
        return token_count_request

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
