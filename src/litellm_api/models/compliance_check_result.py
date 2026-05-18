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
            article (str):
            check_name (str):
            detail (str):
            passed (bool):
     """

    article: str
    check_name: str
    detail: str
    passed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        article = self.article

        check_name = self.check_name

        detail = self.detail

        passed = self.passed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "article": article,
            "check_name": check_name,
            "detail": detail,
            "passed": passed,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        article = d.pop("article")

        check_name = d.pop("check_name")

        detail = d.pop("detail")

        passed = d.pop("passed")

        compliance_check_result = cls(
            article=article,
            check_name=check_name,
            detail=detail,
            passed=passed,
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
