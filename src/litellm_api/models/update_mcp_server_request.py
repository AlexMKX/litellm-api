from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_mcp_server_request_auth_type_type_0 import UpdateMCPServerRequestAuthTypeType0
from ..models.update_mcp_server_request_transport import UpdateMCPServerRequestTransport
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mcp_credentials import MCPCredentials
  from ..models.update_mcp_server_request_env import UpdateMCPServerRequestEnv
  from ..models.update_mcp_server_request_mcp_info_type_0 import UpdateMCPServerRequestMcpInfoType0
  from ..models.update_mcp_server_request_static_headers_type_0 import UpdateMCPServerRequestStaticHeadersType0
  from ..models.update_mcp_server_request_tool_name_to_description_type_0 import UpdateMCPServerRequestToolNameToDescriptionType0
  from ..models.update_mcp_server_request_tool_name_to_display_name_type_0 import UpdateMCPServerRequestToolNameToDisplayNameType0





T = TypeVar("T", bound="UpdateMCPServerRequest")



@_attrs_define
class UpdateMCPServerRequest:
    """ 
        Attributes:
            server_id (str):
            alias (None | str | Unset):
            allow_all_keys (bool | Unset):  Default: False.
            allowed_tools (list[str] | None | Unset):
            args (list[str] | Unset):
            auth_type (None | Unset | UpdateMCPServerRequestAuthTypeType0):
            authorization_url (None | str | Unset):
            available_on_public_internet (bool | Unset):  Default: True.
            byok_api_key_help_url (None | str | Unset):
            byok_description (list[str] | Unset):
            command (None | str | Unset):
            credentials (MCPCredentials | None | Unset):
            description (None | str | Unset):
            env (UpdateMCPServerRequestEnv | Unset):
            extra_headers (list[str] | None | Unset):
            instructions (None | str | Unset):
            is_byok (bool | Unset):  Default: False.
            mcp_access_groups (list[str] | Unset):
            mcp_info (None | Unset | UpdateMCPServerRequestMcpInfoType0):
            registration_url (None | str | Unset):
            server_name (None | str | Unset):
            source_url (None | str | Unset):
            spec_path (None | str | Unset):
            static_headers (None | Unset | UpdateMCPServerRequestStaticHeadersType0):
            token_url (None | str | Unset):
            tool_name_to_description (None | Unset | UpdateMCPServerRequestToolNameToDescriptionType0):
            tool_name_to_display_name (None | Unset | UpdateMCPServerRequestToolNameToDisplayNameType0):
            transport (UpdateMCPServerRequestTransport | Unset):  Default: UpdateMCPServerRequestTransport.SSE.
            url (None | str | Unset):
     """

    server_id: str
    alias: None | str | Unset = UNSET
    allow_all_keys: bool | Unset = False
    allowed_tools: list[str] | None | Unset = UNSET
    args: list[str] | Unset = UNSET
    auth_type: None | Unset | UpdateMCPServerRequestAuthTypeType0 = UNSET
    authorization_url: None | str | Unset = UNSET
    available_on_public_internet: bool | Unset = True
    byok_api_key_help_url: None | str | Unset = UNSET
    byok_description: list[str] | Unset = UNSET
    command: None | str | Unset = UNSET
    credentials: MCPCredentials | None | Unset = UNSET
    description: None | str | Unset = UNSET
    env: UpdateMCPServerRequestEnv | Unset = UNSET
    extra_headers: list[str] | None | Unset = UNSET
    instructions: None | str | Unset = UNSET
    is_byok: bool | Unset = False
    mcp_access_groups: list[str] | Unset = UNSET
    mcp_info: None | Unset | UpdateMCPServerRequestMcpInfoType0 = UNSET
    registration_url: None | str | Unset = UNSET
    server_name: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    spec_path: None | str | Unset = UNSET
    static_headers: None | Unset | UpdateMCPServerRequestStaticHeadersType0 = UNSET
    token_url: None | str | Unset = UNSET
    tool_name_to_description: None | Unset | UpdateMCPServerRequestToolNameToDescriptionType0 = UNSET
    tool_name_to_display_name: None | Unset | UpdateMCPServerRequestToolNameToDisplayNameType0 = UNSET
    transport: UpdateMCPServerRequestTransport | Unset = UpdateMCPServerRequestTransport.SSE
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.mcp_credentials import MCPCredentials
        from ..models.update_mcp_server_request_env import UpdateMCPServerRequestEnv
        from ..models.update_mcp_server_request_mcp_info_type_0 import UpdateMCPServerRequestMcpInfoType0
        from ..models.update_mcp_server_request_static_headers_type_0 import UpdateMCPServerRequestStaticHeadersType0
        from ..models.update_mcp_server_request_tool_name_to_description_type_0 import UpdateMCPServerRequestToolNameToDescriptionType0
        from ..models.update_mcp_server_request_tool_name_to_display_name_type_0 import UpdateMCPServerRequestToolNameToDisplayNameType0
        server_id = self.server_id

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        allow_all_keys = self.allow_all_keys

        allowed_tools: list[str] | None | Unset
        if isinstance(self.allowed_tools, Unset):
            allowed_tools = UNSET
        elif isinstance(self.allowed_tools, list):
            allowed_tools = self.allowed_tools


        else:
            allowed_tools = self.allowed_tools

        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args



        auth_type: None | str | Unset
        if isinstance(self.auth_type, Unset):
            auth_type = UNSET
        elif isinstance(self.auth_type, UpdateMCPServerRequestAuthTypeType0):
            auth_type = self.auth_type.value
        else:
            auth_type = self.auth_type

        authorization_url: None | str | Unset
        if isinstance(self.authorization_url, Unset):
            authorization_url = UNSET
        else:
            authorization_url = self.authorization_url

        available_on_public_internet = self.available_on_public_internet

        byok_api_key_help_url: None | str | Unset
        if isinstance(self.byok_api_key_help_url, Unset):
            byok_api_key_help_url = UNSET
        else:
            byok_api_key_help_url = self.byok_api_key_help_url

        byok_description: list[str] | Unset = UNSET
        if not isinstance(self.byok_description, Unset):
            byok_description = self.byok_description



        command: None | str | Unset
        if isinstance(self.command, Unset):
            command = UNSET
        else:
            command = self.command

        credentials: dict[str, Any] | None | Unset
        if isinstance(self.credentials, Unset):
            credentials = UNSET
        elif isinstance(self.credentials, MCPCredentials):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        env: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

        extra_headers: list[str] | None | Unset
        if isinstance(self.extra_headers, Unset):
            extra_headers = UNSET
        elif isinstance(self.extra_headers, list):
            extra_headers = self.extra_headers


        else:
            extra_headers = self.extra_headers

        instructions: None | str | Unset
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        else:
            instructions = self.instructions

        is_byok = self.is_byok

        mcp_access_groups: list[str] | Unset = UNSET
        if not isinstance(self.mcp_access_groups, Unset):
            mcp_access_groups = self.mcp_access_groups



        mcp_info: dict[str, Any] | None | Unset
        if isinstance(self.mcp_info, Unset):
            mcp_info = UNSET
        elif isinstance(self.mcp_info, UpdateMCPServerRequestMcpInfoType0):
            mcp_info = self.mcp_info.to_dict()
        else:
            mcp_info = self.mcp_info

        registration_url: None | str | Unset
        if isinstance(self.registration_url, Unset):
            registration_url = UNSET
        else:
            registration_url = self.registration_url

        server_name: None | str | Unset
        if isinstance(self.server_name, Unset):
            server_name = UNSET
        else:
            server_name = self.server_name

        source_url: None | str | Unset
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        spec_path: None | str | Unset
        if isinstance(self.spec_path, Unset):
            spec_path = UNSET
        else:
            spec_path = self.spec_path

        static_headers: dict[str, Any] | None | Unset
        if isinstance(self.static_headers, Unset):
            static_headers = UNSET
        elif isinstance(self.static_headers, UpdateMCPServerRequestStaticHeadersType0):
            static_headers = self.static_headers.to_dict()
        else:
            static_headers = self.static_headers

        token_url: None | str | Unset
        if isinstance(self.token_url, Unset):
            token_url = UNSET
        else:
            token_url = self.token_url

        tool_name_to_description: dict[str, Any] | None | Unset
        if isinstance(self.tool_name_to_description, Unset):
            tool_name_to_description = UNSET
        elif isinstance(self.tool_name_to_description, UpdateMCPServerRequestToolNameToDescriptionType0):
            tool_name_to_description = self.tool_name_to_description.to_dict()
        else:
            tool_name_to_description = self.tool_name_to_description

        tool_name_to_display_name: dict[str, Any] | None | Unset
        if isinstance(self.tool_name_to_display_name, Unset):
            tool_name_to_display_name = UNSET
        elif isinstance(self.tool_name_to_display_name, UpdateMCPServerRequestToolNameToDisplayNameType0):
            tool_name_to_display_name = self.tool_name_to_display_name.to_dict()
        else:
            tool_name_to_display_name = self.tool_name_to_display_name

        transport: str | Unset = UNSET
        if not isinstance(self.transport, Unset):
            transport = self.transport.value


        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "server_id": server_id,
        })
        if alias is not UNSET:
            field_dict["alias"] = alias
        if allow_all_keys is not UNSET:
            field_dict["allow_all_keys"] = allow_all_keys
        if allowed_tools is not UNSET:
            field_dict["allowed_tools"] = allowed_tools
        if args is not UNSET:
            field_dict["args"] = args
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if authorization_url is not UNSET:
            field_dict["authorization_url"] = authorization_url
        if available_on_public_internet is not UNSET:
            field_dict["available_on_public_internet"] = available_on_public_internet
        if byok_api_key_help_url is not UNSET:
            field_dict["byok_api_key_help_url"] = byok_api_key_help_url
        if byok_description is not UNSET:
            field_dict["byok_description"] = byok_description
        if command is not UNSET:
            field_dict["command"] = command
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if description is not UNSET:
            field_dict["description"] = description
        if env is not UNSET:
            field_dict["env"] = env
        if extra_headers is not UNSET:
            field_dict["extra_headers"] = extra_headers
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if is_byok is not UNSET:
            field_dict["is_byok"] = is_byok
        if mcp_access_groups is not UNSET:
            field_dict["mcp_access_groups"] = mcp_access_groups
        if mcp_info is not UNSET:
            field_dict["mcp_info"] = mcp_info
        if registration_url is not UNSET:
            field_dict["registration_url"] = registration_url
        if server_name is not UNSET:
            field_dict["server_name"] = server_name
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if spec_path is not UNSET:
            field_dict["spec_path"] = spec_path
        if static_headers is not UNSET:
            field_dict["static_headers"] = static_headers
        if token_url is not UNSET:
            field_dict["token_url"] = token_url
        if tool_name_to_description is not UNSET:
            field_dict["tool_name_to_description"] = tool_name_to_description
        if tool_name_to_display_name is not UNSET:
            field_dict["tool_name_to_display_name"] = tool_name_to_display_name
        if transport is not UNSET:
            field_dict["transport"] = transport
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_credentials import MCPCredentials
        from ..models.update_mcp_server_request_env import UpdateMCPServerRequestEnv
        from ..models.update_mcp_server_request_mcp_info_type_0 import UpdateMCPServerRequestMcpInfoType0
        from ..models.update_mcp_server_request_static_headers_type_0 import UpdateMCPServerRequestStaticHeadersType0
        from ..models.update_mcp_server_request_tool_name_to_description_type_0 import UpdateMCPServerRequestToolNameToDescriptionType0
        from ..models.update_mcp_server_request_tool_name_to_display_name_type_0 import UpdateMCPServerRequestToolNameToDisplayNameType0
        d = dict(src_dict)
        server_id = d.pop("server_id")

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))


        allow_all_keys = d.pop("allow_all_keys", UNSET)

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


        args = cast(list[str], d.pop("args", UNSET))


        def _parse_auth_type(data: object) -> None | Unset | UpdateMCPServerRequestAuthTypeType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_type_type_0 = UpdateMCPServerRequestAuthTypeType0(data)



                return auth_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateMCPServerRequestAuthTypeType0, data)

        auth_type = _parse_auth_type(d.pop("auth_type", UNSET))


        def _parse_authorization_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authorization_url = _parse_authorization_url(d.pop("authorization_url", UNSET))


        available_on_public_internet = d.pop("available_on_public_internet", UNSET)

        def _parse_byok_api_key_help_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        byok_api_key_help_url = _parse_byok_api_key_help_url(d.pop("byok_api_key_help_url", UNSET))


        byok_description = cast(list[str], d.pop("byok_description", UNSET))


        def _parse_command(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        command = _parse_command(d.pop("command", UNSET))


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


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        _env = d.pop("env", UNSET)
        env: UpdateMCPServerRequestEnv | Unset
        if isinstance(_env,  Unset):
            env = UNSET
        else:
            env = UpdateMCPServerRequestEnv.from_dict(_env)




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


        def _parse_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))


        is_byok = d.pop("is_byok", UNSET)

        mcp_access_groups = cast(list[str], d.pop("mcp_access_groups", UNSET))


        def _parse_mcp_info(data: object) -> None | Unset | UpdateMCPServerRequestMcpInfoType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mcp_info_type_0 = UpdateMCPServerRequestMcpInfoType0.from_dict(data)



                return mcp_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateMCPServerRequestMcpInfoType0, data)

        mcp_info = _parse_mcp_info(d.pop("mcp_info", UNSET))


        def _parse_registration_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_url = _parse_registration_url(d.pop("registration_url", UNSET))


        def _parse_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_name = _parse_server_name(d.pop("server_name", UNSET))


        def _parse_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_url = _parse_source_url(d.pop("source_url", UNSET))


        def _parse_spec_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spec_path = _parse_spec_path(d.pop("spec_path", UNSET))


        def _parse_static_headers(data: object) -> None | Unset | UpdateMCPServerRequestStaticHeadersType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                static_headers_type_0 = UpdateMCPServerRequestStaticHeadersType0.from_dict(data)



                return static_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateMCPServerRequestStaticHeadersType0, data)

        static_headers = _parse_static_headers(d.pop("static_headers", UNSET))


        def _parse_token_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token_url = _parse_token_url(d.pop("token_url", UNSET))


        def _parse_tool_name_to_description(data: object) -> None | Unset | UpdateMCPServerRequestToolNameToDescriptionType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tool_name_to_description_type_0 = UpdateMCPServerRequestToolNameToDescriptionType0.from_dict(data)



                return tool_name_to_description_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateMCPServerRequestToolNameToDescriptionType0, data)

        tool_name_to_description = _parse_tool_name_to_description(d.pop("tool_name_to_description", UNSET))


        def _parse_tool_name_to_display_name(data: object) -> None | Unset | UpdateMCPServerRequestToolNameToDisplayNameType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tool_name_to_display_name_type_0 = UpdateMCPServerRequestToolNameToDisplayNameType0.from_dict(data)



                return tool_name_to_display_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateMCPServerRequestToolNameToDisplayNameType0, data)

        tool_name_to_display_name = _parse_tool_name_to_display_name(d.pop("tool_name_to_display_name", UNSET))


        _transport = d.pop("transport", UNSET)
        transport: UpdateMCPServerRequestTransport | Unset
        if isinstance(_transport,  Unset):
            transport = UNSET
        else:
            transport = UpdateMCPServerRequestTransport(_transport)




        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        update_mcp_server_request = cls(
            server_id=server_id,
            alias=alias,
            allow_all_keys=allow_all_keys,
            allowed_tools=allowed_tools,
            args=args,
            auth_type=auth_type,
            authorization_url=authorization_url,
            available_on_public_internet=available_on_public_internet,
            byok_api_key_help_url=byok_api_key_help_url,
            byok_description=byok_description,
            command=command,
            credentials=credentials,
            description=description,
            env=env,
            extra_headers=extra_headers,
            instructions=instructions,
            is_byok=is_byok,
            mcp_access_groups=mcp_access_groups,
            mcp_info=mcp_info,
            registration_url=registration_url,
            server_name=server_name,
            source_url=source_url,
            spec_path=spec_path,
            static_headers=static_headers,
            token_url=token_url,
            tool_name_to_description=tool_name_to_description,
            tool_name_to_display_name=tool_name_to_display_name,
            transport=transport,
            url=url,
        )


        update_mcp_server_request.additional_properties = d
        return update_mcp_server_request

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
