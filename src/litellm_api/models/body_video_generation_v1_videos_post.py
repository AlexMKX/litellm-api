from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import File, FileTypes
from ..types import UNSET, Unset
from io import BytesIO
from typing import cast






T = TypeVar("T", bound="BodyVideoGenerationV1VideosPost")



@_attrs_define
class BodyVideoGenerationV1VideosPost:
    """ 
        Attributes:
            input_reference (File | None | Unset):
     """

    input_reference: File | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        input_reference: FileTypes | None | Unset
        if isinstance(self.input_reference, Unset):
            input_reference = UNSET
        elif isinstance(self.input_reference, File):
            input_reference = self.input_reference.to_tuple()

        else:
            input_reference = self.input_reference


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if input_reference is not UNSET:
            field_dict["input_reference"] = input_reference

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.input_reference, Unset):
            if isinstance(self.input_reference, File):

                files.append(("input_reference", self.input_reference.to_tuple()))
            else:
                files.append(("input_reference", (None, str(self.input_reference).encode(), "text/plain")))



        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_input_reference(data: object) -> File | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                input_reference_type_0 = File(
                     payload = BytesIO(data)
                )



                return input_reference_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(File | None | Unset, data)

        input_reference = _parse_input_reference(d.pop("input_reference", UNSET))


        body_video_generation_v1_videos_post = cls(
            input_reference=input_reference,
        )


        body_video_generation_v1_videos_post.additional_properties = d
        return body_video_generation_v1_videos_post

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
