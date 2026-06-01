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
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.lite_llmmcp_server_table_env import LiteLLMMCPServerTableEnv
  from ..models.lite_llmmcp_server_table_mcp_info_type_0 import LiteLLMMCPServerTableMcpInfoType0
  from ..models.lite_llmmcp_server_table_static_headers_type_0 import LiteLLMMCPServerTableStaticHeadersType0
  from ..models.lite_llmmcp_server_table_teams_item import LiteLLMMCPServerTableTeamsItem
  from ..models.lite_llmmcp_server_table_tool_name_to_description_type_0 import LiteLLMMCPServerTableToolNameToDescriptionType0
  from ..models.lite_llmmcp_server_table_tool_name_to_display_name_type_0 import LiteLLMMCPServerTableToolNameToDisplayNameType0
  from ..models.mcp_credentials import MCPCredentials





T = TypeVar("T", bound="LiteLLMMCPServerTable")



@_attrs_define
class LiteLLMMCPServerTable:
    """ Represents a LiteLLM_MCPServerTable record

        Attributes:
            server_id (str):
            transport (LiteLLMMCPServerTableTransport):
            alias (None | str | Unset):
            allow_all_keys (bool | Unset):  Default: False.
            allowed_tools (list[str] | Unset):
            approval_status (None | str | Unset): Approval status: 'pending_review', 'active', 'rejected' Default: 'active'.
            args (list[str] | Unset):
            auth_type (LiteLLMMCPServerTableAuthTypeType0 | None | Unset):
            authorization_url (None | str | Unset):
            available_on_public_internet (bool | Unset):  Default: True.
            byok_api_key_help_url (None | str | Unset):
            byok_description (list[str] | Unset):
            command (None | str | Unset):
            created_at (datetime.datetime | None | Unset):
            created_by (None | str | Unset):
            credentials (MCPCredentials | None | Unset):
            description (None | str | Unset):
            env (LiteLLMMCPServerTableEnv | Unset):
            extra_headers (list[str] | Unset):
            has_user_credential (bool | None | Unset):
            health_check_error (None | str | Unset):
            instructions (None | str | Unset):
            is_byok (bool | Unset):  Default: False.
            last_health_check (datetime.datetime | None | Unset):
            mcp_access_groups (list[str] | Unset):
            mcp_info (LiteLLMMCPServerTableMcpInfoType0 | None | Unset):
            registration_url (None | str | Unset):
            review_notes (None | str | Unset):
            reviewed_at (datetime.datetime | None | Unset):
            server_name (None | str | Unset):
            source_url (None | str | Unset):
            spec_path (None | str | Unset):
            static_headers (LiteLLMMCPServerTableStaticHeadersType0 | None | Unset):
            status (LiteLLMMCPServerTableStatusType0 | None | Unset): Health status: 'healthy', 'unhealthy', 'unknown'
                Default: LiteLLMMCPServerTableStatusType0.UNKNOWN.
            submitted_at (datetime.datetime | None | Unset):
            submitted_by (None | str | Unset):
            teams (list[LiteLLMMCPServerTableTeamsItem] | Unset):
            token_url (None | str | Unset):
            tool_name_to_description (LiteLLMMCPServerTableToolNameToDescriptionType0 | None | Unset):
            tool_name_to_display_name (LiteLLMMCPServerTableToolNameToDisplayNameType0 | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            updated_by (None | str | Unset):
            url (None | str | Unset):
     """

    server_id: str
    transport: LiteLLMMCPServerTableTransport
    alias: None | str | Unset = UNSET
    allow_all_keys: bool | Unset = False
    allowed_tools: list[str] | Unset = UNSET
    approval_status: None | str | Unset = 'active'
    args: list[str] | Unset = UNSET
    auth_type: LiteLLMMCPServerTableAuthTypeType0 | None | Unset = UNSET
    authorization_url: None | str | Unset = UNSET
    available_on_public_internet: bool | Unset = True
    byok_api_key_help_url: None | str | Unset = UNSET
    byok_description: list[str] | Unset = UNSET
    command: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    credentials: MCPCredentials | None | Unset = UNSET
    description: None | str | Unset = UNSET
    env: LiteLLMMCPServerTableEnv | Unset = UNSET
    extra_headers: list[str] | Unset = UNSET
    has_user_credential: bool | None | Unset = UNSET
    health_check_error: None | str | Unset = UNSET
    instructions: None | str | Unset = UNSET
    is_byok: bool | Unset = False
    last_health_check: datetime.datetime | None | Unset = UNSET
    mcp_access_groups: list[str] | Unset = UNSET
    mcp_info: LiteLLMMCPServerTableMcpInfoType0 | None | Unset = UNSET
    registration_url: None | str | Unset = UNSET
    review_notes: None | str | Unset = UNSET
    reviewed_at: datetime.datetime | None | Unset = UNSET
    server_name: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    spec_path: None | str | Unset = UNSET
    static_headers: LiteLLMMCPServerTableStaticHeadersType0 | None | Unset = UNSET
    status: LiteLLMMCPServerTableStatusType0 | None | Unset = LiteLLMMCPServerTableStatusType0.UNKNOWN
    submitted_at: datetime.datetime | None | Unset = UNSET
    submitted_by: None | str | Unset = UNSET
    teams: list[LiteLLMMCPServerTableTeamsItem] | Unset = UNSET
    token_url: None | str | Unset = UNSET
    tool_name_to_description: LiteLLMMCPServerTableToolNameToDescriptionType0 | None | Unset = UNSET
    tool_name_to_display_name: LiteLLMMCPServerTableToolNameToDisplayNameType0 | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lite_llmmcp_server_table_env import LiteLLMMCPServerTableEnv
        from ..models.lite_llmmcp_server_table_mcp_info_type_0 import LiteLLMMCPServerTableMcpInfoType0
        from ..models.lite_llmmcp_server_table_static_headers_type_0 import LiteLLMMCPServerTableStaticHeadersType0
        from ..models.lite_llmmcp_server_table_teams_item import LiteLLMMCPServerTableTeamsItem
        from ..models.lite_llmmcp_server_table_tool_name_to_description_type_0 import LiteLLMMCPServerTableToolNameToDescriptionType0
        from ..models.lite_llmmcp_server_table_tool_name_to_display_name_type_0 import LiteLLMMCPServerTableToolNameToDisplayNameType0
        from ..models.mcp_credentials import MCPCredentials
        server_id = self.server_id

        transport = self.transport.value

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        allow_all_keys = self.allow_all_keys

        allowed_tools: list[str] | Unset = UNSET
        if not isinstance(self.allowed_tools, Unset):
            allowed_tools = self.allowed_tools



        approval_status: None | str | Unset
        if isinstance(self.approval_status, Unset):
            approval_status = UNSET
        else:
            approval_status = self.approval_status

        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args



        auth_type: None | str | Unset
        if isinstance(self.auth_type, Unset):
            auth_type = UNSET
        elif isinstance(self.auth_type, LiteLLMMCPServerTableAuthTypeType0):
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

        extra_headers: list[str] | Unset = UNSET
        if not isinstance(self.extra_headers, Unset):
            extra_headers = self.extra_headers



        has_user_credential: bool | None | Unset
        if isinstance(self.has_user_credential, Unset):
            has_user_credential = UNSET
        else:
            has_user_credential = self.has_user_credential

        health_check_error: None | str | Unset
        if isinstance(self.health_check_error, Unset):
            health_check_error = UNSET
        else:
            health_check_error = self.health_check_error

        instructions: None | str | Unset
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        else:
            instructions = self.instructions

        is_byok = self.is_byok

        last_health_check: None | str | Unset
        if isinstance(self.last_health_check, Unset):
            last_health_check = UNSET
        elif isinstance(self.last_health_check, datetime.datetime):
            last_health_check = self.last_health_check.isoformat()
        else:
            last_health_check = self.last_health_check

        mcp_access_groups: list[str] | Unset = UNSET
        if not isinstance(self.mcp_access_groups, Unset):
            mcp_access_groups = self.mcp_access_groups



        mcp_info: dict[str, Any] | None | Unset
        if isinstance(self.mcp_info, Unset):
            mcp_info = UNSET
        elif isinstance(self.mcp_info, LiteLLMMCPServerTableMcpInfoType0):
            mcp_info = self.mcp_info.to_dict()
        else:
            mcp_info = self.mcp_info

        registration_url: None | str | Unset
        if isinstance(self.registration_url, Unset):
            registration_url = UNSET
        else:
            registration_url = self.registration_url

        review_notes: None | str | Unset
        if isinstance(self.review_notes, Unset):
            review_notes = UNSET
        else:
            review_notes = self.review_notes

        reviewed_at: None | str | Unset
        if isinstance(self.reviewed_at, Unset):
            reviewed_at = UNSET
        elif isinstance(self.reviewed_at, datetime.datetime):
            reviewed_at = self.reviewed_at.isoformat()
        else:
            reviewed_at = self.reviewed_at

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

        submitted_at: None | str | Unset
        if isinstance(self.submitted_at, Unset):
            submitted_at = UNSET
        elif isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at

        submitted_by: None | str | Unset
        if isinstance(self.submitted_by, Unset):
            submitted_by = UNSET
        else:
            submitted_by = self.submitted_by

        teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)



        token_url: None | str | Unset
        if isinstance(self.token_url, Unset):
            token_url = UNSET
        else:
            token_url = self.token_url

        tool_name_to_description: dict[str, Any] | None | Unset
        if isinstance(self.tool_name_to_description, Unset):
            tool_name_to_description = UNSET
        elif isinstance(self.tool_name_to_description, LiteLLMMCPServerTableToolNameToDescriptionType0):
            tool_name_to_description = self.tool_name_to_description.to_dict()
        else:
            tool_name_to_description = self.tool_name_to_description

        tool_name_to_display_name: dict[str, Any] | None | Unset
        if isinstance(self.tool_name_to_display_name, Unset):
            tool_name_to_display_name = UNSET
        elif isinstance(self.tool_name_to_display_name, LiteLLMMCPServerTableToolNameToDisplayNameType0):
            tool_name_to_display_name = self.tool_name_to_display_name.to_dict()
        else:
            tool_name_to_display_name = self.tool_name_to_display_name

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

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "server_id": server_id,
            "transport": transport,
        })
        if alias is not UNSET:
            field_dict["alias"] = alias
        if allow_all_keys is not UNSET:
            field_dict["allow_all_keys"] = allow_all_keys
        if allowed_tools is not UNSET:
            field_dict["allowed_tools"] = allowed_tools
        if approval_status is not UNSET:
            field_dict["approval_status"] = approval_status
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
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if description is not UNSET:
            field_dict["description"] = description
        if env is not UNSET:
            field_dict["env"] = env
        if extra_headers is not UNSET:
            field_dict["extra_headers"] = extra_headers
        if has_user_credential is not UNSET:
            field_dict["has_user_credential"] = has_user_credential
        if health_check_error is not UNSET:
            field_dict["health_check_error"] = health_check_error
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if is_byok is not UNSET:
            field_dict["is_byok"] = is_byok
        if last_health_check is not UNSET:
            field_dict["last_health_check"] = last_health_check
        if mcp_access_groups is not UNSET:
            field_dict["mcp_access_groups"] = mcp_access_groups
        if mcp_info is not UNSET:
            field_dict["mcp_info"] = mcp_info
        if registration_url is not UNSET:
            field_dict["registration_url"] = registration_url
        if review_notes is not UNSET:
            field_dict["review_notes"] = review_notes
        if reviewed_at is not UNSET:
            field_dict["reviewed_at"] = reviewed_at
        if server_name is not UNSET:
            field_dict["server_name"] = server_name
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if spec_path is not UNSET:
            field_dict["spec_path"] = spec_path
        if static_headers is not UNSET:
            field_dict["static_headers"] = static_headers
        if status is not UNSET:
            field_dict["status"] = status
        if submitted_at is not UNSET:
            field_dict["submitted_at"] = submitted_at
        if submitted_by is not UNSET:
            field_dict["submitted_by"] = submitted_by
        if teams is not UNSET:
            field_dict["teams"] = teams
        if token_url is not UNSET:
            field_dict["token_url"] = token_url
        if tool_name_to_description is not UNSET:
            field_dict["tool_name_to_description"] = tool_name_to_description
        if tool_name_to_display_name is not UNSET:
            field_dict["tool_name_to_display_name"] = tool_name_to_display_name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lite_llmmcp_server_table_env import LiteLLMMCPServerTableEnv
        from ..models.lite_llmmcp_server_table_mcp_info_type_0 import LiteLLMMCPServerTableMcpInfoType0
        from ..models.lite_llmmcp_server_table_static_headers_type_0 import LiteLLMMCPServerTableStaticHeadersType0
        from ..models.lite_llmmcp_server_table_teams_item import LiteLLMMCPServerTableTeamsItem
        from ..models.lite_llmmcp_server_table_tool_name_to_description_type_0 import LiteLLMMCPServerTableToolNameToDescriptionType0
        from ..models.lite_llmmcp_server_table_tool_name_to_display_name_type_0 import LiteLLMMCPServerTableToolNameToDisplayNameType0
        from ..models.mcp_credentials import MCPCredentials
        d = dict(src_dict)
        server_id = d.pop("server_id")

        transport = LiteLLMMCPServerTableTransport(d.pop("transport"))




        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))


        allow_all_keys = d.pop("allow_all_keys", UNSET)

        allowed_tools = cast(list[str], d.pop("allowed_tools", UNSET))


        def _parse_approval_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approval_status = _parse_approval_status(d.pop("approval_status", UNSET))


        args = cast(list[str], d.pop("args", UNSET))


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


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)



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
        env: LiteLLMMCPServerTableEnv | Unset
        if isinstance(_env,  Unset):
            env = UNSET
        else:
            env = LiteLLMMCPServerTableEnv.from_dict(_env)




        extra_headers = cast(list[str], d.pop("extra_headers", UNSET))


        def _parse_has_user_credential(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_user_credential = _parse_has_user_credential(d.pop("has_user_credential", UNSET))


        def _parse_health_check_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        health_check_error = _parse_health_check_error(d.pop("health_check_error", UNSET))


        def _parse_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))


        is_byok = d.pop("is_byok", UNSET)

        def _parse_last_health_check(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_health_check_type_0 = datetime.datetime.fromisoformat(data)



                return last_health_check_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_health_check = _parse_last_health_check(d.pop("last_health_check", UNSET))


        mcp_access_groups = cast(list[str], d.pop("mcp_access_groups", UNSET))


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


        def _parse_registration_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_url = _parse_registration_url(d.pop("registration_url", UNSET))


        def _parse_review_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        review_notes = _parse_review_notes(d.pop("review_notes", UNSET))


        def _parse_reviewed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewed_at_type_0 = datetime.datetime.fromisoformat(data)



                return reviewed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reviewed_at = _parse_reviewed_at(d.pop("reviewed_at", UNSET))


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


        def _parse_submitted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = datetime.datetime.fromisoformat(data)



                return submitted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        submitted_at = _parse_submitted_at(d.pop("submitted_at", UNSET))


        def _parse_submitted_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        submitted_by = _parse_submitted_by(d.pop("submitted_by", UNSET))


        _teams = d.pop("teams", UNSET)
        teams: list[LiteLLMMCPServerTableTeamsItem] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = LiteLLMMCPServerTableTeamsItem.from_dict(teams_item_data)



                teams.append(teams_item)


        def _parse_token_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token_url = _parse_token_url(d.pop("token_url", UNSET))


        def _parse_tool_name_to_description(data: object) -> LiteLLMMCPServerTableToolNameToDescriptionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tool_name_to_description_type_0 = LiteLLMMCPServerTableToolNameToDescriptionType0.from_dict(data)



                return tool_name_to_description_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMMCPServerTableToolNameToDescriptionType0 | None | Unset, data)

        tool_name_to_description = _parse_tool_name_to_description(d.pop("tool_name_to_description", UNSET))


        def _parse_tool_name_to_display_name(data: object) -> LiteLLMMCPServerTableToolNameToDisplayNameType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tool_name_to_display_name_type_0 = LiteLLMMCPServerTableToolNameToDisplayNameType0.from_dict(data)



                return tool_name_to_display_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMMCPServerTableToolNameToDisplayNameType0 | None | Unset, data)

        tool_name_to_display_name = _parse_tool_name_to_display_name(d.pop("tool_name_to_display_name", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)



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


        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        lite_llmmcp_server_table = cls(
            server_id=server_id,
            transport=transport,
            alias=alias,
            allow_all_keys=allow_all_keys,
            allowed_tools=allowed_tools,
            approval_status=approval_status,
            args=args,
            auth_type=auth_type,
            authorization_url=authorization_url,
            available_on_public_internet=available_on_public_internet,
            byok_api_key_help_url=byok_api_key_help_url,
            byok_description=byok_description,
            command=command,
            created_at=created_at,
            created_by=created_by,
            credentials=credentials,
            description=description,
            env=env,
            extra_headers=extra_headers,
            has_user_credential=has_user_credential,
            health_check_error=health_check_error,
            instructions=instructions,
            is_byok=is_byok,
            last_health_check=last_health_check,
            mcp_access_groups=mcp_access_groups,
            mcp_info=mcp_info,
            registration_url=registration_url,
            review_notes=review_notes,
            reviewed_at=reviewed_at,
            server_name=server_name,
            source_url=source_url,
            spec_path=spec_path,
            static_headers=static_headers,
            status=status,
            submitted_at=submitted_at,
            submitted_by=submitted_by,
            teams=teams,
            token_url=token_url,
            tool_name_to_description=tool_name_to_description,
            tool_name_to_display_name=tool_name_to_display_name,
            updated_at=updated_at,
            updated_by=updated_by,
            url=url,
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
