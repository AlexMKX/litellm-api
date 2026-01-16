from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.organization_member_add_request import OrganizationMemberAddRequest
from typing import cast



def _get_kwargs(
    *,
    body: OrganizationMemberAddRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/organization/member_add",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | None:
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OrganizationMemberAddRequest,

) -> Response[HTTPValidationError]:
    r""" Organization Member Add

     [BETA]

    Add new members (either via user_email or user_id) to an organization

    If user doesn't exist, new user row will also be added to User Table

    Only proxy_admin or org_admin of organization, allowed to access this endpoint.

    # Parameters:

    - organization_id: str (required)
    - member: Union[List[Member], Member] (required)
        - role: Literal[LitellmUserRoles] (required)
        - user_id: Optional[str]
        - user_email: Optional[str]

    Note: Either user_id or user_email must be provided for each member.

    Example:
    ```
    curl -X POST 'http://0.0.0.0:4000/organization/member_add'     -H 'Authorization: Bearer sk-1234'
    -H 'Content-Type: application/json'     -d '{
        \"organization_id\": \"45e3e396-ee08-4a61-a88e-16b3ce7e0849\",
        \"member\": {
            \"role\": \"internal_user\",
            \"user_id\": \"krrish247652@berri.ai\"
        },
        \"max_budget_in_organization\": 100.0
    }'
    ```

    The following is executed in this function:

    1. Check if organization exists
    2. Creates a new Internal User if the user_id or user_email is not found in LiteLLM_UserTable
    3. Add Internal User to the `LiteLLM_OrganizationMembership` table

    Args:
        body (OrganizationMemberAddRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
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
    body: OrganizationMemberAddRequest,

) -> HTTPValidationError | None:
    r""" Organization Member Add

     [BETA]

    Add new members (either via user_email or user_id) to an organization

    If user doesn't exist, new user row will also be added to User Table

    Only proxy_admin or org_admin of organization, allowed to access this endpoint.

    # Parameters:

    - organization_id: str (required)
    - member: Union[List[Member], Member] (required)
        - role: Literal[LitellmUserRoles] (required)
        - user_id: Optional[str]
        - user_email: Optional[str]

    Note: Either user_id or user_email must be provided for each member.

    Example:
    ```
    curl -X POST 'http://0.0.0.0:4000/organization/member_add'     -H 'Authorization: Bearer sk-1234'
    -H 'Content-Type: application/json'     -d '{
        \"organization_id\": \"45e3e396-ee08-4a61-a88e-16b3ce7e0849\",
        \"member\": {
            \"role\": \"internal_user\",
            \"user_id\": \"krrish247652@berri.ai\"
        },
        \"max_budget_in_organization\": 100.0
    }'
    ```

    The following is executed in this function:

    1. Check if organization exists
    2. Creates a new Internal User if the user_id or user_email is not found in LiteLLM_UserTable
    3. Add Internal User to the `LiteLLM_OrganizationMembership` table

    Args:
        body (OrganizationMemberAddRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OrganizationMemberAddRequest,

) -> Response[HTTPValidationError]:
    r""" Organization Member Add

     [BETA]

    Add new members (either via user_email or user_id) to an organization

    If user doesn't exist, new user row will also be added to User Table

    Only proxy_admin or org_admin of organization, allowed to access this endpoint.

    # Parameters:

    - organization_id: str (required)
    - member: Union[List[Member], Member] (required)
        - role: Literal[LitellmUserRoles] (required)
        - user_id: Optional[str]
        - user_email: Optional[str]

    Note: Either user_id or user_email must be provided for each member.

    Example:
    ```
    curl -X POST 'http://0.0.0.0:4000/organization/member_add'     -H 'Authorization: Bearer sk-1234'
    -H 'Content-Type: application/json'     -d '{
        \"organization_id\": \"45e3e396-ee08-4a61-a88e-16b3ce7e0849\",
        \"member\": {
            \"role\": \"internal_user\",
            \"user_id\": \"krrish247652@berri.ai\"
        },
        \"max_budget_in_organization\": 100.0
    }'
    ```

    The following is executed in this function:

    1. Check if organization exists
    2. Creates a new Internal User if the user_id or user_email is not found in LiteLLM_UserTable
    3. Add Internal User to the `LiteLLM_OrganizationMembership` table

    Args:
        body (OrganizationMemberAddRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
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
    body: OrganizationMemberAddRequest,

) -> HTTPValidationError | None:
    r""" Organization Member Add

     [BETA]

    Add new members (either via user_email or user_id) to an organization

    If user doesn't exist, new user row will also be added to User Table

    Only proxy_admin or org_admin of organization, allowed to access this endpoint.

    # Parameters:

    - organization_id: str (required)
    - member: Union[List[Member], Member] (required)
        - role: Literal[LitellmUserRoles] (required)
        - user_id: Optional[str]
        - user_email: Optional[str]

    Note: Either user_id or user_email must be provided for each member.

    Example:
    ```
    curl -X POST 'http://0.0.0.0:4000/organization/member_add'     -H 'Authorization: Bearer sk-1234'
    -H 'Content-Type: application/json'     -d '{
        \"organization_id\": \"45e3e396-ee08-4a61-a88e-16b3ce7e0849\",
        \"member\": {
            \"role\": \"internal_user\",
            \"user_id\": \"krrish247652@berri.ai\"
        },
        \"max_budget_in_organization\": 100.0
    }'
    ```

    The following is executed in this function:

    1. Check if organization exists
    2. Creates a new Internal User if the user_id or user_email is not found in LiteLLM_UserTable
    3. Add Internal User to the `LiteLLM_OrganizationMembership` table

    Args:
        body (OrganizationMemberAddRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
