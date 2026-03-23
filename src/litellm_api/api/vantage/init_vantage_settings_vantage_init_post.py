from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.vantage_init_request import VantageInitRequest
from ...models.vantage_init_response import VantageInitResponse
from typing import cast



def _get_kwargs(
    *,
    body: VantageInitRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/vantage/init",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | VantageInitResponse | None:
    if response.status_code == 200:
        response_200 = VantageInitResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | VantageInitResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: VantageInitRequest,

) -> Response[HTTPValidationError | VantageInitResponse]:
    """ Init Vantage Settings

     Initialize Vantage settings and store in the database.

    Parameters:
    - api_key: Vantage API key for authentication
    - integration_token: Vantage integration token for the cost-import endpoint
    - base_url: Vantage API base URL (default: https://api.vantage.sh)

    Only admin users can configure Vantage settings.

    Args:
        body (VantageInitRequest): Request model for initializing Vantage settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | VantageInitResponse]
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
    body: VantageInitRequest,

) -> HTTPValidationError | VantageInitResponse | None:
    """ Init Vantage Settings

     Initialize Vantage settings and store in the database.

    Parameters:
    - api_key: Vantage API key for authentication
    - integration_token: Vantage integration token for the cost-import endpoint
    - base_url: Vantage API base URL (default: https://api.vantage.sh)

    Only admin users can configure Vantage settings.

    Args:
        body (VantageInitRequest): Request model for initializing Vantage settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | VantageInitResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: VantageInitRequest,

) -> Response[HTTPValidationError | VantageInitResponse]:
    """ Init Vantage Settings

     Initialize Vantage settings and store in the database.

    Parameters:
    - api_key: Vantage API key for authentication
    - integration_token: Vantage integration token for the cost-import endpoint
    - base_url: Vantage API base URL (default: https://api.vantage.sh)

    Only admin users can configure Vantage settings.

    Args:
        body (VantageInitRequest): Request model for initializing Vantage settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | VantageInitResponse]
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
    body: VantageInitRequest,

) -> HTTPValidationError | VantageInitResponse | None:
    """ Init Vantage Settings

     Initialize Vantage settings and store in the database.

    Parameters:
    - api_key: Vantage API key for authentication
    - integration_token: Vantage integration token for the cost-import endpoint
    - base_url: Vantage API base URL (default: https://api.vantage.sh)

    Only admin users can configure Vantage settings.

    Args:
        body (VantageInitRequest): Request model for initializing Vantage settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | VantageInitResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
