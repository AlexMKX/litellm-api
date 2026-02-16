from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AttachmentImpactResponse")



@_attrs_define
class AttachmentImpactResponse:
    """ Response for estimating the impact of a policy attachment.

        Attributes:
            affected_keys_count (int | Unset): Number of keys that would be affected (named + unnamed). Default: 0.
            affected_teams_count (int | Unset): Number of teams that would be affected (named + unnamed). Default: 0.
            unnamed_keys_count (int | Unset): Number of affected keys without an alias. Default: 0.
            unnamed_teams_count (int | Unset): Number of affected teams without an alias. Default: 0.
            sample_keys (list[str] | Unset): Sample of affected key aliases (up to 10).
            sample_teams (list[str] | Unset): Sample of affected team aliases (up to 10).
     """

    affected_keys_count: int | Unset = 0
    affected_teams_count: int | Unset = 0
    unnamed_keys_count: int | Unset = 0
    unnamed_teams_count: int | Unset = 0
    sample_keys: list[str] | Unset = UNSET
    sample_teams: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        affected_keys_count = self.affected_keys_count

        affected_teams_count = self.affected_teams_count

        unnamed_keys_count = self.unnamed_keys_count

        unnamed_teams_count = self.unnamed_teams_count

        sample_keys: list[str] | Unset = UNSET
        if not isinstance(self.sample_keys, Unset):
            sample_keys = self.sample_keys



        sample_teams: list[str] | Unset = UNSET
        if not isinstance(self.sample_teams, Unset):
            sample_teams = self.sample_teams




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if affected_keys_count is not UNSET:
            field_dict["affected_keys_count"] = affected_keys_count
        if affected_teams_count is not UNSET:
            field_dict["affected_teams_count"] = affected_teams_count
        if unnamed_keys_count is not UNSET:
            field_dict["unnamed_keys_count"] = unnamed_keys_count
        if unnamed_teams_count is not UNSET:
            field_dict["unnamed_teams_count"] = unnamed_teams_count
        if sample_keys is not UNSET:
            field_dict["sample_keys"] = sample_keys
        if sample_teams is not UNSET:
            field_dict["sample_teams"] = sample_teams

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_keys_count = d.pop("affected_keys_count", UNSET)

        affected_teams_count = d.pop("affected_teams_count", UNSET)

        unnamed_keys_count = d.pop("unnamed_keys_count", UNSET)

        unnamed_teams_count = d.pop("unnamed_teams_count", UNSET)

        sample_keys = cast(list[str], d.pop("sample_keys", UNSET))


        sample_teams = cast(list[str], d.pop("sample_teams", UNSET))


        attachment_impact_response = cls(
            affected_keys_count=affected_keys_count,
            affected_teams_count=affected_teams_count,
            unnamed_keys_count=unnamed_keys_count,
            unnamed_teams_count=unnamed_teams_count,
            sample_keys=sample_keys,
            sample_teams=sample_teams,
        )


        attachment_impact_response.additional_properties = d
        return attachment_impact_response

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
