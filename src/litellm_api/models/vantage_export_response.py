from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.vantage_export_response_dry_run_data_type_0 import VantageExportResponseDryRunDataType0
  from ..models.vantage_export_response_summary_type_0 import VantageExportResponseSummaryType0





T = TypeVar("T", bound="VantageExportResponse")



@_attrs_define
class VantageExportResponse:
    """ Response model for Vantage export operations

        Attributes:
            message (str):
            status (str):
            dry_run_data (None | Unset | VantageExportResponseDryRunDataType0): Dry run data including usage data and FOCUS
                transformed data
            summary (None | Unset | VantageExportResponseSummaryType0): Summary statistics for dry run
     """

    message: str
    status: str
    dry_run_data: None | Unset | VantageExportResponseDryRunDataType0 = UNSET
    summary: None | Unset | VantageExportResponseSummaryType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.vantage_export_response_dry_run_data_type_0 import VantageExportResponseDryRunDataType0
        from ..models.vantage_export_response_summary_type_0 import VantageExportResponseSummaryType0
        message = self.message

        status = self.status

        dry_run_data: dict[str, Any] | None | Unset
        if isinstance(self.dry_run_data, Unset):
            dry_run_data = UNSET
        elif isinstance(self.dry_run_data, VantageExportResponseDryRunDataType0):
            dry_run_data = self.dry_run_data.to_dict()
        else:
            dry_run_data = self.dry_run_data

        summary: dict[str, Any] | None | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        elif isinstance(self.summary, VantageExportResponseSummaryType0):
            summary = self.summary.to_dict()
        else:
            summary = self.summary


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "message": message,
            "status": status,
        })
        if dry_run_data is not UNSET:
            field_dict["dry_run_data"] = dry_run_data
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vantage_export_response_dry_run_data_type_0 import VantageExportResponseDryRunDataType0
        from ..models.vantage_export_response_summary_type_0 import VantageExportResponseSummaryType0
        d = dict(src_dict)
        message = d.pop("message")

        status = d.pop("status")

        def _parse_dry_run_data(data: object) -> None | Unset | VantageExportResponseDryRunDataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dry_run_data_type_0 = VantageExportResponseDryRunDataType0.from_dict(data)



                return dry_run_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VantageExportResponseDryRunDataType0, data)

        dry_run_data = _parse_dry_run_data(d.pop("dry_run_data", UNSET))


        def _parse_summary(data: object) -> None | Unset | VantageExportResponseSummaryType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                summary_type_0 = VantageExportResponseSummaryType0.from_dict(data)



                return summary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VantageExportResponseSummaryType0, data)

        summary = _parse_summary(d.pop("summary", UNSET))


        vantage_export_response = cls(
            message=message,
            status=status,
            dry_run_data=dry_run_data,
            summary=summary,
        )


        vantage_export_response.additional_properties = d
        return vantage_export_response

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
