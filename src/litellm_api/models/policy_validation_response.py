from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.policy_validation_error import PolicyValidationError





T = TypeVar("T", bound="PolicyValidationResponse")



@_attrs_define
class PolicyValidationResponse:
    """ Response from policy validation.

    - `valid`: True if no blocking errors were found
    - `errors`: List of blocking errors (prevent policy from being applied)
    - `warnings`: List of non-blocking warnings (policy can still be applied)

        Attributes:
            valid (bool): True if the policy configuration is valid.
            errors (list[PolicyValidationError] | Unset): List of blocking validation errors.
            warnings (list[PolicyValidationError] | Unset): List of non-blocking validation warnings.
     """

    valid: bool
    errors: list[PolicyValidationError] | Unset = UNSET
    warnings: list[PolicyValidationError] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy_validation_error import PolicyValidationError
        valid = self.valid

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)



        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "valid": valid,
        })
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy_validation_error import PolicyValidationError
        d = dict(src_dict)
        valid = d.pop("valid")

        _errors = d.pop("errors", UNSET)
        errors: list[PolicyValidationError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = PolicyValidationError.from_dict(errors_item_data)



                errors.append(errors_item)


        _warnings = d.pop("warnings", UNSET)
        warnings: list[PolicyValidationError] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = PolicyValidationError.from_dict(warnings_item_data)



                warnings.append(warnings_item)


        policy_validation_response = cls(
            valid=valid,
            errors=errors,
            warnings=warnings,
        )

        return policy_validation_response

