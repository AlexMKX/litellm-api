from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.policy_db_response import PolicyDBResponse





T = TypeVar("T", bound="PolicyListDBResponse")



@_attrs_define
class PolicyListDBResponse:
    """ Response for listing policies from the database.

        Attributes:
            policies (list[PolicyDBResponse] | Unset): List of policies.
            total_count (int | Unset): Total number of policies. Default: 0.
     """

    policies: list[PolicyDBResponse] | Unset = UNSET
    total_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy_db_response import PolicyDBResponse
        policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = []
            for policies_item_data in self.policies:
                policies_item = policies_item_data.to_dict()
                policies.append(policies_item)



        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if policies is not UNSET:
            field_dict["policies"] = policies
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_db_response import PolicyDBResponse
        d = dict(src_dict)
        _policies = d.pop("policies", UNSET)
        policies: list[PolicyDBResponse] | Unset = UNSET
        if _policies is not UNSET:
            policies = []
            for policies_item_data in _policies:
                policies_item = PolicyDBResponse.from_dict(policies_item_data)



                policies.append(policies_item)


        total_count = d.pop("total_count", UNSET)

        policy_list_db_response = cls(
            policies=policies,
            total_count=total_count,
        )


        policy_list_db_response.additional_properties = d
        return policy_list_db_response

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
