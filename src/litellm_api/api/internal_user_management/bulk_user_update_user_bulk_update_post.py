from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulk_update_user_request import BulkUpdateUserRequest
from ...models.bulk_update_user_response import BulkUpdateUserResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: BulkUpdateUserRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(litellm_changed_by, Unset):
        headers["litellm-changed-by"] = litellm_changed_by



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/user/bulk_update",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BulkUpdateUserResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BulkUpdateUserResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BulkUpdateUserResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkUpdateUserRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[BulkUpdateUserResponse | HTTPValidationError]:
    r""" Bulk User Update

     Bulk update multiple users at once.

    This endpoint allows updating multiple users in a single request. Each user update
    is processed independently - if some updates fail, others will still succeed.

    Parameters:
    - users: Optional[List[UpdateUserRequest]] - List of specific user update requests
    - all_users: Optional[bool] - Set to true to update all users in the system
    - user_updates: Optional[UpdateUserRequest] - Updates to apply when all_users=True

    Returns:
    - results: List of individual update results
    - total_requested: Total number of users requested for update
    - successful_updates: Number of successful updates
    - failed_updates: Number of failed updates

    Example request for specific users:
    ```bash
    curl --location 'http://0.0.0.0:4000/user/bulk_update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"users\": [
            {
                \"user_id\": \"user1\",
                \"user_role\": \"internal_user\",
                \"max_budget\": 100.0
            },
            {
                \"user_email\": \"user2@example.com\",
                \"user_role\": \"internal_user_viewer\",
                \"max_budget\": 50.0
            }
        ]
    }'
    ```

    Example request for all users:
    ```bash
    curl --location 'http://0.0.0.0:4000/user/bulk_update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"all_users\": true,
        \"user_updates\": {
            \"user_role\": \"internal_user\",
            \"max_budget\": 50.0
        }
    }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BulkUpdateUserRequest): Request for bulk user updates

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkUpdateUserResponse | HTTPValidationError]
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
    body: BulkUpdateUserRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> BulkUpdateUserResponse | HTTPValidationError | None:
    r""" Bulk User Update

     Bulk update multiple users at once.

    This endpoint allows updating multiple users in a single request. Each user update
    is processed independently - if some updates fail, others will still succeed.

    Parameters:
    - users: Optional[List[UpdateUserRequest]] - List of specific user update requests
    - all_users: Optional[bool] - Set to true to update all users in the system
    - user_updates: Optional[UpdateUserRequest] - Updates to apply when all_users=True

    Returns:
    - results: List of individual update results
    - total_requested: Total number of users requested for update
    - successful_updates: Number of successful updates
    - failed_updates: Number of failed updates

    Example request for specific users:
    ```bash
    curl --location 'http://0.0.0.0:4000/user/bulk_update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"users\": [
            {
                \"user_id\": \"user1\",
                \"user_role\": \"internal_user\",
                \"max_budget\": 100.0
            },
            {
                \"user_email\": \"user2@example.com\",
                \"user_role\": \"internal_user_viewer\",
                \"max_budget\": 50.0
            }
        ]
    }'
    ```

    Example request for all users:
    ```bash
    curl --location 'http://0.0.0.0:4000/user/bulk_update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"all_users\": true,
        \"user_updates\": {
            \"user_role\": \"internal_user\",
            \"max_budget\": 50.0
        }
    }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BulkUpdateUserRequest): Request for bulk user updates

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkUpdateUserResponse | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkUpdateUserRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[BulkUpdateUserResponse | HTTPValidationError]:
    r""" Bulk User Update

     Bulk update multiple users at once.

    This endpoint allows updating multiple users in a single request. Each user update
    is processed independently - if some updates fail, others will still succeed.

    Parameters:
    - users: Optional[List[UpdateUserRequest]] - List of specific user update requests
    - all_users: Optional[bool] - Set to true to update all users in the system
    - user_updates: Optional[UpdateUserRequest] - Updates to apply when all_users=True

    Returns:
    - results: List of individual update results
    - total_requested: Total number of users requested for update
    - successful_updates: Number of successful updates
    - failed_updates: Number of failed updates

    Example request for specific users:
    ```bash
    curl --location 'http://0.0.0.0:4000/user/bulk_update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"users\": [
            {
                \"user_id\": \"user1\",
                \"user_role\": \"internal_user\",
                \"max_budget\": 100.0
            },
            {
                \"user_email\": \"user2@example.com\",
                \"user_role\": \"internal_user_viewer\",
                \"max_budget\": 50.0
            }
        ]
    }'
    ```

    Example request for all users:
    ```bash
    curl --location 'http://0.0.0.0:4000/user/bulk_update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"all_users\": true,
        \"user_updates\": {
            \"user_role\": \"internal_user\",
            \"max_budget\": 50.0
        }
    }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BulkUpdateUserRequest): Request for bulk user updates

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkUpdateUserResponse | HTTPValidationError]
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
    body: BulkUpdateUserRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> BulkUpdateUserResponse | HTTPValidationError | None:
    r""" Bulk User Update

     Bulk update multiple users at once.

    This endpoint allows updating multiple users in a single request. Each user update
    is processed independently - if some updates fail, others will still succeed.

    Parameters:
    - users: Optional[List[UpdateUserRequest]] - List of specific user update requests
    - all_users: Optional[bool] - Set to true to update all users in the system
    - user_updates: Optional[UpdateUserRequest] - Updates to apply when all_users=True

    Returns:
    - results: List of individual update results
    - total_requested: Total number of users requested for update
    - successful_updates: Number of successful updates
    - failed_updates: Number of failed updates

    Example request for specific users:
    ```bash
    curl --location 'http://0.0.0.0:4000/user/bulk_update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"users\": [
            {
                \"user_id\": \"user1\",
                \"user_role\": \"internal_user\",
                \"max_budget\": 100.0
            },
            {
                \"user_email\": \"user2@example.com\",
                \"user_role\": \"internal_user_viewer\",
                \"max_budget\": 50.0
            }
        ]
    }'
    ```

    Example request for all users:
    ```bash
    curl --location 'http://0.0.0.0:4000/user/bulk_update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"all_users\": true,
        \"user_updates\": {
            \"user_role\": \"internal_user\",
            \"max_budget\": 50.0
        }
    }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BulkUpdateUserRequest): Request for bulk user updates

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkUpdateUserResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    )).parsed
