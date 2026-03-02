from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.lite_llm_tool_table_row_call_policy import LiteLLMToolTableRowCallPolicy
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.lite_llm_tool_table_row_assignments_type_0 import LiteLLMToolTableRowAssignmentsType0





T = TypeVar("T", bound="LiteLLMToolTableRow")



@_attrs_define
class LiteLLMToolTableRow:
    """ 
        Attributes:
            tool_id (str):
            tool_name (str):
            origin (None | str | Unset):
            call_policy (LiteLLMToolTableRowCallPolicy | Unset):  Default: LiteLLMToolTableRowCallPolicy.UNTRUSTED.
            call_count (int | Unset):  Default: 0.
            assignments (LiteLLMToolTableRowAssignmentsType0 | None | Unset):
            key_hash (None | str | Unset):
            team_id (None | str | Unset):
            key_alias (None | str | Unset):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            created_by (None | str | Unset):
            updated_by (None | str | Unset):
     """

    tool_id: str
    tool_name: str
    origin: None | str | Unset = UNSET
    call_policy: LiteLLMToolTableRowCallPolicy | Unset = LiteLLMToolTableRowCallPolicy.UNTRUSTED
    call_count: int | Unset = 0
    assignments: LiteLLMToolTableRowAssignmentsType0 | None | Unset = UNSET
    key_hash: None | str | Unset = UNSET
    team_id: None | str | Unset = UNSET
    key_alias: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_tool_table_row_assignments_type_0 import LiteLLMToolTableRowAssignmentsType0
        tool_id = self.tool_id

        tool_name = self.tool_name

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        else:
            origin = self.origin

        call_policy: str | Unset = UNSET
        if not isinstance(self.call_policy, Unset):
            call_policy = self.call_policy.value


        call_count = self.call_count

        assignments: dict[str, Any] | None | Unset
        if isinstance(self.assignments, Unset):
            assignments = UNSET
        elif isinstance(self.assignments, LiteLLMToolTableRowAssignmentsType0):
            assignments = self.assignments.to_dict()
        else:
            assignments = self.assignments

        key_hash: None | str | Unset
        if isinstance(self.key_hash, Unset):
            key_hash = UNSET
        else:
            key_hash = self.key_hash

        team_id: None | str | Unset
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        else:
            team_id = self.team_id

        key_alias: None | str | Unset
        if isinstance(self.key_alias, Unset):
            key_alias = UNSET
        else:
            key_alias = self.key_alias

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tool_id": tool_id,
            "tool_name": tool_name,
        })
        if origin is not UNSET:
            field_dict["origin"] = origin
        if call_policy is not UNSET:
            field_dict["call_policy"] = call_policy
        if call_count is not UNSET:
            field_dict["call_count"] = call_count
        if assignments is not UNSET:
            field_dict["assignments"] = assignments
        if key_hash is not UNSET:
            field_dict["key_hash"] = key_hash
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if key_alias is not UNSET:
            field_dict["key_alias"] = key_alias
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_tool_table_row_assignments_type_0 import LiteLLMToolTableRowAssignmentsType0
        d = dict(src_dict)
        tool_id = d.pop("tool_id")

        tool_name = d.pop("tool_name")

        def _parse_origin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin = _parse_origin(d.pop("origin", UNSET))


        _call_policy = d.pop("call_policy", UNSET)
        call_policy: LiteLLMToolTableRowCallPolicy | Unset
        if isinstance(_call_policy,  Unset):
            call_policy = UNSET
        else:
            call_policy = LiteLLMToolTableRowCallPolicy(_call_policy)




        call_count = d.pop("call_count", UNSET)

        def _parse_assignments(data: object) -> LiteLLMToolTableRowAssignmentsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                assignments_type_0 = LiteLLMToolTableRowAssignmentsType0.from_dict(data)



                return assignments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMToolTableRowAssignmentsType0 | None | Unset, data)

        assignments = _parse_assignments(d.pop("assignments", UNSET))


        def _parse_key_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_hash = _parse_key_hash(d.pop("key_hash", UNSET))


        def _parse_team_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_id = _parse_team_id(d.pop("team_id", UNSET))


        def _parse_key_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_alias = _parse_key_alias(d.pop("key_alias", UNSET))


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))


        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))


        lite_llm_tool_table_row = cls(
            tool_id=tool_id,
            tool_name=tool_name,
            origin=origin,
            call_policy=call_policy,
            call_count=call_count,
            assignments=assignments,
            key_hash=key_hash,
            team_id=team_id,
            key_alias=key_alias,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
        )


        lite_llm_tool_table_row.additional_properties = d
        return lite_llm_tool_table_row

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
