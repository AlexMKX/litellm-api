from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChatCompletionFileObjectFile")



@_attrs_define
class ChatCompletionFileObjectFile:
    """ 
        Attributes:
            file_data (str | Unset):
            file_id (str | Unset):
            filename (str | Unset):
            format_ (str | Unset):
     """

    file_data: str | Unset = UNSET
    file_id: str | Unset = UNSET
    filename: str | Unset = UNSET
    format_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file_data = self.file_data

        file_id = self.file_id

        filename = self.filename

        format_ = self.format_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if file_data is not UNSET:
            field_dict["file_data"] = file_data
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if filename is not UNSET:
            field_dict["filename"] = filename
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_data = d.pop("file_data", UNSET)

        file_id = d.pop("file_id", UNSET)

        filename = d.pop("filename", UNSET)

        format_ = d.pop("format", UNSET)

        chat_completion_file_object_file = cls(
            file_data=file_data,
            file_id=file_id,
            filename=filename,
            format_=format_,
        )


        chat_completion_file_object_file.additional_properties = d
        return chat_completion_file_object_file

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
