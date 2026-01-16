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
    team_ids: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    model: None | str | Unset = UNSET,
    api_key: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    exclude_team_ids: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_team_ids: None | str | Unset
    if isinstance(team_ids, Unset):
        json_team_ids = UNSET
    else:
        json_team_ids = team_ids
    params["team_ids"] = json_team_ids

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

    json_exclude_team_ids: None | str | Unset
    if isinstance(exclude_team_ids, Unset):
        json_exclude_team_ids = UNSET
    else:
        json_exclude_team_ids = exclude_team_ids
    params["exclude_team_ids"] = json_exclude_team_ids


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/team/daily/activity",
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
    team_ids: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    model: None | str | Unset = UNSET,
    api_key: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    exclude_team_ids: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | SpendAnalyticsPaginatedResponse]:
    """ Get Team Daily Activity

     Get daily activity for specific teams or all teams.

    Args:
        team_ids (Optional[str]): Comma-separated list of team IDs to filter by. If not provided,
    returns data for all teams.
        start_date (Optional[str]): Start date for the activity period (YYYY-MM-DD).
        end_date (Optional[str]): End date for the activity period (YYYY-MM-DD).
        model (Optional[str]): Filter by model name.
        api_key (Optional[str]): Filter by API key.
        page (int): Page number for pagination.
        page_size (int): Number of items per page.
        exclude_team_ids (Optional[str]): Comma-separated list of team IDs to exclude.
    Returns:
        SpendAnalyticsPaginatedResponse: Paginated response containing daily activity data.

    Args:
        team_ids (None | str | Unset):
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        model (None | str | Unset):
        api_key (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 10.
        exclude_team_ids (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SpendAnalyticsPaginatedResponse]
     """


    kwargs = _get_kwargs(
        team_ids=team_ids,
start_date=start_date,
end_date=end_date,
model=model,
api_key=api_key,
page=page,
page_size=page_size,
exclude_team_ids=exclude_team_ids,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    team_ids: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    model: None | str | Unset = UNSET,
    api_key: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    exclude_team_ids: None | str | Unset = UNSET,

) -> HTTPValidationError | SpendAnalyticsPaginatedResponse | None:
    """ Get Team Daily Activity

     Get daily activity for specific teams or all teams.

    Args:
        team_ids (Optional[str]): Comma-separated list of team IDs to filter by. If not provided,
    returns data for all teams.
        start_date (Optional[str]): Start date for the activity period (YYYY-MM-DD).
        end_date (Optional[str]): End date for the activity period (YYYY-MM-DD).
        model (Optional[str]): Filter by model name.
        api_key (Optional[str]): Filter by API key.
        page (int): Page number for pagination.
        page_size (int): Number of items per page.
        exclude_team_ids (Optional[str]): Comma-separated list of team IDs to exclude.
    Returns:
        SpendAnalyticsPaginatedResponse: Paginated response containing daily activity data.

    Args:
        team_ids (None | str | Unset):
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        model (None | str | Unset):
        api_key (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 10.
        exclude_team_ids (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SpendAnalyticsPaginatedResponse
     """


    return sync_detailed(
        client=client,
team_ids=team_ids,
start_date=start_date,
end_date=end_date,
model=model,
api_key=api_key,
page=page,
page_size=page_size,
exclude_team_ids=exclude_team_ids,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    team_ids: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    model: None | str | Unset = UNSET,
    api_key: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    exclude_team_ids: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | SpendAnalyticsPaginatedResponse]:
    """ Get Team Daily Activity

     Get daily activity for specific teams or all teams.

    Args:
        team_ids (Optional[str]): Comma-separated list of team IDs to filter by. If not provided,
    returns data for all teams.
        start_date (Optional[str]): Start date for the activity period (YYYY-MM-DD).
        end_date (Optional[str]): End date for the activity period (YYYY-MM-DD).
        model (Optional[str]): Filter by model name.
        api_key (Optional[str]): Filter by API key.
        page (int): Page number for pagination.
        page_size (int): Number of items per page.
        exclude_team_ids (Optional[str]): Comma-separated list of team IDs to exclude.
    Returns:
        SpendAnalyticsPaginatedResponse: Paginated response containing daily activity data.

    Args:
        team_ids (None | str | Unset):
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        model (None | str | Unset):
        api_key (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 10.
        exclude_team_ids (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SpendAnalyticsPaginatedResponse]
     """


    kwargs = _get_kwargs(
        team_ids=team_ids,
start_date=start_date,
end_date=end_date,
model=model,
api_key=api_key,
page=page,
page_size=page_size,
exclude_team_ids=exclude_team_ids,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    team_ids: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    model: None | str | Unset = UNSET,
    api_key: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    exclude_team_ids: None | str | Unset = UNSET,

) -> HTTPValidationError | SpendAnalyticsPaginatedResponse | None:
    """ Get Team Daily Activity

     Get daily activity for specific teams or all teams.

    Args:
        team_ids (Optional[str]): Comma-separated list of team IDs to filter by. If not provided,
    returns data for all teams.
        start_date (Optional[str]): Start date for the activity period (YYYY-MM-DD).
        end_date (Optional[str]): End date for the activity period (YYYY-MM-DD).
        model (Optional[str]): Filter by model name.
        api_key (Optional[str]): Filter by API key.
        page (int): Page number for pagination.
        page_size (int): Number of items per page.
        exclude_team_ids (Optional[str]): Comma-separated list of team IDs to exclude.
    Returns:
        SpendAnalyticsPaginatedResponse: Paginated response containing daily activity data.

    Args:
        team_ids (None | str | Unset):
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        model (None | str | Unset):
        api_key (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 10.
        exclude_team_ids (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SpendAnalyticsPaginatedResponse
     """


    return (await asyncio_detailed(
        client=client,
team_ids=team_ids,
start_date=start_date,
end_date=end_date,
model=model,
api_key=api_key,
page=page,
page_size=page_size,
exclude_team_ids=exclude_team_ids,

    )).parsed
