from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    server_ids: list[str] | None | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_server_ids: list[str] | None | Unset
    if isinstance(server_ids, Unset):
        json_server_ids = UNSET
    elif isinstance(server_ids, list):
        json_server_ids = server_ids


    else:
        json_server_ids = server_ids
    params["server_ids"] = json_server_ids


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/mcp/server/health",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    server_ids: list[str] | None | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Health Check Servers

     Health check for MCP servers

    Args:
        server_ids (list[str] | None | Unset): Server IDs to check. If not provided, checks all
            accessible servers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        server_ids=server_ids,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    server_ids: list[str] | None | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Health Check Servers

     Health check for MCP servers

    Args:
        server_ids (list[str] | None | Unset): Server IDs to check. If not provided, checks all
            accessible servers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
server_ids=server_ids,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    server_ids: list[str] | None | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Health Check Servers

     Health check for MCP servers

    Args:
        server_ids (list[str] | None | Unset): Server IDs to check. If not provided, checks all
            accessible servers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        server_ids=server_ids,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    server_ids: list[str] | None | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Health Check Servers

     Health check for MCP servers

    Args:
        server_ids (list[str] | None | Unset): Server IDs to check. If not provided, checks all
            accessible servers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
server_ids=server_ids,

    )).parsed
