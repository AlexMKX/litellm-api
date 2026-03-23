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
  from ..models.user_info_v2_response_metadata_type_0 import UserInfoV2ResponseMetadataType0





T = TypeVar("T", bound="UserInfoV2Response")



@_attrs_define
class UserInfoV2Response:
    """ Response model for GET /v2/user/info

    Returns ONLY the user object - no keys, no teams objects.
    This is a lightweight alternative to UserInfoResponse.

        Attributes:
            user_id (str):
            user_email (None | str | Unset):
            user_alias (None | str | Unset):
            user_role (None | str | Unset):
            spend (float | Unset):  Default: 0.0.
            max_budget (float | None | Unset):
            models (list[str] | Unset):
            budget_duration (None | str | Unset):
            budget_reset_at (datetime.datetime | None | Unset):
            metadata (None | Unset | UserInfoV2ResponseMetadataType0):
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            sso_user_id (None | str | Unset):
            teams (list[str] | Unset):
     """

    user_id: str
    user_email: None | str | Unset = UNSET
    user_alias: None | str | Unset = UNSET
    user_role: None | str | Unset = UNSET
    spend: float | Unset = 0.0
    max_budget: float | None | Unset = UNSET
    models: list[str] | Unset = UNSET
    budget_duration: None | str | Unset = UNSET
    budget_reset_at: datetime.datetime | None | Unset = UNSET
    metadata: None | Unset | UserInfoV2ResponseMetadataType0 = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    sso_user_id: None | str | Unset = UNSET
    teams: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_info_v2_response_metadata_type_0 import UserInfoV2ResponseMetadataType0
        user_id = self.user_id

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        user_alias: None | str | Unset
        if isinstance(self.user_alias, Unset):
            user_alias = UNSET
        else:
            user_alias = self.user_alias

        user_role: None | str | Unset
        if isinstance(self.user_role, Unset):
            user_role = UNSET
        else:
            user_role = self.user_role

        spend = self.spend

        max_budget: float | None | Unset
        if isinstance(self.max_budget, Unset):
            max_budget = UNSET
        else:
            max_budget = self.max_budget

        models: list[str] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = self.models



        budget_duration: None | str | Unset
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration

        budget_reset_at: None | str | Unset
        if isinstance(self.budget_reset_at, Unset):
            budget_reset_at = UNSET
        elif isinstance(self.budget_reset_at, datetime.datetime):
            budget_reset_at = self.budget_reset_at.isoformat()
        else:
            budget_reset_at = self.budget_reset_at

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, UserInfoV2ResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

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

        sso_user_id: None | str | Unset
        if isinstance(self.sso_user_id, Unset):
            sso_user_id = UNSET
        else:
            sso_user_id = self.sso_user_id

        teams: list[str] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = self.teams




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "user_id": user_id,
        })
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if user_alias is not UNSET:
            field_dict["user_alias"] = user_alias
        if user_role is not UNSET:
            field_dict["user_role"] = user_role
        if spend is not UNSET:
            field_dict["spend"] = spend
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if models is not UNSET:
            field_dict["models"] = models
        if budget_duration is not UNSET:
            field_dict["budget_duration"] = budget_duration
        if budget_reset_at is not UNSET:
            field_dict["budget_reset_at"] = budget_reset_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if sso_user_id is not UNSET:
            field_dict["sso_user_id"] = sso_user_id
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_info_v2_response_metadata_type_0 import UserInfoV2ResponseMetadataType0
        d = dict(src_dict)
        user_id = d.pop("user_id")

        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))


        def _parse_user_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_alias = _parse_user_alias(d.pop("user_alias", UNSET))


        def _parse_user_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_role = _parse_user_role(d.pop("user_role", UNSET))


        spend = d.pop("spend", UNSET)

        def _parse_max_budget(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_budget = _parse_max_budget(d.pop("max_budget", UNSET))


        models = cast(list[str], d.pop("models", UNSET))


        def _parse_budget_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))


        def _parse_budget_reset_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                budget_reset_at_type_0 = isoparse(data)



                return budget_reset_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        budget_reset_at = _parse_budget_reset_at(d.pop("budget_reset_at", UNSET))


        def _parse_metadata(data: object) -> None | Unset | UserInfoV2ResponseMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = UserInfoV2ResponseMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserInfoV2ResponseMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


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


        def _parse_sso_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sso_user_id = _parse_sso_user_id(d.pop("sso_user_id", UNSET))


        teams = cast(list[str], d.pop("teams", UNSET))


        user_info_v2_response = cls(
            user_id=user_id,
            user_email=user_email,
            user_alias=user_alias,
            user_role=user_role,
            spend=spend,
            max_budget=max_budget,
            models=models,
            budget_duration=budget_duration,
            budget_reset_at=budget_reset_at,
            metadata=metadata,
            created_at=created_at,
            updated_at=updated_at,
            sso_user_id=sso_user_id,
            teams=teams,
        )


        user_info_v2_response.additional_properties = d
        return user_info_v2_response

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
