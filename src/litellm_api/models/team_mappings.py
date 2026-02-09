from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TeamMappings")



@_attrs_define
class TeamMappings:
    """ Configuration for mapping SSO JWT fields to team IDs.

    This allows configuring team_ids_jwt_field via the database instead of
    requiring config file changes and restarts.

        Attributes:
            team_ids_jwt_field (None | str | Unset): The field name in the SSO/JWT token that contains the team IDs array
                (e.g., 'groups', 'teams'). Supports dot notation for nested fields.
     """

    team_ids_jwt_field: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        team_ids_jwt_field: None | str | Unset
        if isinstance(self.team_ids_jwt_field, Unset):
            team_ids_jwt_field = UNSET
        else:
            team_ids_jwt_field = self.team_ids_jwt_field


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if team_ids_jwt_field is not UNSET:
            field_dict["team_ids_jwt_field"] = team_ids_jwt_field

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_team_ids_jwt_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_ids_jwt_field = _parse_team_ids_jwt_field(d.pop("team_ids_jwt_field", UNSET))


        team_mappings = cls(
            team_ids_jwt_field=team_ids_jwt_field,
        )


        team_mappings.additional_properties = d
        return team_mappings

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
