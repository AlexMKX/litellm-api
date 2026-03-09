from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.lite_llm_model_table_model_aliases_type_0 import LiteLLMModelTableModelAliasesType0
  from ..models.lite_llm_team_table import LiteLLMTeamTable





T = TypeVar("T", bound="LiteLLMModelTable")



@_attrs_define
class LiteLLMModelTable:
    """ 
        Attributes:
            created_by (str):
            updated_by (str):
            id (int | None | Unset):
            model_aliases (LiteLLMModelTableModelAliasesType0 | None | str | Unset):
            team (LiteLLMTeamTable | None | Unset):
     """

    created_by: str
    updated_by: str
    id: int | None | Unset = UNSET
    model_aliases: LiteLLMModelTableModelAliasesType0 | None | str | Unset = UNSET
    team: LiteLLMTeamTable | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_model_table_model_aliases_type_0 import LiteLLMModelTableModelAliasesType0
        from ..models.lite_llm_team_table import LiteLLMTeamTable
        created_by = self.created_by

        updated_by = self.updated_by

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        model_aliases: dict[str, Any] | None | str | Unset
        if isinstance(self.model_aliases, Unset):
            model_aliases = UNSET
        elif isinstance(self.model_aliases, LiteLLMModelTableModelAliasesType0):
            model_aliases = self.model_aliases.to_dict()
        else:
            model_aliases = self.model_aliases

        team: dict[str, Any] | None | Unset
        if isinstance(self.team, Unset):
            team = UNSET
        elif isinstance(self.team, LiteLLMTeamTable):
            team = self.team.to_dict()
        else:
            team = self.team


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_by": created_by,
            "updated_by": updated_by,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if model_aliases is not UNSET:
            field_dict["model_aliases"] = model_aliases
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_model_table_model_aliases_type_0 import LiteLLMModelTableModelAliasesType0
        from ..models.lite_llm_team_table import LiteLLMTeamTable
        d = dict(src_dict)
        created_by = d.pop("created_by")

        updated_by = d.pop("updated_by")

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_model_aliases(data: object) -> LiteLLMModelTableModelAliasesType0 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_aliases_type_0 = LiteLLMModelTableModelAliasesType0.from_dict(data)



                return model_aliases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMModelTableModelAliasesType0 | None | str | Unset, data)

        model_aliases = _parse_model_aliases(d.pop("model_aliases", UNSET))


        def _parse_team(data: object) -> LiteLLMTeamTable | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                team_type_0 = LiteLLMTeamTable.from_dict(data)



                return team_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMTeamTable | None | Unset, data)

        team = _parse_team(d.pop("team", UNSET))


        lite_llm_model_table = cls(
            created_by=created_by,
            updated_by=updated_by,
            id=id,
            model_aliases=model_aliases,
            team=team,
        )


        lite_llm_model_table.additional_properties = d
        return lite_llm_model_table

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
