from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.key_aliases_key_aliases_get_response_key_aliases_key_aliases_get import KeyAliasesKeyAliasesGetResponseKeyAliasesKeyAliasesGet
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    page: int | Unset = 1,
    size: int | Unset = 50,
    search: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["size"] = size

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_team_id: None | str | Unset
    if isinstance(team_id, Unset):
        json_team_id = UNSET
    else:
        json_team_id = team_id
    params["team_id"] = json_team_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/key/aliases",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | KeyAliasesKeyAliasesGetResponseKeyAliasesKeyAliasesGet | None:
    if response.status_code == 200:
        response_200 = KeyAliasesKeyAliasesGetResponseKeyAliasesKeyAliasesGet.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | KeyAliasesKeyAliasesGetResponseKeyAliasesKeyAliasesGet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    size: int | Unset = 50,
    search: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | KeyAliasesKeyAliasesGetResponseKeyAliasesKeyAliasesGet]:
    r""" Key Aliases

     Lists key aliases with pagination and optional search.

    Non-admin users only see aliases for keys they own or keys belonging to
    their teams.

    Returns:
        {
            \"aliases\": List[str],
            \"total_count\": int,
            \"current_page\": int,
            \"total_pages\": int,
            \"size\": int,
        }

    Args:
        page (int | Unset): Page number Default: 1.
        size (int | Unset): Page size Default: 50.
        search (None | str | Unset): Search key aliases (case-insensitive partial match)
        team_id (None | str | Unset): Filter aliases to keys belonging to this team

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | KeyAliasesKeyAliasesGetResponseKeyAliasesKeyAliasesGet]
     """


    kwargs = _get_kwargs(
        page=page,
size=size,
search=search,
team_id=team_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    size: int | Unset = 50,
    search: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,

) -> HTTPValidationError | KeyAliasesKeyAliasesGetResponseKeyAliasesKeyAliasesGet | None:
    r""" Key Aliases

     Lists key aliases with pagination and optional search.

    Non-admin users only see aliases for keys they own or keys belonging to
    their teams.

    Returns:
        {
            \"aliases\": List[str],
            \"total_count\": int,
            \"current_page\": int,
            \"total_pages\": int,
            \"size\": int,
        }

    Args:
        page (int | Unset): Page number Default: 1.
        size (int | Unset): Page size Default: 50.
        search (None | str | Unset): Search key aliases (case-insensitive partial match)
        team_id (None | str | Unset): Filter aliases to keys belonging to this team

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | KeyAliasesKeyAliasesGetResponseKeyAliasesKeyAliasesGet
     """


    return sync_detailed(
        client=client,
page=page,
size=size,
search=search,
team_id=team_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    size: int | Unset = 50,
    search: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | KeyAliasesKeyAliasesGetResponseKeyAliasesKeyAliasesGet]:
    r""" Key Aliases

     Lists key aliases with pagination and optional search.

    Non-admin users only see aliases for keys they own or keys belonging to
    their teams.

    Returns:
        {
            \"aliases\": List[str],
            \"total_count\": int,
            \"current_page\": int,
            \"total_pages\": int,
            \"size\": int,
        }

    Args:
        page (int | Unset): Page number Default: 1.
        size (int | Unset): Page size Default: 50.
        search (None | str | Unset): Search key aliases (case-insensitive partial match)
        team_id (None | str | Unset): Filter aliases to keys belonging to this team

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | KeyAliasesKeyAliasesGetResponseKeyAliasesKeyAliasesGet]
     """


    kwargs = _get_kwargs(
        page=page,
size=size,
search=search,
team_id=team_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    size: int | Unset = 50,
    search: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,

) -> HTTPValidationError | KeyAliasesKeyAliasesGetResponseKeyAliasesKeyAliasesGet | None:
    r""" Key Aliases

     Lists key aliases with pagination and optional search.

    Non-admin users only see aliases for keys they own or keys belonging to
    their teams.

    Returns:
        {
            \"aliases\": List[str],
            \"total_count\": int,
            \"current_page\": int,
            \"total_pages\": int,
            \"size\": int,
        }

    Args:
        page (int | Unset): Page number Default: 1.
        size (int | Unset): Page size Default: 50.
        search (None | str | Unset): Search key aliases (case-insensitive partial match)
        team_id (None | str | Unset): Filter aliases to keys belonging to this team

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | KeyAliasesKeyAliasesGetResponseKeyAliasesKeyAliasesGet
     """


    return (await asyncio_detailed(
        client=client,
page=page,
size=size,
search=search,
team_id=team_id,

    )).parsed
