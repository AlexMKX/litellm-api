from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PerUserMetrics")



@_attrs_define
class PerUserMetrics:
    """ Metrics for individual user

        Attributes:
            user_id (str):
            user_email (None | str | Unset):
            user_agent (None | str | Unset):
            successful_requests (int | Unset):  Default: 0.
            failed_requests (int | Unset):  Default: 0.
            total_requests (int | Unset):  Default: 0.
            total_tokens (int | Unset):  Default: 0.
            spend (float | Unset):  Default: 0.0.
     """

    user_id: str
    user_email: None | str | Unset = UNSET
    user_agent: None | str | Unset = UNSET
    successful_requests: int | Unset = 0
    failed_requests: int | Unset = 0
    total_requests: int | Unset = 0
    total_tokens: int | Unset = 0
    spend: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        user_agent: None | str | Unset
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        successful_requests = self.successful_requests

        failed_requests = self.failed_requests

        total_requests = self.total_requests

        total_tokens = self.total_tokens

        spend = self.spend


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "user_id": user_id,
        })
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if successful_requests is not UNSET:
            field_dict["successful_requests"] = successful_requests
        if failed_requests is not UNSET:
            field_dict["failed_requests"] = failed_requests
        if total_requests is not UNSET:
            field_dict["total_requests"] = total_requests
        if total_tokens is not UNSET:
            field_dict["total_tokens"] = total_tokens
        if spend is not UNSET:
            field_dict["spend"] = spend

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))


        def _parse_user_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_agent = _parse_user_agent(d.pop("user_agent", UNSET))


        successful_requests = d.pop("successful_requests", UNSET)

        failed_requests = d.pop("failed_requests", UNSET)

        total_requests = d.pop("total_requests", UNSET)

        total_tokens = d.pop("total_tokens", UNSET)

        spend = d.pop("spend", UNSET)

        per_user_metrics = cls(
            user_id=user_id,
            user_email=user_email,
            user_agent=user_agent,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
            total_requests=total_requests,
            total_tokens=total_tokens,
            spend=spend,
        )


        per_user_metrics.additional_properties = d
        return per_user_metrics

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
