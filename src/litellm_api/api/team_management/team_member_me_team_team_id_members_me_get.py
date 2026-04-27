from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.team_member_info_response import TeamMemberInfoResponse
from typing import cast



def _get_kwargs(
    team_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/team/{team_id}/members/me".format(team_id=quote(str(team_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | TeamMemberInfoResponse | None:
    if response.status_code == 200:
        response_200 = TeamMemberInfoResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | TeamMemberInfoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[HTTPValidationError | TeamMemberInfoResponse]:
    """ Team Member Me

     Get the caller's own team-membership row for the given team.

    Used by internal users to view their own spend, budget, budget reset
    date, rate limits, and role within a team — without exposing other
    members' data. The caller is resolved from their API key; the path
    `/members/me` always refers to that caller.

    Returns 404 if the caller is not a member of the team.

    ```
    curl --location 'http://localhost:4000/team/your_team_id/members/me'     --header 'Authorization:
    Bearer your_api_key_here'
    ```

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TeamMemberInfoResponse]
     """


    kwargs = _get_kwargs(
        team_id=team_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    team_id: str,
    *,
    client: AuthenticatedClient,

) -> HTTPValidationError | TeamMemberInfoResponse | None:
    """ Team Member Me

     Get the caller's own team-membership row for the given team.

    Used by internal users to view their own spend, budget, budget reset
    date, rate limits, and role within a team — without exposing other
    members' data. The caller is resolved from their API key; the path
    `/members/me` always refers to that caller.

    Returns 404 if the caller is not a member of the team.

    ```
    curl --location 'http://localhost:4000/team/your_team_id/members/me'     --header 'Authorization:
    Bearer your_api_key_here'
    ```

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TeamMemberInfoResponse
     """


    return sync_detailed(
        team_id=team_id,
client=client,

    ).parsed

async def asyncio_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[HTTPValidationError | TeamMemberInfoResponse]:
    """ Team Member Me

     Get the caller's own team-membership row for the given team.

    Used by internal users to view their own spend, budget, budget reset
    date, rate limits, and role within a team — without exposing other
    members' data. The caller is resolved from their API key; the path
    `/members/me` always refers to that caller.

    Returns 404 if the caller is not a member of the team.

    ```
    curl --location 'http://localhost:4000/team/your_team_id/members/me'     --header 'Authorization:
    Bearer your_api_key_here'
    ```

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TeamMemberInfoResponse]
     """


    kwargs = _get_kwargs(
        team_id=team_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    team_id: str,
    *,
    client: AuthenticatedClient,

) -> HTTPValidationError | TeamMemberInfoResponse | None:
    """ Team Member Me

     Get the caller's own team-membership row for the given team.

    Used by internal users to view their own spend, budget, budget reset
    date, rate limits, and role within a team — without exposing other
    members' data. The caller is resolved from their API key; the path
    `/members/me` always refers to that caller.

    Returns 404 if the caller is not a member of the team.

    ```
    curl --location 'http://localhost:4000/team/your_team_id/members/me'     --header 'Authorization:
    Bearer your_api_key_here'
    ```

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TeamMemberInfoResponse
     """


    return (await asyncio_detailed(
        team_id=team_id,
client=client,

    )).parsed
