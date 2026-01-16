from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.litellm_user_roles import LitellmUserRoles
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OrganizationMemberUpdateRequest")



@_attrs_define
class OrganizationMemberUpdateRequest:
    """ 
        Attributes:
            organization_id (str):
            user_id (None | str | Unset):
            user_email (None | str | Unset):
            max_budget_in_organization (float | None | Unset):
            role (LitellmUserRoles | None | Unset):
     """

    organization_id: str
    user_id: None | str | Unset = UNSET
    user_email: None | str | Unset = UNSET
    max_budget_in_organization: float | None | Unset = UNSET
    role: LitellmUserRoles | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

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

        max_budget_in_organization: float | None | Unset
        if isinstance(self.max_budget_in_organization, Unset):
            max_budget_in_organization = UNSET
        else:
            max_budget_in_organization = self.max_budget_in_organization

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, LitellmUserRoles):
            role = self.role.value
        else:
            role = self.role


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "organization_id": organization_id,
        })
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if max_budget_in_organization is not UNSET:
            field_dict["max_budget_in_organization"] = max_budget_in_organization
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization_id = d.pop("organization_id")

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


        def _parse_max_budget_in_organization(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_budget_in_organization = _parse_max_budget_in_organization(d.pop("max_budget_in_organization", UNSET))


        def _parse_role(data: object) -> LitellmUserRoles | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_0 = LitellmUserRoles(data)



                return role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LitellmUserRoles | None | Unset, data)

        role = _parse_role(d.pop("role", UNSET))


        organization_member_update_request = cls(
            organization_id=organization_id,
            user_id=user_id,
            user_email=user_email,
            max_budget_in_organization=max_budget_in_organization,
            role=role,
        )


        organization_member_update_request.additional_properties = d
        return organization_member_update_request

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
