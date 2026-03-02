from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.audit_log_response_before_value_type_0 import AuditLogResponseBeforeValueType0
  from ..models.audit_log_response_updated_values_type_0 import AuditLogResponseUpdatedValuesType0





T = TypeVar("T", bound="AuditLogResponse")



@_attrs_define
class AuditLogResponse:
    """ Response model for a single audit log entry

        Attributes:
            id (str):
            updated_at (datetime.datetime):
            changed_by (str):
            changed_by_api_key (str):
            action (str):
            table_name (str):
            object_id (str):
            before_value (AuditLogResponseBeforeValueType0 | None | Unset):
            updated_values (AuditLogResponseUpdatedValuesType0 | None | Unset):
     """

    id: str
    updated_at: datetime.datetime
    changed_by: str
    changed_by_api_key: str
    action: str
    table_name: str
    object_id: str
    before_value: AuditLogResponseBeforeValueType0 | None | Unset = UNSET
    updated_values: AuditLogResponseUpdatedValuesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_log_response_before_value_type_0 import AuditLogResponseBeforeValueType0
        from ..models.audit_log_response_updated_values_type_0 import AuditLogResponseUpdatedValuesType0
        id = self.id

        updated_at = self.updated_at.isoformat()

        changed_by = self.changed_by

        changed_by_api_key = self.changed_by_api_key

        action = self.action

        table_name = self.table_name

        object_id = self.object_id

        before_value: dict[str, Any] | None | Unset
        if isinstance(self.before_value, Unset):
            before_value = UNSET
        elif isinstance(self.before_value, AuditLogResponseBeforeValueType0):
            before_value = self.before_value.to_dict()
        else:
            before_value = self.before_value

        updated_values: dict[str, Any] | None | Unset
        if isinstance(self.updated_values, Unset):
            updated_values = UNSET
        elif isinstance(self.updated_values, AuditLogResponseUpdatedValuesType0):
            updated_values = self.updated_values.to_dict()
        else:
            updated_values = self.updated_values


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "updated_at": updated_at,
            "changed_by": changed_by,
            "changed_by_api_key": changed_by_api_key,
            "action": action,
            "table_name": table_name,
            "object_id": object_id,
        })
        if before_value is not UNSET:
            field_dict["before_value"] = before_value
        if updated_values is not UNSET:
            field_dict["updated_values"] = updated_values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_log_response_before_value_type_0 import AuditLogResponseBeforeValueType0
        from ..models.audit_log_response_updated_values_type_0 import AuditLogResponseUpdatedValuesType0
        d = dict(src_dict)
        id = d.pop("id")

        updated_at = isoparse(d.pop("updated_at"))




        changed_by = d.pop("changed_by")

        changed_by_api_key = d.pop("changed_by_api_key")

        action = d.pop("action")

        table_name = d.pop("table_name")

        object_id = d.pop("object_id")

        def _parse_before_value(data: object) -> AuditLogResponseBeforeValueType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                before_value_type_0 = AuditLogResponseBeforeValueType0.from_dict(data)



                return before_value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuditLogResponseBeforeValueType0 | None | Unset, data)

        before_value = _parse_before_value(d.pop("before_value", UNSET))


        def _parse_updated_values(data: object) -> AuditLogResponseUpdatedValuesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_values_type_0 = AuditLogResponseUpdatedValuesType0.from_dict(data)



                return updated_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuditLogResponseUpdatedValuesType0 | None | Unset, data)

        updated_values = _parse_updated_values(d.pop("updated_values", UNSET))


        audit_log_response = cls(
            id=id,
            updated_at=updated_at,
            changed_by=changed_by,
            changed_by_api_key=changed_by_api_key,
            action=action,
            table_name=table_name,
            object_id=object_id,
            before_value=before_value,
            updated_values=updated_values,
        )


        audit_log_response.additional_properties = d
        return audit_log_response

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
