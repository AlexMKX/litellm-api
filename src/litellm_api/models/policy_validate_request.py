from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.policy_validate_request_policies import PolicyValidateRequestPolicies





T = TypeVar("T", bound="PolicyValidateRequest")



@_attrs_define
class PolicyValidateRequest:
    """ Request body for the /policy/validate endpoint.

        Attributes:
            policies (PolicyValidateRequestPolicies): Policy configuration to validate. Map of policy names to policy
                definitions.
     """

    policies: PolicyValidateRequestPolicies





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy_validate_request_policies import PolicyValidateRequestPolicies
        policies = self.policies.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "policies": policies,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_validate_request_policies import PolicyValidateRequestPolicies
        d = dict(src_dict)
        policies = PolicyValidateRequestPolicies.from_dict(d.pop("policies"))




        policy_validate_request = cls(
            policies=policies,
        )

        return policy_validate_request

