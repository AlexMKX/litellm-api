from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="CloudZeroExportRequest")



@_attrs_define
class CloudZeroExportRequest:
    """ Request model for CloudZero export operations

        Attributes:
            limit (int | None | Unset): Optional limit on number of records to export
            operation (str | Unset): CloudZero operation type (replace_hourly or sum) Default: 'replace_hourly'.
            start_time_utc (datetime.datetime | None | Unset): Start time for data export in UTC
            end_time_utc (datetime.datetime | None | Unset): End time for data export in UTC
     """

    limit: int | None | Unset = UNSET
    operation: str | Unset = 'replace_hourly'
    start_time_utc: datetime.datetime | None | Unset = UNSET
    end_time_utc: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        operation = self.operation

        start_time_utc: None | str | Unset
        if isinstance(self.start_time_utc, Unset):
            start_time_utc = UNSET
        elif isinstance(self.start_time_utc, datetime.datetime):
            start_time_utc = self.start_time_utc.isoformat()
        else:
            start_time_utc = self.start_time_utc

        end_time_utc: None | str | Unset
        if isinstance(self.end_time_utc, Unset):
            end_time_utc = UNSET
        elif isinstance(self.end_time_utc, datetime.datetime):
            end_time_utc = self.end_time_utc.isoformat()
        else:
            end_time_utc = self.end_time_utc


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if limit is not UNSET:
            field_dict["limit"] = limit
        if operation is not UNSET:
            field_dict["operation"] = operation
        if start_time_utc is not UNSET:
            field_dict["start_time_utc"] = start_time_utc
        if end_time_utc is not UNSET:
            field_dict["end_time_utc"] = end_time_utc

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))


        operation = d.pop("operation", UNSET)

        def _parse_start_time_utc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_utc_type_0 = isoparse(data)



                return start_time_utc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time_utc = _parse_start_time_utc(d.pop("start_time_utc", UNSET))


        def _parse_end_time_utc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_utc_type_0 = isoparse(data)



                return end_time_utc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time_utc = _parse_end_time_utc(d.pop("end_time_utc", UNSET))


        cloud_zero_export_request = cls(
            limit=limit,
            operation=operation,
            start_time_utc=start_time_utc,
            end_time_utc=end_time_utc,
        )


        cloud_zero_export_request.additional_properties = d
        return cloud_zero_export_request

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
