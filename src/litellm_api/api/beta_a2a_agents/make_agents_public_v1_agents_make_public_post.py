from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_make_public_response import AgentMakePublicResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.make_agents_public_request import MakeAgentsPublicRequest
from typing import cast



def _get_kwargs(
    *,
    body: MakeAgentsPublicRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/agents/make_public",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentMakePublicResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentMakePublicResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentMakePublicResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MakeAgentsPublicRequest,

) -> Response[AgentMakePublicResponse | HTTPValidationError]:
    r""" Make Agents Public

     Make multiple agents publicly discoverable

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/v1/agents/make_public\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"agent_ids\": [\"123e4567-e89b-12d3-a456-426614174000\",
    \"123e4567-e89b-12d3-a456-426614174001\"]
        }'
    ```

    Example Response:
    ```json
    {
        \"agent_id\": \"123e4567-e89b-12d3-a456-426614174000\",
        \"agent_name\": \"my-custom-agent\",
        \"litellm_params\": {
            \"make_public\": true
        },
        \"agent_card_params\": {...},
        \"created_at\": \"2025-11-15T10:30:00Z\",
        \"updated_at\": \"2025-11-15T10:35:00Z\",
        \"created_by\": \"user123\",
        \"updated_by\": \"user123\"
    }
    ```

    Args:
        body (MakeAgentsPublicRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentMakePublicResponse | HTTPValidationError]
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
    body: MakeAgentsPublicRequest,

) -> AgentMakePublicResponse | HTTPValidationError | None:
    r""" Make Agents Public

     Make multiple agents publicly discoverable

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/v1/agents/make_public\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"agent_ids\": [\"123e4567-e89b-12d3-a456-426614174000\",
    \"123e4567-e89b-12d3-a456-426614174001\"]
        }'
    ```

    Example Response:
    ```json
    {
        \"agent_id\": \"123e4567-e89b-12d3-a456-426614174000\",
        \"agent_name\": \"my-custom-agent\",
        \"litellm_params\": {
            \"make_public\": true
        },
        \"agent_card_params\": {...},
        \"created_at\": \"2025-11-15T10:30:00Z\",
        \"updated_at\": \"2025-11-15T10:35:00Z\",
        \"created_by\": \"user123\",
        \"updated_by\": \"user123\"
    }
    ```

    Args:
        body (MakeAgentsPublicRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentMakePublicResponse | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MakeAgentsPublicRequest,

) -> Response[AgentMakePublicResponse | HTTPValidationError]:
    r""" Make Agents Public

     Make multiple agents publicly discoverable

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/v1/agents/make_public\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"agent_ids\": [\"123e4567-e89b-12d3-a456-426614174000\",
    \"123e4567-e89b-12d3-a456-426614174001\"]
        }'
    ```

    Example Response:
    ```json
    {
        \"agent_id\": \"123e4567-e89b-12d3-a456-426614174000\",
        \"agent_name\": \"my-custom-agent\",
        \"litellm_params\": {
            \"make_public\": true
        },
        \"agent_card_params\": {...},
        \"created_at\": \"2025-11-15T10:30:00Z\",
        \"updated_at\": \"2025-11-15T10:35:00Z\",
        \"created_by\": \"user123\",
        \"updated_by\": \"user123\"
    }
    ```

    Args:
        body (MakeAgentsPublicRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentMakePublicResponse | HTTPValidationError]
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
    body: MakeAgentsPublicRequest,

) -> AgentMakePublicResponse | HTTPValidationError | None:
    r""" Make Agents Public

     Make multiple agents publicly discoverable

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/v1/agents/make_public\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"agent_ids\": [\"123e4567-e89b-12d3-a456-426614174000\",
    \"123e4567-e89b-12d3-a456-426614174001\"]
        }'
    ```

    Example Response:
    ```json
    {
        \"agent_id\": \"123e4567-e89b-12d3-a456-426614174000\",
        \"agent_name\": \"my-custom-agent\",
        \"litellm_params\": {
            \"make_public\": true
        },
        \"agent_card_params\": {...},
        \"created_at\": \"2025-11-15T10:30:00Z\",
        \"updated_at\": \"2025-11-15T10:35:00Z\",
        \"created_by\": \"user123\",
        \"updated_by\": \"user123\"
    }
    ```

    Args:
        body (MakeAgentsPublicRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentMakePublicResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
