from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.metric_with_metadata_api_key_breakdown import MetricWithMetadataApiKeyBreakdown
  from ..models.metric_with_metadata_metadata import MetricWithMetadataMetadata
  from ..models.spend_metrics import SpendMetrics





T = TypeVar("T", bound="MetricWithMetadata")



@_attrs_define
class MetricWithMetadata:
    """ 
        Attributes:
            metrics (SpendMetrics):
            metadata (MetricWithMetadataMetadata | Unset):
            api_key_breakdown (MetricWithMetadataApiKeyBreakdown | Unset):
     """

    metrics: SpendMetrics
    metadata: MetricWithMetadataMetadata | Unset = UNSET
    api_key_breakdown: MetricWithMetadataApiKeyBreakdown | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.metric_with_metadata_api_key_breakdown import MetricWithMetadataApiKeyBreakdown
        from ..models.spend_metrics import SpendMetrics
        from ..models.metric_with_metadata_metadata import MetricWithMetadataMetadata
        metrics = self.metrics.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        api_key_breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.api_key_breakdown, Unset):
            api_key_breakdown = self.api_key_breakdown.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "metrics": metrics,
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if api_key_breakdown is not UNSET:
            field_dict["api_key_breakdown"] = api_key_breakdown

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric_with_metadata_api_key_breakdown import MetricWithMetadataApiKeyBreakdown
        from ..models.metric_with_metadata_metadata import MetricWithMetadataMetadata
        from ..models.spend_metrics import SpendMetrics
        d = dict(src_dict)
        metrics = SpendMetrics.from_dict(d.pop("metrics"))




        _metadata = d.pop("metadata", UNSET)
        metadata: MetricWithMetadataMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = MetricWithMetadataMetadata.from_dict(_metadata)




        _api_key_breakdown = d.pop("api_key_breakdown", UNSET)
        api_key_breakdown: MetricWithMetadataApiKeyBreakdown | Unset
        if isinstance(_api_key_breakdown,  Unset):
            api_key_breakdown = UNSET
        else:
            api_key_breakdown = MetricWithMetadataApiKeyBreakdown.from_dict(_api_key_breakdown)




        metric_with_metadata = cls(
            metrics=metrics,
            metadata=metadata,
            api_key_breakdown=api_key_breakdown,
        )


        metric_with_metadata.additional_properties = d
        return metric_with_metadata

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
