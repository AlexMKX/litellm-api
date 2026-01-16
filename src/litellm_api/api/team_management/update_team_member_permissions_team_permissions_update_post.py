from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llm_team_table import LiteLLMTeamTable
from ...models.update_team_member_permissions_request import UpdateTeamMemberPermissionsRequest
from typing import cast



def _get_kwargs(
    *,
    body: UpdateTeamMemberPermissionsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/team/permissions_update",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | LiteLLMTeamTable | None:
    if response.status_code == 200:
        response_200 = LiteLLMTeamTable.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | LiteLLMTeamTable]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateTeamMemberPermissionsRequest,

) -> Response[HTTPValidationError | LiteLLMTeamTable]:
    """ Update Team Member Permissions

     Update the team member permissions for a team

    Args:
        body (UpdateTeamMemberPermissionsRequest): Request to update the team member permissions
            for a team

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiteLLMTeamTable]
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
    body: UpdateTeamMemberPermissionsRequest,

) -> HTTPValidationError | LiteLLMTeamTable | None:
    """ Update Team Member Permissions

     Update the team member permissions for a team

    Args:
        body (UpdateTeamMemberPermissionsRequest): Request to update the team member permissions
            for a team

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiteLLMTeamTable
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateTeamMemberPermissionsRequest,

) -> Response[HTTPValidationError | LiteLLMTeamTable]:
    """ Update Team Member Permissions

     Update the team member permissions for a team

    Args:
        body (UpdateTeamMemberPermissionsRequest): Request to update the team member permissions
            for a team

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiteLLMTeamTable]
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
    body: UpdateTeamMemberPermissionsRequest,

) -> HTTPValidationError | LiteLLMTeamTable | None:
    """ Update Team Member Permissions

     Update the team member permissions for a team

    Args:
        body (UpdateTeamMemberPermissionsRequest): Request to update the team member permissions
            for a team

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiteLLMTeamTable
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
