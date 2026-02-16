from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PolicyScopeResponse")



@_attrs_define
class PolicyScopeResponse:
    """ Scope configuration for a policy.

        Attributes:
            teams (list[str] | Unset):
            keys (list[str] | Unset):
            models (list[str] | Unset):
            tags (list[str] | Unset):
     """

    teams: list[str] | Unset = UNSET
    keys: list[str] | Unset = UNSET
    models: list[str] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        teams: list[str] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = self.teams



        keys: list[str] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = self.keys



        models: list[str] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = self.models



        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if teams is not UNSET:
            field_dict["teams"] = teams
        if keys is not UNSET:
            field_dict["keys"] = keys
        if models is not UNSET:
            field_dict["models"] = models
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        teams = cast(list[str], d.pop("teams", UNSET))


        keys = cast(list[str], d.pop("keys", UNSET))


        models = cast(list[str], d.pop("models", UNSET))


        tags = cast(list[str], d.pop("tags", UNSET))


        policy_scope_response = cls(
            teams=teams,
            keys=keys,
            models=models,
            tags=tags,
        )


        policy_scope_response.additional_properties = d
        return policy_scope_response

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
