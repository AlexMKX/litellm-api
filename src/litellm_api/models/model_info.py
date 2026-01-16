from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.model_info_tier_type_0 import ModelInfoTierType0
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ModelInfo")



@_attrs_define
class ModelInfo:
    """ 
        Attributes:
            id (None | str):
            db_model (bool | Unset):  Default: False.
            updated_at (datetime.datetime | None | Unset):
            updated_by (None | str | Unset):
            created_at (datetime.datetime | None | Unset):
            created_by (None | str | Unset):
            base_model (None | str | Unset):
            tier (ModelInfoTierType0 | None | Unset):
            team_id (None | str | Unset):
            team_public_model_name (None | str | Unset):
     """

    id: None | str
    db_model: bool | Unset = False
    updated_at: datetime.datetime | None | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    base_model: None | str | Unset = UNSET
    tier: ModelInfoTierType0 | None | Unset = UNSET
    team_id: None | str | Unset = UNSET
    team_public_model_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id: None | str
        id = self.id

        db_model = self.db_model

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        base_model: None | str | Unset
        if isinstance(self.base_model, Unset):
            base_model = UNSET
        else:
            base_model = self.base_model

        tier: None | str | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        elif isinstance(self.tier, ModelInfoTierType0):
            tier = self.tier.value
        else:
            tier = self.tier

        team_id: None | str | Unset
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        else:
            team_id = self.team_id

        team_public_model_name: None | str | Unset
        if isinstance(self.team_public_model_name, Unset):
            team_public_model_name = UNSET
        else:
            team_public_model_name = self.team_public_model_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
        })
        if db_model is not UNSET:
            field_dict["db_model"] = db_model
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if base_model is not UNSET:
            field_dict["base_model"] = base_model
        if tier is not UNSET:
            field_dict["tier"] = tier
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if team_public_model_name is not UNSET:
            field_dict["team_public_model_name"] = team_public_model_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))


        db_model = d.pop("db_model", UNSET)

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))


        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))


        def _parse_base_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_model = _parse_base_model(d.pop("base_model", UNSET))


        def _parse_tier(data: object) -> ModelInfoTierType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tier_type_0 = ModelInfoTierType0(data)



                return tier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelInfoTierType0 | None | Unset, data)

        tier = _parse_tier(d.pop("tier", UNSET))


        def _parse_team_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_id = _parse_team_id(d.pop("team_id", UNSET))


        def _parse_team_public_model_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_public_model_name = _parse_team_public_model_name(d.pop("team_public_model_name", UNSET))


        model_info = cls(
            id=id,
            db_model=db_model,
            updated_at=updated_at,
            updated_by=updated_by,
            created_at=created_at,
            created_by=created_by,
            base_model=base_model,
            tier=tier,
            team_id=team_id,
            team_public_model_name=team_public_model_name,
        )


        model_info.additional_properties = d
        return model_info

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
