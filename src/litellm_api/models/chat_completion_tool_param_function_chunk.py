from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chat_completion_tool_param_function_chunk_parameters import ChatCompletionToolParamFunctionChunkParameters





T = TypeVar("T", bound="ChatCompletionToolParamFunctionChunk")



@_attrs_define
class ChatCompletionToolParamFunctionChunk:
    """ 
        Attributes:
            name (str):
            description (str | Unset):
            parameters (ChatCompletionToolParamFunctionChunkParameters | Unset):
            strict (bool | Unset):
     """

    name: str
    description: str | Unset = UNSET
    parameters: ChatCompletionToolParamFunctionChunkParameters | Unset = UNSET
    strict: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_tool_param_function_chunk_parameters import ChatCompletionToolParamFunctionChunkParameters
        name = self.name

        description = self.description

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        strict = self.strict


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if strict is not UNSET:
            field_dict["strict"] = strict

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_tool_param_function_chunk_parameters import ChatCompletionToolParamFunctionChunkParameters
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: ChatCompletionToolParamFunctionChunkParameters | Unset
        if isinstance(_parameters,  Unset):
            parameters = UNSET
        else:
            parameters = ChatCompletionToolParamFunctionChunkParameters.from_dict(_parameters)




        strict = d.pop("strict", UNSET)

        chat_completion_tool_param_function_chunk = cls(
            name=name,
            description=description,
            parameters=parameters,
            strict=strict,
        )


        chat_completion_tool_param_function_chunk.additional_properties = d
        return chat_completion_tool_param_function_chunk

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
