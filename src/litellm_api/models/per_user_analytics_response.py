from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.per_user_metrics import PerUserMetrics





T = TypeVar("T", bound="PerUserAnalyticsResponse")



@_attrs_define
class PerUserAnalyticsResponse:
    """ Response for per-user analytics

        Attributes:
            results (list[PerUserMetrics]):
            total_count (int):
            page (int):
            page_size (int):
            total_pages (int):
     """

    results: list[PerUserMetrics]
    total_count: int
    page: int
    page_size: int
    total_pages: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.per_user_metrics import PerUserMetrics
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)



        total_count = self.total_count

        page = self.page

        page_size = self.page_size

        total_pages = self.total_pages


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "results": results,
            "total_count": total_count,
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.per_user_metrics import PerUserMetrics
        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in (_results):
            results_item = PerUserMetrics.from_dict(results_item_data)



            results.append(results_item)


        total_count = d.pop("total_count")

        page = d.pop("page")

        page_size = d.pop("page_size")

        total_pages = d.pop("total_pages")

        per_user_analytics_response = cls(
            results=results,
            total_count=total_count,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )


        per_user_analytics_response.additional_properties = d
        return per_user_analytics_response

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
