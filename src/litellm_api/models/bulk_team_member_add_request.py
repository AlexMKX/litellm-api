from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.member import Member





T = TypeVar("T", bound="BulkTeamMemberAddRequest")



@_attrs_define
class BulkTeamMemberAddRequest:
    """ Request for bulk team member addition

        Attributes:
            team_id (str):
            members (list[Member] | None | Unset):
            all_users (bool | None | Unset):  Default: False.
            max_budget_in_team (float | None | Unset):
     """

    team_id: str
    members: list[Member] | None | Unset = UNSET
    all_users: bool | None | Unset = False
    max_budget_in_team: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.member import Member
        team_id = self.team_id

        members: list[dict[str, Any]] | None | Unset
        if isinstance(self.members, Unset):
            members = UNSET
        elif isinstance(self.members, list):
            members = []
            for members_type_0_item_data in self.members:
                members_type_0_item = members_type_0_item_data.to_dict()
                members.append(members_type_0_item)


        else:
            members = self.members

        all_users: bool | None | Unset
        if isinstance(self.all_users, Unset):
            all_users = UNSET
        else:
            all_users = self.all_users

        max_budget_in_team: float | None | Unset
        if isinstance(self.max_budget_in_team, Unset):
            max_budget_in_team = UNSET
        else:
            max_budget_in_team = self.max_budget_in_team


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "team_id": team_id,
        })
        if members is not UNSET:
            field_dict["members"] = members
        if all_users is not UNSET:
            field_dict["all_users"] = all_users
        if max_budget_in_team is not UNSET:
            field_dict["max_budget_in_team"] = max_budget_in_team

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.member import Member
        d = dict(src_dict)
        team_id = d.pop("team_id")

        def _parse_members(data: object) -> list[Member] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                members_type_0 = []
                _members_type_0 = data
                for members_type_0_item_data in (_members_type_0):
                    members_type_0_item = Member.from_dict(members_type_0_item_data)



                    members_type_0.append(members_type_0_item)

                return members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Member] | None | Unset, data)

        members = _parse_members(d.pop("members", UNSET))


        def _parse_all_users(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        all_users = _parse_all_users(d.pop("all_users", UNSET))


        def _parse_max_budget_in_team(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_budget_in_team = _parse_max_budget_in_team(d.pop("max_budget_in_team", UNSET))


        bulk_team_member_add_request = cls(
            team_id=team_id,
            members=members,
            all_users=all_users,
            max_budget_in_team=max_budget_in_team,
        )


        bulk_team_member_add_request.additional_properties = d
        return bulk_team_member_add_request

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
