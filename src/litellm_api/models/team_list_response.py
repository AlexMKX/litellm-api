from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.lite_llm_team_table import LiteLLMTeamTable





T = TypeVar("T", bound="TeamListResponse")



@_attrs_define
class TeamListResponse:
    """ Response to get the list of teams

        Attributes:
            teams (list[LiteLLMTeamTable]):
            total (int):
            page (int):
            page_size (int):
            total_pages (int):
     """

    teams: list[LiteLLMTeamTable]
    total: int
    page: int
    page_size: int
    total_pages: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_team_table import LiteLLMTeamTable
        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()
            teams.append(teams_item)



        total = self.total

        page = self.page

        page_size = self.page_size

        total_pages = self.total_pages


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "teams": teams,
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_team_table import LiteLLMTeamTable
        d = dict(src_dict)
        teams = []
        _teams = d.pop("teams")
        for teams_item_data in (_teams):
            teams_item = LiteLLMTeamTable.from_dict(teams_item_data)



            teams.append(teams_item)


        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        total_pages = d.pop("total_pages")

        team_list_response = cls(
            teams=teams,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )


        team_list_response.additional_properties = d
        return team_list_response

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
