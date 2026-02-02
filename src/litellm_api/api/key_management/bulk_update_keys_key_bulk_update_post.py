from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulk_update_key_request import BulkUpdateKeyRequest
from ...models.bulk_update_key_response import BulkUpdateKeyResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: BulkUpdateKeyRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(litellm_changed_by, Unset):
        headers["litellm-changed-by"] = litellm_changed_by



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/key/bulk_update",
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
    body: BulkUpdateKeyRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[BulkUpdateKeyResponse | HTTPValidationError]:
    r""" Bulk Update Keys

     Bulk update multiple keys at once.

    This endpoint allows updating multiple keys in a single request. Each key update
    is processed independently - if some updates fail, others will still succeed.

    Parameters:
    - keys: List[BulkUpdateKeyRequestItem] - List of key update requests, each containing:
        - key: str - The key identifier (token) to update
        - budget_id: Optional[str] - Budget ID associated with the key
        - max_budget: Optional[float] - Max budget for key
        - team_id: Optional[str] - Team ID associated with key
        - tags: Optional[List[str]] - Tags for organizing keys

    Returns:
    - total_requested: int - Total number of keys requested for update
    - successful_updates: List[SuccessfulKeyUpdate] - List of successfully updated keys with their
    updated info
    - failed_updates: List[FailedKeyUpdate] - List of failed updates with key_info and failed_reason

    Example request:
    ```bash
    curl --location 'http://0.0.0.0:4000/key/bulk_update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"keys\": [
            {
                \"key\": \"sk-1234\",
                \"max_budget\": 100.0,
                \"team_id\": \"team-123\",
                \"tags\": [\"production\", \"api\"]
            },
            {
                \"key\": \"sk-5678\",
                \"budget_id\": \"budget-456\",
                \"tags\": [\"staging\"]
            }
        ]
    }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BulkUpdateKeyRequest): Request for bulk key updates

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
    body: BulkUpdateKeyRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> BulkUpdateKeyResponse | HTTPValidationError | None:
    r""" Bulk Update Keys

     Bulk update multiple keys at once.

    This endpoint allows updating multiple keys in a single request. Each key update
    is processed independently - if some updates fail, others will still succeed.

    Parameters:
    - keys: List[BulkUpdateKeyRequestItem] - List of key update requests, each containing:
        - key: str - The key identifier (token) to update
        - budget_id: Optional[str] - Budget ID associated with the key
        - max_budget: Optional[float] - Max budget for key
        - team_id: Optional[str] - Team ID associated with key
        - tags: Optional[List[str]] - Tags for organizing keys

    Returns:
    - total_requested: int - Total number of keys requested for update
    - successful_updates: List[SuccessfulKeyUpdate] - List of successfully updated keys with their
    updated info
    - failed_updates: List[FailedKeyUpdate] - List of failed updates with key_info and failed_reason

    Example request:
    ```bash
    curl --location 'http://0.0.0.0:4000/key/bulk_update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"keys\": [
            {
                \"key\": \"sk-1234\",
                \"max_budget\": 100.0,
                \"team_id\": \"team-123\",
                \"tags\": [\"production\", \"api\"]
            },
            {
                \"key\": \"sk-5678\",
                \"budget_id\": \"budget-456\",
                \"tags\": [\"staging\"]
            }
        ]
    }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BulkUpdateKeyRequest): Request for bulk key updates

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
    body: BulkUpdateKeyRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[BulkUpdateKeyResponse | HTTPValidationError]:
    r""" Bulk Update Keys

     Bulk update multiple keys at once.

    This endpoint allows updating multiple keys in a single request. Each key update
    is processed independently - if some updates fail, others will still succeed.

    Parameters:
    - keys: List[BulkUpdateKeyRequestItem] - List of key update requests, each containing:
        - key: str - The key identifier (token) to update
        - budget_id: Optional[str] - Budget ID associated with the key
        - max_budget: Optional[float] - Max budget for key
        - team_id: Optional[str] - Team ID associated with key
        - tags: Optional[List[str]] - Tags for organizing keys

    Returns:
    - total_requested: int - Total number of keys requested for update
    - successful_updates: List[SuccessfulKeyUpdate] - List of successfully updated keys with their
    updated info
    - failed_updates: List[FailedKeyUpdate] - List of failed updates with key_info and failed_reason

    Example request:
    ```bash
    curl --location 'http://0.0.0.0:4000/key/bulk_update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"keys\": [
            {
                \"key\": \"sk-1234\",
                \"max_budget\": 100.0,
                \"team_id\": \"team-123\",
                \"tags\": [\"production\", \"api\"]
            },
            {
                \"key\": \"sk-5678\",
                \"budget_id\": \"budget-456\",
                \"tags\": [\"staging\"]
            }
        ]
    }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BulkUpdateKeyRequest): Request for bulk key updates

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
    body: BulkUpdateKeyRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> BulkUpdateKeyResponse | HTTPValidationError | None:
    r""" Bulk Update Keys

     Bulk update multiple keys at once.

    This endpoint allows updating multiple keys in a single request. Each key update
    is processed independently - if some updates fail, others will still succeed.

    Parameters:
    - keys: List[BulkUpdateKeyRequestItem] - List of key update requests, each containing:
        - key: str - The key identifier (token) to update
        - budget_id: Optional[str] - Budget ID associated with the key
        - max_budget: Optional[float] - Max budget for key
        - team_id: Optional[str] - Team ID associated with key
        - tags: Optional[List[str]] - Tags for organizing keys

    Returns:
    - total_requested: int - Total number of keys requested for update
    - successful_updates: List[SuccessfulKeyUpdate] - List of successfully updated keys with their
    updated info
    - failed_updates: List[FailedKeyUpdate] - List of failed updates with key_info and failed_reason

    Example request:
    ```bash
    curl --location 'http://0.0.0.0:4000/key/bulk_update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"keys\": [
            {
                \"key\": \"sk-1234\",
                \"max_budget\": 100.0,
                \"team_id\": \"team-123\",
                \"tags\": [\"production\", \"api\"]
            },
            {
                \"key\": \"sk-5678\",
                \"budget_id\": \"budget-456\",
                \"tags\": [\"staging\"]
            }
        ]
    }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BulkUpdateKeyRequest): Request for bulk key updates

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
