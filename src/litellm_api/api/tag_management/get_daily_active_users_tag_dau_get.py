from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.active_users_analytics_response import ActiveUsersAnalyticsResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    tag_filter: None | str | Unset = UNSET,
    tag_filters: list[str] | None | Unset = UNSET,

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


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tag/dau",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ActiveUsersAnalyticsResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ActiveUsersAnalyticsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ActiveUsersAnalyticsResponse | HTTPValidationError]:
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

) -> Response[ActiveUsersAnalyticsResponse | HTTPValidationError]:
    """ Get Daily Active Users

     Get Daily Active Users (DAU) by tags for the last {MAX_DAYS} days ending on UTC today + 1 day.

    This endpoint efficiently calculates unique users per tag for each of the last {MAX_DAYS} days
    using a single optimized SQL query, perfect for dashboard time series visualization.

    Args:
        tag_filter: Optional filter to specific tag (legacy)
        tag_filters: Optional filter to multiple specific tags (takes precedence over tag_filter)

    Returns:
        ActiveUsersAnalyticsResponse: DAU data by tag for each of the last {MAX_DAYS} days

    Args:
        tag_filter (None | str | Unset): Filter by specific tag (optional)
        tag_filters (list[str] | None | Unset): Filter by multiple specific tags (optional, takes
            precedence over tag_filter)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActiveUsersAnalyticsResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        tag_filter=tag_filter,
tag_filters=tag_filters,

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

) -> ActiveUsersAnalyticsResponse | HTTPValidationError | None:
    """ Get Daily Active Users

     Get Daily Active Users (DAU) by tags for the last {MAX_DAYS} days ending on UTC today + 1 day.

    This endpoint efficiently calculates unique users per tag for each of the last {MAX_DAYS} days
    using a single optimized SQL query, perfect for dashboard time series visualization.

    Args:
        tag_filter: Optional filter to specific tag (legacy)
        tag_filters: Optional filter to multiple specific tags (takes precedence over tag_filter)

    Returns:
        ActiveUsersAnalyticsResponse: DAU data by tag for each of the last {MAX_DAYS} days

    Args:
        tag_filter (None | str | Unset): Filter by specific tag (optional)
        tag_filters (list[str] | None | Unset): Filter by multiple specific tags (optional, takes
            precedence over tag_filter)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActiveUsersAnalyticsResponse | HTTPValidationError
     """


    return sync_detailed(
        client=client,
tag_filter=tag_filter,
tag_filters=tag_filters,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    tag_filter: None | str | Unset = UNSET,
    tag_filters: list[str] | None | Unset = UNSET,

) -> Response[ActiveUsersAnalyticsResponse | HTTPValidationError]:
    """ Get Daily Active Users

     Get Daily Active Users (DAU) by tags for the last {MAX_DAYS} days ending on UTC today + 1 day.

    This endpoint efficiently calculates unique users per tag for each of the last {MAX_DAYS} days
    using a single optimized SQL query, perfect for dashboard time series visualization.

    Args:
        tag_filter: Optional filter to specific tag (legacy)
        tag_filters: Optional filter to multiple specific tags (takes precedence over tag_filter)

    Returns:
        ActiveUsersAnalyticsResponse: DAU data by tag for each of the last {MAX_DAYS} days

    Args:
        tag_filter (None | str | Unset): Filter by specific tag (optional)
        tag_filters (list[str] | None | Unset): Filter by multiple specific tags (optional, takes
            precedence over tag_filter)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActiveUsersAnalyticsResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        tag_filter=tag_filter,
tag_filters=tag_filters,

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

) -> ActiveUsersAnalyticsResponse | HTTPValidationError | None:
    """ Get Daily Active Users

     Get Daily Active Users (DAU) by tags for the last {MAX_DAYS} days ending on UTC today + 1 day.

    This endpoint efficiently calculates unique users per tag for each of the last {MAX_DAYS} days
    using a single optimized SQL query, perfect for dashboard time series visualization.

    Args:
        tag_filter: Optional filter to specific tag (legacy)
        tag_filters: Optional filter to multiple specific tags (takes precedence over tag_filter)

    Returns:
        ActiveUsersAnalyticsResponse: DAU data by tag for each of the last {MAX_DAYS} days

    Args:
        tag_filter (None | str | Unset): Filter by specific tag (optional)
        tag_filters (list[str] | None | Unset): Filter by multiple specific tags (optional, takes
            precedence over tag_filter)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActiveUsersAnalyticsResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
tag_filter=tag_filter,
tag_filters=tag_filters,

    )).parsed
