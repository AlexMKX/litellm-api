from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.spend_analytics_paginated_response import SpendAnalyticsPaginatedResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    model: None | str | Unset = UNSET,
    api_key: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_start_date: None | str | Unset
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: None | str | Unset
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date

    json_model: None | str | Unset
    if isinstance(model, Unset):
        json_model = UNSET
    else:
        json_model = model
    params["model"] = json_model

    json_api_key: None | str | Unset
    if isinstance(api_key, Unset):
        json_api_key = UNSET
    else:
        json_api_key = api_key
    params["api_key"] = json_api_key

    params["page"] = page

    params["page_size"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/user/daily/activity",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | SpendAnalyticsPaginatedResponse | None:
    if response.status_code == 200:
        response_200 = SpendAnalyticsPaginatedResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | SpendAnalyticsPaginatedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    model: None | str | Unset = UNSET,
    api_key: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[HTTPValidationError | SpendAnalyticsPaginatedResponse]:
    """ Get User Daily Activity

     [BETA] This is a beta endpoint. It will change.

    Meant to optimize querying spend data for analytics for a user.

    Returns:
    (by date)
    - spend
    - prompt_tokens
    - completion_tokens
    - cache_read_input_tokens
    - cache_creation_input_tokens
    - total_tokens
    - api_requests
    - breakdown by model, api_key, provider

    Args:
        start_date (None | str | Unset): Start date in YYYY-MM-DD format
        end_date (None | str | Unset): End date in YYYY-MM-DD format
        model (None | str | Unset): Filter by specific model
        api_key (None | str | Unset): Filter by specific API key
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SpendAnalyticsPaginatedResponse]
     """


    kwargs = _get_kwargs(
        start_date=start_date,
end_date=end_date,
model=model,
api_key=api_key,
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
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    model: None | str | Unset = UNSET,
    api_key: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> HTTPValidationError | SpendAnalyticsPaginatedResponse | None:
    """ Get User Daily Activity

     [BETA] This is a beta endpoint. It will change.

    Meant to optimize querying spend data for analytics for a user.

    Returns:
    (by date)
    - spend
    - prompt_tokens
    - completion_tokens
    - cache_read_input_tokens
    - cache_creation_input_tokens
    - total_tokens
    - api_requests
    - breakdown by model, api_key, provider

    Args:
        start_date (None | str | Unset): Start date in YYYY-MM-DD format
        end_date (None | str | Unset): End date in YYYY-MM-DD format
        model (None | str | Unset): Filter by specific model
        api_key (None | str | Unset): Filter by specific API key
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SpendAnalyticsPaginatedResponse
     """


    return sync_detailed(
        client=client,
start_date=start_date,
end_date=end_date,
model=model,
api_key=api_key,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    model: None | str | Unset = UNSET,
    api_key: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[HTTPValidationError | SpendAnalyticsPaginatedResponse]:
    """ Get User Daily Activity

     [BETA] This is a beta endpoint. It will change.

    Meant to optimize querying spend data for analytics for a user.

    Returns:
    (by date)
    - spend
    - prompt_tokens
    - completion_tokens
    - cache_read_input_tokens
    - cache_creation_input_tokens
    - total_tokens
    - api_requests
    - breakdown by model, api_key, provider

    Args:
        start_date (None | str | Unset): Start date in YYYY-MM-DD format
        end_date (None | str | Unset): End date in YYYY-MM-DD format
        model (None | str | Unset): Filter by specific model
        api_key (None | str | Unset): Filter by specific API key
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SpendAnalyticsPaginatedResponse]
     """


    kwargs = _get_kwargs(
        start_date=start_date,
end_date=end_date,
model=model,
api_key=api_key,
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
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    model: None | str | Unset = UNSET,
    api_key: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> HTTPValidationError | SpendAnalyticsPaginatedResponse | None:
    """ Get User Daily Activity

     [BETA] This is a beta endpoint. It will change.

    Meant to optimize querying spend data for analytics for a user.

    Returns:
    (by date)
    - spend
    - prompt_tokens
    - completion_tokens
    - cache_read_input_tokens
    - cache_creation_input_tokens
    - total_tokens
    - api_requests
    - breakdown by model, api_key, provider

    Args:
        start_date (None | str | Unset): Start date in YYYY-MM-DD format
        end_date (None | str | Unset): End date in YYYY-MM-DD format
        model (None | str | Unset): Filter by specific model
        api_key (None | str | Unset): Filter by specific API key
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SpendAnalyticsPaginatedResponse
     """


    return (await asyncio_detailed(
        client=client,
start_date=start_date,
end_date=end_date,
model=model,
api_key=api_key,
page=page,
page_size=page_size,

    )).parsed
