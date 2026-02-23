from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.result_counts import ResultCounts





T = TypeVar("T", bound="PerTestingCriteriaResult")



@_attrs_define
class PerTestingCriteriaResult:
    """ Results for a specific testing criteria

        Attributes:
            testing_criteria_index (int):
            result_counts (ResultCounts): Result counts for a run
            average_score (float | None | Unset):
     """

    testing_criteria_index: int
    result_counts: ResultCounts
    average_score: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.result_counts import ResultCounts
        testing_criteria_index = self.testing_criteria_index

        result_counts = self.result_counts.to_dict()

        average_score: float | None | Unset
        if isinstance(self.average_score, Unset):
            average_score = UNSET
        else:
            average_score = self.average_score


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "testing_criteria_index": testing_criteria_index,
            "result_counts": result_counts,
        })
        if average_score is not UNSET:
            field_dict["average_score"] = average_score

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.result_counts import ResultCounts
        d = dict(src_dict)
        testing_criteria_index = d.pop("testing_criteria_index")

        result_counts = ResultCounts.from_dict(d.pop("result_counts"))




        def _parse_average_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        average_score = _parse_average_score(d.pop("average_score", UNSET))


        per_testing_criteria_result = cls(
            testing_criteria_index=testing_criteria_index,
            result_counts=result_counts,
            average_score=average_score,
        )


        per_testing_criteria_result.additional_properties = d
        return per_testing_criteria_result

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
