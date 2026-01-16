from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.default_internal_user_params_user_role_type_0 import DefaultInternalUserParamsUserRoleType0
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.new_user_request_team import NewUserRequestTeam





T = TypeVar("T", bound="DefaultInternalUserParams")



@_attrs_define
class DefaultInternalUserParams:
    """ Default parameters to apply when a new user signs in via SSO or is created on the /user/new API endpoint

        Attributes:
            user_role (DefaultInternalUserParamsUserRoleType0 | None | Unset): Default role assigned to new users created
                Default: DefaultInternalUserParamsUserRoleType0.INTERNAL_USER.
            max_budget (float | None | Unset): Default maximum budget (in USD) for new users created
            budget_duration (None | str | Unset): Default budget duration for new users (e.g. 'daily', 'weekly', 'monthly')
            models (list[str] | None | Unset): Default list of models that new users can access
            teams (list[NewUserRequestTeam] | list[str] | None | Unset): Default teams for new users created
     """

    user_role: DefaultInternalUserParamsUserRoleType0 | None | Unset = DefaultInternalUserParamsUserRoleType0.INTERNAL_USER
    max_budget: float | None | Unset = UNSET
    budget_duration: None | str | Unset = UNSET
    models: list[str] | None | Unset = UNSET
    teams: list[NewUserRequestTeam] | list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.new_user_request_team import NewUserRequestTeam
        user_role: None | str | Unset
        if isinstance(self.user_role, Unset):
            user_role = UNSET
        elif isinstance(self.user_role, DefaultInternalUserParamsUserRoleType0):
            user_role = self.user_role.value
        else:
            user_role = self.user_role

        max_budget: float | None | Unset
        if isinstance(self.max_budget, Unset):
            max_budget = UNSET
        else:
            max_budget = self.max_budget

        budget_duration: None | str | Unset
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration

        models: list[str] | None | Unset
        if isinstance(self.models, Unset):
            models = UNSET
        elif isinstance(self.models, list):
            models = self.models


        else:
            models = self.models

        teams: list[dict[str, Any]] | list[str] | None | Unset
        if isinstance(self.teams, Unset):
            teams = UNSET
        elif isinstance(self.teams, list):
            teams = self.teams


        elif isinstance(self.teams, list):
            teams = []
            for teams_type_1_item_data in self.teams:
                teams_type_1_item = teams_type_1_item_data.to_dict()
                teams.append(teams_type_1_item)


        else:
            teams = self.teams


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if user_role is not UNSET:
            field_dict["user_role"] = user_role
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if budget_duration is not UNSET:
            field_dict["budget_duration"] = budget_duration
        if models is not UNSET:
            field_dict["models"] = models
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_user_request_team import NewUserRequestTeam
        d = dict(src_dict)
        def _parse_user_role(data: object) -> DefaultInternalUserParamsUserRoleType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_role_type_0 = DefaultInternalUserParamsUserRoleType0(data)



                return user_role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DefaultInternalUserParamsUserRoleType0 | None | Unset, data)

        user_role = _parse_user_role(d.pop("user_role", UNSET))


        def _parse_max_budget(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_budget = _parse_max_budget(d.pop("max_budget", UNSET))


        def _parse_budget_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))


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


        def _parse_teams(data: object) -> list[NewUserRequestTeam] | list[str] | None | Unset:
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
            try:
                if not isinstance(data, list):
                    raise TypeError()
                teams_type_1 = []
                _teams_type_1 = data
                for teams_type_1_item_data in (_teams_type_1):
                    teams_type_1_item = NewUserRequestTeam.from_dict(teams_type_1_item_data)



                    teams_type_1.append(teams_type_1_item)

                return teams_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NewUserRequestTeam] | list[str] | None | Unset, data)

        teams = _parse_teams(d.pop("teams", UNSET))


        default_internal_user_params = cls(
            user_role=user_role,
            max_budget=max_budget,
            budget_duration=budget_duration,
            models=models,
            teams=teams,
        )


        default_internal_user_params.additional_properties = d
        return default_internal_user_params

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
