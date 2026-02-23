from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ComplianceCheckResult")



@_attrs_define
class ComplianceCheckResult:
    """ Result of a single compliance check.

        Attributes:
            check_name (str):
            article (str):
            passed (bool):
            detail (str):
     """

    check_name: str
    article: str
    passed: bool
    detail: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        check_name = self.check_name

        article = self.article

        passed = self.passed

        detail = self.detail


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "check_name": check_name,
            "article": article,
            "passed": passed,
            "detail": detail,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        check_name = d.pop("check_name")

        article = d.pop("article")

        passed = d.pop("passed")

        detail = d.pop("detail")

        compliance_check_result = cls(
            check_name=check_name,
            article=article,
            passed=passed,
            detail=detail,
        )


        compliance_check_result.additional_properties = d
        return compliance_check_result

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
