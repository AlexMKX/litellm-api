from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chat_completion_tool_call_function_chunk_provider_specific_fields_type_0 import ChatCompletionToolCallFunctionChunkProviderSpecificFieldsType0





T = TypeVar("T", bound="ChatCompletionToolCallFunctionChunk")



@_attrs_define
class ChatCompletionToolCallFunctionChunk:
    """ 
        Attributes:
            name (None | str | Unset):
            arguments (str | Unset):
            provider_specific_fields (ChatCompletionToolCallFunctionChunkProviderSpecificFieldsType0 | None | Unset):
     """

    name: None | str | Unset = UNSET
    arguments: str | Unset = UNSET
    provider_specific_fields: ChatCompletionToolCallFunctionChunkProviderSpecificFieldsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_tool_call_function_chunk_provider_specific_fields_type_0 import ChatCompletionToolCallFunctionChunkProviderSpecificFieldsType0
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        arguments = self.arguments

        provider_specific_fields: dict[str, Any] | None | Unset
        if isinstance(self.provider_specific_fields, Unset):
            provider_specific_fields = UNSET
        elif isinstance(self.provider_specific_fields, ChatCompletionToolCallFunctionChunkProviderSpecificFieldsType0):
            provider_specific_fields = self.provider_specific_fields.to_dict()
        else:
            provider_specific_fields = self.provider_specific_fields


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if arguments is not UNSET:
            field_dict["arguments"] = arguments
        if provider_specific_fields is not UNSET:
            field_dict["provider_specific_fields"] = provider_specific_fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_tool_call_function_chunk_provider_specific_fields_type_0 import ChatCompletionToolCallFunctionChunkProviderSpecificFieldsType0
        d = dict(src_dict)
        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        arguments = d.pop("arguments", UNSET)

        def _parse_provider_specific_fields(data: object) -> ChatCompletionToolCallFunctionChunkProviderSpecificFieldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_specific_fields_type_0 = ChatCompletionToolCallFunctionChunkProviderSpecificFieldsType0.from_dict(data)



                return provider_specific_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatCompletionToolCallFunctionChunkProviderSpecificFieldsType0 | None | Unset, data)

        provider_specific_fields = _parse_provider_specific_fields(d.pop("provider_specific_fields", UNSET))


        chat_completion_tool_call_function_chunk = cls(
            name=name,
            arguments=arguments,
            provider_specific_fields=provider_specific_fields,
        )


        chat_completion_tool_call_function_chunk.additional_properties = d
        return chat_completion_tool_call_function_chunk

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
