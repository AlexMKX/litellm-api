from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_config import AgentConfig
from ...models.agent_response import AgentResponse
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    agent_id: str,
    *,
    body: AgentConfig,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/agents/{agent_id}".format(agent_id=quote(str(agent_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient,
    body: AgentConfig,

) -> Response[AgentResponse | HTTPValidationError]:
    r""" Update Agent

     Update an existing agent

    Example Request:
    ```bash
    curl -X PUT \"http://localhost:4000/agents/123e4567-e89b-12d3-a456-426614174000\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"agent\": {
                \"agent_name\": \"updated-agent\",
                \"agent_card_params\": {
                    \"protocolVersion\": \"1.0\",
                    \"name\": \"Updated Agent\",
                    \"description\": \"Updated description\",
                    \"url\": \"http://localhost:9999/\",
                    \"version\": \"1.1.0\",
                    \"defaultInputModes\": [\"text\"],
                    \"defaultOutputModes\": [\"text\"],
                    \"capabilities\": {
                        \"streaming\": true
                    },
                    \"skills\": []
                },
                \"litellm_params\": {
                    \"make_public\": false
                }
            }
        }'
    ```

    Args:
        agent_id (str):
        body (AgentConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient,
    body: AgentConfig,

) -> AgentResponse | HTTPValidationError | None:
    r""" Update Agent

     Update an existing agent

    Example Request:
    ```bash
    curl -X PUT \"http://localhost:4000/agents/123e4567-e89b-12d3-a456-426614174000\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"agent\": {
                \"agent_name\": \"updated-agent\",
                \"agent_card_params\": {
                    \"protocolVersion\": \"1.0\",
                    \"name\": \"Updated Agent\",
                    \"description\": \"Updated description\",
                    \"url\": \"http://localhost:9999/\",
                    \"version\": \"1.1.0\",
                    \"defaultInputModes\": [\"text\"],
                    \"defaultOutputModes\": [\"text\"],
                    \"capabilities\": {
                        \"streaming\": true
                    },
                    \"skills\": []
                },
                \"litellm_params\": {
                    \"make_public\": false
                }
            }
        }'
    ```

    Args:
        agent_id (str):
        body (AgentConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentResponse | HTTPValidationError
     """


    return sync_detailed(
        agent_id=agent_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient,
    body: AgentConfig,

) -> Response[AgentResponse | HTTPValidationError]:
    r""" Update Agent

     Update an existing agent

    Example Request:
    ```bash
    curl -X PUT \"http://localhost:4000/agents/123e4567-e89b-12d3-a456-426614174000\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"agent\": {
                \"agent_name\": \"updated-agent\",
                \"agent_card_params\": {
                    \"protocolVersion\": \"1.0\",
                    \"name\": \"Updated Agent\",
                    \"description\": \"Updated description\",
                    \"url\": \"http://localhost:9999/\",
                    \"version\": \"1.1.0\",
                    \"defaultInputModes\": [\"text\"],
                    \"defaultOutputModes\": [\"text\"],
                    \"capabilities\": {
                        \"streaming\": true
                    },
                    \"skills\": []
                },
                \"litellm_params\": {
                    \"make_public\": false
                }
            }
        }'
    ```

    Args:
        agent_id (str):
        body (AgentConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient,
    body: AgentConfig,

) -> AgentResponse | HTTPValidationError | None:
    r""" Update Agent

     Update an existing agent

    Example Request:
    ```bash
    curl -X PUT \"http://localhost:4000/agents/123e4567-e89b-12d3-a456-426614174000\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"agent\": {
                \"agent_name\": \"updated-agent\",
                \"agent_card_params\": {
                    \"protocolVersion\": \"1.0\",
                    \"name\": \"Updated Agent\",
                    \"description\": \"Updated description\",
                    \"url\": \"http://localhost:9999/\",
                    \"version\": \"1.1.0\",
                    \"defaultInputModes\": [\"text\"],
                    \"defaultOutputModes\": [\"text\"],
                    \"capabilities\": {
                        \"streaming\": true
                    },
                    \"skills\": []
                },
                \"litellm_params\": {
                    \"make_public\": false
                }
            }
        }'
    ```

    Args:
        agent_id (str):
        body (AgentConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
client=client,
body=body,

    )).parsed
