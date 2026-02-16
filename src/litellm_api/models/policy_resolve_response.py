from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.policy_match_detail import PolicyMatchDetail





T = TypeVar("T", bound="PolicyResolveResponse")



@_attrs_define
class PolicyResolveResponse:
    """ Response for resolving effective policies/guardrails for a context.

        Attributes:
            effective_guardrails (list[str] | Unset): Final list of guardrails that would be applied.
            matched_policies (list[PolicyMatchDetail] | Unset): Details about each matched policy and why it matched.
     """

    effective_guardrails: list[str] | Unset = UNSET
    matched_policies: list[PolicyMatchDetail] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy_match_detail import PolicyMatchDetail
        effective_guardrails: list[str] | Unset = UNSET
        if not isinstance(self.effective_guardrails, Unset):
            effective_guardrails = self.effective_guardrails



        matched_policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.matched_policies, Unset):
            matched_policies = []
            for matched_policies_item_data in self.matched_policies:
                matched_policies_item = matched_policies_item_data.to_dict()
                matched_policies.append(matched_policies_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if effective_guardrails is not UNSET:
            field_dict["effective_guardrails"] = effective_guardrails
        if matched_policies is not UNSET:
            field_dict["matched_policies"] = matched_policies

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_match_detail import PolicyMatchDetail
        d = dict(src_dict)
        effective_guardrails = cast(list[str], d.pop("effective_guardrails", UNSET))


        _matched_policies = d.pop("matched_policies", UNSET)
        matched_policies: list[PolicyMatchDetail] | Unset = UNSET
        if _matched_policies is not UNSET:
            matched_policies = []
            for matched_policies_item_data in _matched_policies:
                matched_policies_item = PolicyMatchDetail.from_dict(matched_policies_item_data)



                matched_policies.append(matched_policies_item)


        policy_resolve_response = cls(
            effective_guardrails=effective_guardrails,
            matched_policies=matched_policies,
        )


        policy_resolve_response.additional_properties = d
        return policy_resolve_response

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
