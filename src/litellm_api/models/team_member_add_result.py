from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.team_member_add_result_updated_team_membership_type_0 import TeamMemberAddResultUpdatedTeamMembershipType0
  from ..models.team_member_add_result_updated_user_type_0 import TeamMemberAddResultUpdatedUserType0





T = TypeVar("T", bound="TeamMemberAddResult")



@_attrs_define
class TeamMemberAddResult:
    """ Result of a single team member add operation

        Attributes:
            success (bool):
            user_id (None | str | Unset):
            user_email (None | str | Unset):
            error (None | str | Unset):
            updated_user (None | TeamMemberAddResultUpdatedUserType0 | Unset):
            updated_team_membership (None | TeamMemberAddResultUpdatedTeamMembershipType0 | Unset):
     """

    success: bool
    user_id: None | str | Unset = UNSET
    user_email: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    updated_user: None | TeamMemberAddResultUpdatedUserType0 | Unset = UNSET
    updated_team_membership: None | TeamMemberAddResultUpdatedTeamMembershipType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.team_member_add_result_updated_team_membership_type_0 import TeamMemberAddResultUpdatedTeamMembershipType0
        from ..models.team_member_add_result_updated_user_type_0 import TeamMemberAddResultUpdatedUserType0
        success = self.success

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

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        updated_user: dict[str, Any] | None | Unset
        if isinstance(self.updated_user, Unset):
            updated_user = UNSET
        elif isinstance(self.updated_user, TeamMemberAddResultUpdatedUserType0):
            updated_user = self.updated_user.to_dict()
        else:
            updated_user = self.updated_user

        updated_team_membership: dict[str, Any] | None | Unset
        if isinstance(self.updated_team_membership, Unset):
            updated_team_membership = UNSET
        elif isinstance(self.updated_team_membership, TeamMemberAddResultUpdatedTeamMembershipType0):
            updated_team_membership = self.updated_team_membership.to_dict()
        else:
            updated_team_membership = self.updated_team_membership


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "success": success,
        })
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if error is not UNSET:
            field_dict["error"] = error
        if updated_user is not UNSET:
            field_dict["updated_user"] = updated_user
        if updated_team_membership is not UNSET:
            field_dict["updated_team_membership"] = updated_team_membership

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_member_add_result_updated_team_membership_type_0 import TeamMemberAddResultUpdatedTeamMembershipType0
        from ..models.team_member_add_result_updated_user_type_0 import TeamMemberAddResultUpdatedUserType0
        d = dict(src_dict)
        success = d.pop("success")

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


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        def _parse_updated_user(data: object) -> None | TeamMemberAddResultUpdatedUserType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_user_type_0 = TeamMemberAddResultUpdatedUserType0.from_dict(data)



                return updated_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TeamMemberAddResultUpdatedUserType0 | Unset, data)

        updated_user = _parse_updated_user(d.pop("updated_user", UNSET))


        def _parse_updated_team_membership(data: object) -> None | TeamMemberAddResultUpdatedTeamMembershipType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_team_membership_type_0 = TeamMemberAddResultUpdatedTeamMembershipType0.from_dict(data)



                return updated_team_membership_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TeamMemberAddResultUpdatedTeamMembershipType0 | Unset, data)

        updated_team_membership = _parse_updated_team_membership(d.pop("updated_team_membership", UNSET))


        team_member_add_result = cls(
            success=success,
            user_id=user_id,
            user_email=user_email,
            error=error,
            updated_user=updated_user,
            updated_team_membership=updated_team_membership,
        )


        team_member_add_result.additional_properties = d
        return team_member_add_result

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
