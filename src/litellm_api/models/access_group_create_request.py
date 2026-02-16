from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AccessGroupCreateRequest")



@_attrs_define
class AccessGroupCreateRequest:
    """ 
        Attributes:
            access_group_name (str):
            description (None | str | Unset):
            access_model_names (list[str] | None | Unset):
            access_mcp_server_ids (list[str] | None | Unset):
            access_agent_ids (list[str] | None | Unset):
            assigned_team_ids (list[str] | None | Unset):
            assigned_key_ids (list[str] | None | Unset):
     """

    access_group_name: str
    description: None | str | Unset = UNSET
    access_model_names: list[str] | None | Unset = UNSET
    access_mcp_server_ids: list[str] | None | Unset = UNSET
    access_agent_ids: list[str] | None | Unset = UNSET
    assigned_team_ids: list[str] | None | Unset = UNSET
    assigned_key_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        access_group_name = self.access_group_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        access_model_names: list[str] | None | Unset
        if isinstance(self.access_model_names, Unset):
            access_model_names = UNSET
        elif isinstance(self.access_model_names, list):
            access_model_names = self.access_model_names


        else:
            access_model_names = self.access_model_names

        access_mcp_server_ids: list[str] | None | Unset
        if isinstance(self.access_mcp_server_ids, Unset):
            access_mcp_server_ids = UNSET
        elif isinstance(self.access_mcp_server_ids, list):
            access_mcp_server_ids = self.access_mcp_server_ids


        else:
            access_mcp_server_ids = self.access_mcp_server_ids

        access_agent_ids: list[str] | None | Unset
        if isinstance(self.access_agent_ids, Unset):
            access_agent_ids = UNSET
        elif isinstance(self.access_agent_ids, list):
            access_agent_ids = self.access_agent_ids


        else:
            access_agent_ids = self.access_agent_ids

        assigned_team_ids: list[str] | None | Unset
        if isinstance(self.assigned_team_ids, Unset):
            assigned_team_ids = UNSET
        elif isinstance(self.assigned_team_ids, list):
            assigned_team_ids = self.assigned_team_ids


        else:
            assigned_team_ids = self.assigned_team_ids

        assigned_key_ids: list[str] | None | Unset
        if isinstance(self.assigned_key_ids, Unset):
            assigned_key_ids = UNSET
        elif isinstance(self.assigned_key_ids, list):
            assigned_key_ids = self.assigned_key_ids


        else:
            assigned_key_ids = self.assigned_key_ids


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "access_group_name": access_group_name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if access_model_names is not UNSET:
            field_dict["access_model_names"] = access_model_names
        if access_mcp_server_ids is not UNSET:
            field_dict["access_mcp_server_ids"] = access_mcp_server_ids
        if access_agent_ids is not UNSET:
            field_dict["access_agent_ids"] = access_agent_ids
        if assigned_team_ids is not UNSET:
            field_dict["assigned_team_ids"] = assigned_team_ids
        if assigned_key_ids is not UNSET:
            field_dict["assigned_key_ids"] = assigned_key_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_group_name = d.pop("access_group_name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_access_model_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_model_names_type_0 = cast(list[str], data)

                return access_model_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        access_model_names = _parse_access_model_names(d.pop("access_model_names", UNSET))


        def _parse_access_mcp_server_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_mcp_server_ids_type_0 = cast(list[str], data)

                return access_mcp_server_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        access_mcp_server_ids = _parse_access_mcp_server_ids(d.pop("access_mcp_server_ids", UNSET))


        def _parse_access_agent_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_agent_ids_type_0 = cast(list[str], data)

                return access_agent_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        access_agent_ids = _parse_access_agent_ids(d.pop("access_agent_ids", UNSET))


        def _parse_assigned_team_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_team_ids_type_0 = cast(list[str], data)

                return assigned_team_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        assigned_team_ids = _parse_assigned_team_ids(d.pop("assigned_team_ids", UNSET))


        def _parse_assigned_key_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_key_ids_type_0 = cast(list[str], data)

                return assigned_key_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        assigned_key_ids = _parse_assigned_key_ids(d.pop("assigned_key_ids", UNSET))


        access_group_create_request = cls(
            access_group_name=access_group_name,
            description=description,
            access_model_names=access_model_names,
            access_mcp_server_ids=access_mcp_server_ids,
            access_agent_ids=access_agent_ids,
            assigned_team_ids=assigned_team_ids,
            assigned_key_ids=assigned_key_ids,
        )


        access_group_create_request.additional_properties = d
        return access_group_create_request

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
