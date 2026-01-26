from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PolicyAttachmentCreateRequest")



@_attrs_define
class PolicyAttachmentCreateRequest:
    """ Request body for creating a policy attachment.

        Attributes:
            policy_name (str): Name of the policy to attach.
            scope (None | str | Unset): Use '*' for global scope (applies to all requests).
            teams (list[str] | None | Unset): Team aliases or patterns this attachment applies to.
            keys (list[str] | None | Unset): Key aliases or patterns this attachment applies to.
            models (list[str] | None | Unset): Model names or patterns this attachment applies to.
     """

    policy_name: str
    scope: None | str | Unset = UNSET
    teams: list[str] | None | Unset = UNSET
    keys: list[str] | None | Unset = UNSET
    models: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        policy_name = self.policy_name

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        teams: list[str] | None | Unset
        if isinstance(self.teams, Unset):
            teams = UNSET
        elif isinstance(self.teams, list):
            teams = self.teams


        else:
            teams = self.teams

        keys: list[str] | None | Unset
        if isinstance(self.keys, Unset):
            keys = UNSET
        elif isinstance(self.keys, list):
            keys = self.keys


        else:
            keys = self.keys

        models: list[str] | None | Unset
        if isinstance(self.models, Unset):
            models = UNSET
        elif isinstance(self.models, list):
            models = self.models


        else:
            models = self.models


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "policy_name": policy_name,
        })
        if scope is not UNSET:
            field_dict["scope"] = scope
        if teams is not UNSET:
            field_dict["teams"] = teams
        if keys is not UNSET:
            field_dict["keys"] = keys
        if models is not UNSET:
            field_dict["models"] = models

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        policy_name = d.pop("policy_name")

        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))


        def _parse_teams(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                teams_type_0 = cast(list[str], data)

                return teams_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        teams = _parse_teams(d.pop("teams", UNSET))


        def _parse_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keys_type_0 = cast(list[str], data)

                return keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keys = _parse_keys(d.pop("keys", UNSET))


        def _parse_models(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                models_type_0 = cast(list[str], data)

                return models_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        models = _parse_models(d.pop("models", UNSET))


        policy_attachment_create_request = cls(
            policy_name=policy_name,
            scope=scope,
            teams=teams,
            keys=keys,
            models=models,
        )


        policy_attachment_create_request.additional_properties = d
        return policy_attachment_create_request

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
