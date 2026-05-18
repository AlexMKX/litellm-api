from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.policy_attachment_create_request import PolicyAttachmentCreateRequest
from ...models.policy_attachment_db_response import PolicyAttachmentDBResponse
from typing import cast



def _get_kwargs(
    *,
    body: PolicyAttachmentCreateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/policies/attachments",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | PolicyAttachmentDBResponse | None:
    if response.status_code == 200:
        response_200 = PolicyAttachmentDBResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | PolicyAttachmentDBResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PolicyAttachmentCreateRequest,

) -> Response[HTTPValidationError | PolicyAttachmentDBResponse]:
    r""" Create Policy Attachment

     Create a new policy attachment.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/attachments\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"policy_name\": \"global-baseline\",
            \"scope\": \"*\"
        }'
    ```

    Example with team-specific attachment:
    ```bash
    curl -X POST \"http://localhost:4000/policies/attachments\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"policy_name\": \"healthcare-compliance\",
            \"teams\": [\"healthcare-team\", \"medical-research\"]
        }'
    ```

    Example Response:
    ```json
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
    ```

    Args:
        body (PolicyAttachmentCreateRequest): Request body for creating a policy attachment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyAttachmentDBResponse]
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
    body: PolicyAttachmentCreateRequest,

) -> HTTPValidationError | PolicyAttachmentDBResponse | None:
    r""" Create Policy Attachment

     Create a new policy attachment.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/attachments\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"policy_name\": \"global-baseline\",
            \"scope\": \"*\"
        }'
    ```

    Example with team-specific attachment:
    ```bash
    curl -X POST \"http://localhost:4000/policies/attachments\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"policy_name\": \"healthcare-compliance\",
            \"teams\": [\"healthcare-team\", \"medical-research\"]
        }'
    ```

    Example Response:
    ```json
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
    ```

    Args:
        body (PolicyAttachmentCreateRequest): Request body for creating a policy attachment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyAttachmentDBResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PolicyAttachmentCreateRequest,

) -> Response[HTTPValidationError | PolicyAttachmentDBResponse]:
    r""" Create Policy Attachment

     Create a new policy attachment.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/attachments\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"policy_name\": \"global-baseline\",
            \"scope\": \"*\"
        }'
    ```

    Example with team-specific attachment:
    ```bash
    curl -X POST \"http://localhost:4000/policies/attachments\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"policy_name\": \"healthcare-compliance\",
            \"teams\": [\"healthcare-team\", \"medical-research\"]
        }'
    ```

    Example Response:
    ```json
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
    ```

    Args:
        body (PolicyAttachmentCreateRequest): Request body for creating a policy attachment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyAttachmentDBResponse]
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
    body: PolicyAttachmentCreateRequest,

) -> HTTPValidationError | PolicyAttachmentDBResponse | None:
    r""" Create Policy Attachment

     Create a new policy attachment.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/attachments\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"policy_name\": \"global-baseline\",
            \"scope\": \"*\"
        }'
    ```

    Example with team-specific attachment:
    ```bash
    curl -X POST \"http://localhost:4000/policies/attachments\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"policy_name\": \"healthcare-compliance\",
            \"teams\": [\"healthcare-team\", \"medical-research\"]
        }'
    ```

    Example Response:
    ```json
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
    ```

    Args:
        body (PolicyAttachmentCreateRequest): Request body for creating a policy attachment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyAttachmentDBResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
