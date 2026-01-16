from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.team_list_response import TeamListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    user_id: None | str | Unset = UNSET,
    organization_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    team_alias: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'asc',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_user_id: None | str | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    json_organization_id: None | str | Unset
    if isinstance(organization_id, Unset):
        json_organization_id = UNSET
    else:
        json_organization_id = organization_id
    params["organization_id"] = json_organization_id

    json_team_id: None | str | Unset
    if isinstance(team_id, Unset):
        json_team_id = UNSET
    else:
        json_team_id = team_id
    params["team_id"] = json_team_id

    json_team_alias: None | str | Unset
    if isinstance(team_alias, Unset):
        json_team_alias = UNSET
    else:
        json_team_alias = team_alias
    params["team_alias"] = json_team_alias

    params["page"] = page

    params["page_size"] = page_size

    json_sort_by: None | str | Unset
    if isinstance(sort_by, Unset):
        json_sort_by = UNSET
    else:
        json_sort_by = sort_by
    params["sort_by"] = json_sort_by

    params["sort_order"] = sort_order


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/team/list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | TeamListResponse | None:
    if response.status_code == 200:
        response_200 = TeamListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | TeamListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_id: None | str | Unset = UNSET,
    organization_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    team_alias: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'asc',

) -> Response[HTTPValidationError | TeamListResponse]:
    """ List Team V2

     Get a paginated list of teams with filtering and sorting options.

    Parameters:
        user_id: Optional[str]
            Only return teams which this user belongs to
        organization_id: Optional[str]
            Only return teams which belong to this organization
        team_id: Optional[str]
            Filter teams by exact team_id match
        team_alias: Optional[str]
            Filter teams by partial team_alias match
        page: int
            The page number to return
        page_size: int
            The number of items per page
        sort_by: Optional[str]
            Column to sort by (e.g. 'team_id', 'team_alias', 'created_at')
        sort_order: str
            Sort order ('asc' or 'desc')

    Args:
        user_id (None | str | Unset): Only return teams which this 'user_id' belongs to
        organization_id (None | str | Unset): Only return teams which this 'organization_id'
            belongs to
        team_id (None | str | Unset): Only return teams which this 'team_id' belongs to
        team_alias (None | str | Unset): Only return teams which this 'team_alias' belongs to.
            Supports partial matching.
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Number of teams per page Default: 10.
        sort_by (None | str | Unset): Column to sort by (e.g. 'team_id', 'team_alias',
            'created_at')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TeamListResponse]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
organization_id=organization_id,
team_id=team_id,
team_alias=team_alias,
page=page,
page_size=page_size,
sort_by=sort_by,
sort_order=sort_order,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    user_id: None | str | Unset = UNSET,
    organization_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    team_alias: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'asc',

) -> HTTPValidationError | TeamListResponse | None:
    """ List Team V2

     Get a paginated list of teams with filtering and sorting options.

    Parameters:
        user_id: Optional[str]
            Only return teams which this user belongs to
        organization_id: Optional[str]
            Only return teams which belong to this organization
        team_id: Optional[str]
            Filter teams by exact team_id match
        team_alias: Optional[str]
            Filter teams by partial team_alias match
        page: int
            The page number to return
        page_size: int
            The number of items per page
        sort_by: Optional[str]
            Column to sort by (e.g. 'team_id', 'team_alias', 'created_at')
        sort_order: str
            Sort order ('asc' or 'desc')

    Args:
        user_id (None | str | Unset): Only return teams which this 'user_id' belongs to
        organization_id (None | str | Unset): Only return teams which this 'organization_id'
            belongs to
        team_id (None | str | Unset): Only return teams which this 'team_id' belongs to
        team_alias (None | str | Unset): Only return teams which this 'team_alias' belongs to.
            Supports partial matching.
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Number of teams per page Default: 10.
        sort_by (None | str | Unset): Column to sort by (e.g. 'team_id', 'team_alias',
            'created_at')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TeamListResponse
     """


    return sync_detailed(
        client=client,
user_id=user_id,
organization_id=organization_id,
team_id=team_id,
team_alias=team_alias,
page=page,
page_size=page_size,
sort_by=sort_by,
sort_order=sort_order,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: None | str | Unset = UNSET,
    organization_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    team_alias: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'asc',

) -> Response[HTTPValidationError | TeamListResponse]:
    """ List Team V2

     Get a paginated list of teams with filtering and sorting options.

    Parameters:
        user_id: Optional[str]
            Only return teams which this user belongs to
        organization_id: Optional[str]
            Only return teams which belong to this organization
        team_id: Optional[str]
            Filter teams by exact team_id match
        team_alias: Optional[str]
            Filter teams by partial team_alias match
        page: int
            The page number to return
        page_size: int
            The number of items per page
        sort_by: Optional[str]
            Column to sort by (e.g. 'team_id', 'team_alias', 'created_at')
        sort_order: str
            Sort order ('asc' or 'desc')

    Args:
        user_id (None | str | Unset): Only return teams which this 'user_id' belongs to
        organization_id (None | str | Unset): Only return teams which this 'organization_id'
            belongs to
        team_id (None | str | Unset): Only return teams which this 'team_id' belongs to
        team_alias (None | str | Unset): Only return teams which this 'team_alias' belongs to.
            Supports partial matching.
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Number of teams per page Default: 10.
        sort_by (None | str | Unset): Column to sort by (e.g. 'team_id', 'team_alias',
            'created_at')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TeamListResponse]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
organization_id=organization_id,
team_id=team_id,
team_alias=team_alias,
page=page,
page_size=page_size,
sort_by=sort_by,
sort_order=sort_order,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: None | str | Unset = UNSET,
    organization_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    team_alias: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'asc',

) -> HTTPValidationError | TeamListResponse | None:
    """ List Team V2

     Get a paginated list of teams with filtering and sorting options.

    Parameters:
        user_id: Optional[str]
            Only return teams which this user belongs to
        organization_id: Optional[str]
            Only return teams which belong to this organization
        team_id: Optional[str]
            Filter teams by exact team_id match
        team_alias: Optional[str]
            Filter teams by partial team_alias match
        page: int
            The page number to return
        page_size: int
            The number of items per page
        sort_by: Optional[str]
            Column to sort by (e.g. 'team_id', 'team_alias', 'created_at')
        sort_order: str
            Sort order ('asc' or 'desc')

    Args:
        user_id (None | str | Unset): Only return teams which this 'user_id' belongs to
        organization_id (None | str | Unset): Only return teams which this 'organization_id'
            belongs to
        team_id (None | str | Unset): Only return teams which this 'team_id' belongs to
        team_alias (None | str | Unset): Only return teams which this 'team_alias' belongs to.
            Supports partial matching.
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Number of teams per page Default: 10.
        sort_by (None | str | Unset): Column to sort by (e.g. 'team_id', 'team_alias',
            'created_at')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TeamListResponse
     """


    return (await asyncio_detailed(
        client=client,
user_id=user_id,
organization_id=organization_id,
team_id=team_id,
team_alias=team_alias,
page=page,
page_size=page_size,
sort_by=sort_by,
sort_order=sort_order,

    )).parsed
