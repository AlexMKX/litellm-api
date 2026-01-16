from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetTeamMemberPermissionsResponse")



@_attrs_define
class GetTeamMemberPermissionsResponse:
    """ Response to get the team member permissions for a team

        Attributes:
            team_id (str):
            all_available_permissions (list[str]):
            team_member_permissions (list[str] | None | Unset):
     """

    team_id: str
    all_available_permissions: list[str]
    team_member_permissions: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        all_available_permissions = self.all_available_permissions



        team_member_permissions: list[str] | None | Unset
        if isinstance(self.team_member_permissions, Unset):
            team_member_permissions = UNSET
        elif isinstance(self.team_member_permissions, list):
            team_member_permissions = self.team_member_permissions


        else:
            team_member_permissions = self.team_member_permissions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "team_id": team_id,
            "all_available_permissions": all_available_permissions,
        })
        if team_member_permissions is not UNSET:
            field_dict["team_member_permissions"] = team_member_permissions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("team_id")

        all_available_permissions = cast(list[str], d.pop("all_available_permissions"))


        def _parse_team_member_permissions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                team_member_permissions_type_0 = cast(list[str], data)

                return team_member_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        team_member_permissions = _parse_team_member_permissions(d.pop("team_member_permissions", UNSET))


        get_team_member_permissions_response = cls(
            team_id=team_id,
            all_available_permissions=all_available_permissions,
            team_member_permissions=team_member_permissions,
        )


        get_team_member_permissions_response.additional_properties = d
        return get_team_member_permissions_response

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
