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
    mcp_server_name: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_mcp_server_name: None | str | Unset
    if isinstance(mcp_server_name, Unset):
        json_mcp_server_name = UNSET
    else:
        json_mcp_server_name = mcp_server_name
    params["mcp_server_name"] = json_mcp_server_name


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/.well-known/oauth-authorization-server",
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
    client: AuthenticatedClient | Client,
    mcp_server_name: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Oauth Authorization Server Mcp

     OAuth authorization server discovery endpoint.

    Supports both legacy pattern (/{server_name}) and root endpoint.

    Args:
        mcp_server_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        mcp_server_name=mcp_server_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    mcp_server_name: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Oauth Authorization Server Mcp

     OAuth authorization server discovery endpoint.

    Supports both legacy pattern (/{server_name}) and root endpoint.

    Args:
        mcp_server_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
mcp_server_name=mcp_server_name,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    mcp_server_name: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Oauth Authorization Server Mcp

     OAuth authorization server discovery endpoint.

    Supports both legacy pattern (/{server_name}) and root endpoint.

    Args:
        mcp_server_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        mcp_server_name=mcp_server_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    mcp_server_name: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Oauth Authorization Server Mcp

     OAuth authorization server discovery endpoint.

    Supports both legacy pattern (/{server_name}) and root endpoint.

    Args:
        mcp_server_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
mcp_server_name=mcp_server_name,

    )).parsed
