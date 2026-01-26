from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.policy_list_response_policies import PolicyListResponsePolicies





T = TypeVar("T", bound="PolicyListResponse")



@_attrs_define
class PolicyListResponse:
    """ Response for /policy/list endpoint.

        Attributes:
            policies (PolicyListResponsePolicies):
            total_count (int):
     """

    policies: PolicyListResponsePolicies
    total_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy_list_response_policies import PolicyListResponsePolicies
        policies = self.policies.to_dict()

        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "policies": policies,
            "total_count": total_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_list_response_policies import PolicyListResponsePolicies
        d = dict(src_dict)
        policies = PolicyListResponsePolicies.from_dict(d.pop("policies"))




        total_count = d.pop("total_count")

        policy_list_response = cls(
            policies=policies,
            total_count=total_count,
        )


        policy_list_response.additional_properties = d
        return policy_list_response

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
