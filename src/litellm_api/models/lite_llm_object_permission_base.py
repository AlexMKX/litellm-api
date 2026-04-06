from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.lite_llm_object_permission_base_mcp_tool_permissions_type_0 import LiteLLMObjectPermissionBaseMcpToolPermissionsType0





T = TypeVar("T", bound="LiteLLMObjectPermissionBase")



@_attrs_define
class LiteLLMObjectPermissionBase:
    """ 
        Attributes:
            mcp_servers (list[str] | None | Unset):
            mcp_access_groups (list[str] | None | Unset):
            mcp_tool_permissions (LiteLLMObjectPermissionBaseMcpToolPermissionsType0 | None | Unset):
            mcp_toolsets (list[str] | None | Unset):
            blocked_tools (list[str] | None | Unset):
            vector_stores (list[str] | None | Unset):
            agents (list[str] | None | Unset):
            agent_access_groups (list[str] | None | Unset):
            models (list[str] | None | Unset):
     """

    mcp_servers: list[str] | None | Unset = UNSET
    mcp_access_groups: list[str] | None | Unset = UNSET
    mcp_tool_permissions: LiteLLMObjectPermissionBaseMcpToolPermissionsType0 | None | Unset = UNSET
    mcp_toolsets: list[str] | None | Unset = UNSET
    blocked_tools: list[str] | None | Unset = UNSET
    vector_stores: list[str] | None | Unset = UNSET
    agents: list[str] | None | Unset = UNSET
    agent_access_groups: list[str] | None | Unset = UNSET
    models: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llm_object_permission_base_mcp_tool_permissions_type_0 import LiteLLMObjectPermissionBaseMcpToolPermissionsType0
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
        elif isinstance(self.mcp_tool_permissions, LiteLLMObjectPermissionBaseMcpToolPermissionsType0):
            mcp_tool_permissions = self.mcp_tool_permissions.to_dict()
        else:
            mcp_tool_permissions = self.mcp_tool_permissions

        mcp_toolsets: list[str] | None | Unset
        if isinstance(self.mcp_toolsets, Unset):
            mcp_toolsets = UNSET
        elif isinstance(self.mcp_toolsets, list):
            mcp_toolsets = self.mcp_toolsets


        else:
            mcp_toolsets = self.mcp_toolsets

        blocked_tools: list[str] | None | Unset
        if isinstance(self.blocked_tools, Unset):
            blocked_tools = UNSET
        elif isinstance(self.blocked_tools, list):
            blocked_tools = self.blocked_tools


        else:
            blocked_tools = self.blocked_tools

        vector_stores: list[str] | None | Unset
        if isinstance(self.vector_stores, Unset):
            vector_stores = UNSET
        elif isinstance(self.vector_stores, list):
            vector_stores = self.vector_stores


        else:
            vector_stores = self.vector_stores

        agents: list[str] | None | Unset
        if isinstance(self.agents, Unset):
            agents = UNSET
        elif isinstance(self.agents, list):
            agents = self.agents


        else:
            agents = self.agents

        agent_access_groups: list[str] | None | Unset
        if isinstance(self.agent_access_groups, Unset):
            agent_access_groups = UNSET
        elif isinstance(self.agent_access_groups, list):
            agent_access_groups = self.agent_access_groups


        else:
            agent_access_groups = self.agent_access_groups

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
        })
        if mcp_servers is not UNSET:
            field_dict["mcp_servers"] = mcp_servers
        if mcp_access_groups is not UNSET:
            field_dict["mcp_access_groups"] = mcp_access_groups
        if mcp_tool_permissions is not UNSET:
            field_dict["mcp_tool_permissions"] = mcp_tool_permissions
        if mcp_toolsets is not UNSET:
            field_dict["mcp_toolsets"] = mcp_toolsets
        if blocked_tools is not UNSET:
            field_dict["blocked_tools"] = blocked_tools
        if vector_stores is not UNSET:
            field_dict["vector_stores"] = vector_stores
        if agents is not UNSET:
            field_dict["agents"] = agents
        if agent_access_groups is not UNSET:
            field_dict["agent_access_groups"] = agent_access_groups
        if models is not UNSET:
            field_dict["models"] = models

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llm_object_permission_base_mcp_tool_permissions_type_0 import LiteLLMObjectPermissionBaseMcpToolPermissionsType0
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


        def _parse_mcp_tool_permissions(data: object) -> LiteLLMObjectPermissionBaseMcpToolPermissionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mcp_tool_permissions_type_0 = LiteLLMObjectPermissionBaseMcpToolPermissionsType0.from_dict(data)



                return mcp_tool_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMObjectPermissionBaseMcpToolPermissionsType0 | None | Unset, data)

        mcp_tool_permissions = _parse_mcp_tool_permissions(d.pop("mcp_tool_permissions", UNSET))


        def _parse_mcp_toolsets(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mcp_toolsets_type_0 = cast(list[str], data)

                return mcp_toolsets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        mcp_toolsets = _parse_mcp_toolsets(d.pop("mcp_toolsets", UNSET))


        def _parse_blocked_tools(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blocked_tools_type_0 = cast(list[str], data)

                return blocked_tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        blocked_tools = _parse_blocked_tools(d.pop("blocked_tools", UNSET))


        def _parse_vector_stores(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                vector_stores_type_0 = cast(list[str], data)

                return vector_stores_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        vector_stores = _parse_vector_stores(d.pop("vector_stores", UNSET))


        def _parse_agents(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                agents_type_0 = cast(list[str], data)

                return agents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        agents = _parse_agents(d.pop("agents", UNSET))


        def _parse_agent_access_groups(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                agent_access_groups_type_0 = cast(list[str], data)

                return agent_access_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        agent_access_groups = _parse_agent_access_groups(d.pop("agent_access_groups", UNSET))


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


        lite_llm_object_permission_base = cls(
            mcp_servers=mcp_servers,
            mcp_access_groups=mcp_access_groups,
            mcp_tool_permissions=mcp_tool_permissions,
            mcp_toolsets=mcp_toolsets,
            blocked_tools=blocked_tools,
            vector_stores=vector_stores,
            agents=agents,
            agent_access_groups=agent_access_groups,
            models=models,
        )


        lite_llm_object_permission_base.additional_properties = d
        return lite_llm_object_permission_base

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
