from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PolicyMatchDetail")



@_attrs_define
class PolicyMatchDetail:
    """ Details about why a specific policy matched.

        Attributes:
            policy_name (str): Name of the matched policy.
            matched_via (str): How the policy was matched (e.g., 'tag:healthcare', 'team:health-team', 'scope:*').
            guardrails_added (list[str] | Unset): Guardrails this policy contributes.
     """

    policy_name: str
    matched_via: str
    guardrails_added: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        policy_name = self.policy_name

        matched_via = self.matched_via

        guardrails_added: list[str] | Unset = UNSET
        if not isinstance(self.guardrails_added, Unset):
            guardrails_added = self.guardrails_added




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "policy_name": policy_name,
            "matched_via": matched_via,
        })
        if guardrails_added is not UNSET:
            field_dict["guardrails_added"] = guardrails_added

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        policy_name = d.pop("policy_name")

        matched_via = d.pop("matched_via")

        guardrails_added = cast(list[str], d.pop("guardrails_added", UNSET))


        policy_match_detail = cls(
            policy_name=policy_name,
            matched_via=matched_via,
            guardrails_added=guardrails_added,
        )


        policy_match_detail.additional_properties = d
        return policy_match_detail

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
