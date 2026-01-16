from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.per_user_analytics_response import PerUserAnalyticsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    tag_filter: None | str | Unset = UNSET,
    tag_filters: list[str] | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_tag_filter: None | str | Unset
    if isinstance(tag_filter, Unset):
        json_tag_filter = UNSET
    else:
        json_tag_filter = tag_filter
    params["tag_filter"] = json_tag_filter

    json_tag_filters: list[str] | None | Unset
    if isinstance(tag_filters, Unset):
        json_tag_filters = UNSET
    elif isinstance(tag_filters, list):
        json_tag_filters = tag_filters


    else:
        json_tag_filters = tag_filters
    params["tag_filters"] = json_tag_filters

    params["page"] = page

    params["page_size"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tag/user-agent/per-user-analytics",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | PerUserAnalyticsResponse | None:
    if response.status_code == 200:
        response_200 = PerUserAnalyticsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | PerUserAnalyticsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    tag_filter: None | str | Unset = UNSET,
    tag_filters: list[str] | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[HTTPValidationError | PerUserAnalyticsResponse]:
    """ Get Per User Analytics

     Get per-user analytics including successful requests, tokens, and spend by individual users.

    This endpoint provides usage metrics broken down by individual users based on their
    tag activity during the last 30 days ending on UTC today + 1 day.

    Args:
        tag_filter: Optional filter to specific tag (legacy)
        tag_filters: Optional filter to multiple specific tags (takes precedence over tag_filter)
        page: Page number for pagination
        page_size: Number of items per page

    Returns:
        PerUserAnalyticsResponse: Analytics data broken down by individual users for the last 30 days

    Args:
        tag_filter (None | str | Unset): Filter by specific tag (optional)
        tag_filters (list[str] | None | Unset): Filter by multiple specific tags (optional, takes
            precedence over tag_filter)
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PerUserAnalyticsResponse]
     """


    kwargs = _get_kwargs(
        tag_filter=tag_filter,
tag_filters=tag_filters,
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
    tag_filter: None | str | Unset = UNSET,
    tag_filters: list[str] | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> HTTPValidationError | PerUserAnalyticsResponse | None:
    """ Get Per User Analytics

     Get per-user analytics including successful requests, tokens, and spend by individual users.

    This endpoint provides usage metrics broken down by individual users based on their
    tag activity during the last 30 days ending on UTC today + 1 day.

    Args:
        tag_filter: Optional filter to specific tag (legacy)
        tag_filters: Optional filter to multiple specific tags (takes precedence over tag_filter)
        page: Page number for pagination
        page_size: Number of items per page

    Returns:
        PerUserAnalyticsResponse: Analytics data broken down by individual users for the last 30 days

    Args:
        tag_filter (None | str | Unset): Filter by specific tag (optional)
        tag_filters (list[str] | None | Unset): Filter by multiple specific tags (optional, takes
            precedence over tag_filter)
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PerUserAnalyticsResponse
     """


    return sync_detailed(
        client=client,
tag_filter=tag_filter,
tag_filters=tag_filters,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    tag_filter: None | str | Unset = UNSET,
    tag_filters: list[str] | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[HTTPValidationError | PerUserAnalyticsResponse]:
    """ Get Per User Analytics

     Get per-user analytics including successful requests, tokens, and spend by individual users.

    This endpoint provides usage metrics broken down by individual users based on their
    tag activity during the last 30 days ending on UTC today + 1 day.

    Args:
        tag_filter: Optional filter to specific tag (legacy)
        tag_filters: Optional filter to multiple specific tags (takes precedence over tag_filter)
        page: Page number for pagination
        page_size: Number of items per page

    Returns:
        PerUserAnalyticsResponse: Analytics data broken down by individual users for the last 30 days

    Args:
        tag_filter (None | str | Unset): Filter by specific tag (optional)
        tag_filters (list[str] | None | Unset): Filter by multiple specific tags (optional, takes
            precedence over tag_filter)
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PerUserAnalyticsResponse]
     """


    kwargs = _get_kwargs(
        tag_filter=tag_filter,
tag_filters=tag_filters,
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
    tag_filter: None | str | Unset = UNSET,
    tag_filters: list[str] | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> HTTPValidationError | PerUserAnalyticsResponse | None:
    """ Get Per User Analytics

     Get per-user analytics including successful requests, tokens, and spend by individual users.

    This endpoint provides usage metrics broken down by individual users based on their
    tag activity during the last 30 days ending on UTC today + 1 day.

    Args:
        tag_filter: Optional filter to specific tag (legacy)
        tag_filters: Optional filter to multiple specific tags (takes precedence over tag_filter)
        page: Page number for pagination
        page_size: Number of items per page

    Returns:
        PerUserAnalyticsResponse: Analytics data broken down by individual users for the last 30 days

    Args:
        tag_filter (None | str | Unset): Filter by specific tag (optional)
        tag_filters (list[str] | None | Unset): Filter by multiple specific tags (optional, takes
            precedence over tag_filter)
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PerUserAnalyticsResponse
     """


    return (await asyncio_detailed(
        client=client,
tag_filter=tag_filter,
tag_filters=tag_filters,
page=page,
page_size=page_size,

    )).parsed
