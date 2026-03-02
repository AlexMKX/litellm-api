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
  from ..models.policy_version_compare_response_field_diffs import PolicyVersionCompareResponseFieldDiffs





T = TypeVar("T", bound="PolicyVersionCompareResponse")



@_attrs_define
class PolicyVersionCompareResponse:
    """ Response for comparing two policy versions.

        Attributes:
            version_a (PolicyDBResponse): Response for a policy from the database.
            version_b (PolicyDBResponse): Response for a policy from the database.
            field_diffs (PolicyVersionCompareResponseFieldDiffs | Unset): Field name -> {version_a: val, version_b: val} for
                differing fields.
     """

    version_a: PolicyDBResponse
    version_b: PolicyDBResponse
    field_diffs: PolicyVersionCompareResponseFieldDiffs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy_version_compare_response_field_diffs import PolicyVersionCompareResponseFieldDiffs
        from ..models.policy_db_response import PolicyDBResponse
        version_a = self.version_a.to_dict()

        version_b = self.version_b.to_dict()

        field_diffs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_diffs, Unset):
            field_diffs = self.field_diffs.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "version_a": version_a,
            "version_b": version_b,
        })
        if field_diffs is not UNSET:
            field_dict["field_diffs"] = field_diffs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_db_response import PolicyDBResponse
        from ..models.policy_version_compare_response_field_diffs import PolicyVersionCompareResponseFieldDiffs
        d = dict(src_dict)
        version_a = PolicyDBResponse.from_dict(d.pop("version_a"))




        version_b = PolicyDBResponse.from_dict(d.pop("version_b"))




        _field_diffs = d.pop("field_diffs", UNSET)
        field_diffs: PolicyVersionCompareResponseFieldDiffs | Unset
        if isinstance(_field_diffs,  Unset):
            field_diffs = UNSET
        else:
            field_diffs = PolicyVersionCompareResponseFieldDiffs.from_dict(_field_diffs)




        policy_version_compare_response = cls(
            version_a=version_a,
            version_b=version_b,
            field_diffs=field_diffs,
        )


        policy_version_compare_response.additional_properties = d
        return policy_version_compare_response

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
