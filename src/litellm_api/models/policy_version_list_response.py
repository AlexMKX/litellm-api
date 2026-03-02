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





T = TypeVar("T", bound="PolicyVersionListResponse")



@_attrs_define
class PolicyVersionListResponse:
    """ Response for listing all versions of a policy.

        Attributes:
            policy_name (str): Name of the policy.
            versions (list[PolicyDBResponse] | Unset): All versions ordered by version_number desc.
            total_count (int | Unset): Total number of versions. Default: 0.
     """

    policy_name: str
    versions: list[PolicyDBResponse] | Unset = UNSET
    total_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy_db_response import PolicyDBResponse
        policy_name = self.policy_name

        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)



        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "policy_name": policy_name,
        })
        if versions is not UNSET:
            field_dict["versions"] = versions
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_db_response import PolicyDBResponse
        d = dict(src_dict)
        policy_name = d.pop("policy_name")

        _versions = d.pop("versions", UNSET)
        versions: list[PolicyDBResponse] | Unset = UNSET
        if _versions is not UNSET:
            versions = []
            for versions_item_data in _versions:
                versions_item = PolicyDBResponse.from_dict(versions_item_data)



                versions.append(versions_item)


        total_count = d.pop("total_count", UNSET)

        policy_version_list_response = cls(
            policy_name=policy_name,
            versions=versions,
            total_count=total_count,
        )


        policy_version_list_response.additional_properties = d
        return policy_version_list_response

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
