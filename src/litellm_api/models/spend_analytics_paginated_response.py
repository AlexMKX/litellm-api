from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.daily_spend_data import DailySpendData
  from ..models.daily_spend_metadata import DailySpendMetadata





T = TypeVar("T", bound="SpendAnalyticsPaginatedResponse")



@_attrs_define
class SpendAnalyticsPaginatedResponse:
    """ 
        Attributes:
            results (list[DailySpendData]):
            metadata (DailySpendMetadata | Unset):
     """

    results: list[DailySpendData]
    metadata: DailySpendMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.daily_spend_data import DailySpendData
        from ..models.daily_spend_metadata import DailySpendMetadata
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)



        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "results": results,
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_spend_data import DailySpendData
        from ..models.daily_spend_metadata import DailySpendMetadata
        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in (_results):
            results_item = DailySpendData.from_dict(results_item_data)



            results.append(results_item)


        _metadata = d.pop("metadata", UNSET)
        metadata: DailySpendMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = DailySpendMetadata.from_dict(_metadata)




        spend_analytics_paginated_response = cls(
            results=results,
            metadata=metadata,
        )


        spend_analytics_paginated_response.additional_properties = d
        return spend_analytics_paginated_response

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
