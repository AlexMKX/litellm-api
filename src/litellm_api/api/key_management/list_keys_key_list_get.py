from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.key_list_response_object import KeyListResponseObject
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    page: int | Unset = 1,
    size: int | Unset = 10,
    user_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    organization_id: None | str | Unset = UNSET,
    key_hash: None | str | Unset = UNSET,
    key_alias: None | str | Unset = UNSET,
    return_full_object: bool | Unset = False,
    include_team_keys: bool | Unset = False,
    include_created_by_keys: bool | Unset = False,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'desc',
    expand: list[str] | None | Unset = UNSET,
    status: None | str | Unset = UNSET,
    project_id: None | str | Unset = UNSET,
    access_group_id: None | str | Unset = UNSET,
    agent_id: None | str | Unset = UNSET,
    substring_matching: bool | Unset = False,
    expires: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["size"] = size

    json_user_id: None | str | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    json_team_id: None | str | Unset
    if isinstance(team_id, Unset):
        json_team_id = UNSET
    else:
        json_team_id = team_id
    params["team_id"] = json_team_id

    json_organization_id: None | str | Unset
    if isinstance(organization_id, Unset):
        json_organization_id = UNSET
    else:
        json_organization_id = organization_id
    params["organization_id"] = json_organization_id

    json_key_hash: None | str | Unset
    if isinstance(key_hash, Unset):
        json_key_hash = UNSET
    else:
        json_key_hash = key_hash
    params["key_hash"] = json_key_hash

    json_key_alias: None | str | Unset
    if isinstance(key_alias, Unset):
        json_key_alias = UNSET
    else:
        json_key_alias = key_alias
    params["key_alias"] = json_key_alias

    params["return_full_object"] = return_full_object

    params["include_team_keys"] = include_team_keys

    params["include_created_by_keys"] = include_created_by_keys

    json_sort_by: None | str | Unset
    if isinstance(sort_by, Unset):
        json_sort_by = UNSET
    else:
        json_sort_by = sort_by
    params["sort_by"] = json_sort_by

    params["sort_order"] = sort_order

    json_expand: list[str] | None | Unset
    if isinstance(expand, Unset):
        json_expand = UNSET
    elif isinstance(expand, list):
        json_expand = expand


    else:
        json_expand = expand
    params["expand"] = json_expand

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_project_id: None | str | Unset
    if isinstance(project_id, Unset):
        json_project_id = UNSET
    else:
        json_project_id = project_id
    params["project_id"] = json_project_id

    json_access_group_id: None | str | Unset
    if isinstance(access_group_id, Unset):
        json_access_group_id = UNSET
    else:
        json_access_group_id = access_group_id
    params["access_group_id"] = json_access_group_id

    json_agent_id: None | str | Unset
    if isinstance(agent_id, Unset):
        json_agent_id = UNSET
    else:
        json_agent_id = agent_id
    params["agent_id"] = json_agent_id

    params["substring_matching"] = substring_matching

    json_expires: None | str | Unset
    if isinstance(expires, Unset):
        json_expires = UNSET
    else:
        json_expires = expires
    params["expires"] = json_expires


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/key/list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | KeyListResponseObject | None:
    if response.status_code == 200:
        response_200 = KeyListResponseObject.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | KeyListResponseObject]:
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
    size: int | Unset = 10,
    user_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    organization_id: None | str | Unset = UNSET,
    key_hash: None | str | Unset = UNSET,
    key_alias: None | str | Unset = UNSET,
    return_full_object: bool | Unset = False,
    include_team_keys: bool | Unset = False,
    include_created_by_keys: bool | Unset = False,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'desc',
    expand: list[str] | None | Unset = UNSET,
    status: None | str | Unset = UNSET,
    project_id: None | str | Unset = UNSET,
    access_group_id: None | str | Unset = UNSET,
    agent_id: None | str | Unset = UNSET,
    substring_matching: bool | Unset = False,
    expires: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | KeyListResponseObject]:
    r""" List Keys

     List all keys for a given user / team / organization.

    Parameters:
        expand: Optional[List[str]] - Expand related objects (e.g. 'user' to include user information)
        status: Optional[str] - Filter by status. Currently supports \"deleted\" to query deleted keys.

    Returns:
        {
            \"keys\": List[str] or List[UserAPIKeyAuth],
            \"total_count\": int,
            \"current_page\": int,
            \"total_pages\": int,
        }

    When expand includes \"user\", each key object will include a \"user\" field with the associated
    user object.
    Note: When expand=user is specified, full key objects are returned regardless of the
    return_full_object parameter.

    Args:
        page (int | Unset): Page number Default: 1.
        size (int | Unset): Page size Default: 10.
        user_id (None | str | Unset): Filter keys by user ID. Exact match by default; set
            substring_matching=true (admin only) for case-insensitive substring matching.
        team_id (None | str | Unset): Filter keys by team ID
        organization_id (None | str | Unset): Filter keys by organization ID
        key_hash (None | str | Unset): Filter keys by key hash
        key_alias (None | str | Unset): Filter keys by key alias. Exact match by default; set
            substring_matching=true (admin only) for case-insensitive substring matching.
        return_full_object (bool | Unset): Return full key object Default: False.
        include_team_keys (bool | Unset): Include all keys for teams that user is an admin of.
            Default: False.
        include_created_by_keys (bool | Unset): Include keys created by the user Default: False.
        sort_by (None | str | Unset): Column to sort by (e.g. 'user_id', 'created_at', 'spend')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'desc'.
        expand (list[str] | None | Unset): Expand related objects (e.g. 'user')
        status (None | str | Unset): Filter by status (e.g. 'deleted')
        project_id (None | str | Unset): Filter keys by project ID
        access_group_id (None | str | Unset): Filter keys by access group ID
        agent_id (None | str | Unset): Filter keys by agent ID
        substring_matching (bool | Unset): If true (proxy admins only), match user_id/key_alias as
            case-insensitive substrings instead of exact values. Defaults to false: /key/list matched
            these exactly before substring search was added, and an exact user_id/key_alias filter
            must never return another user's keys. Default: False.
        expires (None | str | Unset): Filter keys by expiration. 'expired' returns keys whose
            expires is in the past; 'active' returns keys that never expire or expire in the future.
            Omit to return keys regardless of expiration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | KeyListResponseObject]
     """


    kwargs = _get_kwargs(
        page=page,
size=size,
user_id=user_id,
team_id=team_id,
organization_id=organization_id,
key_hash=key_hash,
key_alias=key_alias,
return_full_object=return_full_object,
include_team_keys=include_team_keys,
include_created_by_keys=include_created_by_keys,
sort_by=sort_by,
sort_order=sort_order,
expand=expand,
status=status,
project_id=project_id,
access_group_id=access_group_id,
agent_id=agent_id,
substring_matching=substring_matching,
expires=expires,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    size: int | Unset = 10,
    user_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    organization_id: None | str | Unset = UNSET,
    key_hash: None | str | Unset = UNSET,
    key_alias: None | str | Unset = UNSET,
    return_full_object: bool | Unset = False,
    include_team_keys: bool | Unset = False,
    include_created_by_keys: bool | Unset = False,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'desc',
    expand: list[str] | None | Unset = UNSET,
    status: None | str | Unset = UNSET,
    project_id: None | str | Unset = UNSET,
    access_group_id: None | str | Unset = UNSET,
    agent_id: None | str | Unset = UNSET,
    substring_matching: bool | Unset = False,
    expires: None | str | Unset = UNSET,

) -> HTTPValidationError | KeyListResponseObject | None:
    r""" List Keys

     List all keys for a given user / team / organization.

    Parameters:
        expand: Optional[List[str]] - Expand related objects (e.g. 'user' to include user information)
        status: Optional[str] - Filter by status. Currently supports \"deleted\" to query deleted keys.

    Returns:
        {
            \"keys\": List[str] or List[UserAPIKeyAuth],
            \"total_count\": int,
            \"current_page\": int,
            \"total_pages\": int,
        }

    When expand includes \"user\", each key object will include a \"user\" field with the associated
    user object.
    Note: When expand=user is specified, full key objects are returned regardless of the
    return_full_object parameter.

    Args:
        page (int | Unset): Page number Default: 1.
        size (int | Unset): Page size Default: 10.
        user_id (None | str | Unset): Filter keys by user ID. Exact match by default; set
            substring_matching=true (admin only) for case-insensitive substring matching.
        team_id (None | str | Unset): Filter keys by team ID
        organization_id (None | str | Unset): Filter keys by organization ID
        key_hash (None | str | Unset): Filter keys by key hash
        key_alias (None | str | Unset): Filter keys by key alias. Exact match by default; set
            substring_matching=true (admin only) for case-insensitive substring matching.
        return_full_object (bool | Unset): Return full key object Default: False.
        include_team_keys (bool | Unset): Include all keys for teams that user is an admin of.
            Default: False.
        include_created_by_keys (bool | Unset): Include keys created by the user Default: False.
        sort_by (None | str | Unset): Column to sort by (e.g. 'user_id', 'created_at', 'spend')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'desc'.
        expand (list[str] | None | Unset): Expand related objects (e.g. 'user')
        status (None | str | Unset): Filter by status (e.g. 'deleted')
        project_id (None | str | Unset): Filter keys by project ID
        access_group_id (None | str | Unset): Filter keys by access group ID
        agent_id (None | str | Unset): Filter keys by agent ID
        substring_matching (bool | Unset): If true (proxy admins only), match user_id/key_alias as
            case-insensitive substrings instead of exact values. Defaults to false: /key/list matched
            these exactly before substring search was added, and an exact user_id/key_alias filter
            must never return another user's keys. Default: False.
        expires (None | str | Unset): Filter keys by expiration. 'expired' returns keys whose
            expires is in the past; 'active' returns keys that never expire or expire in the future.
            Omit to return keys regardless of expiration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | KeyListResponseObject
     """


    return sync_detailed(
        client=client,
page=page,
size=size,
user_id=user_id,
team_id=team_id,
organization_id=organization_id,
key_hash=key_hash,
key_alias=key_alias,
return_full_object=return_full_object,
include_team_keys=include_team_keys,
include_created_by_keys=include_created_by_keys,
sort_by=sort_by,
sort_order=sort_order,
expand=expand,
status=status,
project_id=project_id,
access_group_id=access_group_id,
agent_id=agent_id,
substring_matching=substring_matching,
expires=expires,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    size: int | Unset = 10,
    user_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    organization_id: None | str | Unset = UNSET,
    key_hash: None | str | Unset = UNSET,
    key_alias: None | str | Unset = UNSET,
    return_full_object: bool | Unset = False,
    include_team_keys: bool | Unset = False,
    include_created_by_keys: bool | Unset = False,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'desc',
    expand: list[str] | None | Unset = UNSET,
    status: None | str | Unset = UNSET,
    project_id: None | str | Unset = UNSET,
    access_group_id: None | str | Unset = UNSET,
    agent_id: None | str | Unset = UNSET,
    substring_matching: bool | Unset = False,
    expires: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | KeyListResponseObject]:
    r""" List Keys

     List all keys for a given user / team / organization.

    Parameters:
        expand: Optional[List[str]] - Expand related objects (e.g. 'user' to include user information)
        status: Optional[str] - Filter by status. Currently supports \"deleted\" to query deleted keys.

    Returns:
        {
            \"keys\": List[str] or List[UserAPIKeyAuth],
            \"total_count\": int,
            \"current_page\": int,
            \"total_pages\": int,
        }

    When expand includes \"user\", each key object will include a \"user\" field with the associated
    user object.
    Note: When expand=user is specified, full key objects are returned regardless of the
    return_full_object parameter.

    Args:
        page (int | Unset): Page number Default: 1.
        size (int | Unset): Page size Default: 10.
        user_id (None | str | Unset): Filter keys by user ID. Exact match by default; set
            substring_matching=true (admin only) for case-insensitive substring matching.
        team_id (None | str | Unset): Filter keys by team ID
        organization_id (None | str | Unset): Filter keys by organization ID
        key_hash (None | str | Unset): Filter keys by key hash
        key_alias (None | str | Unset): Filter keys by key alias. Exact match by default; set
            substring_matching=true (admin only) for case-insensitive substring matching.
        return_full_object (bool | Unset): Return full key object Default: False.
        include_team_keys (bool | Unset): Include all keys for teams that user is an admin of.
            Default: False.
        include_created_by_keys (bool | Unset): Include keys created by the user Default: False.
        sort_by (None | str | Unset): Column to sort by (e.g. 'user_id', 'created_at', 'spend')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'desc'.
        expand (list[str] | None | Unset): Expand related objects (e.g. 'user')
        status (None | str | Unset): Filter by status (e.g. 'deleted')
        project_id (None | str | Unset): Filter keys by project ID
        access_group_id (None | str | Unset): Filter keys by access group ID
        agent_id (None | str | Unset): Filter keys by agent ID
        substring_matching (bool | Unset): If true (proxy admins only), match user_id/key_alias as
            case-insensitive substrings instead of exact values. Defaults to false: /key/list matched
            these exactly before substring search was added, and an exact user_id/key_alias filter
            must never return another user's keys. Default: False.
        expires (None | str | Unset): Filter keys by expiration. 'expired' returns keys whose
            expires is in the past; 'active' returns keys that never expire or expire in the future.
            Omit to return keys regardless of expiration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | KeyListResponseObject]
     """


    kwargs = _get_kwargs(
        page=page,
size=size,
user_id=user_id,
team_id=team_id,
organization_id=organization_id,
key_hash=key_hash,
key_alias=key_alias,
return_full_object=return_full_object,
include_team_keys=include_team_keys,
include_created_by_keys=include_created_by_keys,
sort_by=sort_by,
sort_order=sort_order,
expand=expand,
status=status,
project_id=project_id,
access_group_id=access_group_id,
agent_id=agent_id,
substring_matching=substring_matching,
expires=expires,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    size: int | Unset = 10,
    user_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    organization_id: None | str | Unset = UNSET,
    key_hash: None | str | Unset = UNSET,
    key_alias: None | str | Unset = UNSET,
    return_full_object: bool | Unset = False,
    include_team_keys: bool | Unset = False,
    include_created_by_keys: bool | Unset = False,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'desc',
    expand: list[str] | None | Unset = UNSET,
    status: None | str | Unset = UNSET,
    project_id: None | str | Unset = UNSET,
    access_group_id: None | str | Unset = UNSET,
    agent_id: None | str | Unset = UNSET,
    substring_matching: bool | Unset = False,
    expires: None | str | Unset = UNSET,

) -> HTTPValidationError | KeyListResponseObject | None:
    r""" List Keys

     List all keys for a given user / team / organization.

    Parameters:
        expand: Optional[List[str]] - Expand related objects (e.g. 'user' to include user information)
        status: Optional[str] - Filter by status. Currently supports \"deleted\" to query deleted keys.

    Returns:
        {
            \"keys\": List[str] or List[UserAPIKeyAuth],
            \"total_count\": int,
            \"current_page\": int,
            \"total_pages\": int,
        }

    When expand includes \"user\", each key object will include a \"user\" field with the associated
    user object.
    Note: When expand=user is specified, full key objects are returned regardless of the
    return_full_object parameter.

    Args:
        page (int | Unset): Page number Default: 1.
        size (int | Unset): Page size Default: 10.
        user_id (None | str | Unset): Filter keys by user ID. Exact match by default; set
            substring_matching=true (admin only) for case-insensitive substring matching.
        team_id (None | str | Unset): Filter keys by team ID
        organization_id (None | str | Unset): Filter keys by organization ID
        key_hash (None | str | Unset): Filter keys by key hash
        key_alias (None | str | Unset): Filter keys by key alias. Exact match by default; set
            substring_matching=true (admin only) for case-insensitive substring matching.
        return_full_object (bool | Unset): Return full key object Default: False.
        include_team_keys (bool | Unset): Include all keys for teams that user is an admin of.
            Default: False.
        include_created_by_keys (bool | Unset): Include keys created by the user Default: False.
        sort_by (None | str | Unset): Column to sort by (e.g. 'user_id', 'created_at', 'spend')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'desc'.
        expand (list[str] | None | Unset): Expand related objects (e.g. 'user')
        status (None | str | Unset): Filter by status (e.g. 'deleted')
        project_id (None | str | Unset): Filter keys by project ID
        access_group_id (None | str | Unset): Filter keys by access group ID
        agent_id (None | str | Unset): Filter keys by agent ID
        substring_matching (bool | Unset): If true (proxy admins only), match user_id/key_alias as
            case-insensitive substrings instead of exact values. Defaults to false: /key/list matched
            these exactly before substring search was added, and an exact user_id/key_alias filter
            must never return another user's keys. Default: False.
        expires (None | str | Unset): Filter keys by expiration. 'expired' returns keys whose
            expires is in the past; 'active' returns keys that never expire or expire in the future.
            Omit to return keys regardless of expiration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | KeyListResponseObject
     """


    return (await asyncio_detailed(
        client=client,
page=page,
size=size,
user_id=user_id,
team_id=team_id,
organization_id=organization_id,
key_hash=key_hash,
key_alias=key_alias,
return_full_object=return_full_object,
include_team_keys=include_team_keys,
include_created_by_keys=include_created_by_keys,
sort_by=sort_by,
sort_order=sort_order,
expand=expand,
status=status,
project_id=project_id,
access_group_id=access_group_id,
agent_id=agent_id,
substring_matching=substring_matching,
expires=expires,

    )).parsed
