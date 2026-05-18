from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.policy_attachment_list_response import PolicyAttachmentListResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/policies/attachments/list",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PolicyAttachmentListResponse | None:
    if response.status_code == 200:
        response_200 = PolicyAttachmentListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PolicyAttachmentListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[PolicyAttachmentListResponse]:
    r""" List Policy Attachments

     List all policy attachments from the database.

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/policies/attachments/list\" \
        -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"attachments\": [
            {
                \"attachment_id\": \"123e4567-e89b-12d3-a456-426614174000\",
                \"policy_name\": \"global-baseline\",
                \"scope\": \"*\",
                \"teams\": [],
                \"keys\": [],
                \"models\": [],
                \"created_at\": \"2024-01-01T00:00:00Z\",
                \"updated_at\": \"2024-01-01T00:00:00Z\"
            }
        ],
        \"total_count\": 1
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PolicyAttachmentListResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> PolicyAttachmentListResponse | None:
    r""" List Policy Attachments

     List all policy attachments from the database.

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/policies/attachments/list\" \
        -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"attachments\": [
            {
                \"attachment_id\": \"123e4567-e89b-12d3-a456-426614174000\",
                \"policy_name\": \"global-baseline\",
                \"scope\": \"*\",
                \"teams\": [],
                \"keys\": [],
                \"models\": [],
                \"created_at\": \"2024-01-01T00:00:00Z\",
                \"updated_at\": \"2024-01-01T00:00:00Z\"
            }
        ],
        \"total_count\": 1
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PolicyAttachmentListResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[PolicyAttachmentListResponse]:
    r""" List Policy Attachments

     List all policy attachments from the database.

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/policies/attachments/list\" \
        -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"attachments\": [
            {
                \"attachment_id\": \"123e4567-e89b-12d3-a456-426614174000\",
                \"policy_name\": \"global-baseline\",
                \"scope\": \"*\",
                \"teams\": [],
                \"keys\": [],
                \"models\": [],
                \"created_at\": \"2024-01-01T00:00:00Z\",
                \"updated_at\": \"2024-01-01T00:00:00Z\"
            }
        ],
        \"total_count\": 1
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PolicyAttachmentListResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> PolicyAttachmentListResponse | None:
    r""" List Policy Attachments

     List all policy attachments from the database.

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/policies/attachments/list\" \
        -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"attachments\": [
            {
                \"attachment_id\": \"123e4567-e89b-12d3-a456-426614174000\",
                \"policy_name\": \"global-baseline\",
                \"scope\": \"*\",
                \"teams\": [],
                \"keys\": [],
                \"models\": [],
                \"created_at\": \"2024-01-01T00:00:00Z\",
                \"updated_at\": \"2024-01-01T00:00:00Z\"
            }
        ],
        \"total_count\": 1
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PolicyAttachmentListResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
