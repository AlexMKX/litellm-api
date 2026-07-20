from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.coordination_redis_settings_response import CoordinationRedisSettingsResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/coordination_redis/settings",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CoordinationRedisSettingsResponse | None:
    if response.status_code == 200:
        response_200 = CoordinationRedisSettingsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CoordinationRedisSettingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[CoordinationRedisSettingsResponse]:
    r""" Get Coordination Redis Settings

     Get the coordination Redis configuration and available settings.

    Returns:
    - values: current coordination Redis settings, with password/sentinel_password/url redacted
    - fields: all configurable settings with their metadata (type, description, default, section)
    - source: \"coordination_redis\" | \"cache_backend\" | \"environment\" | null

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CoordinationRedisSettingsResponse]
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

) -> CoordinationRedisSettingsResponse | None:
    r""" Get Coordination Redis Settings

     Get the coordination Redis configuration and available settings.

    Returns:
    - values: current coordination Redis settings, with password/sentinel_password/url redacted
    - fields: all configurable settings with their metadata (type, description, default, section)
    - source: \"coordination_redis\" | \"cache_backend\" | \"environment\" | null

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CoordinationRedisSettingsResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[CoordinationRedisSettingsResponse]:
    r""" Get Coordination Redis Settings

     Get the coordination Redis configuration and available settings.

    Returns:
    - values: current coordination Redis settings, with password/sentinel_password/url redacted
    - fields: all configurable settings with their metadata (type, description, default, section)
    - source: \"coordination_redis\" | \"cache_backend\" | \"environment\" | null

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CoordinationRedisSettingsResponse]
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

) -> CoordinationRedisSettingsResponse | None:
    r""" Get Coordination Redis Settings

     Get the coordination Redis configuration and available settings.

    Returns:
    - values: current coordination Redis settings, with password/sentinel_password/url redacted
    - fields: all configurable settings with their metadata (type, description, default, section)
    - source: \"coordination_redis\" | \"cache_backend\" | \"environment\" | null

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CoordinationRedisSettingsResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
