from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.chat_completion_file_object_file import ChatCompletionFileObjectFile





T = TypeVar("T", bound="ChatCompletionFileObject")



@_attrs_define
class ChatCompletionFileObject:
    """ 
        Attributes:
            type_ (Literal['file']):
            file (ChatCompletionFileObjectFile):
     """

    type_: Literal['file']
    file: ChatCompletionFileObjectFile
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_file_object_file import ChatCompletionFileObjectFile
        type_ = self.type_

        file = self.file.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "file": file,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_file_object_file import ChatCompletionFileObjectFile
        d = dict(src_dict)
        type_ = cast(Literal['file'] , d.pop("type"))
        if type_ != 'file':
            raise ValueError(f"type must match const 'file', got '{type_}'")

        file = ChatCompletionFileObjectFile.from_dict(d.pop("file"))




        chat_completion_file_object = cls(
            type_=type_,
            file=file,
        )


        chat_completion_file_object.additional_properties = d
        return chat_completion_file_object

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
