from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cache_settings_update_request import CacheSettingsUpdateRequest
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    *,
    body: CacheSettingsUpdateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cache/settings",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: CacheSettingsUpdateRequest,

) -> Response[Any | HTTPValidationError]:
    """ Update Cache Settings

     Save cache settings to database and initialize cache.

    This endpoint:
    1. Encrypts sensitive fields (passwords, etc.)
    2. Saves to LiteLLM_CacheConfig table
    3. Reinitializes cache with new settings

    Args:
        body (CacheSettingsUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: CacheSettingsUpdateRequest,

) -> Any | HTTPValidationError | None:
    """ Update Cache Settings

     Save cache settings to database and initialize cache.

    This endpoint:
    1. Encrypts sensitive fields (passwords, etc.)
    2. Saves to LiteLLM_CacheConfig table
    3. Reinitializes cache with new settings

    Args:
        body (CacheSettingsUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CacheSettingsUpdateRequest,

) -> Response[Any | HTTPValidationError]:
    """ Update Cache Settings

     Save cache settings to database and initialize cache.

    This endpoint:
    1. Encrypts sensitive fields (passwords, etc.)
    2. Saves to LiteLLM_CacheConfig table
    3. Reinitializes cache with new settings

    Args:
        body (CacheSettingsUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CacheSettingsUpdateRequest,

) -> Any | HTTPValidationError | None:
    """ Update Cache Settings

     Save cache settings to database and initialize cache.

    This endpoint:
    1. Encrypts sensitive fields (passwords, etc.)
    2. Saves to LiteLLM_CacheConfig table
    3. Reinitializes cache with new settings

    Args:
        body (CacheSettingsUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
