from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PolicyMatchContext")



@_attrs_define
class PolicyMatchContext:
    """ Context used to match a request against policies.

    Contains the team alias, key alias, and model from the incoming request.

        Attributes:
            team_alias (None | str | Unset): Team alias from the request.
            key_alias (None | str | Unset): API key alias from the request.
            model (None | str | Unset): Model name from the request.
            tags (list[str] | None | Unset): Tags from key/team metadata.
     """

    team_alias: None | str | Unset = UNSET
    key_alias: None | str | Unset = UNSET
    model: None | str | Unset = UNSET
    tags: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        team_alias: None | str | Unset
        if isinstance(self.team_alias, Unset):
            team_alias = UNSET
        else:
            team_alias = self.team_alias

        key_alias: None | str | Unset
        if isinstance(self.key_alias, Unset):
            key_alias = UNSET
        else:
            key_alias = self.key_alias

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags


        else:
            tags = self.tags


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if team_alias is not UNSET:
            field_dict["team_alias"] = team_alias
        if key_alias is not UNSET:
            field_dict["key_alias"] = key_alias
        if model is not UNSET:
            field_dict["model"] = model
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_team_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_alias = _parse_team_alias(d.pop("team_alias", UNSET))


        def _parse_key_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_alias = _parse_key_alias(d.pop("key_alias", UNSET))


        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))


        policy_match_context = cls(
            team_alias=team_alias,
            key_alias=key_alias,
            model=model,
            tags=tags,
        )

        return policy_match_context

