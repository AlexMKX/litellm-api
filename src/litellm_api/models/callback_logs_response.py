from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.callback_log_failure import CallbackLogFailure





T = TypeVar("T", bound="CallbackLogsResponse")



@_attrs_define
class CallbackLogsResponse:
    """ Per-batch result: counts plus per-record failure detail so the caller can
    distinguish a transient callback error from a structurally bad payload.

        Attributes:
            processed (int):
            failed (int):
            failures (list[CallbackLogFailure] | Unset):
     """

    processed: int
    failed: int
    failures: list[CallbackLogFailure] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.callback_log_failure import CallbackLogFailure
        processed = self.processed

        failed = self.failed

        failures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failures, Unset):
            failures = []
            for failures_item_data in self.failures:
                failures_item = failures_item_data.to_dict()
                failures.append(failures_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "processed": processed,
            "failed": failed,
        })
        if failures is not UNSET:
            field_dict["failures"] = failures

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.callback_log_failure import CallbackLogFailure
        d = dict(src_dict)
        processed = d.pop("processed")

        failed = d.pop("failed")

        _failures = d.pop("failures", UNSET)
        failures: list[CallbackLogFailure] | Unset = UNSET
        if _failures is not UNSET:
            failures = []
            for failures_item_data in _failures:
                failures_item = CallbackLogFailure.from_dict(failures_item_data)



                failures.append(failures_item)


        callback_logs_response = cls(
            processed=processed,
            failed=failed,
            failures=failures,
        )


        callback_logs_response.additional_properties = d
        return callback_logs_response

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
