from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.new_mcp_server_request_auth_type_type_0 import NewMCPServerRequestAuthTypeType0
from ..models.new_mcp_server_request_transport import NewMCPServerRequestTransport
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mcp_credentials import MCPCredentials
  from ..models.new_mcp_server_request_env import NewMCPServerRequestEnv
  from ..models.new_mcp_server_request_mcp_info_type_0 import NewMCPServerRequestMcpInfoType0
  from ..models.new_mcp_server_request_static_headers_type_0 import NewMCPServerRequestStaticHeadersType0





T = TypeVar("T", bound="NewMCPServerRequest")



@_attrs_define
class NewMCPServerRequest:
    """ 
        Attributes:
            server_id (None | str | Unset):
            server_name (None | str | Unset):
            alias (None | str | Unset):
            description (None | str | Unset):
            transport (NewMCPServerRequestTransport | Unset):  Default: NewMCPServerRequestTransport.SSE.
            auth_type (NewMCPServerRequestAuthTypeType0 | None | Unset):
            credentials (MCPCredentials | None | Unset):
            url (None | str | Unset):
            mcp_info (NewMCPServerRequestMcpInfoType0 | None | Unset):
            mcp_access_groups (list[str] | Unset):
            allowed_tools (list[str] | None | Unset):
            extra_headers (list[str] | None | Unset):
            static_headers (NewMCPServerRequestStaticHeadersType0 | None | Unset):
            command (None | str | Unset):
            args (list[str] | Unset):
            env (NewMCPServerRequestEnv | Unset):
            authorization_url (None | str | Unset):
            token_url (None | str | Unset):
            registration_url (None | str | Unset):
            allow_all_keys (bool | Unset):  Default: False.
     """

    server_id: None | str | Unset = UNSET
    server_name: None | str | Unset = UNSET
    alias: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    transport: NewMCPServerRequestTransport | Unset = NewMCPServerRequestTransport.SSE
    auth_type: NewMCPServerRequestAuthTypeType0 | None | Unset = UNSET
    credentials: MCPCredentials | None | Unset = UNSET
    url: None | str | Unset = UNSET
    mcp_info: NewMCPServerRequestMcpInfoType0 | None | Unset = UNSET
    mcp_access_groups: list[str] | Unset = UNSET
    allowed_tools: list[str] | None | Unset = UNSET
    extra_headers: list[str] | None | Unset = UNSET
    static_headers: NewMCPServerRequestStaticHeadersType0 | None | Unset = UNSET
    command: None | str | Unset = UNSET
    args: list[str] | Unset = UNSET
    env: NewMCPServerRequestEnv | Unset = UNSET
    authorization_url: None | str | Unset = UNSET
    token_url: None | str | Unset = UNSET
    registration_url: None | str | Unset = UNSET
    allow_all_keys: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.new_mcp_server_request_static_headers_type_0 import NewMCPServerRequestStaticHeadersType0
        from ..models.new_mcp_server_request_env import NewMCPServerRequestEnv
        from ..models.new_mcp_server_request_mcp_info_type_0 import NewMCPServerRequestMcpInfoType0
        from ..models.mcp_credentials import MCPCredentials
        server_id: None | str | Unset
        if isinstance(self.server_id, Unset):
            server_id = UNSET
        else:
            server_id = self.server_id

        server_name: None | str | Unset
        if isinstance(self.server_name, Unset):
            server_name = UNSET
        else:
            server_name = self.server_name

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        transport: str | Unset = UNSET
        if not isinstance(self.transport, Unset):
            transport = self.transport.value


        auth_type: None | str | Unset
        if isinstance(self.auth_type, Unset):
            auth_type = UNSET
        elif isinstance(self.auth_type, NewMCPServerRequestAuthTypeType0):
            auth_type = self.auth_type.value
        else:
            auth_type = self.auth_type

        credentials: dict[str, Any] | None | Unset
        if isinstance(self.credentials, Unset):
            credentials = UNSET
        elif isinstance(self.credentials, MCPCredentials):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        mcp_info: dict[str, Any] | None | Unset
        if isinstance(self.mcp_info, Unset):
            mcp_info = UNSET
        elif isinstance(self.mcp_info, NewMCPServerRequestMcpInfoType0):
            mcp_info = self.mcp_info.to_dict()
        else:
            mcp_info = self.mcp_info

        mcp_access_groups: list[str] | Unset = UNSET
        if not isinstance(self.mcp_access_groups, Unset):
            mcp_access_groups = self.mcp_access_groups



        allowed_tools: list[str] | None | Unset
        if isinstance(self.allowed_tools, Unset):
            allowed_tools = UNSET
        elif isinstance(self.allowed_tools, list):
            allowed_tools = self.allowed_tools


        else:
            allowed_tools = self.allowed_tools

        extra_headers: list[str] | None | Unset
        if isinstance(self.extra_headers, Unset):
            extra_headers = UNSET
        elif isinstance(self.extra_headers, list):
            extra_headers = self.extra_headers


        else:
            extra_headers = self.extra_headers

        static_headers: dict[str, Any] | None | Unset
        if isinstance(self.static_headers, Unset):
            static_headers = UNSET
        elif isinstance(self.static_headers, NewMCPServerRequestStaticHeadersType0):
            static_headers = self.static_headers.to_dict()
        else:
            static_headers = self.static_headers

        command: None | str | Unset
        if isinstance(self.command, Unset):
            command = UNSET
        else:
            command = self.command

        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args



        env: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

        authorization_url: None | str | Unset
        if isinstance(self.authorization_url, Unset):
            authorization_url = UNSET
        else:
            authorization_url = self.authorization_url

        token_url: None | str | Unset
        if isinstance(self.token_url, Unset):
            token_url = UNSET
        else:
            token_url = self.token_url

        registration_url: None | str | Unset
        if isinstance(self.registration_url, Unset):
            registration_url = UNSET
        else:
            registration_url = self.registration_url

        allow_all_keys = self.allow_all_keys


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if server_id is not UNSET:
            field_dict["server_id"] = server_id
        if server_name is not UNSET:
            field_dict["server_name"] = server_name
        if alias is not UNSET:
            field_dict["alias"] = alias
        if description is not UNSET:
            field_dict["description"] = description
        if transport is not UNSET:
            field_dict["transport"] = transport
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if url is not UNSET:
            field_dict["url"] = url
        if mcp_info is not UNSET:
            field_dict["mcp_info"] = mcp_info
        if mcp_access_groups is not UNSET:
            field_dict["mcp_access_groups"] = mcp_access_groups
        if allowed_tools is not UNSET:
            field_dict["allowed_tools"] = allowed_tools
        if extra_headers is not UNSET:
            field_dict["extra_headers"] = extra_headers
        if static_headers is not UNSET:
            field_dict["static_headers"] = static_headers
        if command is not UNSET:
            field_dict["command"] = command
        if args is not UNSET:
            field_dict["args"] = args
        if env is not UNSET:
            field_dict["env"] = env
        if authorization_url is not UNSET:
            field_dict["authorization_url"] = authorization_url
        if token_url is not UNSET:
            field_dict["token_url"] = token_url
        if registration_url is not UNSET:
            field_dict["registration_url"] = registration_url
        if allow_all_keys is not UNSET:
            field_dict["allow_all_keys"] = allow_all_keys

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_credentials import MCPCredentials
        from ..models.new_mcp_server_request_env import NewMCPServerRequestEnv
        from ..models.new_mcp_server_request_mcp_info_type_0 import NewMCPServerRequestMcpInfoType0
        from ..models.new_mcp_server_request_static_headers_type_0 import NewMCPServerRequestStaticHeadersType0
        d = dict(src_dict)
        def _parse_server_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_id = _parse_server_id(d.pop("server_id", UNSET))


        def _parse_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_name = _parse_server_name(d.pop("server_name", UNSET))


        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        _transport = d.pop("transport", UNSET)
        transport: NewMCPServerRequestTransport | Unset
        if isinstance(_transport,  Unset):
            transport = UNSET
        else:
            transport = NewMCPServerRequestTransport(_transport)




        def _parse_auth_type(data: object) -> NewMCPServerRequestAuthTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_type_type_0 = NewMCPServerRequestAuthTypeType0(data)



                return auth_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewMCPServerRequestAuthTypeType0 | None | Unset, data)

        auth_type = _parse_auth_type(d.pop("auth_type", UNSET))


        def _parse_credentials(data: object) -> MCPCredentials | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = MCPCredentials.from_dict(data)



                return credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MCPCredentials | None | Unset, data)

        credentials = _parse_credentials(d.pop("credentials", UNSET))


        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        def _parse_mcp_info(data: object) -> NewMCPServerRequestMcpInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mcp_info_type_0 = NewMCPServerRequestMcpInfoType0.from_dict(data)



                return mcp_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewMCPServerRequestMcpInfoType0 | None | Unset, data)

        mcp_info = _parse_mcp_info(d.pop("mcp_info", UNSET))


        mcp_access_groups = cast(list[str], d.pop("mcp_access_groups", UNSET))


        def _parse_allowed_tools(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_tools_type_0 = cast(list[str], data)

                return allowed_tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_tools = _parse_allowed_tools(d.pop("allowed_tools", UNSET))


        def _parse_extra_headers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                extra_headers_type_0 = cast(list[str], data)

                return extra_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        extra_headers = _parse_extra_headers(d.pop("extra_headers", UNSET))


        def _parse_static_headers(data: object) -> NewMCPServerRequestStaticHeadersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                static_headers_type_0 = NewMCPServerRequestStaticHeadersType0.from_dict(data)



                return static_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewMCPServerRequestStaticHeadersType0 | None | Unset, data)

        static_headers = _parse_static_headers(d.pop("static_headers", UNSET))


        def _parse_command(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        command = _parse_command(d.pop("command", UNSET))


        args = cast(list[str], d.pop("args", UNSET))


        _env = d.pop("env", UNSET)
        env: NewMCPServerRequestEnv | Unset
        if isinstance(_env,  Unset):
            env = UNSET
        else:
            env = NewMCPServerRequestEnv.from_dict(_env)




        def _parse_authorization_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authorization_url = _parse_authorization_url(d.pop("authorization_url", UNSET))


        def _parse_token_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token_url = _parse_token_url(d.pop("token_url", UNSET))


        def _parse_registration_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_url = _parse_registration_url(d.pop("registration_url", UNSET))


        allow_all_keys = d.pop("allow_all_keys", UNSET)

        new_mcp_server_request = cls(
            server_id=server_id,
            server_name=server_name,
            alias=alias,
            description=description,
            transport=transport,
            auth_type=auth_type,
            credentials=credentials,
            url=url,
            mcp_info=mcp_info,
            mcp_access_groups=mcp_access_groups,
            allowed_tools=allowed_tools,
            extra_headers=extra_headers,
            static_headers=static_headers,
            command=command,
            args=args,
            env=env,
            authorization_url=authorization_url,
            token_url=token_url,
            registration_url=registration_url,
            allow_all_keys=allow_all_keys,
        )


        new_mcp_server_request.additional_properties = d
        return new_mcp_server_request

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
