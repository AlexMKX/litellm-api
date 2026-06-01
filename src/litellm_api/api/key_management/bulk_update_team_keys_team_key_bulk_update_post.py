from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulk_update_key_response import BulkUpdateKeyResponse
from ...models.bulk_update_team_keys_request import BulkUpdateTeamKeysRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: BulkUpdateTeamKeysRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(litellm_changed_by, Unset):
        headers["litellm-changed-by"] = litellm_changed_by



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/team/key/bulk_update",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BulkUpdateKeyResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BulkUpdateKeyResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BulkUpdateKeyResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkUpdateTeamKeysRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[BulkUpdateKeyResponse | HTTPValidationError]:
    """ Bulk Update Team Keys

     Apply one update payload to many keys inside a single team.

    Pass `team_id` plus either `key_ids` or `all_keys_in_team=True`. The
    `update_fields` payload is broadcast to every selected key. Per-key
    failures are returned in `failed_updates` rather than aborting the batch.

    Callable by proxy admins, or by team admins with `KEY_UPDATE` permission.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BulkUpdateTeamKeysRequest): Apply one update payload to many keys inside a team;
            provide either `key_ids` or `all_keys_in_team=True`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkUpdateKeyResponse | HTTPValidationError]
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
    body: BulkUpdateTeamKeysRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> BulkUpdateKeyResponse | HTTPValidationError | None:
    """ Bulk Update Team Keys

     Apply one update payload to many keys inside a single team.

    Pass `team_id` plus either `key_ids` or `all_keys_in_team=True`. The
    `update_fields` payload is broadcast to every selected key. Per-key
    failures are returned in `failed_updates` rather than aborting the batch.

    Callable by proxy admins, or by team admins with `KEY_UPDATE` permission.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BulkUpdateTeamKeysRequest): Apply one update payload to many keys inside a team;
            provide either `key_ids` or `all_keys_in_team=True`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkUpdateKeyResponse | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkUpdateTeamKeysRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[BulkUpdateKeyResponse | HTTPValidationError]:
    """ Bulk Update Team Keys

     Apply one update payload to many keys inside a single team.

    Pass `team_id` plus either `key_ids` or `all_keys_in_team=True`. The
    `update_fields` payload is broadcast to every selected key. Per-key
    failures are returned in `failed_updates` rather than aborting the batch.

    Callable by proxy admins, or by team admins with `KEY_UPDATE` permission.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BulkUpdateTeamKeysRequest): Apply one update payload to many keys inside a team;
            provide either `key_ids` or `all_keys_in_team=True`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkUpdateKeyResponse | HTTPValidationError]
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
    body: BulkUpdateTeamKeysRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> BulkUpdateKeyResponse | HTTPValidationError | None:
    """ Bulk Update Team Keys

     Apply one update payload to many keys inside a single team.

    Pass `team_id` plus either `key_ids` or `all_keys_in_team=True`. The
    `update_fields` payload is broadcast to every selected key. Per-key
    failures are returned in `failed_updates` rather than aborting the batch.

    Callable by proxy admins, or by team admins with `KEY_UPDATE` permission.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BulkUpdateTeamKeysRequest): Apply one update payload to many keys inside a team;
            provide either `key_ids` or `all_keys_in_team=True`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkUpdateKeyResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    )).parsed
