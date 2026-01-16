from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.lite_llmmcp_server_table_auth_type_type_0 import LiteLLMMCPServerTableAuthTypeType0
from ..models.lite_llmmcp_server_table_status_type_0 import LiteLLMMCPServerTableStatusType0
from ..models.lite_llmmcp_server_table_transport import LiteLLMMCPServerTableTransport
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.lite_llmmcp_server_table_env import LiteLLMMCPServerTableEnv
  from ..models.lite_llmmcp_server_table_mcp_info_type_0 import LiteLLMMCPServerTableMcpInfoType0
  from ..models.lite_llmmcp_server_table_static_headers_type_0 import LiteLLMMCPServerTableStaticHeadersType0
  from ..models.lite_llmmcp_server_table_teams_item import LiteLLMMCPServerTableTeamsItem
  from ..models.mcp_credentials import MCPCredentials





T = TypeVar("T", bound="LiteLLMMCPServerTable")



@_attrs_define
class LiteLLMMCPServerTable:
    """ Represents a LiteLLM_MCPServerTable record

        Attributes:
            server_id (str):
            transport (LiteLLMMCPServerTableTransport):
            server_name (None | str | Unset):
            alias (None | str | Unset):
            description (None | str | Unset):
            url (None | str | Unset):
            auth_type (LiteLLMMCPServerTableAuthTypeType0 | None | Unset):
            credentials (MCPCredentials | None | Unset):
            created_at (datetime.datetime | None | Unset):
            created_by (None | str | Unset):
            updated_at (datetime.datetime | None | Unset):
            updated_by (None | str | Unset):
            teams (list[LiteLLMMCPServerTableTeamsItem] | Unset):
            mcp_access_groups (list[str] | Unset):
            allowed_tools (list[str] | Unset):
            extra_headers (list[str] | Unset):
            mcp_info (LiteLLMMCPServerTableMcpInfoType0 | None | Unset):
            static_headers (LiteLLMMCPServerTableStaticHeadersType0 | None | Unset):
            status (LiteLLMMCPServerTableStatusType0 | None | Unset): Health status: 'healthy', 'unhealthy', 'unknown'
                Default: LiteLLMMCPServerTableStatusType0.UNKNOWN.
            last_health_check (datetime.datetime | None | Unset):
            health_check_error (None | str | Unset):
            command (None | str | Unset):
            args (list[str] | Unset):
            env (LiteLLMMCPServerTableEnv | Unset):
            authorization_url (None | str | Unset):
            token_url (None | str | Unset):
            registration_url (None | str | Unset):
            allow_all_keys (bool | Unset):  Default: False.
     """

    server_id: str
    transport: LiteLLMMCPServerTableTransport
    server_name: None | str | Unset = UNSET
    alias: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    auth_type: LiteLLMMCPServerTableAuthTypeType0 | None | Unset = UNSET
    credentials: MCPCredentials | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    teams: list[LiteLLMMCPServerTableTeamsItem] | Unset = UNSET
    mcp_access_groups: list[str] | Unset = UNSET
    allowed_tools: list[str] | Unset = UNSET
    extra_headers: list[str] | Unset = UNSET
    mcp_info: LiteLLMMCPServerTableMcpInfoType0 | None | Unset = UNSET
    static_headers: LiteLLMMCPServerTableStaticHeadersType0 | None | Unset = UNSET
    status: LiteLLMMCPServerTableStatusType0 | None | Unset = LiteLLMMCPServerTableStatusType0.UNKNOWN
    last_health_check: datetime.datetime | None | Unset = UNSET
    health_check_error: None | str | Unset = UNSET
    command: None | str | Unset = UNSET
    args: list[str] | Unset = UNSET
    env: LiteLLMMCPServerTableEnv | Unset = UNSET
    authorization_url: None | str | Unset = UNSET
    token_url: None | str | Unset = UNSET
    registration_url: None | str | Unset = UNSET
    allow_all_keys: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llmmcp_server_table_static_headers_type_0 import LiteLLMMCPServerTableStaticHeadersType0
        from ..models.lite_llmmcp_server_table_mcp_info_type_0 import LiteLLMMCPServerTableMcpInfoType0
        from ..models.mcp_credentials import MCPCredentials
        from ..models.lite_llmmcp_server_table_teams_item import LiteLLMMCPServerTableTeamsItem
        from ..models.lite_llmmcp_server_table_env import LiteLLMMCPServerTableEnv
        server_id = self.server_id

        transport = self.transport.value

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

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        auth_type: None | str | Unset
        if isinstance(self.auth_type, Unset):
            auth_type = UNSET
        elif isinstance(self.auth_type, LiteLLMMCPServerTableAuthTypeType0):
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

        teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)



        mcp_access_groups: list[str] | Unset = UNSET
        if not isinstance(self.mcp_access_groups, Unset):
            mcp_access_groups = self.mcp_access_groups



        allowed_tools: list[str] | Unset = UNSET
        if not isinstance(self.allowed_tools, Unset):
            allowed_tools = self.allowed_tools



        extra_headers: list[str] | Unset = UNSET
        if not isinstance(self.extra_headers, Unset):
            extra_headers = self.extra_headers



        mcp_info: dict[str, Any] | None | Unset
        if isinstance(self.mcp_info, Unset):
            mcp_info = UNSET
        elif isinstance(self.mcp_info, LiteLLMMCPServerTableMcpInfoType0):
            mcp_info = self.mcp_info.to_dict()
        else:
            mcp_info = self.mcp_info

        static_headers: dict[str, Any] | None | Unset
        if isinstance(self.static_headers, Unset):
            static_headers = UNSET
        elif isinstance(self.static_headers, LiteLLMMCPServerTableStaticHeadersType0):
            static_headers = self.static_headers.to_dict()
        else:
            static_headers = self.static_headers

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, LiteLLMMCPServerTableStatusType0):
            status = self.status.value
        else:
            status = self.status

        last_health_check: None | str | Unset
        if isinstance(self.last_health_check, Unset):
            last_health_check = UNSET
        elif isinstance(self.last_health_check, datetime.datetime):
            last_health_check = self.last_health_check.isoformat()
        else:
            last_health_check = self.last_health_check

        health_check_error: None | str | Unset
        if isinstance(self.health_check_error, Unset):
            health_check_error = UNSET
        else:
            health_check_error = self.health_check_error

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
            "server_id": server_id,
            "transport": transport,
        })
        if server_name is not UNSET:
            field_dict["server_name"] = server_name
        if alias is not UNSET:
            field_dict["alias"] = alias
        if description is not UNSET:
            field_dict["description"] = description
        if url is not UNSET:
            field_dict["url"] = url
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if teams is not UNSET:
            field_dict["teams"] = teams
        if mcp_access_groups is not UNSET:
            field_dict["mcp_access_groups"] = mcp_access_groups
        if allowed_tools is not UNSET:
            field_dict["allowed_tools"] = allowed_tools
        if extra_headers is not UNSET:
            field_dict["extra_headers"] = extra_headers
        if mcp_info is not UNSET:
            field_dict["mcp_info"] = mcp_info
        if static_headers is not UNSET:
            field_dict["static_headers"] = static_headers
        if status is not UNSET:
            field_dict["status"] = status
        if last_health_check is not UNSET:
            field_dict["last_health_check"] = last_health_check
        if health_check_error is not UNSET:
            field_dict["health_check_error"] = health_check_error
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
        from ..models.lite_llmmcp_server_table_env import LiteLLMMCPServerTableEnv
        from ..models.lite_llmmcp_server_table_mcp_info_type_0 import LiteLLMMCPServerTableMcpInfoType0
        from ..models.lite_llmmcp_server_table_static_headers_type_0 import LiteLLMMCPServerTableStaticHeadersType0
        from ..models.lite_llmmcp_server_table_teams_item import LiteLLMMCPServerTableTeamsItem
        from ..models.mcp_credentials import MCPCredentials
        d = dict(src_dict)
        server_id = d.pop("server_id")

        transport = LiteLLMMCPServerTableTransport(d.pop("transport"))




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


        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        def _parse_auth_type(data: object) -> LiteLLMMCPServerTableAuthTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_type_type_0 = LiteLLMMCPServerTableAuthTypeType0(data)



                return auth_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMMCPServerTableAuthTypeType0 | None | Unset, data)

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


        _teams = d.pop("teams", UNSET)
        teams: list[LiteLLMMCPServerTableTeamsItem] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = LiteLLMMCPServerTableTeamsItem.from_dict(teams_item_data)



                teams.append(teams_item)


        mcp_access_groups = cast(list[str], d.pop("mcp_access_groups", UNSET))


        allowed_tools = cast(list[str], d.pop("allowed_tools", UNSET))


        extra_headers = cast(list[str], d.pop("extra_headers", UNSET))


        def _parse_mcp_info(data: object) -> LiteLLMMCPServerTableMcpInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mcp_info_type_0 = LiteLLMMCPServerTableMcpInfoType0.from_dict(data)



                return mcp_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMMCPServerTableMcpInfoType0 | None | Unset, data)

        mcp_info = _parse_mcp_info(d.pop("mcp_info", UNSET))


        def _parse_static_headers(data: object) -> LiteLLMMCPServerTableStaticHeadersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                static_headers_type_0 = LiteLLMMCPServerTableStaticHeadersType0.from_dict(data)



                return static_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMMCPServerTableStaticHeadersType0 | None | Unset, data)

        static_headers = _parse_static_headers(d.pop("static_headers", UNSET))


        def _parse_status(data: object) -> LiteLLMMCPServerTableStatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = LiteLLMMCPServerTableStatusType0(data)



                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMMCPServerTableStatusType0 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_last_health_check(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_health_check_type_0 = isoparse(data)



                return last_health_check_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_health_check = _parse_last_health_check(d.pop("last_health_check", UNSET))


        def _parse_health_check_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        health_check_error = _parse_health_check_error(d.pop("health_check_error", UNSET))


        def _parse_command(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        command = _parse_command(d.pop("command", UNSET))


        args = cast(list[str], d.pop("args", UNSET))


        _env = d.pop("env", UNSET)
        env: LiteLLMMCPServerTableEnv | Unset
        if isinstance(_env,  Unset):
            env = UNSET
        else:
            env = LiteLLMMCPServerTableEnv.from_dict(_env)




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

        lite_llmmcp_server_table = cls(
            server_id=server_id,
            transport=transport,
            server_name=server_name,
            alias=alias,
            description=description,
            url=url,
            auth_type=auth_type,
            credentials=credentials,
            created_at=created_at,
            created_by=created_by,
            updated_at=updated_at,
            updated_by=updated_by,
            teams=teams,
            mcp_access_groups=mcp_access_groups,
            allowed_tools=allowed_tools,
            extra_headers=extra_headers,
            mcp_info=mcp_info,
            static_headers=static_headers,
            status=status,
            last_health_check=last_health_check,
            health_check_error=health_check_error,
            command=command,
            args=args,
            env=env,
            authorization_url=authorization_url,
            token_url=token_url,
            registration_url=registration_url,
            allow_all_keys=allow_all_keys,
        )


        lite_llmmcp_server_table.additional_properties = d
        return lite_llmmcp_server_table

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
