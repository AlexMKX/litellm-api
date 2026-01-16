from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.distinct_tags_response import DistinctTagsResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tag/distinct",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DistinctTagsResponse | None:
    if response.status_code == 200:
        response_200 = DistinctTagsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DistinctTagsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[DistinctTagsResponse]:
    """ Get Distinct User Agent Tags

     Get all distinct user agent tags up to a maximum of {MAX_TAGS} tags.

    This endpoint returns all unique user agent tags found in the database,
    sorted by frequency of usage.

    Returns:
        DistinctTagsResponse: List of distinct user agent tags

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DistinctTagsResponse]
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

) -> DistinctTagsResponse | None:
    """ Get Distinct User Agent Tags

     Get all distinct user agent tags up to a maximum of {MAX_TAGS} tags.

    This endpoint returns all unique user agent tags found in the database,
    sorted by frequency of usage.

    Returns:
        DistinctTagsResponse: List of distinct user agent tags

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DistinctTagsResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[DistinctTagsResponse]:
    """ Get Distinct User Agent Tags

     Get all distinct user agent tags up to a maximum of {MAX_TAGS} tags.

    This endpoint returns all unique user agent tags found in the database,
    sorted by frequency of usage.

    Returns:
        DistinctTagsResponse: List of distinct user agent tags

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DistinctTagsResponse]
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

) -> DistinctTagsResponse | None:
    """ Get Distinct User Agent Tags

     Get all distinct user agent tags up to a maximum of {MAX_TAGS} tags.

    This endpoint returns all unique user agent tags found in the database,
    sorted by frequency of usage.

    Returns:
        DistinctTagsResponse: List of distinct user agent tags

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DistinctTagsResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
