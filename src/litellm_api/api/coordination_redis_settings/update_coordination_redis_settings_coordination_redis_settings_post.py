from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.coordination_redis_settings_request import CoordinationRedisSettingsRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.update_coordination_redis_settings_coordination_redis_settings_post_response_update_coordination_redis_settings_coordination_redis_settings_post import UpdateCoordinationRedisSettingsCoordinationRedisSettingsPostResponseUpdateCoordinationRedisSettingsCoordinationRedisSettingsPost
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: CoordinationRedisSettingsRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(litellm_changed_by, Unset):
        headers["litellm-changed-by"] = litellm_changed_by



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/coordination_redis/settings",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | UpdateCoordinationRedisSettingsCoordinationRedisSettingsPostResponseUpdateCoordinationRedisSettingsCoordinationRedisSettingsPost | None:
    if response.status_code == 200:
        response_200 = UpdateCoordinationRedisSettingsCoordinationRedisSettingsPostResponseUpdateCoordinationRedisSettingsCoordinationRedisSettingsPost.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | UpdateCoordinationRedisSettingsCoordinationRedisSettingsPostResponseUpdateCoordinationRedisSettingsCoordinationRedisSettingsPost]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CoordinationRedisSettingsRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | UpdateCoordinationRedisSettingsCoordinationRedisSettingsPostResponseUpdateCoordinationRedisSettingsCoordinationRedisSettingsPost]:
    """ Update Coordination Redis Settings

     Save coordination Redis settings under `general_settings.coordination_redis`.

    Parameters:
    - settings: dict - Redis connection params (host, port, username, password, url, ssl, startup_nodes,
    sentinel_nodes, sentinel_password, service_name). Values may be `os.environ/VAR` references, which
    are stored as written and resolved at startup

    The settings are written to the `general_settings` row of LiteLLM_Config,
    which startup merges over the yaml config; the proxy picks them up on its
    next restart.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (CoordinationRedisSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UpdateCoordinationRedisSettingsCoordinationRedisSettingsPostResponseUpdateCoordinationRedisSettingsCoordinationRedisSettingsPost]
     """


    kwargs = _get_kwargs(
        body=body,
litellm_changed_by=litellm_changed_by,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: CoordinationRedisSettingsRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> HTTPValidationError | UpdateCoordinationRedisSettingsCoordinationRedisSettingsPostResponseUpdateCoordinationRedisSettingsCoordinationRedisSettingsPost | None:
    """ Update Coordination Redis Settings

     Save coordination Redis settings under `general_settings.coordination_redis`.

    Parameters:
    - settings: dict - Redis connection params (host, port, username, password, url, ssl, startup_nodes,
    sentinel_nodes, sentinel_password, service_name). Values may be `os.environ/VAR` references, which
    are stored as written and resolved at startup

    The settings are written to the `general_settings` row of LiteLLM_Config,
    which startup merges over the yaml config; the proxy picks them up on its
    next restart.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (CoordinationRedisSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UpdateCoordinationRedisSettingsCoordinationRedisSettingsPostResponseUpdateCoordinationRedisSettingsCoordinationRedisSettingsPost
     """


    return sync_detailed(
        client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CoordinationRedisSettingsRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | UpdateCoordinationRedisSettingsCoordinationRedisSettingsPostResponseUpdateCoordinationRedisSettingsCoordinationRedisSettingsPost]:
    """ Update Coordination Redis Settings

     Save coordination Redis settings under `general_settings.coordination_redis`.

    Parameters:
    - settings: dict - Redis connection params (host, port, username, password, url, ssl, startup_nodes,
    sentinel_nodes, sentinel_password, service_name). Values may be `os.environ/VAR` references, which
    are stored as written and resolved at startup

    The settings are written to the `general_settings` row of LiteLLM_Config,
    which startup merges over the yaml config; the proxy picks them up on its
    next restart.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (CoordinationRedisSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UpdateCoordinationRedisSettingsCoordinationRedisSettingsPostResponseUpdateCoordinationRedisSettingsCoordinationRedisSettingsPost]
     """


    kwargs = _get_kwargs(
        body=body,
litellm_changed_by=litellm_changed_by,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CoordinationRedisSettingsRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> HTTPValidationError | UpdateCoordinationRedisSettingsCoordinationRedisSettingsPostResponseUpdateCoordinationRedisSettingsCoordinationRedisSettingsPost | None:
    """ Update Coordination Redis Settings

     Save coordination Redis settings under `general_settings.coordination_redis`.

    Parameters:
    - settings: dict - Redis connection params (host, port, username, password, url, ssl, startup_nodes,
    sentinel_nodes, sentinel_password, service_name). Values may be `os.environ/VAR` references, which
    are stored as written and resolved at startup

    The settings are written to the `general_settings` row of LiteLLM_Config,
    which startup merges over the yaml config; the proxy picks them up on its
    next restart.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (CoordinationRedisSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UpdateCoordinationRedisSettingsCoordinationRedisSettingsPostResponseUpdateCoordinationRedisSettingsCoordinationRedisSettingsPost
     """


    return (await asyncio_detailed(
        client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    )).parsed
