from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.new_user_request_team_user_role import NewUserRequestTeamUserRole
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="NewUserRequestTeam")



@_attrs_define
class NewUserRequestTeam:
    """ 
        Attributes:
            team_id (str):
            max_budget_in_team (float | None | Unset):
            user_role (NewUserRequestTeamUserRole | Unset):  Default: NewUserRequestTeamUserRole.USER.
     """

    team_id: str
    max_budget_in_team: float | None | Unset = UNSET
    user_role: NewUserRequestTeamUserRole | Unset = NewUserRequestTeamUserRole.USER
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        max_budget_in_team: float | None | Unset
        if isinstance(self.max_budget_in_team, Unset):
            max_budget_in_team = UNSET
        else:
            max_budget_in_team = self.max_budget_in_team

        user_role: str | Unset = UNSET
        if not isinstance(self.user_role, Unset):
            user_role = self.user_role.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "team_id": team_id,
        })
        if max_budget_in_team is not UNSET:
            field_dict["max_budget_in_team"] = max_budget_in_team
        if user_role is not UNSET:
            field_dict["user_role"] = user_role

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("team_id")

        def _parse_max_budget_in_team(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_budget_in_team = _parse_max_budget_in_team(d.pop("max_budget_in_team", UNSET))


        _user_role = d.pop("user_role", UNSET)
        user_role: NewUserRequestTeamUserRole | Unset
        if isinstance(_user_role,  Unset):
            user_role = UNSET
        else:
            user_role = NewUserRequestTeamUserRole(_user_role)




        new_user_request_team = cls(
            team_id=team_id,
            max_budget_in_team=max_budget_in_team,
            user_role=user_role,
        )


        new_user_request_team.additional_properties = d
        return new_user_request_team

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
