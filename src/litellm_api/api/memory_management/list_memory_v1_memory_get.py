from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.memory_list_response import MemoryListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    key: None | str | Unset = UNSET,
    key_prefix: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_key: None | str | Unset
    if isinstance(key, Unset):
        json_key = UNSET
    else:
        json_key = key
    params["key"] = json_key

    json_key_prefix: None | str | Unset
    if isinstance(key_prefix, Unset):
        json_key_prefix = UNSET
    else:
        json_key_prefix = key_prefix
    params["key_prefix"] = json_key_prefix

    params["page"] = page

    params["page_size"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/memory",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | MemoryListResponse | None:
    if response.status_code == 200:
        response_200 = MemoryListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | MemoryListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    key: None | str | Unset = UNSET,
    key_prefix: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[HTTPValidationError | MemoryListResponse]:
    """ List Memory

     List memory entries visible to the caller.

    Args:
        key (None | str | Unset): Filter by exact key match.
        key_prefix (None | str | Unset): Filter by key prefix (Redis-style namespace scan).
            Mutually exclusive with `key`; if both are provided, `key_prefix` wins.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MemoryListResponse]
     """


    kwargs = _get_kwargs(
        key=key,
key_prefix=key_prefix,
page=page,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    key: None | str | Unset = UNSET,
    key_prefix: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> HTTPValidationError | MemoryListResponse | None:
    """ List Memory

     List memory entries visible to the caller.

    Args:
        key (None | str | Unset): Filter by exact key match.
        key_prefix (None | str | Unset): Filter by key prefix (Redis-style namespace scan).
            Mutually exclusive with `key`; if both are provided, `key_prefix` wins.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MemoryListResponse
     """


    return sync_detailed(
        client=client,
key=key,
key_prefix=key_prefix,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    key: None | str | Unset = UNSET,
    key_prefix: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[HTTPValidationError | MemoryListResponse]:
    """ List Memory

     List memory entries visible to the caller.

    Args:
        key (None | str | Unset): Filter by exact key match.
        key_prefix (None | str | Unset): Filter by key prefix (Redis-style namespace scan).
            Mutually exclusive with `key`; if both are provided, `key_prefix` wins.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MemoryListResponse]
     """


    kwargs = _get_kwargs(
        key=key,
key_prefix=key_prefix,
page=page,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    key: None | str | Unset = UNSET,
    key_prefix: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> HTTPValidationError | MemoryListResponse | None:
    """ List Memory

     List memory entries visible to the caller.

    Args:
        key (None | str | Unset): Filter by exact key match.
        key_prefix (None | str | Unset): Filter by key prefix (Redis-style namespace scan).
            Mutually exclusive with `key`; if both are provided, `key_prefix` wins.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MemoryListResponse
     """


    return (await asyncio_detailed(
        client=client,
key=key,
key_prefix=key_prefix,
page=page,
page_size=page_size,

    )).parsed
