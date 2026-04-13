from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.key_management_routes import KeyManagementRoutes
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BulkUpdateTeamMemberPermissionsRequest")



@_attrs_define
class BulkUpdateTeamMemberPermissionsRequest:
    """ Request to bulk-update team member permissions across teams.

        Attributes:
            permissions (list[KeyManagementRoutes]):
            team_ids (list[str] | None | Unset):
            apply_to_all_teams (bool | Unset):  Default: False.
     """

    permissions: list[KeyManagementRoutes]
    team_ids: list[str] | None | Unset = UNSET
    apply_to_all_teams: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.value
            permissions.append(permissions_item)



        team_ids: list[str] | None | Unset
        if isinstance(self.team_ids, Unset):
            team_ids = UNSET
        elif isinstance(self.team_ids, list):
            team_ids = self.team_ids


        else:
            team_ids = self.team_ids

        apply_to_all_teams = self.apply_to_all_teams


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "permissions": permissions,
        })
        if team_ids is not UNSET:
            field_dict["team_ids"] = team_ids
        if apply_to_all_teams is not UNSET:
            field_dict["apply_to_all_teams"] = apply_to_all_teams

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in (_permissions):
            permissions_item = KeyManagementRoutes(permissions_item_data)



            permissions.append(permissions_item)


        def _parse_team_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                team_ids_type_0 = cast(list[str], data)

                return team_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        team_ids = _parse_team_ids(d.pop("team_ids", UNSET))


        apply_to_all_teams = d.pop("apply_to_all_teams", UNSET)

        bulk_update_team_member_permissions_request = cls(
            permissions=permissions,
            team_ids=team_ids,
            apply_to_all_teams=apply_to_all_teams,
        )


        bulk_update_team_member_permissions_request.additional_properties = d
        return bulk_update_team_member_permissions_request

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
