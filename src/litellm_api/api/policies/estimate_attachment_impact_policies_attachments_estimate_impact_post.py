from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.attachment_impact_response import AttachmentImpactResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.policy_attachment_create_request import PolicyAttachmentCreateRequest
from typing import cast



def _get_kwargs(
    *,
    body: PolicyAttachmentCreateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/policies/attachments/estimate-impact",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AttachmentImpactResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AttachmentImpactResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AttachmentImpactResponse | HTTPValidationError]:
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

) -> Response[AttachmentImpactResponse | HTTPValidationError]:
    r""" Estimate Attachment Impact

     Estimate how many keys and teams would be affected by a policy attachment.

    Use this before creating an attachment to preview the blast radius.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/attachments/estimate-impact\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"policy_name\": \"hipaa-compliance\",
            \"tags\": [\"healthcare\", \"health-*\"]
        }'
    ```

    Args:
        body (PolicyAttachmentCreateRequest): Request body for creating a policy attachment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentImpactResponse | HTTPValidationError]
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

) -> AttachmentImpactResponse | HTTPValidationError | None:
    r""" Estimate Attachment Impact

     Estimate how many keys and teams would be affected by a policy attachment.

    Use this before creating an attachment to preview the blast radius.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/attachments/estimate-impact\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"policy_name\": \"hipaa-compliance\",
            \"tags\": [\"healthcare\", \"health-*\"]
        }'
    ```

    Args:
        body (PolicyAttachmentCreateRequest): Request body for creating a policy attachment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentImpactResponse | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PolicyAttachmentCreateRequest,

) -> Response[AttachmentImpactResponse | HTTPValidationError]:
    r""" Estimate Attachment Impact

     Estimate how many keys and teams would be affected by a policy attachment.

    Use this before creating an attachment to preview the blast radius.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/attachments/estimate-impact\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"policy_name\": \"hipaa-compliance\",
            \"tags\": [\"healthcare\", \"health-*\"]
        }'
    ```

    Args:
        body (PolicyAttachmentCreateRequest): Request body for creating a policy attachment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentImpactResponse | HTTPValidationError]
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

) -> AttachmentImpactResponse | HTTPValidationError | None:
    r""" Estimate Attachment Impact

     Estimate how many keys and teams would be affected by a policy attachment.

    Use this before creating an attachment to preview the blast radius.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/attachments/estimate-impact\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"policy_name\": \"hipaa-compliance\",
            \"tags\": [\"healthcare\", \"health-*\"]
        }'
    ```

    Args:
        body (PolicyAttachmentCreateRequest): Request body for creating a policy attachment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentImpactResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
