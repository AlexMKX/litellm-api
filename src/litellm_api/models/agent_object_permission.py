from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_object_permission_mcp_tool_permissions_type_0 import AgentObjectPermissionMcpToolPermissionsType0





T = TypeVar("T", bound="AgentObjectPermission")



@_attrs_define
class AgentObjectPermission:
    """ 
        Attributes:
            mcp_servers (list[str] | None | Unset):
            mcp_access_groups (list[str] | None | Unset):
            mcp_tool_permissions (AgentObjectPermissionMcpToolPermissionsType0 | None | Unset):
     """

    mcp_servers: list[str] | None | Unset = UNSET
    mcp_access_groups: list[str] | None | Unset = UNSET
    mcp_tool_permissions: AgentObjectPermissionMcpToolPermissionsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_object_permission_mcp_tool_permissions_type_0 import AgentObjectPermissionMcpToolPermissionsType0
        mcp_servers: list[str] | None | Unset
        if isinstance(self.mcp_servers, Unset):
            mcp_servers = UNSET
        elif isinstance(self.mcp_servers, list):
            mcp_servers = self.mcp_servers


        else:
            mcp_servers = self.mcp_servers

        mcp_access_groups: list[str] | None | Unset
        if isinstance(self.mcp_access_groups, Unset):
            mcp_access_groups = UNSET
        elif isinstance(self.mcp_access_groups, list):
            mcp_access_groups = self.mcp_access_groups


        else:
            mcp_access_groups = self.mcp_access_groups

        mcp_tool_permissions: dict[str, Any] | None | Unset
        if isinstance(self.mcp_tool_permissions, Unset):
            mcp_tool_permissions = UNSET
        elif isinstance(self.mcp_tool_permissions, AgentObjectPermissionMcpToolPermissionsType0):
            mcp_tool_permissions = self.mcp_tool_permissions.to_dict()
        else:
            mcp_tool_permissions = self.mcp_tool_permissions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if mcp_servers is not UNSET:
            field_dict["mcp_servers"] = mcp_servers
        if mcp_access_groups is not UNSET:
            field_dict["mcp_access_groups"] = mcp_access_groups
        if mcp_tool_permissions is not UNSET:
            field_dict["mcp_tool_permissions"] = mcp_tool_permissions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_object_permission_mcp_tool_permissions_type_0 import AgentObjectPermissionMcpToolPermissionsType0
        d = dict(src_dict)
        def _parse_mcp_servers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mcp_servers_type_0 = cast(list[str], data)

                return mcp_servers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        mcp_servers = _parse_mcp_servers(d.pop("mcp_servers", UNSET))


        def _parse_mcp_access_groups(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mcp_access_groups_type_0 = cast(list[str], data)

                return mcp_access_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        mcp_access_groups = _parse_mcp_access_groups(d.pop("mcp_access_groups", UNSET))


        def _parse_mcp_tool_permissions(data: object) -> AgentObjectPermissionMcpToolPermissionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mcp_tool_permissions_type_0 = AgentObjectPermissionMcpToolPermissionsType0.from_dict(data)



                return mcp_tool_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentObjectPermissionMcpToolPermissionsType0 | None | Unset, data)

        mcp_tool_permissions = _parse_mcp_tool_permissions(d.pop("mcp_tool_permissions", UNSET))


        agent_object_permission = cls(
            mcp_servers=mcp_servers,
            mcp_access_groups=mcp_access_groups,
            mcp_tool_permissions=mcp_tool_permissions,
        )


        agent_object_permission.additional_properties = d
        return agent_object_permission

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
