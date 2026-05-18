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
    *,
    body: AgentConfig,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/agents",
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
    *,
    client: AuthenticatedClient,
    body: AgentConfig,

) -> Response[AgentResponse | HTTPValidationError]:
    r""" Create Agent

     Create a new agent

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/agents\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"agent\": {
                \"agent_name\": \"my-custom-agent\",
                \"agent_card_params\": {
                    \"protocolVersion\": \"1.0\",
                    \"name\": \"Hello World Agent\",
                    \"description\": \"Just a hello world agent\",
                    \"url\": \"http://localhost:9999/\",
                    \"version\": \"1.0.0\",
                    \"defaultInputModes\": [\"text\"],
                    \"defaultOutputModes\": [\"text\"],
                    \"capabilities\": {
                        \"streaming\": true
                    },
                    \"skills\": [
                        {
                            \"id\": \"hello_world\",
                            \"name\": \"Returns hello world\",
                            \"description\": \"just returns hello world\",
                            \"tags\": [\"hello world\"],
                            \"examples\": [\"hi\", \"hello world\"]
                        }
                    ]
                },
                \"litellm_params\": {
                    \"make_public\": true
                }
            }
        }'
    ```

    Args:
        body (AgentConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentResponse | HTTPValidationError]
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
    body: AgentConfig,

) -> AgentResponse | HTTPValidationError | None:
    r""" Create Agent

     Create a new agent

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/agents\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"agent\": {
                \"agent_name\": \"my-custom-agent\",
                \"agent_card_params\": {
                    \"protocolVersion\": \"1.0\",
                    \"name\": \"Hello World Agent\",
                    \"description\": \"Just a hello world agent\",
                    \"url\": \"http://localhost:9999/\",
                    \"version\": \"1.0.0\",
                    \"defaultInputModes\": [\"text\"],
                    \"defaultOutputModes\": [\"text\"],
                    \"capabilities\": {
                        \"streaming\": true
                    },
                    \"skills\": [
                        {
                            \"id\": \"hello_world\",
                            \"name\": \"Returns hello world\",
                            \"description\": \"just returns hello world\",
                            \"tags\": [\"hello world\"],
                            \"examples\": [\"hi\", \"hello world\"]
                        }
                    ]
                },
                \"litellm_params\": {
                    \"make_public\": true
                }
            }
        }'
    ```

    Args:
        body (AgentConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentResponse | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AgentConfig,

) -> Response[AgentResponse | HTTPValidationError]:
    r""" Create Agent

     Create a new agent

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/agents\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"agent\": {
                \"agent_name\": \"my-custom-agent\",
                \"agent_card_params\": {
                    \"protocolVersion\": \"1.0\",
                    \"name\": \"Hello World Agent\",
                    \"description\": \"Just a hello world agent\",
                    \"url\": \"http://localhost:9999/\",
                    \"version\": \"1.0.0\",
                    \"defaultInputModes\": [\"text\"],
                    \"defaultOutputModes\": [\"text\"],
                    \"capabilities\": {
                        \"streaming\": true
                    },
                    \"skills\": [
                        {
                            \"id\": \"hello_world\",
                            \"name\": \"Returns hello world\",
                            \"description\": \"just returns hello world\",
                            \"tags\": [\"hello world\"],
                            \"examples\": [\"hi\", \"hello world\"]
                        }
                    ]
                },
                \"litellm_params\": {
                    \"make_public\": true
                }
            }
        }'
    ```

    Args:
        body (AgentConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentResponse | HTTPValidationError]
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
    body: AgentConfig,

) -> AgentResponse | HTTPValidationError | None:
    r""" Create Agent

     Create a new agent

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/agents\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"agent\": {
                \"agent_name\": \"my-custom-agent\",
                \"agent_card_params\": {
                    \"protocolVersion\": \"1.0\",
                    \"name\": \"Hello World Agent\",
                    \"description\": \"Just a hello world agent\",
                    \"url\": \"http://localhost:9999/\",
                    \"version\": \"1.0.0\",
                    \"defaultInputModes\": [\"text\"],
                    \"defaultOutputModes\": [\"text\"],
                    \"capabilities\": {
                        \"streaming\": true
                    },
                    \"skills\": [
                        {
                            \"id\": \"hello_world\",
                            \"name\": \"Returns hello world\",
                            \"description\": \"just returns hello world\",
                            \"tags\": [\"hello world\"],
                            \"examples\": [\"hi\", \"hello world\"]
                        }
                    ]
                },
                \"litellm_params\": {
                    \"make_public\": true
                }
            }
        }'
    ```

    Args:
        body (AgentConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
