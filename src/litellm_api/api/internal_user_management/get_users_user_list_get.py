from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    role: None | str | Unset = UNSET,
    user_ids: None | str | Unset = UNSET,
    sso_user_ids: None | str | Unset = UNSET,
    user_email: None | str | Unset = UNSET,
    team: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'asc',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_role: None | str | Unset
    if isinstance(role, Unset):
        json_role = UNSET
    else:
        json_role = role
    params["role"] = json_role

    json_user_ids: None | str | Unset
    if isinstance(user_ids, Unset):
        json_user_ids = UNSET
    else:
        json_user_ids = user_ids
    params["user_ids"] = json_user_ids

    json_sso_user_ids: None | str | Unset
    if isinstance(sso_user_ids, Unset):
        json_sso_user_ids = UNSET
    else:
        json_sso_user_ids = sso_user_ids
    params["sso_user_ids"] = json_sso_user_ids

    json_user_email: None | str | Unset
    if isinstance(user_email, Unset):
        json_user_email = UNSET
    else:
        json_user_email = user_email
    params["user_email"] = json_user_email

    json_team: None | str | Unset
    if isinstance(team, Unset):
        json_team = UNSET
    else:
        json_team = team
    params["team"] = json_team

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
        "url": "/user/list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | None:
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    role: None | str | Unset = UNSET,
    user_ids: None | str | Unset = UNSET,
    sso_user_ids: None | str | Unset = UNSET,
    user_email: None | str | Unset = UNSET,
    team: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'asc',

) -> Response[HTTPValidationError]:
    """ Get Users

     Get a paginated list of users with filtering and sorting options.

    Parameters:
        role: Optional[str]
            Filter users by role. Can be one of:
            - proxy_admin
            - proxy_admin_viewer
            - internal_user
            - internal_user_viewer
        user_ids: Optional[str]
            Get list of users by user_ids. Comma separated list of user_ids.
        sso_ids: Optional[str]
            Get list of users by sso_ids. Comma separated list of sso_ids.
        user_email: Optional[str]
            Filter users by partial email match
        team: Optional[str]
            Filter users by team id. Will match if user has this team in their teams array.
        page: int
            The page number to return
        page_size: int
            The number of items per page
        sort_by: Optional[str]
            Column to sort by (e.g. 'user_id', 'user_email', 'created_at', 'spend')
        sort_order: Optional[str]
            Sort order ('asc' or 'desc')

    Args:
        role (None | str | Unset): Filter users by role
        user_ids (None | str | Unset): Get list of users by user_ids
        sso_user_ids (None | str | Unset): Get list of users by sso_user_id
        user_email (None | str | Unset): Filter users by partial email match
        team (None | str | Unset): Filter users by team id
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Number of items per page Default: 25.
        sort_by (None | str | Unset): Column to sort by (e.g. 'user_id', 'user_email',
            'created_at', 'spend')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
     """


    kwargs = _get_kwargs(
        role=role,
user_ids=user_ids,
sso_user_ids=sso_user_ids,
user_email=user_email,
team=team,
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
    role: None | str | Unset = UNSET,
    user_ids: None | str | Unset = UNSET,
    sso_user_ids: None | str | Unset = UNSET,
    user_email: None | str | Unset = UNSET,
    team: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'asc',

) -> HTTPValidationError | None:
    """ Get Users

     Get a paginated list of users with filtering and sorting options.

    Parameters:
        role: Optional[str]
            Filter users by role. Can be one of:
            - proxy_admin
            - proxy_admin_viewer
            - internal_user
            - internal_user_viewer
        user_ids: Optional[str]
            Get list of users by user_ids. Comma separated list of user_ids.
        sso_ids: Optional[str]
            Get list of users by sso_ids. Comma separated list of sso_ids.
        user_email: Optional[str]
            Filter users by partial email match
        team: Optional[str]
            Filter users by team id. Will match if user has this team in their teams array.
        page: int
            The page number to return
        page_size: int
            The number of items per page
        sort_by: Optional[str]
            Column to sort by (e.g. 'user_id', 'user_email', 'created_at', 'spend')
        sort_order: Optional[str]
            Sort order ('asc' or 'desc')

    Args:
        role (None | str | Unset): Filter users by role
        user_ids (None | str | Unset): Get list of users by user_ids
        sso_user_ids (None | str | Unset): Get list of users by sso_user_id
        user_email (None | str | Unset): Filter users by partial email match
        team (None | str | Unset): Filter users by team id
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Number of items per page Default: 25.
        sort_by (None | str | Unset): Column to sort by (e.g. 'user_id', 'user_email',
            'created_at', 'spend')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
     """


    return sync_detailed(
        client=client,
role=role,
user_ids=user_ids,
sso_user_ids=sso_user_ids,
user_email=user_email,
team=team,
page=page,
page_size=page_size,
sort_by=sort_by,
sort_order=sort_order,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    role: None | str | Unset = UNSET,
    user_ids: None | str | Unset = UNSET,
    sso_user_ids: None | str | Unset = UNSET,
    user_email: None | str | Unset = UNSET,
    team: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'asc',

) -> Response[HTTPValidationError]:
    """ Get Users

     Get a paginated list of users with filtering and sorting options.

    Parameters:
        role: Optional[str]
            Filter users by role. Can be one of:
            - proxy_admin
            - proxy_admin_viewer
            - internal_user
            - internal_user_viewer
        user_ids: Optional[str]
            Get list of users by user_ids. Comma separated list of user_ids.
        sso_ids: Optional[str]
            Get list of users by sso_ids. Comma separated list of sso_ids.
        user_email: Optional[str]
            Filter users by partial email match
        team: Optional[str]
            Filter users by team id. Will match if user has this team in their teams array.
        page: int
            The page number to return
        page_size: int
            The number of items per page
        sort_by: Optional[str]
            Column to sort by (e.g. 'user_id', 'user_email', 'created_at', 'spend')
        sort_order: Optional[str]
            Sort order ('asc' or 'desc')

    Args:
        role (None | str | Unset): Filter users by role
        user_ids (None | str | Unset): Get list of users by user_ids
        sso_user_ids (None | str | Unset): Get list of users by sso_user_id
        user_email (None | str | Unset): Filter users by partial email match
        team (None | str | Unset): Filter users by team id
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Number of items per page Default: 25.
        sort_by (None | str | Unset): Column to sort by (e.g. 'user_id', 'user_email',
            'created_at', 'spend')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
     """


    kwargs = _get_kwargs(
        role=role,
user_ids=user_ids,
sso_user_ids=sso_user_ids,
user_email=user_email,
team=team,
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
    role: None | str | Unset = UNSET,
    user_ids: None | str | Unset = UNSET,
    sso_user_ids: None | str | Unset = UNSET,
    user_email: None | str | Unset = UNSET,
    team: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'asc',

) -> HTTPValidationError | None:
    """ Get Users

     Get a paginated list of users with filtering and sorting options.

    Parameters:
        role: Optional[str]
            Filter users by role. Can be one of:
            - proxy_admin
            - proxy_admin_viewer
            - internal_user
            - internal_user_viewer
        user_ids: Optional[str]
            Get list of users by user_ids. Comma separated list of user_ids.
        sso_ids: Optional[str]
            Get list of users by sso_ids. Comma separated list of sso_ids.
        user_email: Optional[str]
            Filter users by partial email match
        team: Optional[str]
            Filter users by team id. Will match if user has this team in their teams array.
        page: int
            The page number to return
        page_size: int
            The number of items per page
        sort_by: Optional[str]
            Column to sort by (e.g. 'user_id', 'user_email', 'created_at', 'spend')
        sort_order: Optional[str]
            Sort order ('asc' or 'desc')

    Args:
        role (None | str | Unset): Filter users by role
        user_ids (None | str | Unset): Get list of users by user_ids
        sso_user_ids (None | str | Unset): Get list of users by sso_user_id
        user_email (None | str | Unset): Filter users by partial email match
        team (None | str | Unset): Filter users by team id
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Number of items per page Default: 25.
        sort_by (None | str | Unset): Column to sort by (e.g. 'user_id', 'user_email',
            'created_at', 'spend')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
role=role,
user_ids=user_ids,
sso_user_ids=sso_user_ids,
user_email=user_email,
team=team,
page=page,
page_size=page_size,
sort_by=sort_by,
sort_order=sort_order,

    )).parsed
