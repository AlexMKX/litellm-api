from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cloud_zero_export_response_dry_run_data_type_0 import CloudZeroExportResponseDryRunDataType0
  from ..models.cloud_zero_export_response_summary_type_0 import CloudZeroExportResponseSummaryType0





T = TypeVar("T", bound="CloudZeroExportResponse")



@_attrs_define
class CloudZeroExportResponse:
    """ Response model for CloudZero export operations

        Attributes:
            message (str):
            status (str):
            records_exported (int | None | Unset):
            dry_run_data (CloudZeroExportResponseDryRunDataType0 | None | Unset): Dry run data including usage data and CBF
                transformed data
            summary (CloudZeroExportResponseSummaryType0 | None | Unset): Summary statistics for dry run
     """

    message: str
    status: str
    records_exported: int | None | Unset = UNSET
    dry_run_data: CloudZeroExportResponseDryRunDataType0 | None | Unset = UNSET
    summary: CloudZeroExportResponseSummaryType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cloud_zero_export_response_summary_type_0 import CloudZeroExportResponseSummaryType0
        from ..models.cloud_zero_export_response_dry_run_data_type_0 import CloudZeroExportResponseDryRunDataType0
        message = self.message

        status = self.status

        records_exported: int | None | Unset
        if isinstance(self.records_exported, Unset):
            records_exported = UNSET
        else:
            records_exported = self.records_exported

        dry_run_data: dict[str, Any] | None | Unset
        if isinstance(self.dry_run_data, Unset):
            dry_run_data = UNSET
        elif isinstance(self.dry_run_data, CloudZeroExportResponseDryRunDataType0):
            dry_run_data = self.dry_run_data.to_dict()
        else:
            dry_run_data = self.dry_run_data

        summary: dict[str, Any] | None | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        elif isinstance(self.summary, CloudZeroExportResponseSummaryType0):
            summary = self.summary.to_dict()
        else:
            summary = self.summary


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "message": message,
            "status": status,
        })
        if records_exported is not UNSET:
            field_dict["records_exported"] = records_exported
        if dry_run_data is not UNSET:
            field_dict["dry_run_data"] = dry_run_data
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_zero_export_response_dry_run_data_type_0 import CloudZeroExportResponseDryRunDataType0
        from ..models.cloud_zero_export_response_summary_type_0 import CloudZeroExportResponseSummaryType0
        d = dict(src_dict)
        message = d.pop("message")

        status = d.pop("status")

        def _parse_records_exported(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        records_exported = _parse_records_exported(d.pop("records_exported", UNSET))


        def _parse_dry_run_data(data: object) -> CloudZeroExportResponseDryRunDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dry_run_data_type_0 = CloudZeroExportResponseDryRunDataType0.from_dict(data)



                return dry_run_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CloudZeroExportResponseDryRunDataType0 | None | Unset, data)

        dry_run_data = _parse_dry_run_data(d.pop("dry_run_data", UNSET))


        def _parse_summary(data: object) -> CloudZeroExportResponseSummaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                summary_type_0 = CloudZeroExportResponseSummaryType0.from_dict(data)



                return summary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CloudZeroExportResponseSummaryType0 | None | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))


        cloud_zero_export_response = cls(
            message=message,
            status=status,
            records_exported=records_exported,
            dry_run_data=dry_run_data,
            summary=summary,
        )


        cloud_zero_export_response.additional_properties = d
        return cloud_zero_export_response

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
