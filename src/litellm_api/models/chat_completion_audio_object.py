from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.input_audio import InputAudio





T = TypeVar("T", bound="ChatCompletionAudioObject")



@_attrs_define
class ChatCompletionAudioObject:
    """ 
        Attributes:
            input_audio (InputAudio):
            type_ (Literal['input_audio']):
     """

    input_audio: InputAudio
    type_: Literal['input_audio']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.input_audio import InputAudio
        input_audio = self.input_audio.to_dict()

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "input_audio": input_audio,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_audio import InputAudio
        d = dict(src_dict)
        input_audio = InputAudio.from_dict(d.pop("input_audio"))




        type_ = cast(Literal['input_audio'] , d.pop("type"))
        if type_ != 'input_audio':
            raise ValueError(f"type must match const 'input_audio', got '{type_}'")

        chat_completion_audio_object = cls(
            input_audio=input_audio,
            type_=type_,
        )


        chat_completion_audio_object.additional_properties = d
        return chat_completion_audio_object

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
