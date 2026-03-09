from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.bulk_team_member_add_response_updated_team_type_0 import BulkTeamMemberAddResponseUpdatedTeamType0
  from ..models.team_member_add_result import TeamMemberAddResult





T = TypeVar("T", bound="BulkTeamMemberAddResponse")



@_attrs_define
class BulkTeamMemberAddResponse:
    """ Response for bulk team member add operations

        Attributes:
            team_id (str):
            results (list[TeamMemberAddResult]):
            total_requested (int):
            successful_additions (int):
            failed_additions (int):
            updated_team (BulkTeamMemberAddResponseUpdatedTeamType0 | None | Unset):
     """

    team_id: str
    results: list[TeamMemberAddResult]
    total_requested: int
    successful_additions: int
    failed_additions: int
    updated_team: BulkTeamMemberAddResponseUpdatedTeamType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_team_member_add_response_updated_team_type_0 import BulkTeamMemberAddResponseUpdatedTeamType0
        from ..models.team_member_add_result import TeamMemberAddResult
        team_id = self.team_id

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)



        total_requested = self.total_requested

        successful_additions = self.successful_additions

        failed_additions = self.failed_additions

        updated_team: dict[str, Any] | None | Unset
        if isinstance(self.updated_team, Unset):
            updated_team = UNSET
        elif isinstance(self.updated_team, BulkTeamMemberAddResponseUpdatedTeamType0):
            updated_team = self.updated_team.to_dict()
        else:
            updated_team = self.updated_team


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "team_id": team_id,
            "results": results,
            "total_requested": total_requested,
            "successful_additions": successful_additions,
            "failed_additions": failed_additions,
        })
        if updated_team is not UNSET:
            field_dict["updated_team"] = updated_team

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_team_member_add_response_updated_team_type_0 import BulkTeamMemberAddResponseUpdatedTeamType0
        from ..models.team_member_add_result import TeamMemberAddResult
        d = dict(src_dict)
        team_id = d.pop("team_id")

        results = []
        _results = d.pop("results")
        for results_item_data in (_results):
            results_item = TeamMemberAddResult.from_dict(results_item_data)



            results.append(results_item)


        total_requested = d.pop("total_requested")

        successful_additions = d.pop("successful_additions")

        failed_additions = d.pop("failed_additions")

        def _parse_updated_team(data: object) -> BulkTeamMemberAddResponseUpdatedTeamType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_team_type_0 = BulkTeamMemberAddResponseUpdatedTeamType0.from_dict(data)



                return updated_team_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BulkTeamMemberAddResponseUpdatedTeamType0 | None | Unset, data)

        updated_team = _parse_updated_team(d.pop("updated_team", UNSET))


        bulk_team_member_add_response = cls(
            team_id=team_id,
            results=results,
            total_requested=total_requested,
            successful_additions=successful_additions,
            failed_additions=failed_additions,
            updated_team=updated_team,
        )


        bulk_team_member_add_response.additional_properties = d
        return bulk_team_member_add_response

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
