from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.tag_summary_response import TagSummaryResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_date: str,
    end_date: str,
    tag_filter: None | str | Unset = UNSET,
    tag_filters: list[str] | None | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["start_date"] = start_date

    params["end_date"] = end_date

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
        "url": "/tag/summary",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | TagSummaryResponse | None:
    if response.status_code == 200:
        response_200 = TagSummaryResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | TagSummaryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_date: str,
    end_date: str,
    tag_filter: None | str | Unset = UNSET,
    tag_filters: list[str] | None | Unset = UNSET,

) -> Response[HTTPValidationError | TagSummaryResponse]:
    """ Get Tag Summary

     Get summary analytics for tags including unique users, requests, tokens, and spend.

    Args:
        start_date: Start date for the analytics period (YYYY-MM-DD)
        end_date: End date for the analytics period (YYYY-MM-DD)
        tag_filter: Optional filter to specific tag (legacy)
        tag_filters: Optional filter to multiple specific tags (takes precedence over tag_filter)

    Returns:
        TagSummaryResponse: Summary analytics data by tag

    Args:
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        tag_filter (None | str | Unset): Filter by specific tag (optional)
        tag_filters (list[str] | None | Unset): Filter by multiple specific tags (optional, takes
            precedence over tag_filter)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TagSummaryResponse]
     """


    kwargs = _get_kwargs(
        start_date=start_date,
end_date=end_date,
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
    start_date: str,
    end_date: str,
    tag_filter: None | str | Unset = UNSET,
    tag_filters: list[str] | None | Unset = UNSET,

) -> HTTPValidationError | TagSummaryResponse | None:
    """ Get Tag Summary

     Get summary analytics for tags including unique users, requests, tokens, and spend.

    Args:
        start_date: Start date for the analytics period (YYYY-MM-DD)
        end_date: End date for the analytics period (YYYY-MM-DD)
        tag_filter: Optional filter to specific tag (legacy)
        tag_filters: Optional filter to multiple specific tags (takes precedence over tag_filter)

    Returns:
        TagSummaryResponse: Summary analytics data by tag

    Args:
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        tag_filter (None | str | Unset): Filter by specific tag (optional)
        tag_filters (list[str] | None | Unset): Filter by multiple specific tags (optional, takes
            precedence over tag_filter)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TagSummaryResponse
     """


    return sync_detailed(
        client=client,
start_date=start_date,
end_date=end_date,
tag_filter=tag_filter,
tag_filters=tag_filters,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: str,
    end_date: str,
    tag_filter: None | str | Unset = UNSET,
    tag_filters: list[str] | None | Unset = UNSET,

) -> Response[HTTPValidationError | TagSummaryResponse]:
    """ Get Tag Summary

     Get summary analytics for tags including unique users, requests, tokens, and spend.

    Args:
        start_date: Start date for the analytics period (YYYY-MM-DD)
        end_date: End date for the analytics period (YYYY-MM-DD)
        tag_filter: Optional filter to specific tag (legacy)
        tag_filters: Optional filter to multiple specific tags (takes precedence over tag_filter)

    Returns:
        TagSummaryResponse: Summary analytics data by tag

    Args:
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        tag_filter (None | str | Unset): Filter by specific tag (optional)
        tag_filters (list[str] | None | Unset): Filter by multiple specific tags (optional, takes
            precedence over tag_filter)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TagSummaryResponse]
     """


    kwargs = _get_kwargs(
        start_date=start_date,
end_date=end_date,
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
    start_date: str,
    end_date: str,
    tag_filter: None | str | Unset = UNSET,
    tag_filters: list[str] | None | Unset = UNSET,

) -> HTTPValidationError | TagSummaryResponse | None:
    """ Get Tag Summary

     Get summary analytics for tags including unique users, requests, tokens, and spend.

    Args:
        start_date: Start date for the analytics period (YYYY-MM-DD)
        end_date: End date for the analytics period (YYYY-MM-DD)
        tag_filter: Optional filter to specific tag (legacy)
        tag_filters: Optional filter to multiple specific tags (takes precedence over tag_filter)

    Returns:
        TagSummaryResponse: Summary analytics data by tag

    Args:
        start_date (str): Start date in YYYY-MM-DD format
        end_date (str): End date in YYYY-MM-DD format
        tag_filter (None | str | Unset): Filter by specific tag (optional)
        tag_filters (list[str] | None | Unset): Filter by multiple specific tags (optional, takes
            precedence over tag_filter)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TagSummaryResponse
     """


    return (await asyncio_detailed(
        client=client,
start_date=start_date,
end_date=end_date,
tag_filter=tag_filter,
tag_filters=tag_filters,

    )).parsed
