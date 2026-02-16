from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="AccessGroupResponse")



@_attrs_define
class AccessGroupResponse:
    """ 
        Attributes:
            access_group_id (str):
            access_group_name (str):
            access_model_names (list[str]):
            access_mcp_server_ids (list[str]):
            access_agent_ids (list[str]):
            assigned_team_ids (list[str]):
            assigned_key_ids (list[str]):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            description (None | str | Unset):
            created_by (None | str | Unset):
            updated_by (None | str | Unset):
     """

    access_group_id: str
    access_group_name: str
    access_model_names: list[str]
    access_mcp_server_ids: list[str]
    access_agent_ids: list[str]
    assigned_team_ids: list[str]
    assigned_key_ids: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: None | str | Unset = UNSET
    created_by: None | str | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        access_group_id = self.access_group_id

        access_group_name = self.access_group_name

        access_model_names = self.access_model_names



        access_mcp_server_ids = self.access_mcp_server_ids



        access_agent_ids = self.access_agent_ids



        assigned_team_ids = self.assigned_team_ids



        assigned_key_ids = self.assigned_key_ids



        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "access_group_id": access_group_id,
            "access_group_name": access_group_name,
            "access_model_names": access_model_names,
            "access_mcp_server_ids": access_mcp_server_ids,
            "access_agent_ids": access_agent_ids,
            "assigned_team_ids": assigned_team_ids,
            "assigned_key_ids": assigned_key_ids,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_group_id = d.pop("access_group_id")

        access_group_name = d.pop("access_group_name")

        access_model_names = cast(list[str], d.pop("access_model_names"))


        access_mcp_server_ids = cast(list[str], d.pop("access_mcp_server_ids"))


        access_agent_ids = cast(list[str], d.pop("access_agent_ids"))


        assigned_team_ids = cast(list[str], d.pop("assigned_team_ids"))


        assigned_key_ids = cast(list[str], d.pop("assigned_key_ids"))


        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))


        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))


        access_group_response = cls(
            access_group_id=access_group_id,
            access_group_name=access_group_name,
            access_model_names=access_model_names,
            access_mcp_server_ids=access_mcp_server_ids,
            access_agent_ids=access_agent_ids,
            assigned_team_ids=assigned_team_ids,
            assigned_key_ids=assigned_key_ids,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            created_by=created_by,
            updated_by=updated_by,
        )


        access_group_response.additional_properties = d
        return access_group_response

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
