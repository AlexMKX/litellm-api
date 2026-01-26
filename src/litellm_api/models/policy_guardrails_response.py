from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PolicyGuardrailsResponse")



@_attrs_define
class PolicyGuardrailsResponse:
    """ Guardrails configuration for a policy.

        Attributes:
            add (list[str] | Unset):
            remove (list[str] | Unset):
     """

    add: list[str] | Unset = UNSET
    remove: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        add: list[str] | Unset = UNSET
        if not isinstance(self.add, Unset):
            add = self.add



        remove: list[str] | Unset = UNSET
        if not isinstance(self.remove, Unset):
            remove = self.remove




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if add is not UNSET:
            field_dict["add"] = add
        if remove is not UNSET:
            field_dict["remove"] = remove

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        add = cast(list[str], d.pop("add", UNSET))


        remove = cast(list[str], d.pop("remove", UNSET))


        policy_guardrails_response = cls(
            add=add,
            remove=remove,
        )


        policy_guardrails_response.additional_properties = d
        return policy_guardrails_response

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
