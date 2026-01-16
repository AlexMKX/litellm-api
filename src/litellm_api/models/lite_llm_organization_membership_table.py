from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.lite_llm_budget_table import LiteLLMBudgetTable





T = TypeVar("T", bound="LiteLLMOrganizationMembershipTable")



@_attrs_define
class LiteLLMOrganizationMembershipTable:
    """ This is the table that track what organizations a user belongs to and users spend within the organization

        Attributes:
            user_id (str):
            organization_id (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            user_role (None | str | Unset):
            spend (float | Unset):  Default: 0.0.
            budget_id (None | str | Unset):
            user (Any | None | Unset):
            litellm_budget_table (LiteLLMBudgetTable | None | Unset):
     """

    user_id: str
    organization_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    user_role: None | str | Unset = UNSET
    spend: float | Unset = 0.0
    budget_id: None | str | Unset = UNSET
    user: Any | None | Unset = UNSET
    litellm_budget_table: LiteLLMBudgetTable | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_budget_table import LiteLLMBudgetTable
        user_id = self.user_id

        organization_id = self.organization_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        user_role: None | str | Unset
        if isinstance(self.user_role, Unset):
            user_role = UNSET
        else:
            user_role = self.user_role

        spend = self.spend

        budget_id: None | str | Unset
        if isinstance(self.budget_id, Unset):
            budget_id = UNSET
        else:
            budget_id = self.budget_id

        user: Any | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        litellm_budget_table: dict[str, Any] | None | Unset
        if isinstance(self.litellm_budget_table, Unset):
            litellm_budget_table = UNSET
        elif isinstance(self.litellm_budget_table, LiteLLMBudgetTable):
            litellm_budget_table = self.litellm_budget_table.to_dict()
        else:
            litellm_budget_table = self.litellm_budget_table


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "user_id": user_id,
            "organization_id": organization_id,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if user_role is not UNSET:
            field_dict["user_role"] = user_role
        if spend is not UNSET:
            field_dict["spend"] = spend
        if budget_id is not UNSET:
            field_dict["budget_id"] = budget_id
        if user is not UNSET:
            field_dict["user"] = user
        if litellm_budget_table is not UNSET:
            field_dict["litellm_budget_table"] = litellm_budget_table

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_budget_table import LiteLLMBudgetTable
        d = dict(src_dict)
        user_id = d.pop("user_id")

        organization_id = d.pop("organization_id")

        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        def _parse_user_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_role = _parse_user_role(d.pop("user_role", UNSET))


        spend = d.pop("spend", UNSET)

        def _parse_budget_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_id = _parse_budget_id(d.pop("budget_id", UNSET))


        def _parse_user(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        user = _parse_user(d.pop("user", UNSET))


        def _parse_litellm_budget_table(data: object) -> LiteLLMBudgetTable | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_budget_table_type_0 = LiteLLMBudgetTable.from_dict(data)



                return litellm_budget_table_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMBudgetTable | None | Unset, data)

        litellm_budget_table = _parse_litellm_budget_table(d.pop("litellm_budget_table", UNSET))


        lite_llm_organization_membership_table = cls(
            user_id=user_id,
            organization_id=organization_id,
            created_at=created_at,
            updated_at=updated_at,
            user_role=user_role,
            spend=spend,
            budget_id=budget_id,
            user=user,
            litellm_budget_table=litellm_budget_table,
        )


        lite_llm_organization_membership_table.additional_properties = d
        return lite_llm_organization_membership_table

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
