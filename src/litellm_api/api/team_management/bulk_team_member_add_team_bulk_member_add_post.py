from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulk_team_member_add_request import BulkTeamMemberAddRequest
from ...models.bulk_team_member_add_response import BulkTeamMemberAddResponse
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    *,
    body: BulkTeamMemberAddRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/team/bulk_member_add",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BulkTeamMemberAddResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BulkTeamMemberAddResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BulkTeamMemberAddResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkTeamMemberAddRequest,

) -> Response[BulkTeamMemberAddResponse | HTTPValidationError]:
    r""" Bulk Team Member Add

     Bulk add multiple members to a team at once.

    This endpoint reuses the same logic as /team/member_add but provides a bulk-friendly response
    format.

    Parameters:
    - team_id: str - The ID of the team to add members to
    - members: List[Member] - List of members to add to the team
    - all_users: Optional[bool] - Flag to add all users on Proxy to the team
    - max_budget_in_team: Optional[float] - Maximum budget allocated to each user within the team

    Returns:
    - results: List of individual member addition results
    - total_requested: Total number of members requested for addition
    - successful_additions: Number of successful additions
    - failed_additions: Number of failed additions
    - updated_team: The updated team object

    Example request:
    ```bash
    curl --location 'http://0.0.0.0:4000/team/bulk_member_add'     --header 'Authorization: Bearer
    sk-1234'     --header 'Content-Type: application/json'     --data '{
        \"team_id\": \"team-1234\",
        \"members\": [
            {
                \"user_id\": \"user1\",
                \"role\": \"user\"
            },
            {
                \"user_email\": \"user2@example.com\",
                \"role\": \"admin\"
            }
        ],
        \"max_budget_in_team\": 100.0
    }'
    ```

    Args:
        body (BulkTeamMemberAddRequest): Request for bulk team member addition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkTeamMemberAddResponse | HTTPValidationError]
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
    body: BulkTeamMemberAddRequest,

) -> BulkTeamMemberAddResponse | HTTPValidationError | None:
    r""" Bulk Team Member Add

     Bulk add multiple members to a team at once.

    This endpoint reuses the same logic as /team/member_add but provides a bulk-friendly response
    format.

    Parameters:
    - team_id: str - The ID of the team to add members to
    - members: List[Member] - List of members to add to the team
    - all_users: Optional[bool] - Flag to add all users on Proxy to the team
    - max_budget_in_team: Optional[float] - Maximum budget allocated to each user within the team

    Returns:
    - results: List of individual member addition results
    - total_requested: Total number of members requested for addition
    - successful_additions: Number of successful additions
    - failed_additions: Number of failed additions
    - updated_team: The updated team object

    Example request:
    ```bash
    curl --location 'http://0.0.0.0:4000/team/bulk_member_add'     --header 'Authorization: Bearer
    sk-1234'     --header 'Content-Type: application/json'     --data '{
        \"team_id\": \"team-1234\",
        \"members\": [
            {
                \"user_id\": \"user1\",
                \"role\": \"user\"
            },
            {
                \"user_email\": \"user2@example.com\",
                \"role\": \"admin\"
            }
        ],
        \"max_budget_in_team\": 100.0
    }'
    ```

    Args:
        body (BulkTeamMemberAddRequest): Request for bulk team member addition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkTeamMemberAddResponse | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkTeamMemberAddRequest,

) -> Response[BulkTeamMemberAddResponse | HTTPValidationError]:
    r""" Bulk Team Member Add

     Bulk add multiple members to a team at once.

    This endpoint reuses the same logic as /team/member_add but provides a bulk-friendly response
    format.

    Parameters:
    - team_id: str - The ID of the team to add members to
    - members: List[Member] - List of members to add to the team
    - all_users: Optional[bool] - Flag to add all users on Proxy to the team
    - max_budget_in_team: Optional[float] - Maximum budget allocated to each user within the team

    Returns:
    - results: List of individual member addition results
    - total_requested: Total number of members requested for addition
    - successful_additions: Number of successful additions
    - failed_additions: Number of failed additions
    - updated_team: The updated team object

    Example request:
    ```bash
    curl --location 'http://0.0.0.0:4000/team/bulk_member_add'     --header 'Authorization: Bearer
    sk-1234'     --header 'Content-Type: application/json'     --data '{
        \"team_id\": \"team-1234\",
        \"members\": [
            {
                \"user_id\": \"user1\",
                \"role\": \"user\"
            },
            {
                \"user_email\": \"user2@example.com\",
                \"role\": \"admin\"
            }
        ],
        \"max_budget_in_team\": 100.0
    }'
    ```

    Args:
        body (BulkTeamMemberAddRequest): Request for bulk team member addition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkTeamMemberAddResponse | HTTPValidationError]
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
    body: BulkTeamMemberAddRequest,

) -> BulkTeamMemberAddResponse | HTTPValidationError | None:
    r""" Bulk Team Member Add

     Bulk add multiple members to a team at once.

    This endpoint reuses the same logic as /team/member_add but provides a bulk-friendly response
    format.

    Parameters:
    - team_id: str - The ID of the team to add members to
    - members: List[Member] - List of members to add to the team
    - all_users: Optional[bool] - Flag to add all users on Proxy to the team
    - max_budget_in_team: Optional[float] - Maximum budget allocated to each user within the team

    Returns:
    - results: List of individual member addition results
    - total_requested: Total number of members requested for addition
    - successful_additions: Number of successful additions
    - failed_additions: Number of failed additions
    - updated_team: The updated team object

    Example request:
    ```bash
    curl --location 'http://0.0.0.0:4000/team/bulk_member_add'     --header 'Authorization: Bearer
    sk-1234'     --header 'Content-Type: application/json'     --data '{
        \"team_id\": \"team-1234\",
        \"members\": [
            {
                \"user_id\": \"user1\",
                \"role\": \"user\"
            },
            {
                \"user_email\": \"user2@example.com\",
                \"role\": \"admin\"
            }
        ],
        \"max_budget_in_team\": 100.0
    }'
    ```

    Args:
        body (BulkTeamMemberAddRequest): Request for bulk team member addition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkTeamMemberAddResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
