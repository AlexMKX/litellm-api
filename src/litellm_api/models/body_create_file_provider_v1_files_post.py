from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import File, FileTypes
from ..types import UNSET, Unset
from io import BytesIO
from typing import cast






T = TypeVar("T", bound="BodyCreateFileProviderV1FilesPost")



@_attrs_define
class BodyCreateFileProviderV1FilesPost:
    """ 
        Attributes:
            purpose (str):
            file (File):
            target_model_names (str | Unset):  Default: ''.
            target_storage (str | Unset):  Default: 'default'.
            custom_llm_provider (str | Unset):  Default: 'openai'.
            litellm_metadata (None | str | Unset):
     """

    purpose: str
    file: File
    target_model_names: str | Unset = ''
    target_storage: str | Unset = 'default'
    custom_llm_provider: str | Unset = 'openai'
    litellm_metadata: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        purpose = self.purpose

        file = self.file.to_tuple()


        target_model_names = self.target_model_names

        target_storage = self.target_storage

        custom_llm_provider = self.custom_llm_provider

        litellm_metadata: None | str | Unset
        if isinstance(self.litellm_metadata, Unset):
            litellm_metadata = UNSET
        else:
            litellm_metadata = self.litellm_metadata


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "purpose": purpose,
            "file": file,
        })
        if target_model_names is not UNSET:
            field_dict["target_model_names"] = target_model_names
        if target_storage is not UNSET:
            field_dict["target_storage"] = target_storage
        if custom_llm_provider is not UNSET:
            field_dict["custom_llm_provider"] = custom_llm_provider
        if litellm_metadata is not UNSET:
            field_dict["litellm_metadata"] = litellm_metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        purpose = d.pop("purpose")

        file = File(
             payload = BytesIO(d.pop("file"))
        )




        target_model_names = d.pop("target_model_names", UNSET)

        target_storage = d.pop("target_storage", UNSET)

        custom_llm_provider = d.pop("custom_llm_provider", UNSET)

        def _parse_litellm_metadata(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        litellm_metadata = _parse_litellm_metadata(d.pop("litellm_metadata", UNSET))


        body_create_file_provider_v1_files_post = cls(
            purpose=purpose,
            file=file,
            target_model_names=target_model_names,
            target_storage=target_storage,
            custom_llm_provider=custom_llm_provider,
            litellm_metadata=litellm_metadata,
        )


        body_create_file_provider_v1_files_post.additional_properties = d
        return body_create_file_provider_v1_files_post

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
