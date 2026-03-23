from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.vantage_init_response import VantageInitResponse
from ...models.vantage_settings_update import VantageSettingsUpdate
from typing import cast



def _get_kwargs(
    *,
    body: VantageSettingsUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/vantage/settings",
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
    body: VantageSettingsUpdate,

) -> Response[HTTPValidationError | VantageInitResponse]:
    """ Update Vantage Settings

     Update existing Vantage settings.

    Allows updating individual Vantage configuration fields without requiring all fields.
    Only admin users can update Vantage settings.

    Args:
        body (VantageSettingsUpdate): Request model for updating Vantage settings

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
    body: VantageSettingsUpdate,

) -> HTTPValidationError | VantageInitResponse | None:
    """ Update Vantage Settings

     Update existing Vantage settings.

    Allows updating individual Vantage configuration fields without requiring all fields.
    Only admin users can update Vantage settings.

    Args:
        body (VantageSettingsUpdate): Request model for updating Vantage settings

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
    body: VantageSettingsUpdate,

) -> Response[HTTPValidationError | VantageInitResponse]:
    """ Update Vantage Settings

     Update existing Vantage settings.

    Allows updating individual Vantage configuration fields without requiring all fields.
    Only admin users can update Vantage settings.

    Args:
        body (VantageSettingsUpdate): Request model for updating Vantage settings

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
    body: VantageSettingsUpdate,

) -> HTTPValidationError | VantageInitResponse | None:
    """ Update Vantage Settings

     Update existing Vantage settings.

    Allows updating individual Vantage configuration fields without requiring all fields.
    Only admin users can update Vantage settings.

    Args:
        body (VantageSettingsUpdate): Request model for updating Vantage settings

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
