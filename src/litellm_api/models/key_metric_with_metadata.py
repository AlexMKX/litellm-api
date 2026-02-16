from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.key_metadata import KeyMetadata
  from ..models.spend_metrics import SpendMetrics





T = TypeVar("T", bound="KeyMetricWithMetadata")



@_attrs_define
class KeyMetricWithMetadata:
    """ Base class for metrics with additional metadata

        Attributes:
            metrics (SpendMetrics):
            metadata (KeyMetadata | Unset): Metadata for a key
     """

    metrics: SpendMetrics
    metadata: KeyMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.spend_metrics import SpendMetrics
        from ..models.key_metadata import KeyMetadata
        metrics = self.metrics.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "metrics": metrics,
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_metadata import KeyMetadata
        from ..models.spend_metrics import SpendMetrics
        d = dict(src_dict)
        metrics = SpendMetrics.from_dict(d.pop("metrics"))




        _metadata = d.pop("metadata", UNSET)
        metadata: KeyMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = KeyMetadata.from_dict(_metadata)




        key_metric_with_metadata = cls(
            metrics=metrics,
            metadata=metadata,
        )


        key_metric_with_metadata.additional_properties = d
        return key_metric_with_metadata

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
