from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RetryPolicy")



@_attrs_define
class RetryPolicy:
    """ Use this to set a custom number of retries per exception type
    If RateLimitErrorRetries = 3, then 3 retries will be made for RateLimitError
    Mapping of Exception type to number of retries
    https://docs.litellm.ai/docs/exception_mapping

        Attributes:
            bad_request_error_retries (int | None | Unset):
            authentication_error_retries (int | None | Unset):
            timeout_error_retries (int | None | Unset):
            rate_limit_error_retries (int | None | Unset):
            content_policy_violation_error_retries (int | None | Unset):
            internal_server_error_retries (int | None | Unset):
     """

    bad_request_error_retries: int | None | Unset = UNSET
    authentication_error_retries: int | None | Unset = UNSET
    timeout_error_retries: int | None | Unset = UNSET
    rate_limit_error_retries: int | None | Unset = UNSET
    content_policy_violation_error_retries: int | None | Unset = UNSET
    internal_server_error_retries: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        bad_request_error_retries: int | None | Unset
        if isinstance(self.bad_request_error_retries, Unset):
            bad_request_error_retries = UNSET
        else:
            bad_request_error_retries = self.bad_request_error_retries

        authentication_error_retries: int | None | Unset
        if isinstance(self.authentication_error_retries, Unset):
            authentication_error_retries = UNSET
        else:
            authentication_error_retries = self.authentication_error_retries

        timeout_error_retries: int | None | Unset
        if isinstance(self.timeout_error_retries, Unset):
            timeout_error_retries = UNSET
        else:
            timeout_error_retries = self.timeout_error_retries

        rate_limit_error_retries: int | None | Unset
        if isinstance(self.rate_limit_error_retries, Unset):
            rate_limit_error_retries = UNSET
        else:
            rate_limit_error_retries = self.rate_limit_error_retries

        content_policy_violation_error_retries: int | None | Unset
        if isinstance(self.content_policy_violation_error_retries, Unset):
            content_policy_violation_error_retries = UNSET
        else:
            content_policy_violation_error_retries = self.content_policy_violation_error_retries

        internal_server_error_retries: int | None | Unset
        if isinstance(self.internal_server_error_retries, Unset):
            internal_server_error_retries = UNSET
        else:
            internal_server_error_retries = self.internal_server_error_retries


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bad_request_error_retries is not UNSET:
            field_dict["BadRequestErrorRetries"] = bad_request_error_retries
        if authentication_error_retries is not UNSET:
            field_dict["AuthenticationErrorRetries"] = authentication_error_retries
        if timeout_error_retries is not UNSET:
            field_dict["TimeoutErrorRetries"] = timeout_error_retries
        if rate_limit_error_retries is not UNSET:
            field_dict["RateLimitErrorRetries"] = rate_limit_error_retries
        if content_policy_violation_error_retries is not UNSET:
            field_dict["ContentPolicyViolationErrorRetries"] = content_policy_violation_error_retries
        if internal_server_error_retries is not UNSET:
            field_dict["InternalServerErrorRetries"] = internal_server_error_retries

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_bad_request_error_retries(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bad_request_error_retries = _parse_bad_request_error_retries(d.pop("BadRequestErrorRetries", UNSET))


        def _parse_authentication_error_retries(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        authentication_error_retries = _parse_authentication_error_retries(d.pop("AuthenticationErrorRetries", UNSET))


        def _parse_timeout_error_retries(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        timeout_error_retries = _parse_timeout_error_retries(d.pop("TimeoutErrorRetries", UNSET))


        def _parse_rate_limit_error_retries(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rate_limit_error_retries = _parse_rate_limit_error_retries(d.pop("RateLimitErrorRetries", UNSET))


        def _parse_content_policy_violation_error_retries(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        content_policy_violation_error_retries = _parse_content_policy_violation_error_retries(d.pop("ContentPolicyViolationErrorRetries", UNSET))


        def _parse_internal_server_error_retries(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        internal_server_error_retries = _parse_internal_server_error_retries(d.pop("InternalServerErrorRetries", UNSET))


        retry_policy = cls(
            bad_request_error_retries=bad_request_error_retries,
            authentication_error_retries=authentication_error_retries,
            timeout_error_retries=timeout_error_retries,
            rate_limit_error_retries=rate_limit_error_retries,
            content_policy_violation_error_retries=content_policy_violation_error_retries,
            internal_server_error_retries=internal_server_error_retries,
        )


        retry_policy.additional_properties = d
        return retry_policy

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
