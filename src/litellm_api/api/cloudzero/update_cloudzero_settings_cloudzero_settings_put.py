from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cloud_zero_init_response import CloudZeroInitResponse
from ...models.cloud_zero_settings_update import CloudZeroSettingsUpdate
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    *,
    body: CloudZeroSettingsUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/cloudzero/settings",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CloudZeroInitResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CloudZeroInitResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CloudZeroInitResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CloudZeroSettingsUpdate,

) -> Response[CloudZeroInitResponse | HTTPValidationError]:
    """ Update Cloudzero Settings

     Update existing CloudZero settings.

    Allows updating individual CloudZero configuration fields without requiring all fields.
    Only provided fields will be updated; others will remain unchanged.

    Parameters:
    - api_key: (Optional) New CloudZero API key for authentication
    - connection_id: (Optional) New CloudZero connection ID for data submission
    - timezone: (Optional) New timezone for date handling

    Only admin users can update CloudZero settings.

    Args:
        body (CloudZeroSettingsUpdate): Request model for updating CloudZero settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudZeroInitResponse | HTTPValidationError]
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
    body: CloudZeroSettingsUpdate,

) -> CloudZeroInitResponse | HTTPValidationError | None:
    """ Update Cloudzero Settings

     Update existing CloudZero settings.

    Allows updating individual CloudZero configuration fields without requiring all fields.
    Only provided fields will be updated; others will remain unchanged.

    Parameters:
    - api_key: (Optional) New CloudZero API key for authentication
    - connection_id: (Optional) New CloudZero connection ID for data submission
    - timezone: (Optional) New timezone for date handling

    Only admin users can update CloudZero settings.

    Args:
        body (CloudZeroSettingsUpdate): Request model for updating CloudZero settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudZeroInitResponse | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CloudZeroSettingsUpdate,

) -> Response[CloudZeroInitResponse | HTTPValidationError]:
    """ Update Cloudzero Settings

     Update existing CloudZero settings.

    Allows updating individual CloudZero configuration fields without requiring all fields.
    Only provided fields will be updated; others will remain unchanged.

    Parameters:
    - api_key: (Optional) New CloudZero API key for authentication
    - connection_id: (Optional) New CloudZero connection ID for data submission
    - timezone: (Optional) New timezone for date handling

    Only admin users can update CloudZero settings.

    Args:
        body (CloudZeroSettingsUpdate): Request model for updating CloudZero settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudZeroInitResponse | HTTPValidationError]
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
    body: CloudZeroSettingsUpdate,

) -> CloudZeroInitResponse | HTTPValidationError | None:
    """ Update Cloudzero Settings

     Update existing CloudZero settings.

    Allows updating individual CloudZero configuration fields without requiring all fields.
    Only provided fields will be updated; others will remain unchanged.

    Parameters:
    - api_key: (Optional) New CloudZero API key for authentication
    - connection_id: (Optional) New CloudZero connection ID for data submission
    - timezone: (Optional) New timezone for date handling

    Only admin users can update CloudZero settings.

    Args:
        body (CloudZeroSettingsUpdate): Request model for updating CloudZero settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudZeroInitResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
