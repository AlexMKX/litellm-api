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





T = TypeVar("T", bound="LiteLLMTeamMembership")



@_attrs_define
class LiteLLMTeamMembership:
    """ 
        Attributes:
            user_id (str):
            team_id (str):
            litellm_budget_table (LiteLLMBudgetTable | None):
            budget_id (None | str | Unset):
            spend (float | None | Unset):  Default: 0.0.
     """

    user_id: str
    team_id: str
    litellm_budget_table: LiteLLMBudgetTable | None
    budget_id: None | str | Unset = UNSET
    spend: float | None | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_budget_table import LiteLLMBudgetTable
        user_id = self.user_id

        team_id = self.team_id

        litellm_budget_table: dict[str, Any] | None
        if isinstance(self.litellm_budget_table, LiteLLMBudgetTable):
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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_budget_table import LiteLLMBudgetTable
        d = dict(src_dict)
        user_id = d.pop("user_id")

        team_id = d.pop("team_id")

        def _parse_litellm_budget_table(data: object) -> LiteLLMBudgetTable | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_budget_table_type_0 = LiteLLMBudgetTable.from_dict(data)



                return litellm_budget_table_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMBudgetTable | None, data)

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


        lite_llm_team_membership = cls(
            user_id=user_id,
            team_id=team_id,
            litellm_budget_table=litellm_budget_table,
            budget_id=budget_id,
            spend=spend,
        )


        lite_llm_team_membership.additional_properties = d
        return lite_llm_team_membership

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
