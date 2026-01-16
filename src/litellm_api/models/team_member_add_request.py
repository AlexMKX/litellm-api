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





T = TypeVar("T", bound="TeamMemberAddRequest")



@_attrs_define
class TeamMemberAddRequest:
    """ Request body for adding members to a team.

    Example:
    ```json
    {
        "team_id": "45e3e396-ee08-4a61-a88e-16b3ce7e0849",
        "member": {
            "role": "user",
            "user_id": "user123"
        },
        "max_budget_in_team": 100.0
    }
    ```

        Attributes:
            member (list[Member] | Member): Member object or list of member objects to add. Each member must include either
                user_id or user_email, and a role
            team_id (str): The ID of the team to add the member to
            max_budget_in_team (float | None | Unset): Maximum budget allocated to this user within the team. If not set,
                user has unlimited budget within team limits
     """

    member: list[Member] | Member
    team_id: str
    max_budget_in_team: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.member import Member
        member: dict[str, Any] | list[dict[str, Any]]
        if isinstance(self.member, list):
            member = []
            for member_type_0_item_data in self.member:
                member_type_0_item = member_type_0_item_data.to_dict()
                member.append(member_type_0_item)


        else:
            member = self.member.to_dict()


        team_id = self.team_id

        max_budget_in_team: float | None | Unset
        if isinstance(self.max_budget_in_team, Unset):
            max_budget_in_team = UNSET
        else:
            max_budget_in_team = self.max_budget_in_team


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "member": member,
            "team_id": team_id,
        })
        if max_budget_in_team is not UNSET:
            field_dict["max_budget_in_team"] = max_budget_in_team

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.member import Member
        d = dict(src_dict)
        def _parse_member(data: object) -> list[Member] | Member:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                member_type_0 = []
                _member_type_0 = data
                for member_type_0_item_data in (_member_type_0):
                    member_type_0_item = Member.from_dict(member_type_0_item_data)



                    member_type_0.append(member_type_0_item)

                return member_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            member_type_1 = Member.from_dict(data)



            return member_type_1

        member = _parse_member(d.pop("member"))


        team_id = d.pop("team_id")

        def _parse_max_budget_in_team(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_budget_in_team = _parse_max_budget_in_team(d.pop("max_budget_in_team", UNSET))


        team_member_add_request = cls(
            member=member,
            team_id=team_id,
            max_budget_in_team=max_budget_in_team,
        )


        team_member_add_request.additional_properties = d
        return team_member_add_request

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
