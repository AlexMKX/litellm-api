from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.policy_validation_error_type import PolicyValidationErrorType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PolicyValidationError")



@_attrs_define
class PolicyValidationError:
    """ Represents a validation error or warning for a policy.

        Attributes:
            error_type (PolicyValidationErrorType): Types of validation errors that can occur.
            message (str): Human-readable error message.
            policy_name (str): Name of the policy with the issue.
            field (None | str | Unset): Specific field that caused the error (e.g., 'guardrails.add', 'scope.teams').
            value (None | str | Unset): The invalid value that caused the error.
     """

    error_type: PolicyValidationErrorType
    message: str
    policy_name: str
    field: None | str | Unset = UNSET
    value: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        error_type = self.error_type.value

        message = self.message

        policy_name = self.policy_name

        field: None | str | Unset
        if isinstance(self.field, Unset):
            field = UNSET
        else:
            field = self.field

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "error_type": error_type,
            "message": message,
            "policy_name": policy_name,
        })
        if field is not UNSET:
            field_dict["field"] = field
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_type = PolicyValidationErrorType(d.pop("error_type"))




        message = d.pop("message")

        policy_name = d.pop("policy_name")

        def _parse_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field = _parse_field(d.pop("field", UNSET))


        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        policy_validation_error = cls(
            error_type=error_type,
            message=message,
            policy_name=policy_name,
            field=field,
            value=value,
        )

        return policy_validation_error

