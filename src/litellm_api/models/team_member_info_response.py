from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.lite_llm_budget_table import LiteLLMBudgetTable
  from ..models.lite_llm_budget_table_full import LiteLLMBudgetTableFull





T = TypeVar("T", bound="TeamMemberInfoResponse")



@_attrs_define
class TeamMemberInfoResponse:
    """ Response for GET /team/{team_id}/members/me — caller's own membership row.

        Attributes:
            user_id (str):
            team_id (str):
            litellm_budget_table (LiteLLMBudgetTable | LiteLLMBudgetTableFull | None):
            budget_id (None | str | Unset):
            spend (float | None | Unset):  Default: 0.0.
            total_spend (float | None | Unset):  Default: 0.0.
            role (None | str | Unset):
            user_email (None | str | Unset):
            team_alias (None | str | Unset):
     """

    user_id: str
    team_id: str
    litellm_budget_table: LiteLLMBudgetTable | LiteLLMBudgetTableFull | None
    budget_id: None | str | Unset = UNSET
    spend: float | None | Unset = 0.0
    total_spend: float | None | Unset = 0.0
    role: None | str | Unset = UNSET
    user_email: None | str | Unset = UNSET
    team_alias: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_budget_table import LiteLLMBudgetTable
        from ..models.lite_llm_budget_table_full import LiteLLMBudgetTableFull
        user_id = self.user_id

        team_id = self.team_id

        litellm_budget_table: dict[str, Any] | None
        if isinstance(self.litellm_budget_table, LiteLLMBudgetTableFull):
            litellm_budget_table = self.litellm_budget_table.to_dict()
        elif isinstance(self.litellm_budget_table, LiteLLMBudgetTable):
            litellm_budget_table = self.litellm_budget_table.to_dict()
        else:
            litellm_budget_table = self.litellm_budget_table

        budget_id: None | str | Unset
        if isinstance(self.budget_id, Unset):
            budget_id = UNSET
        else:
            budget_id = self.budget_id

        spend: float | None | Unset
        if isinstance(self.spend, Unset):
            spend = UNSET
        else:
            spend = self.spend

        total_spend: float | None | Unset
        if isinstance(self.total_spend, Unset):
            total_spend = UNSET
        else:
            total_spend = self.total_spend

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        team_alias: None | str | Unset
        if isinstance(self.team_alias, Unset):
            team_alias = UNSET
        else:
            team_alias = self.team_alias


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "user_id": user_id,
            "team_id": team_id,
            "litellm_budget_table": litellm_budget_table,
        })
        if budget_id is not UNSET:
            field_dict["budget_id"] = budget_id
        if spend is not UNSET:
            field_dict["spend"] = spend
        if total_spend is not UNSET:
            field_dict["total_spend"] = total_spend
        if role is not UNSET:
            field_dict["role"] = role
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if team_alias is not UNSET:
            field_dict["team_alias"] = team_alias

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_budget_table import LiteLLMBudgetTable
        from ..models.lite_llm_budget_table_full import LiteLLMBudgetTableFull
        d = dict(src_dict)
        user_id = d.pop("user_id")

        team_id = d.pop("team_id")

        def _parse_litellm_budget_table(data: object) -> LiteLLMBudgetTable | LiteLLMBudgetTableFull | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_budget_table_type_0 = LiteLLMBudgetTableFull.from_dict(data)



                return litellm_budget_table_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_budget_table_type_1 = LiteLLMBudgetTable.from_dict(data)



                return litellm_budget_table_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMBudgetTable | LiteLLMBudgetTableFull | None, data)

        litellm_budget_table = _parse_litellm_budget_table(d.pop("litellm_budget_table"))


        def _parse_budget_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_id = _parse_budget_id(d.pop("budget_id", UNSET))


        def _parse_spend(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        spend = _parse_spend(d.pop("spend", UNSET))


        def _parse_total_spend(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_spend = _parse_total_spend(d.pop("total_spend", UNSET))


        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))


        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))


        def _parse_team_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_alias = _parse_team_alias(d.pop("team_alias", UNSET))


        team_member_info_response = cls(
            user_id=user_id,
            team_id=team_id,
            litellm_budget_table=litellm_budget_table,
            budget_id=budget_id,
            spend=spend,
            total_spend=total_spend,
            role=role,
            user_email=user_email,
            team_alias=team_alias,
        )


        team_member_info_response.additional_properties = d
        return team_member_info_response

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
