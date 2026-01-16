from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.key_metric_with_metadata import KeyMetricWithMetadata





T = TypeVar("T", bound="MetricWithMetadataApiKeyBreakdown")



@_attrs_define
class MetricWithMetadataApiKeyBreakdown:
    """ 
     """

    additional_properties: dict[str, KeyMetricWithMetadata] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.key_metric_with_metadata import KeyMetricWithMetadata
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_metric_with_metadata import KeyMetricWithMetadata
        d = dict(src_dict)
        metric_with_metadata_api_key_breakdown = cls(
        )


        from ..models.spend_metrics import SpendMetrics
        from ..models.key_metadata import KeyMetadata
        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = KeyMetricWithMetadata.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        metric_with_metadata_api_key_breakdown.additional_properties = additional_properties
        return metric_with_metadata_api_key_breakdown

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> KeyMetricWithMetadata:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: KeyMetricWithMetadata) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
