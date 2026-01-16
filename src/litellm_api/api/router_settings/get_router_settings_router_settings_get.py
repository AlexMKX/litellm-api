from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.router_settings_response import RouterSettingsResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/router/settings",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RouterSettingsResponse | None:
    if response.status_code == 200:
        response_200 = RouterSettingsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RouterSettingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[RouterSettingsResponse]:
    """ Get Router Settings

     Get router configuration and available settings.

    Returns:
    - fields: List of all configurable router settings with their metadata (type, description, default,
    options)
              The routing_strategy field includes available options extracted from the Router class
    - current_values: Current values of router settings from config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RouterSettingsResponse]
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

) -> RouterSettingsResponse | None:
    """ Get Router Settings

     Get router configuration and available settings.

    Returns:
    - fields: List of all configurable router settings with their metadata (type, description, default,
    options)
              The routing_strategy field includes available options extracted from the Router class
    - current_values: Current values of router settings from config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RouterSettingsResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[RouterSettingsResponse]:
    """ Get Router Settings

     Get router configuration and available settings.

    Returns:
    - fields: List of all configurable router settings with their metadata (type, description, default,
    options)
              The routing_strategy field includes available options extracted from the Router class
    - current_values: Current values of router settings from config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RouterSettingsResponse]
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

) -> RouterSettingsResponse | None:
    """ Get Router Settings

     Get router configuration and available settings.

    Returns:
    - fields: List of all configurable router settings with their metadata (type, description, default,
    options)
              The routing_strategy field includes available options extracted from the Router class
    - current_values: Current values of router settings from config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RouterSettingsResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
