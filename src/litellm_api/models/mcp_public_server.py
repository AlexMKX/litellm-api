from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mcp_public_server_auth_type_type_0 import MCPPublicServerAuthTypeType0
from ..models.mcp_public_server_transport import MCPPublicServerTransport
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mcp_public_server_mcp_info_type_0 import MCPPublicServerMcpInfoType0





T = TypeVar("T", bound="MCPPublicServer")



@_attrs_define
class MCPPublicServer:
    """ Safe params for public MCP servers

        Attributes:
            server_id (str):
            name (str):
            transport (MCPPublicServerTransport):
            alias (None | str | Unset):
            server_name (None | str | Unset):
            url (None | str | Unset):
            spec_path (None | str | Unset):
            auth_type (MCPPublicServerAuthTypeType0 | None | Unset):
            mcp_info (MCPPublicServerMcpInfoType0 | None | Unset):
     """

    server_id: str
    name: str
    transport: MCPPublicServerTransport
    alias: None | str | Unset = UNSET
    server_name: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    spec_path: None | str | Unset = UNSET
    auth_type: MCPPublicServerAuthTypeType0 | None | Unset = UNSET
    mcp_info: MCPPublicServerMcpInfoType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.mcp_public_server_mcp_info_type_0 import MCPPublicServerMcpInfoType0
        server_id = self.server_id

        name = self.name

        transport = self.transport.value

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        server_name: None | str | Unset
        if isinstance(self.server_name, Unset):
            server_name = UNSET
        else:
            server_name = self.server_name

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        spec_path: None | str | Unset
        if isinstance(self.spec_path, Unset):
            spec_path = UNSET
        else:
            spec_path = self.spec_path

        auth_type: None | str | Unset
        if isinstance(self.auth_type, Unset):
            auth_type = UNSET
        elif isinstance(self.auth_type, MCPPublicServerAuthTypeType0):
            auth_type = self.auth_type.value
        else:
            auth_type = self.auth_type

        mcp_info: dict[str, Any] | None | Unset
        if isinstance(self.mcp_info, Unset):
            mcp_info = UNSET
        elif isinstance(self.mcp_info, MCPPublicServerMcpInfoType0):
            mcp_info = self.mcp_info.to_dict()
        else:
            mcp_info = self.mcp_info


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "server_id": server_id,
            "name": name,
            "transport": transport,
        })
        if alias is not UNSET:
            field_dict["alias"] = alias
        if server_name is not UNSET:
            field_dict["server_name"] = server_name
        if url is not UNSET:
            field_dict["url"] = url
        if spec_path is not UNSET:
            field_dict["spec_path"] = spec_path
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if mcp_info is not UNSET:
            field_dict["mcp_info"] = mcp_info

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_public_server_mcp_info_type_0 import MCPPublicServerMcpInfoType0
        d = dict(src_dict)
        server_id = d.pop("server_id")

        name = d.pop("name")

        transport = MCPPublicServerTransport(d.pop("transport"))




        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))


        def _parse_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_name = _parse_server_name(d.pop("server_name", UNSET))


        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        def _parse_spec_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spec_path = _parse_spec_path(d.pop("spec_path", UNSET))


        def _parse_auth_type(data: object) -> MCPPublicServerAuthTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_type_type_0 = MCPPublicServerAuthTypeType0(data)



                return auth_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MCPPublicServerAuthTypeType0 | None | Unset, data)

        auth_type = _parse_auth_type(d.pop("auth_type", UNSET))


        def _parse_mcp_info(data: object) -> MCPPublicServerMcpInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mcp_info_type_0 = MCPPublicServerMcpInfoType0.from_dict(data)



                return mcp_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MCPPublicServerMcpInfoType0 | None | Unset, data)

        mcp_info = _parse_mcp_info(d.pop("mcp_info", UNSET))


        mcp_public_server = cls(
            server_id=server_id,
            name=name,
            transport=transport,
            alias=alias,
            server_name=server_name,
            url=url,
            spec_path=spec_path,
            auth_type=auth_type,
            mcp_info=mcp_info,
        )


        mcp_public_server.additional_properties = d
        return mcp_public_server

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
