from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.team_member_delete_request import TeamMemberDeleteRequest
from typing import cast



def _get_kwargs(
    *,
    body: TeamMemberDeleteRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/team/member_delete",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: TeamMemberDeleteRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Team Member Delete

     [BETA]

    delete members (either via user_email or user_id) from a team

    If user doesn't exist, an exception will be raised
    ```
    curl -X POST 'http://0.0.0.0:8000/team/member_delete'
    -H 'Authorization: Bearer sk-1234'
    -H 'Content-Type: application/json'
    -d '{
        \"team_id\": \"45e3e396-ee08-4a61-a88e-16b3ce7e0849\",
        \"user_id\": \"krrish247652@berri.ai\"
    }'
    ```

    Args:
        body (TeamMemberDeleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: TeamMemberDeleteRequest,

) -> Any | HTTPValidationError | None:
    r""" Team Member Delete

     [BETA]

    delete members (either via user_email or user_id) from a team

    If user doesn't exist, an exception will be raised
    ```
    curl -X POST 'http://0.0.0.0:8000/team/member_delete'
    -H 'Authorization: Bearer sk-1234'
    -H 'Content-Type: application/json'
    -d '{
        \"team_id\": \"45e3e396-ee08-4a61-a88e-16b3ce7e0849\",
        \"user_id\": \"krrish247652@berri.ai\"
    }'
    ```

    Args:
        body (TeamMemberDeleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TeamMemberDeleteRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Team Member Delete

     [BETA]

    delete members (either via user_email or user_id) from a team

    If user doesn't exist, an exception will be raised
    ```
    curl -X POST 'http://0.0.0.0:8000/team/member_delete'
    -H 'Authorization: Bearer sk-1234'
    -H 'Content-Type: application/json'
    -d '{
        \"team_id\": \"45e3e396-ee08-4a61-a88e-16b3ce7e0849\",
        \"user_id\": \"krrish247652@berri.ai\"
    }'
    ```

    Args:
        body (TeamMemberDeleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: TeamMemberDeleteRequest,

) -> Any | HTTPValidationError | None:
    r""" Team Member Delete

     [BETA]

    delete members (either via user_email or user_id) from a team

    If user doesn't exist, an exception will be raised
    ```
    curl -X POST 'http://0.0.0.0:8000/team/member_delete'
    -H 'Authorization: Bearer sk-1234'
    -H 'Content-Type: application/json'
    -d '{
        \"team_id\": \"45e3e396-ee08-4a61-a88e-16b3ce7e0849\",
        \"user_id\": \"krrish247652@berri.ai\"
    }'
    ```

    Args:
        body (TeamMemberDeleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
