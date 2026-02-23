from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SuggestTemplatesRequest")



@_attrs_define
class SuggestTemplatesRequest:
    """ 
        Attributes:
            attack_examples (list[str] | Unset):
            description (str | Unset):  Default: ''.
            model (None | str | Unset):
     """

    attack_examples: list[str] | Unset = UNSET
    description: str | Unset = ''
    model: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        attack_examples: list[str] | Unset = UNSET
        if not isinstance(self.attack_examples, Unset):
            attack_examples = self.attack_examples



        description = self.description

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attack_examples is not UNSET:
            field_dict["attack_examples"] = attack_examples
        if description is not UNSET:
            field_dict["description"] = description
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attack_examples = cast(list[str], d.pop("attack_examples", UNSET))


        description = d.pop("description", UNSET)

        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        suggest_templates_request = cls(
            attack_examples=attack_examples,
            description=description,
            model=model,
        )


        suggest_templates_request.additional_properties = d
        return suggest_templates_request

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
