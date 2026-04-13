from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulk_update_team_member_permissions_request import BulkUpdateTeamMemberPermissionsRequest
from ...models.bulk_update_team_member_permissions_response import BulkUpdateTeamMemberPermissionsResponse
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    *,
    body: BulkUpdateTeamMemberPermissionsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/team/permissions_bulk_update",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BulkUpdateTeamMemberPermissionsResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BulkUpdateTeamMemberPermissionsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BulkUpdateTeamMemberPermissionsResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkUpdateTeamMemberPermissionsRequest,

) -> Response[BulkUpdateTeamMemberPermissionsResponse | HTTPValidationError]:
    """ Bulk Update Team Member Permissions

     Append permissions to existing teams.

    Either pass team_ids to target specific teams, or set
    apply_to_all_teams=True to update every team. For each team,
    the provided permissions are merged with the team's existing
    permissions (duplicates are skipped).

    Args:
        body (BulkUpdateTeamMemberPermissionsRequest): Request to bulk-update team member
            permissions across teams.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkUpdateTeamMemberPermissionsResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: BulkUpdateTeamMemberPermissionsRequest,

) -> BulkUpdateTeamMemberPermissionsResponse | HTTPValidationError | None:
    """ Bulk Update Team Member Permissions

     Append permissions to existing teams.

    Either pass team_ids to target specific teams, or set
    apply_to_all_teams=True to update every team. For each team,
    the provided permissions are merged with the team's existing
    permissions (duplicates are skipped).

    Args:
        body (BulkUpdateTeamMemberPermissionsRequest): Request to bulk-update team member
            permissions across teams.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkUpdateTeamMemberPermissionsResponse | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkUpdateTeamMemberPermissionsRequest,

) -> Response[BulkUpdateTeamMemberPermissionsResponse | HTTPValidationError]:
    """ Bulk Update Team Member Permissions

     Append permissions to existing teams.

    Either pass team_ids to target specific teams, or set
    apply_to_all_teams=True to update every team. For each team,
    the provided permissions are merged with the team's existing
    permissions (duplicates are skipped).

    Args:
        body (BulkUpdateTeamMemberPermissionsRequest): Request to bulk-update team member
            permissions across teams.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkUpdateTeamMemberPermissionsResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BulkUpdateTeamMemberPermissionsRequest,

) -> BulkUpdateTeamMemberPermissionsResponse | HTTPValidationError | None:
    """ Bulk Update Team Member Permissions

     Append permissions to existing teams.

    Either pass team_ids to target specific teams, or set
    apply_to_all_teams=True to update every team. For each team,
    the provided permissions are merged with the team's existing
    permissions (duplicates are skipped).

    Args:
        body (BulkUpdateTeamMemberPermissionsRequest): Request to bulk-update team member
            permissions across teams.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkUpdateTeamMemberPermissionsResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
