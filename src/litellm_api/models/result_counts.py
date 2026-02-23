from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ResultCounts")



@_attrs_define
class ResultCounts:
    """ Result counts for a run

        Attributes:
            total (int):
            passed (int | Unset):  Default: 0.
            failed (int | Unset):  Default: 0.
            error (int | Unset):  Default: 0.
     """

    total: int
    passed: int | Unset = 0
    failed: int | Unset = 0
    error: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        total = self.total

        passed = self.passed

        failed = self.failed

        error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "total": total,
        })
        if passed is not UNSET:
            field_dict["passed"] = passed
        if failed is not UNSET:
            field_dict["failed"] = failed
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        passed = d.pop("passed", UNSET)

        failed = d.pop("failed", UNSET)

        error = d.pop("error", UNSET)

        result_counts = cls(
            total=total,
            passed=passed,
            failed=failed,
            error=error,
        )


        result_counts.additional_properties = d
        return result_counts

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
