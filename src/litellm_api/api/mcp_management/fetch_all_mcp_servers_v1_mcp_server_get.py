from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llmmcp_server_table import LiteLLMMCPServerTable
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    team_id: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_team_id: None | str | Unset
    if isinstance(team_id, Unset):
        json_team_id = UNSET
    else:
        json_team_id = team_id
    params["team_id"] = json_team_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/mcp/server",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | list[LiteLLMMCPServerTable] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = LiteLLMMCPServerTable.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | list[LiteLLMMCPServerTable]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    team_id: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | list[LiteLLMMCPServerTable]]:
    """ Fetch All Mcp Servers

     Returns the mcp server list with associated teams

    Args:
        team_id (None | str | Unset): Filter MCP servers by team scope. When provided, returns
            only servers the team has access to plus globally available (allow_all_keys) servers. Used
            by the Create Key UI to show team-scoped MCP servers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LiteLLMMCPServerTable]]
     """


    kwargs = _get_kwargs(
        team_id=team_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    team_id: None | str | Unset = UNSET,

) -> HTTPValidationError | list[LiteLLMMCPServerTable] | None:
    """ Fetch All Mcp Servers

     Returns the mcp server list with associated teams

    Args:
        team_id (None | str | Unset): Filter MCP servers by team scope. When provided, returns
            only servers the team has access to plus globally available (allow_all_keys) servers. Used
            by the Create Key UI to show team-scoped MCP servers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LiteLLMMCPServerTable]
     """


    return sync_detailed(
        client=client,
team_id=team_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    team_id: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | list[LiteLLMMCPServerTable]]:
    """ Fetch All Mcp Servers

     Returns the mcp server list with associated teams

    Args:
        team_id (None | str | Unset): Filter MCP servers by team scope. When provided, returns
            only servers the team has access to plus globally available (allow_all_keys) servers. Used
            by the Create Key UI to show team-scoped MCP servers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LiteLLMMCPServerTable]]
     """


    kwargs = _get_kwargs(
        team_id=team_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    team_id: None | str | Unset = UNSET,

) -> HTTPValidationError | list[LiteLLMMCPServerTable] | None:
    """ Fetch All Mcp Servers

     Returns the mcp server list with associated teams

    Args:
        team_id (None | str | Unset): Filter MCP servers by team scope. When provided, returns
            only servers the team has access to plus globally available (allow_all_keys) servers. Used
            by the Create Key UI to show team-scoped MCP servers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LiteLLMMCPServerTable]
     """


    return (await asyncio_detailed(
        client=client,
team_id=team_id,

    )).parsed
