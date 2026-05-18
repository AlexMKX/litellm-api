from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GuardrailSubmissionSummary")



@_attrs_define
class GuardrailSubmissionSummary:
    """ 
        Attributes:
            active (int):
            pending_review (int):
            rejected (int):
            total (int):
     """

    active: int
    pending_review: int
    rejected: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        active = self.active

        pending_review = self.pending_review

        rejected = self.rejected

        total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "active": active,
            "pending_review": pending_review,
            "rejected": rejected,
            "total": total,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        pending_review = d.pop("pending_review")

        rejected = d.pop("rejected")

        total = d.pop("total")

        guardrail_submission_summary = cls(
            active=active,
            pending_review=pending_review,
            rejected=rejected,
            total=total,
        )


        guardrail_submission_summary.additional_properties = d
        return guardrail_submission_summary

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
