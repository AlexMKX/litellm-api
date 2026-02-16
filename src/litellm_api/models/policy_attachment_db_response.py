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






T = TypeVar("T", bound="PolicyAttachmentDBResponse")



@_attrs_define
class PolicyAttachmentDBResponse:
    """ Response for a policy attachment from the database.

        Attributes:
            attachment_id (str): Unique ID of the attachment.
            policy_name (str): Name of the attached policy.
            scope (None | str | Unset): Scope of the attachment.
            teams (list[str] | Unset): Team patterns.
            keys (list[str] | Unset): Key patterns.
            models (list[str] | Unset): Model patterns.
            tags (list[str] | Unset): Tag patterns.
            created_at (datetime.datetime | None | Unset): When the attachment was created.
            updated_at (datetime.datetime | None | Unset): When the attachment was last updated.
            created_by (None | str | Unset): Who created the attachment.
            updated_by (None | str | Unset): Who last updated the attachment.
     """

    attachment_id: str
    policy_name: str
    scope: None | str | Unset = UNSET
    teams: list[str] | Unset = UNSET
    keys: list[str] | Unset = UNSET
    models: list[str] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        attachment_id = self.attachment_id

        policy_name = self.policy_name

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        teams: list[str] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = self.teams



        keys: list[str] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = self.keys



        models: list[str] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = self.models



        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags



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
            "attachment_id": attachment_id,
            "policy_name": policy_name,
        })
        if scope is not UNSET:
            field_dict["scope"] = scope
        if teams is not UNSET:
            field_dict["teams"] = teams
        if keys is not UNSET:
            field_dict["keys"] = keys
        if models is not UNSET:
            field_dict["models"] = models
        if tags is not UNSET:
            field_dict["tags"] = tags
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
        d = dict(src_dict)
        attachment_id = d.pop("attachment_id")

        policy_name = d.pop("policy_name")

        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))


        teams = cast(list[str], d.pop("teams", UNSET))


        keys = cast(list[str], d.pop("keys", UNSET))


        models = cast(list[str], d.pop("models", UNSET))


        tags = cast(list[str], d.pop("tags", UNSET))


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


        policy_attachment_db_response = cls(
            attachment_id=attachment_id,
            policy_name=policy_name,
            scope=scope,
            teams=teams,
            keys=keys,
            models=models,
            tags=tags,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
        )


        policy_attachment_db_response.additional_properties = d
        return policy_attachment_db_response

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
