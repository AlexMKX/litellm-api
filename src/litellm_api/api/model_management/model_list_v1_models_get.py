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
    return_wildcard_routes: bool | None | Unset = False,
    team_id: None | str | Unset = UNSET,
    include_model_access_groups: bool | None | Unset = False,
    only_model_access_groups: bool | None | Unset = False,
    include_metadata: bool | None | Unset = False,
    fallback_type: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_return_wildcard_routes: bool | None | Unset
    if isinstance(return_wildcard_routes, Unset):
        json_return_wildcard_routes = UNSET
    else:
        json_return_wildcard_routes = return_wildcard_routes
    params["return_wildcard_routes"] = json_return_wildcard_routes

    json_team_id: None | str | Unset
    if isinstance(team_id, Unset):
        json_team_id = UNSET
    else:
        json_team_id = team_id
    params["team_id"] = json_team_id

    json_include_model_access_groups: bool | None | Unset
    if isinstance(include_model_access_groups, Unset):
        json_include_model_access_groups = UNSET
    else:
        json_include_model_access_groups = include_model_access_groups
    params["include_model_access_groups"] = json_include_model_access_groups

    json_only_model_access_groups: bool | None | Unset
    if isinstance(only_model_access_groups, Unset):
        json_only_model_access_groups = UNSET
    else:
        json_only_model_access_groups = only_model_access_groups
    params["only_model_access_groups"] = json_only_model_access_groups

    json_include_metadata: bool | None | Unset
    if isinstance(include_metadata, Unset):
        json_include_metadata = UNSET
    else:
        json_include_metadata = include_metadata
    params["include_metadata"] = json_include_metadata

    json_fallback_type: None | str | Unset
    if isinstance(fallback_type, Unset):
        json_fallback_type = UNSET
    else:
        json_fallback_type = fallback_type
    params["fallback_type"] = json_fallback_type

    json_scope: None | str | Unset
    if isinstance(scope, Unset):
        json_scope = UNSET
    else:
        json_scope = scope
    params["scope"] = json_scope


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/models",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    return_wildcard_routes: bool | None | Unset = False,
    team_id: None | str | Unset = UNSET,
    include_model_access_groups: bool | None | Unset = False,
    only_model_access_groups: bool | None | Unset = False,
    include_metadata: bool | None | Unset = False,
    fallback_type: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Model List

     Use `/model/info` - to get detailed model information, example - pricing, mode, etc.

    This is just for compatibility with openai projects like aider.

    Query Parameters:
    - include_metadata: Include additional metadata in the response with fallback information
    - fallback_type: Type of fallbacks to include (\"general\", \"context_window\", \"content_policy\")
                    Defaults to \"general\" when include_metadata=true
    - scope: Optional scope parameter. Currently only accepts \"expand\".
             When scope=expand is passed, proxy admins, team admins, and org admins
             will receive all proxy models as if they are a proxy admin.

    Args:
        return_wildcard_routes (bool | None | Unset):  Default: False.
        team_id (None | str | Unset):
        include_model_access_groups (bool | None | Unset):  Default: False.
        only_model_access_groups (bool | None | Unset):  Default: False.
        include_metadata (bool | None | Unset):  Default: False.
        fallback_type (None | str | Unset):
        scope (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        return_wildcard_routes=return_wildcard_routes,
team_id=team_id,
include_model_access_groups=include_model_access_groups,
only_model_access_groups=only_model_access_groups,
include_metadata=include_metadata,
fallback_type=fallback_type,
scope=scope,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    return_wildcard_routes: bool | None | Unset = False,
    team_id: None | str | Unset = UNSET,
    include_model_access_groups: bool | None | Unset = False,
    only_model_access_groups: bool | None | Unset = False,
    include_metadata: bool | None | Unset = False,
    fallback_type: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Model List

     Use `/model/info` - to get detailed model information, example - pricing, mode, etc.

    This is just for compatibility with openai projects like aider.

    Query Parameters:
    - include_metadata: Include additional metadata in the response with fallback information
    - fallback_type: Type of fallbacks to include (\"general\", \"context_window\", \"content_policy\")
                    Defaults to \"general\" when include_metadata=true
    - scope: Optional scope parameter. Currently only accepts \"expand\".
             When scope=expand is passed, proxy admins, team admins, and org admins
             will receive all proxy models as if they are a proxy admin.

    Args:
        return_wildcard_routes (bool | None | Unset):  Default: False.
        team_id (None | str | Unset):
        include_model_access_groups (bool | None | Unset):  Default: False.
        only_model_access_groups (bool | None | Unset):  Default: False.
        include_metadata (bool | None | Unset):  Default: False.
        fallback_type (None | str | Unset):
        scope (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
return_wildcard_routes=return_wildcard_routes,
team_id=team_id,
include_model_access_groups=include_model_access_groups,
only_model_access_groups=only_model_access_groups,
include_metadata=include_metadata,
fallback_type=fallback_type,
scope=scope,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    return_wildcard_routes: bool | None | Unset = False,
    team_id: None | str | Unset = UNSET,
    include_model_access_groups: bool | None | Unset = False,
    only_model_access_groups: bool | None | Unset = False,
    include_metadata: bool | None | Unset = False,
    fallback_type: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Model List

     Use `/model/info` - to get detailed model information, example - pricing, mode, etc.

    This is just for compatibility with openai projects like aider.

    Query Parameters:
    - include_metadata: Include additional metadata in the response with fallback information
    - fallback_type: Type of fallbacks to include (\"general\", \"context_window\", \"content_policy\")
                    Defaults to \"general\" when include_metadata=true
    - scope: Optional scope parameter. Currently only accepts \"expand\".
             When scope=expand is passed, proxy admins, team admins, and org admins
             will receive all proxy models as if they are a proxy admin.

    Args:
        return_wildcard_routes (bool | None | Unset):  Default: False.
        team_id (None | str | Unset):
        include_model_access_groups (bool | None | Unset):  Default: False.
        only_model_access_groups (bool | None | Unset):  Default: False.
        include_metadata (bool | None | Unset):  Default: False.
        fallback_type (None | str | Unset):
        scope (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        return_wildcard_routes=return_wildcard_routes,
team_id=team_id,
include_model_access_groups=include_model_access_groups,
only_model_access_groups=only_model_access_groups,
include_metadata=include_metadata,
fallback_type=fallback_type,
scope=scope,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    return_wildcard_routes: bool | None | Unset = False,
    team_id: None | str | Unset = UNSET,
    include_model_access_groups: bool | None | Unset = False,
    only_model_access_groups: bool | None | Unset = False,
    include_metadata: bool | None | Unset = False,
    fallback_type: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Model List

     Use `/model/info` - to get detailed model information, example - pricing, mode, etc.

    This is just for compatibility with openai projects like aider.

    Query Parameters:
    - include_metadata: Include additional metadata in the response with fallback information
    - fallback_type: Type of fallbacks to include (\"general\", \"context_window\", \"content_policy\")
                    Defaults to \"general\" when include_metadata=true
    - scope: Optional scope parameter. Currently only accepts \"expand\".
             When scope=expand is passed, proxy admins, team admins, and org admins
             will receive all proxy models as if they are a proxy admin.

    Args:
        return_wildcard_routes (bool | None | Unset):  Default: False.
        team_id (None | str | Unset):
        include_model_access_groups (bool | None | Unset):  Default: False.
        only_model_access_groups (bool | None | Unset):  Default: False.
        include_metadata (bool | None | Unset):  Default: False.
        fallback_type (None | str | Unset):
        scope (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
return_wildcard_routes=return_wildcard_routes,
team_id=team_id,
include_model_access_groups=include_model_access_groups,
only_model_access_groups=only_model_access_groups,
include_metadata=include_metadata,
fallback_type=fallback_type,
scope=scope,

    )).parsed
