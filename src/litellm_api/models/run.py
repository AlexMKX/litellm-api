from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_status import RunStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.per_testing_criteria_result import PerTestingCriteriaResult
  from ..models.run_data_source import RunDataSource
  from ..models.run_error_type_0 import RunErrorType0
  from ..models.run_metadata_type_0 import RunMetadataType0
  from ..models.run_result_counts_type_0 import RunResultCountsType0





T = TypeVar("T", bound="Run")



@_attrs_define
class Run:
    """ Represents a run from the OpenAI Evals API

        Attributes:
            id (str):
            created_at (int):
            status (RunStatus):
            data_source (RunDataSource):
            eval_id (str):
            object_ (str | Unset):  Default: 'eval.run'.
            name (None | str | Unset):
            started_at (int | None | Unset):
            completed_at (int | None | Unset):
            model (None | str | Unset):
            per_model_usage (Any | None | Unset):
            per_testing_criteria_results (list[PerTestingCriteriaResult] | None | Unset):
            report_url (None | str | Unset):
            result_counts (None | RunResultCountsType0 | Unset):
            shared_with_openai (bool | None | Unset):
            metadata (None | RunMetadataType0 | Unset):
            error (None | RunErrorType0 | Unset):
     """

    id: str
    created_at: int
    status: RunStatus
    data_source: RunDataSource
    eval_id: str
    object_: str | Unset = 'eval.run'
    name: None | str | Unset = UNSET
    started_at: int | None | Unset = UNSET
    completed_at: int | None | Unset = UNSET
    model: None | str | Unset = UNSET
    per_model_usage: Any | None | Unset = UNSET
    per_testing_criteria_results: list[PerTestingCriteriaResult] | None | Unset = UNSET
    report_url: None | str | Unset = UNSET
    result_counts: None | RunResultCountsType0 | Unset = UNSET
    shared_with_openai: bool | None | Unset = UNSET
    metadata: None | RunMetadataType0 | Unset = UNSET
    error: None | RunErrorType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.per_testing_criteria_result import PerTestingCriteriaResult
        from ..models.run_data_source import RunDataSource
        from ..models.run_error_type_0 import RunErrorType0
        from ..models.run_metadata_type_0 import RunMetadataType0
        from ..models.run_result_counts_type_0 import RunResultCountsType0
        id = self.id

        created_at = self.created_at

        status = self.status.value

        data_source = self.data_source.to_dict()

        eval_id = self.eval_id

        object_ = self.object_

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        started_at: int | None | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        completed_at: int | None | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = self.completed_at

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        per_model_usage: Any | None | Unset
        if isinstance(self.per_model_usage, Unset):
            per_model_usage = UNSET
        else:
            per_model_usage = self.per_model_usage

        per_testing_criteria_results: list[dict[str, Any]] | None | Unset
        if isinstance(self.per_testing_criteria_results, Unset):
            per_testing_criteria_results = UNSET
        elif isinstance(self.per_testing_criteria_results, list):
            per_testing_criteria_results = []
            for per_testing_criteria_results_type_0_item_data in self.per_testing_criteria_results:
                per_testing_criteria_results_type_0_item = per_testing_criteria_results_type_0_item_data.to_dict()
                per_testing_criteria_results.append(per_testing_criteria_results_type_0_item)


        else:
            per_testing_criteria_results = self.per_testing_criteria_results

        report_url: None | str | Unset
        if isinstance(self.report_url, Unset):
            report_url = UNSET
        else:
            report_url = self.report_url

        result_counts: dict[str, Any] | None | Unset
        if isinstance(self.result_counts, Unset):
            result_counts = UNSET
        elif isinstance(self.result_counts, RunResultCountsType0):
            result_counts = self.result_counts.to_dict()
        else:
            result_counts = self.result_counts

        shared_with_openai: bool | None | Unset
        if isinstance(self.shared_with_openai, Unset):
            shared_with_openai = UNSET
        else:
            shared_with_openai = self.shared_with_openai

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, RunMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, RunErrorType0):
            error = self.error.to_dict()
        else:
            error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "created_at": created_at,
            "status": status,
            "data_source": data_source,
            "eval_id": eval_id,
        })
        if object_ is not UNSET:
            field_dict["object"] = object_
        if name is not UNSET:
            field_dict["name"] = name
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if model is not UNSET:
            field_dict["model"] = model
        if per_model_usage is not UNSET:
            field_dict["per_model_usage"] = per_model_usage
        if per_testing_criteria_results is not UNSET:
            field_dict["per_testing_criteria_results"] = per_testing_criteria_results
        if report_url is not UNSET:
            field_dict["report_url"] = report_url
        if result_counts is not UNSET:
            field_dict["result_counts"] = result_counts
        if shared_with_openai is not UNSET:
            field_dict["shared_with_openai"] = shared_with_openai
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.per_testing_criteria_result import PerTestingCriteriaResult
        from ..models.run_data_source import RunDataSource
        from ..models.run_error_type_0 import RunErrorType0
        from ..models.run_metadata_type_0 import RunMetadataType0
        from ..models.run_result_counts_type_0 import RunResultCountsType0
        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("created_at")

        status = RunStatus(d.pop("status"))




        data_source = RunDataSource.from_dict(d.pop("data_source"))




        eval_id = d.pop("eval_id")

        object_ = d.pop("object", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_started_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))


        def _parse_completed_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))


        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        def _parse_per_model_usage(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        per_model_usage = _parse_per_model_usage(d.pop("per_model_usage", UNSET))


        def _parse_per_testing_criteria_results(data: object) -> list[PerTestingCriteriaResult] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                per_testing_criteria_results_type_0 = []
                _per_testing_criteria_results_type_0 = data
                for per_testing_criteria_results_type_0_item_data in (_per_testing_criteria_results_type_0):
                    per_testing_criteria_results_type_0_item = PerTestingCriteriaResult.from_dict(per_testing_criteria_results_type_0_item_data)



                    per_testing_criteria_results_type_0.append(per_testing_criteria_results_type_0_item)

                return per_testing_criteria_results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PerTestingCriteriaResult] | None | Unset, data)

        per_testing_criteria_results = _parse_per_testing_criteria_results(d.pop("per_testing_criteria_results", UNSET))


        def _parse_report_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        report_url = _parse_report_url(d.pop("report_url", UNSET))


        def _parse_result_counts(data: object) -> None | RunResultCountsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_counts_type_0 = RunResultCountsType0.from_dict(data)



                return result_counts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunResultCountsType0 | Unset, data)

        result_counts = _parse_result_counts(d.pop("result_counts", UNSET))


        def _parse_shared_with_openai(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        shared_with_openai = _parse_shared_with_openai(d.pop("shared_with_openai", UNSET))


        def _parse_metadata(data: object) -> None | RunMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = RunMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        def _parse_error(data: object) -> None | RunErrorType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = RunErrorType0.from_dict(data)



                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RunErrorType0 | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        run = cls(
            id=id,
            created_at=created_at,
            status=status,
            data_source=data_source,
            eval_id=eval_id,
            object_=object_,
            name=name,
            started_at=started_at,
            completed_at=completed_at,
            model=model,
            per_model_usage=per_model_usage,
            per_testing_criteria_results=per_testing_criteria_results,
            report_url=report_url,
            result_counts=result_counts,
            shared_with_openai=shared_with_openai,
            metadata=metadata,
            error=error,
        )


        run.additional_properties = d
        return run

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
