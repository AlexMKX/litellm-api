from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.key_update_fields_rpm_limit_type_type_0 import KeyUpdateFieldsRpmLimitTypeType0
from ..models.key_update_fields_tpm_limit_type_type_0 import KeyUpdateFieldsTpmLimitTypeType0
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.key_update_fields_metadata_type_0 import KeyUpdateFieldsMetadataType0
  from ..models.key_update_fields_model_max_budget_type_0 import KeyUpdateFieldsModelMaxBudgetType0
  from ..models.key_update_fields_model_rpm_limit_type_0 import KeyUpdateFieldsModelRpmLimitType0
  from ..models.key_update_fields_model_tpm_limit_type_0 import KeyUpdateFieldsModelTpmLimitType0





T = TypeVar("T", bound="KeyUpdateFields")



@_attrs_define
class KeyUpdateFields:
    """ Allowlist of bulk-broadcastable fields for /team/key/bulk_update; `extra="forbid"` blocks RBAC/ownership/scope
    mutations even by team admins.

        Attributes:
            max_budget (float | None | Unset):
            budget_id (None | str | Unset):
            budget_duration (None | str | Unset):
            budget_limits (list[Any] | None | Unset):
            model_max_budget (KeyUpdateFieldsModelMaxBudgetType0 | None | Unset):
            tpm_limit (int | None | Unset):
            rpm_limit (int | None | Unset):
            model_tpm_limit (KeyUpdateFieldsModelTpmLimitType0 | None | Unset):
            model_rpm_limit (KeyUpdateFieldsModelRpmLimitType0 | None | Unset):
            max_parallel_requests (int | None | Unset):
            rpm_limit_type (KeyUpdateFieldsRpmLimitTypeType0 | None | Unset):
            tpm_limit_type (KeyUpdateFieldsTpmLimitTypeType0 | None | Unset):
            temp_budget_increase (float | None | Unset):
            temp_budget_expiry (datetime.datetime | None | Unset):
            duration (None | str | Unset):
            tags (list[str] | None | Unset):
            metadata (KeyUpdateFieldsMetadataType0 | None | Unset):
     """

    max_budget: float | None | Unset = UNSET
    budget_id: None | str | Unset = UNSET
    budget_duration: None | str | Unset = UNSET
    budget_limits: list[Any] | None | Unset = UNSET
    model_max_budget: KeyUpdateFieldsModelMaxBudgetType0 | None | Unset = UNSET
    tpm_limit: int | None | Unset = UNSET
    rpm_limit: int | None | Unset = UNSET
    model_tpm_limit: KeyUpdateFieldsModelTpmLimitType0 | None | Unset = UNSET
    model_rpm_limit: KeyUpdateFieldsModelRpmLimitType0 | None | Unset = UNSET
    max_parallel_requests: int | None | Unset = UNSET
    rpm_limit_type: KeyUpdateFieldsRpmLimitTypeType0 | None | Unset = UNSET
    tpm_limit_type: KeyUpdateFieldsTpmLimitTypeType0 | None | Unset = UNSET
    temp_budget_increase: float | None | Unset = UNSET
    temp_budget_expiry: datetime.datetime | None | Unset = UNSET
    duration: None | str | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    metadata: KeyUpdateFieldsMetadataType0 | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.key_update_fields_metadata_type_0 import KeyUpdateFieldsMetadataType0
        from ..models.key_update_fields_model_max_budget_type_0 import KeyUpdateFieldsModelMaxBudgetType0
        from ..models.key_update_fields_model_rpm_limit_type_0 import KeyUpdateFieldsModelRpmLimitType0
        from ..models.key_update_fields_model_tpm_limit_type_0 import KeyUpdateFieldsModelTpmLimitType0
        max_budget: float | None | Unset
        if isinstance(self.max_budget, Unset):
            max_budget = UNSET
        else:
            max_budget = self.max_budget

        budget_id: None | str | Unset
        if isinstance(self.budget_id, Unset):
            budget_id = UNSET
        else:
            budget_id = self.budget_id

        budget_duration: None | str | Unset
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration

        budget_limits: list[Any] | None | Unset
        if isinstance(self.budget_limits, Unset):
            budget_limits = UNSET
        elif isinstance(self.budget_limits, list):
            budget_limits = self.budget_limits


        else:
            budget_limits = self.budget_limits

        model_max_budget: dict[str, Any] | None | Unset
        if isinstance(self.model_max_budget, Unset):
            model_max_budget = UNSET
        elif isinstance(self.model_max_budget, KeyUpdateFieldsModelMaxBudgetType0):
            model_max_budget = self.model_max_budget.to_dict()
        else:
            model_max_budget = self.model_max_budget

        tpm_limit: int | None | Unset
        if isinstance(self.tpm_limit, Unset):
            tpm_limit = UNSET
        else:
            tpm_limit = self.tpm_limit

        rpm_limit: int | None | Unset
        if isinstance(self.rpm_limit, Unset):
            rpm_limit = UNSET
        else:
            rpm_limit = self.rpm_limit

        model_tpm_limit: dict[str, Any] | None | Unset
        if isinstance(self.model_tpm_limit, Unset):
            model_tpm_limit = UNSET
        elif isinstance(self.model_tpm_limit, KeyUpdateFieldsModelTpmLimitType0):
            model_tpm_limit = self.model_tpm_limit.to_dict()
        else:
            model_tpm_limit = self.model_tpm_limit

        model_rpm_limit: dict[str, Any] | None | Unset
        if isinstance(self.model_rpm_limit, Unset):
            model_rpm_limit = UNSET
        elif isinstance(self.model_rpm_limit, KeyUpdateFieldsModelRpmLimitType0):
            model_rpm_limit = self.model_rpm_limit.to_dict()
        else:
            model_rpm_limit = self.model_rpm_limit

        max_parallel_requests: int | None | Unset
        if isinstance(self.max_parallel_requests, Unset):
            max_parallel_requests = UNSET
        else:
            max_parallel_requests = self.max_parallel_requests

        rpm_limit_type: None | str | Unset
        if isinstance(self.rpm_limit_type, Unset):
            rpm_limit_type = UNSET
        elif isinstance(self.rpm_limit_type, KeyUpdateFieldsRpmLimitTypeType0):
            rpm_limit_type = self.rpm_limit_type.value
        else:
            rpm_limit_type = self.rpm_limit_type

        tpm_limit_type: None | str | Unset
        if isinstance(self.tpm_limit_type, Unset):
            tpm_limit_type = UNSET
        elif isinstance(self.tpm_limit_type, KeyUpdateFieldsTpmLimitTypeType0):
            tpm_limit_type = self.tpm_limit_type.value
        else:
            tpm_limit_type = self.tpm_limit_type

        temp_budget_increase: float | None | Unset
        if isinstance(self.temp_budget_increase, Unset):
            temp_budget_increase = UNSET
        else:
            temp_budget_increase = self.temp_budget_increase

        temp_budget_expiry: None | str | Unset
        if isinstance(self.temp_budget_expiry, Unset):
            temp_budget_expiry = UNSET
        elif isinstance(self.temp_budget_expiry, datetime.datetime):
            temp_budget_expiry = self.temp_budget_expiry.isoformat()
        else:
            temp_budget_expiry = self.temp_budget_expiry

        duration: None | str | Unset
        if isinstance(self.duration, Unset):
            duration = UNSET
        else:
            duration = self.duration

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags


        else:
            tags = self.tags

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, KeyUpdateFieldsMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if budget_id is not UNSET:
            field_dict["budget_id"] = budget_id
        if budget_duration is not UNSET:
            field_dict["budget_duration"] = budget_duration
        if budget_limits is not UNSET:
            field_dict["budget_limits"] = budget_limits
        if model_max_budget is not UNSET:
            field_dict["model_max_budget"] = model_max_budget
        if tpm_limit is not UNSET:
            field_dict["tpm_limit"] = tpm_limit
        if rpm_limit is not UNSET:
            field_dict["rpm_limit"] = rpm_limit
        if model_tpm_limit is not UNSET:
            field_dict["model_tpm_limit"] = model_tpm_limit
        if model_rpm_limit is not UNSET:
            field_dict["model_rpm_limit"] = model_rpm_limit
        if max_parallel_requests is not UNSET:
            field_dict["max_parallel_requests"] = max_parallel_requests
        if rpm_limit_type is not UNSET:
            field_dict["rpm_limit_type"] = rpm_limit_type
        if tpm_limit_type is not UNSET:
            field_dict["tpm_limit_type"] = tpm_limit_type
        if temp_budget_increase is not UNSET:
            field_dict["temp_budget_increase"] = temp_budget_increase
        if temp_budget_expiry is not UNSET:
            field_dict["temp_budget_expiry"] = temp_budget_expiry
        if duration is not UNSET:
            field_dict["duration"] = duration
        if tags is not UNSET:
            field_dict["tags"] = tags
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_update_fields_metadata_type_0 import KeyUpdateFieldsMetadataType0
        from ..models.key_update_fields_model_max_budget_type_0 import KeyUpdateFieldsModelMaxBudgetType0
        from ..models.key_update_fields_model_rpm_limit_type_0 import KeyUpdateFieldsModelRpmLimitType0
        from ..models.key_update_fields_model_tpm_limit_type_0 import KeyUpdateFieldsModelTpmLimitType0
        d = dict(src_dict)
        def _parse_max_budget(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_budget = _parse_max_budget(d.pop("max_budget", UNSET))


        def _parse_budget_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_id = _parse_budget_id(d.pop("budget_id", UNSET))


        def _parse_budget_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))


        def _parse_budget_limits(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                budget_limits_type_0 = cast(list[Any], data)

                return budget_limits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        budget_limits = _parse_budget_limits(d.pop("budget_limits", UNSET))


        def _parse_model_max_budget(data: object) -> KeyUpdateFieldsModelMaxBudgetType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_max_budget_type_0 = KeyUpdateFieldsModelMaxBudgetType0.from_dict(data)



                return model_max_budget_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeyUpdateFieldsModelMaxBudgetType0 | None | Unset, data)

        model_max_budget = _parse_model_max_budget(d.pop("model_max_budget", UNSET))


        def _parse_tpm_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tpm_limit = _parse_tpm_limit(d.pop("tpm_limit", UNSET))


        def _parse_rpm_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rpm_limit = _parse_rpm_limit(d.pop("rpm_limit", UNSET))


        def _parse_model_tpm_limit(data: object) -> KeyUpdateFieldsModelTpmLimitType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_tpm_limit_type_0 = KeyUpdateFieldsModelTpmLimitType0.from_dict(data)



                return model_tpm_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeyUpdateFieldsModelTpmLimitType0 | None | Unset, data)

        model_tpm_limit = _parse_model_tpm_limit(d.pop("model_tpm_limit", UNSET))


        def _parse_model_rpm_limit(data: object) -> KeyUpdateFieldsModelRpmLimitType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_rpm_limit_type_0 = KeyUpdateFieldsModelRpmLimitType0.from_dict(data)



                return model_rpm_limit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeyUpdateFieldsModelRpmLimitType0 | None | Unset, data)

        model_rpm_limit = _parse_model_rpm_limit(d.pop("model_rpm_limit", UNSET))


        def _parse_max_parallel_requests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_parallel_requests = _parse_max_parallel_requests(d.pop("max_parallel_requests", UNSET))


        def _parse_rpm_limit_type(data: object) -> KeyUpdateFieldsRpmLimitTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rpm_limit_type_type_0 = KeyUpdateFieldsRpmLimitTypeType0(data)



                return rpm_limit_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeyUpdateFieldsRpmLimitTypeType0 | None | Unset, data)

        rpm_limit_type = _parse_rpm_limit_type(d.pop("rpm_limit_type", UNSET))


        def _parse_tpm_limit_type(data: object) -> KeyUpdateFieldsTpmLimitTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tpm_limit_type_type_0 = KeyUpdateFieldsTpmLimitTypeType0(data)



                return tpm_limit_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeyUpdateFieldsTpmLimitTypeType0 | None | Unset, data)

        tpm_limit_type = _parse_tpm_limit_type(d.pop("tpm_limit_type", UNSET))


        def _parse_temp_budget_increase(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        temp_budget_increase = _parse_temp_budget_increase(d.pop("temp_budget_increase", UNSET))


        def _parse_temp_budget_expiry(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                temp_budget_expiry_type_0 = isoparse(data)



                return temp_budget_expiry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        temp_budget_expiry = _parse_temp_budget_expiry(d.pop("temp_budget_expiry", UNSET))


        def _parse_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        duration = _parse_duration(d.pop("duration", UNSET))


        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))


        def _parse_metadata(data: object) -> KeyUpdateFieldsMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = KeyUpdateFieldsMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeyUpdateFieldsMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        key_update_fields = cls(
            max_budget=max_budget,
            budget_id=budget_id,
            budget_duration=budget_duration,
            budget_limits=budget_limits,
            model_max_budget=model_max_budget,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
            model_tpm_limit=model_tpm_limit,
            model_rpm_limit=model_rpm_limit,
            max_parallel_requests=max_parallel_requests,
            rpm_limit_type=rpm_limit_type,
            tpm_limit_type=tpm_limit_type,
            temp_budget_increase=temp_budget_increase,
            temp_budget_expiry=temp_budget_expiry,
            duration=duration,
            tags=tags,
            metadata=metadata,
        )

        return key_update_fields

