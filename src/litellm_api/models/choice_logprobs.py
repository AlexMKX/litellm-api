from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chat_completion_token_logprob import ChatCompletionTokenLogprob





T = TypeVar("T", bound="ChoiceLogprobs")



@_attrs_define
class ChoiceLogprobs:
    """ 
        Attributes:
            content (list[ChatCompletionTokenLogprob] | None | Unset):
     """

    content: list[ChatCompletionTokenLogprob] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_token_logprob import ChatCompletionTokenLogprob
        content: list[dict[str, Any]] | None | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, list):
            content = []
            for content_type_0_item_data in self.content:
                content_type_0_item = content_type_0_item_data.to_dict()
                content.append(content_type_0_item)


        else:
            content = self.content


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_token_logprob import ChatCompletionTokenLogprob
        d = dict(src_dict)
        def _parse_content(data: object) -> list[ChatCompletionTokenLogprob] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_type_0 = []
                _content_type_0 = data
                for content_type_0_item_data in (_content_type_0):
                    content_type_0_item = ChatCompletionTokenLogprob.from_dict(content_type_0_item_data)



                    content_type_0.append(content_type_0_item)

                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ChatCompletionTokenLogprob] | None | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        choice_logprobs = cls(
            content=content,
        )


        choice_logprobs.additional_properties = d
        return choice_logprobs

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
