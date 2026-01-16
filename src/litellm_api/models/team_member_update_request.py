from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.team_member_update_request_role_type_0 import TeamMemberUpdateRequestRoleType0
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TeamMemberUpdateRequest")



@_attrs_define
class TeamMemberUpdateRequest:
    """ 
        Attributes:
            team_id (str):
            user_id (None | str | Unset):
            user_email (None | str | Unset):
            max_budget_in_team (float | None | Unset):
            role (None | TeamMemberUpdateRequestRoleType0 | Unset):
            tpm_limit (int | None | Unset): Tokens per minute limit for this team member
            rpm_limit (int | None | Unset): Requests per minute limit for this team member
     """

    team_id: str
    user_id: None | str | Unset = UNSET
    user_email: None | str | Unset = UNSET
    max_budget_in_team: float | None | Unset = UNSET
    role: None | TeamMemberUpdateRequestRoleType0 | Unset = UNSET
    tpm_limit: int | None | Unset = UNSET
    rpm_limit: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        max_budget_in_team: float | None | Unset
        if isinstance(self.max_budget_in_team, Unset):
            max_budget_in_team = UNSET
        else:
            max_budget_in_team = self.max_budget_in_team

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, TeamMemberUpdateRequestRoleType0):
            role = self.role.value
        else:
            role = self.role

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "team_id": team_id,
        })
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if max_budget_in_team is not UNSET:
            field_dict["max_budget_in_team"] = max_budget_in_team
        if role is not UNSET:
            field_dict["role"] = role
        if tpm_limit is not UNSET:
            field_dict["tpm_limit"] = tpm_limit
        if rpm_limit is not UNSET:
            field_dict["rpm_limit"] = rpm_limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("team_id")

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))


        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))


        def _parse_max_budget_in_team(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_budget_in_team = _parse_max_budget_in_team(d.pop("max_budget_in_team", UNSET))


        def _parse_role(data: object) -> None | TeamMemberUpdateRequestRoleType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_0 = TeamMemberUpdateRequestRoleType0(data)



                return role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TeamMemberUpdateRequestRoleType0 | Unset, data)

        role = _parse_role(d.pop("role", UNSET))


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


        team_member_update_request = cls(
            team_id=team_id,
            user_id=user_id,
            user_email=user_email,
            max_budget_in_team=max_budget_in_team,
            role=role,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
        )


        team_member_update_request.additional_properties = d
        return team_member_update_request

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
