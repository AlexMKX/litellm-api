from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.org_member import OrgMember





T = TypeVar("T", bound="OrganizationMemberAddRequest")



@_attrs_define
class OrganizationMemberAddRequest:
    """ 
        Attributes:
            member (list[OrgMember] | OrgMember):
            organization_id (str):
            max_budget_in_organization (float | None | Unset):
     """

    member: list[OrgMember] | OrgMember
    organization_id: str
    max_budget_in_organization: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.org_member import OrgMember
        member: dict[str, Any] | list[dict[str, Any]]
        if isinstance(self.member, list):
            member = []
            for member_type_0_item_data in self.member:
                member_type_0_item = member_type_0_item_data.to_dict()
                member.append(member_type_0_item)


        else:
            member = self.member.to_dict()


        organization_id = self.organization_id

        max_budget_in_organization: float | None | Unset
        if isinstance(self.max_budget_in_organization, Unset):
            max_budget_in_organization = UNSET
        else:
            max_budget_in_organization = self.max_budget_in_organization


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "member": member,
            "organization_id": organization_id,
        })
        if max_budget_in_organization is not UNSET:
            field_dict["max_budget_in_organization"] = max_budget_in_organization

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_member import OrgMember
        d = dict(src_dict)
        def _parse_member(data: object) -> list[OrgMember] | OrgMember:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                member_type_0 = []
                _member_type_0 = data
                for member_type_0_item_data in (_member_type_0):
                    member_type_0_item = OrgMember.from_dict(member_type_0_item_data)



                    member_type_0.append(member_type_0_item)

                return member_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            member_type_1 = OrgMember.from_dict(data)



            return member_type_1

        member = _parse_member(d.pop("member"))


        organization_id = d.pop("organization_id")

        def _parse_max_budget_in_organization(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_budget_in_organization = _parse_max_budget_in_organization(d.pop("max_budget_in_organization", UNSET))


        organization_member_add_request = cls(
            member=member,
            organization_id=organization_id,
            max_budget_in_organization=max_budget_in_organization,
        )


        organization_member_add_request.additional_properties = d
        return organization_member_add_request

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
