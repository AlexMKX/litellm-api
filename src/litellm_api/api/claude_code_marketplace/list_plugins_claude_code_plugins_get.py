from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.list_plugins_response import ListPluginsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    enabled_only: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["enabled_only"] = enabled_only


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/claude-code/plugins",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | ListPluginsResponse | None:
    if response.status_code == 200:
        response_200 = ListPluginsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | ListPluginsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    enabled_only: bool | Unset = False,

) -> Response[HTTPValidationError | ListPluginsResponse]:
    """ List Plugins

     List all plugins in the marketplace.

    Parameters:
        - enabled_only: If true, only return enabled plugins

    Returns:
        List of plugins with their metadata.

    Args:
        enabled_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListPluginsResponse]
     """


    kwargs = _get_kwargs(
        enabled_only=enabled_only,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    enabled_only: bool | Unset = False,

) -> HTTPValidationError | ListPluginsResponse | None:
    """ List Plugins

     List all plugins in the marketplace.

    Parameters:
        - enabled_only: If true, only return enabled plugins

    Returns:
        List of plugins with their metadata.

    Args:
        enabled_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListPluginsResponse
     """


    return sync_detailed(
        client=client,
enabled_only=enabled_only,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    enabled_only: bool | Unset = False,

) -> Response[HTTPValidationError | ListPluginsResponse]:
    """ List Plugins

     List all plugins in the marketplace.

    Parameters:
        - enabled_only: If true, only return enabled plugins

    Returns:
        List of plugins with their metadata.

    Args:
        enabled_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListPluginsResponse]
     """


    kwargs = _get_kwargs(
        enabled_only=enabled_only,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    enabled_only: bool | Unset = False,

) -> HTTPValidationError | ListPluginsResponse | None:
    """ List Plugins

     List all plugins in the marketplace.

    Parameters:
        - enabled_only: If true, only return enabled plugins

    Returns:
        List of plugins with their metadata.

    Args:
        enabled_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListPluginsResponse
     """


    return (await asyncio_detailed(
        client=client,
enabled_only=enabled_only,

    )).parsed
