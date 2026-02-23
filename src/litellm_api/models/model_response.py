from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.choices import Choices
  from ..models.streaming_choices import StreamingChoices





T = TypeVar("T", bound="ModelResponse")



@_attrs_define
class ModelResponse:
    """ 
        Attributes:
            id (str):
            created (int):
            object_ (str):
            choices (list[Choices | StreamingChoices]):
            model (None | str | Unset):
            system_fingerprint (None | str | Unset):
     """

    id: str
    created: int
    object_: str
    choices: list[Choices | StreamingChoices]
    model: None | str | Unset = UNSET
    system_fingerprint: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.streaming_choices import StreamingChoices
        from ..models.choices import Choices
        id = self.id

        created = self.created

        object_ = self.object_

        choices = []
        for choices_item_data in self.choices:
            choices_item: dict[str, Any]
            if isinstance(choices_item_data, Choices):
                choices_item = choices_item_data.to_dict()
            else:
                choices_item = choices_item_data.to_dict()

            choices.append(choices_item)



        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        system_fingerprint: None | str | Unset
        if isinstance(self.system_fingerprint, Unset):
            system_fingerprint = UNSET
        else:
            system_fingerprint = self.system_fingerprint


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "created": created,
            "object": object_,
            "choices": choices,
        })
        if model is not UNSET:
            field_dict["model"] = model
        if system_fingerprint is not UNSET:
            field_dict["system_fingerprint"] = system_fingerprint

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.choices import Choices
        from ..models.streaming_choices import StreamingChoices
        d = dict(src_dict)
        id = d.pop("id")

        created = d.pop("created")

        object_ = d.pop("object")

        choices = []
        _choices = d.pop("choices")
        for choices_item_data in (_choices):
            def _parse_choices_item(data: object) -> Choices | StreamingChoices:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    choices_item_type_0 = Choices.from_dict(data)



                    return choices_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                choices_item_type_1 = StreamingChoices.from_dict(data)



                return choices_item_type_1

            choices_item = _parse_choices_item(choices_item_data)

            choices.append(choices_item)


        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        def _parse_system_fingerprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_fingerprint = _parse_system_fingerprint(d.pop("system_fingerprint", UNSET))


        model_response = cls(
            id=id,
            created=created,
            object_=object_,
            choices=choices,
            model=model,
            system_fingerprint=system_fingerprint,
        )


        model_response.additional_properties = d
        return model_response

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
