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
  from ..models.policy_db_response_condition_type_0 import PolicyDBResponseConditionType0





T = TypeVar("T", bound="PolicyDBResponse")



@_attrs_define
class PolicyDBResponse:
    """ Response for a policy from the database.

        Attributes:
            policy_id (str): Unique ID of the policy.
            policy_name (str): Name of the policy.
            inherit (None | str | Unset): Parent policy name.
            description (None | str | Unset): Policy description.
            guardrails_add (list[str] | Unset): Guardrails to add.
            guardrails_remove (list[str] | Unset): Guardrails to remove.
            condition (None | PolicyDBResponseConditionType0 | Unset): Policy condition.
            created_at (datetime.datetime | None | Unset): When the policy was created.
            updated_at (datetime.datetime | None | Unset): When the policy was last updated.
            created_by (None | str | Unset): Who created the policy.
            updated_by (None | str | Unset): Who last updated the policy.
     """

    policy_id: str
    policy_name: str
    inherit: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    guardrails_add: list[str] | Unset = UNSET
    guardrails_remove: list[str] | Unset = UNSET
    condition: None | PolicyDBResponseConditionType0 | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy_db_response_condition_type_0 import PolicyDBResponseConditionType0
        policy_id = self.policy_id

        policy_name = self.policy_name

        inherit: None | str | Unset
        if isinstance(self.inherit, Unset):
            inherit = UNSET
        else:
            inherit = self.inherit

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        guardrails_add: list[str] | Unset = UNSET
        if not isinstance(self.guardrails_add, Unset):
            guardrails_add = self.guardrails_add



        guardrails_remove: list[str] | Unset = UNSET
        if not isinstance(self.guardrails_remove, Unset):
            guardrails_remove = self.guardrails_remove



        condition: dict[str, Any] | None | Unset
        if isinstance(self.condition, Unset):
            condition = UNSET
        elif isinstance(self.condition, PolicyDBResponseConditionType0):
            condition = self.condition.to_dict()
        else:
            condition = self.condition

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
            "policy_id": policy_id,
            "policy_name": policy_name,
        })
        if inherit is not UNSET:
            field_dict["inherit"] = inherit
        if description is not UNSET:
            field_dict["description"] = description
        if guardrails_add is not UNSET:
            field_dict["guardrails_add"] = guardrails_add
        if guardrails_remove is not UNSET:
            field_dict["guardrails_remove"] = guardrails_remove
        if condition is not UNSET:
            field_dict["condition"] = condition
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
        from ..models.policy_db_response_condition_type_0 import PolicyDBResponseConditionType0
        d = dict(src_dict)
        policy_id = d.pop("policy_id")

        policy_name = d.pop("policy_name")

        def _parse_inherit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inherit = _parse_inherit(d.pop("inherit", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        guardrails_add = cast(list[str], d.pop("guardrails_add", UNSET))


        guardrails_remove = cast(list[str], d.pop("guardrails_remove", UNSET))


        def _parse_condition(data: object) -> None | PolicyDBResponseConditionType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                condition_type_0 = PolicyDBResponseConditionType0.from_dict(data)



                return condition_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PolicyDBResponseConditionType0 | Unset, data)

        condition = _parse_condition(d.pop("condition", UNSET))


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


        policy_db_response = cls(
            policy_id=policy_id,
            policy_name=policy_name,
            inherit=inherit,
            description=description,
            guardrails_add=guardrails_add,
            guardrails_remove=guardrails_remove,
            condition=condition,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
        )


        policy_db_response.additional_properties = d
        return policy_db_response

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
