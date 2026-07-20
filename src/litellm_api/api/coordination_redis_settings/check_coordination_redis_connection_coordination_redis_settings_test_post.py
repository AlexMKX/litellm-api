from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.coordination_redis_settings_request import CoordinationRedisSettingsRequest
from ...models.coordination_redis_test_response import CoordinationRedisTestResponse
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    *,
    body: CoordinationRedisSettingsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/coordination_redis/settings/test",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CoordinationRedisTestResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CoordinationRedisTestResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CoordinationRedisTestResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CoordinationRedisSettingsRequest,

) -> Response[CoordinationRedisTestResponse | HTTPValidationError]:
    """ Check Coordination Redis Connection

     Test a coordination Redis connection with the provided credentials.

    Parameters:
    - settings: dict - Redis connection params to test. Credential fields sent back as `***REDACTED***`
    fall back to the saved value

    Builds a throwaway client (never touching global state) and pings it.

    Args:
        body (CoordinationRedisSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CoordinationRedisTestResponse | HTTPValidationError]
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
    body: CoordinationRedisSettingsRequest,

) -> CoordinationRedisTestResponse | HTTPValidationError | None:
    """ Check Coordination Redis Connection

     Test a coordination Redis connection with the provided credentials.

    Parameters:
    - settings: dict - Redis connection params to test. Credential fields sent back as `***REDACTED***`
    fall back to the saved value

    Builds a throwaway client (never touching global state) and pings it.

    Args:
        body (CoordinationRedisSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CoordinationRedisTestResponse | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CoordinationRedisSettingsRequest,

) -> Response[CoordinationRedisTestResponse | HTTPValidationError]:
    """ Check Coordination Redis Connection

     Test a coordination Redis connection with the provided credentials.

    Parameters:
    - settings: dict - Redis connection params to test. Credential fields sent back as `***REDACTED***`
    fall back to the saved value

    Builds a throwaway client (never touching global state) and pings it.

    Args:
        body (CoordinationRedisSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CoordinationRedisTestResponse | HTTPValidationError]
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
    body: CoordinationRedisSettingsRequest,

) -> CoordinationRedisTestResponse | HTTPValidationError | None:
    """ Check Coordination Redis Connection

     Test a coordination Redis connection with the provided credentials.

    Parameters:
    - settings: dict - Redis connection params to test. Credential fields sent back as `***REDACTED***`
    fall back to the saved value

    Builds a throwaway client (never touching global state) and pings it.

    Args:
        body (CoordinationRedisSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CoordinationRedisTestResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
