from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TagSummaryMetrics")



@_attrs_define
class TagSummaryMetrics:
    """ Summary metrics for a tag

        Attributes:
            tag (str):
            unique_users (int):
            total_requests (int):
            successful_requests (int):
            failed_requests (int):
            total_tokens (int):
            total_spend (float):
     """

    tag: str
    unique_users: int
    total_requests: int
    successful_requests: int
    failed_requests: int
    total_tokens: int
    total_spend: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tag = self.tag

        unique_users = self.unique_users

        total_requests = self.total_requests

        successful_requests = self.successful_requests

        failed_requests = self.failed_requests

        total_tokens = self.total_tokens

        total_spend = self.total_spend


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tag": tag,
            "unique_users": unique_users,
            "total_requests": total_requests,
            "successful_requests": successful_requests,
            "failed_requests": failed_requests,
            "total_tokens": total_tokens,
            "total_spend": total_spend,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tag = d.pop("tag")

        unique_users = d.pop("unique_users")

        total_requests = d.pop("total_requests")

        successful_requests = d.pop("successful_requests")

        failed_requests = d.pop("failed_requests")

        total_tokens = d.pop("total_tokens")

        total_spend = d.pop("total_spend")

        tag_summary_metrics = cls(
            tag=tag,
            unique_users=unique_users,
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
            total_tokens=total_tokens,
            total_spend=total_spend,
        )


        tag_summary_metrics.additional_properties = d
        return tag_summary_metrics

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
