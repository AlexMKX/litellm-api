from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cloud_zero_init_response import CloudZeroInitResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/cloudzero/delete",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CloudZeroInitResponse | None:
    if response.status_code == 200:
        response_200 = CloudZeroInitResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CloudZeroInitResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[CloudZeroInitResponse]:
    """ Delete Cloudzero Settings

     Delete CloudZero settings from the database.

    This endpoint removes the CloudZero configuration (API key, connection ID, timezone)
    from the proxy database. Only the CloudZero settings entry will be deleted;
    other configuration values in the database will remain unchanged.

    Only admin users can delete CloudZero settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudZeroInitResponse]
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

) -> CloudZeroInitResponse | None:
    """ Delete Cloudzero Settings

     Delete CloudZero settings from the database.

    This endpoint removes the CloudZero configuration (API key, connection ID, timezone)
    from the proxy database. Only the CloudZero settings entry will be deleted;
    other configuration values in the database will remain unchanged.

    Only admin users can delete CloudZero settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudZeroInitResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[CloudZeroInitResponse]:
    """ Delete Cloudzero Settings

     Delete CloudZero settings from the database.

    This endpoint removes the CloudZero configuration (API key, connection ID, timezone)
    from the proxy database. Only the CloudZero settings entry will be deleted;
    other configuration values in the database will remain unchanged.

    Only admin users can delete CloudZero settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudZeroInitResponse]
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

) -> CloudZeroInitResponse | None:
    """ Delete Cloudzero Settings

     Delete CloudZero settings from the database.

    This endpoint removes the CloudZero configuration (API key, connection ID, timezone)
    from the proxy database. Only the CloudZero settings entry will be deleted;
    other configuration values in the database will remain unchanged.

    Only admin users can delete CloudZero settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudZeroInitResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
