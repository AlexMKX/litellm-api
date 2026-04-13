from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BulkUpdateTeamMemberPermissionsResponse")



@_attrs_define
class BulkUpdateTeamMemberPermissionsResponse:
    """ Response for bulk team member permissions update.

        Attributes:
            message (str):
            teams_updated (int):
            permissions_appended (list[str] | None | Unset):
     """

    message: str
    teams_updated: int
    permissions_appended: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        message = self.message

        teams_updated = self.teams_updated

        permissions_appended: list[str] | None | Unset
        if isinstance(self.permissions_appended, Unset):
            permissions_appended = UNSET
        elif isinstance(self.permissions_appended, list):
            permissions_appended = self.permissions_appended


        else:
            permissions_appended = self.permissions_appended


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "message": message,
            "teams_updated": teams_updated,
        })
        if permissions_appended is not UNSET:
            field_dict["permissions_appended"] = permissions_appended

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        teams_updated = d.pop("teams_updated")

        def _parse_permissions_appended(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permissions_appended_type_0 = cast(list[str], data)

                return permissions_appended_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        permissions_appended = _parse_permissions_appended(d.pop("permissions_appended", UNSET))


        bulk_update_team_member_permissions_response = cls(
            message=message,
            teams_updated=teams_updated,
            permissions_appended=permissions_appended,
        )


        bulk_update_team_member_permissions_response.additional_properties = d
        return bulk_update_team_member_permissions_response

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
