from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cloud_zero_settings_view import CloudZeroSettingsView
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloudzero/settings",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CloudZeroSettingsView | None:
    if response.status_code == 200:
        response_200 = CloudZeroSettingsView.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CloudZeroSettingsView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[CloudZeroSettingsView]:
    """ Get Cloudzero Settings

     View current CloudZero settings.

    Returns the current CloudZero configuration with the API key masked for security.
    Only the first 4 and last 4 characters of the API key are shown.
    Returns null/empty values when settings are not configured (consistent with other settings
    endpoints).

    Only admin users can view CloudZero settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudZeroSettingsView]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> CloudZeroSettingsView | None:
    """ Get Cloudzero Settings

     View current CloudZero settings.

    Returns the current CloudZero configuration with the API key masked for security.
    Only the first 4 and last 4 characters of the API key are shown.
    Returns null/empty values when settings are not configured (consistent with other settings
    endpoints).

    Only admin users can view CloudZero settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudZeroSettingsView
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[CloudZeroSettingsView]:
    """ Get Cloudzero Settings

     View current CloudZero settings.

    Returns the current CloudZero configuration with the API key masked for security.
    Only the first 4 and last 4 characters of the API key are shown.
    Returns null/empty values when settings are not configured (consistent with other settings
    endpoints).

    Only admin users can view CloudZero settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudZeroSettingsView]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> CloudZeroSettingsView | None:
    """ Get Cloudzero Settings

     View current CloudZero settings.

    Returns the current CloudZero configuration with the API key masked for security.
    Only the first 4 and last 4 characters of the API key are shown.
    Returns null/empty values when settings are not configured (consistent with other settings
    endpoints).

    Only admin users can view CloudZero settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudZeroSettingsView
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
