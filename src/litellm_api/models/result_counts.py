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
            error (int | Unset):  Default: 0.
            failed (int | Unset):  Default: 0.
            passed (int | Unset):  Default: 0.
     """

    total: int
    error: int | Unset = 0
    failed: int | Unset = 0
    passed: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        total = self.total

        error = self.error

        failed = self.failed

        passed = self.passed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "total": total,
        })
        if error is not UNSET:
            field_dict["error"] = error
        if failed is not UNSET:
            field_dict["failed"] = failed
        if passed is not UNSET:
            field_dict["passed"] = passed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        error = d.pop("error", UNSET)

        failed = d.pop("failed", UNSET)

        passed = d.pop("passed", UNSET)

        result_counts = cls(
            total=total,
            error=error,
            failed=failed,
            passed=passed,
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
