from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_response import AgentResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    health_check: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["health_check"] = health_check


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | list[AgentResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = AgentResponse.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | list[AgentResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    health_check: bool | Unset = False,

) -> Response[HTTPValidationError | list[AgentResponse]]:
    r""" Get Agents

     Example usage:
    ```
    curl -X GET \"http://localhost:4000/v1/agents\"       -H \"Content-Type: application/json\"       -H
    \"Authorization: Bearer your-key\"     ```

    Pass `?health_check=true` to filter out agents whose URL is unreachable:
    ```
    curl -X GET \"http://localhost:4000/v1/agents?health_check=true\"       -H \"Content-Type:
    application/json\"       -H \"Authorization: Bearer your-key\"     ```

    Returns: List[AgentResponse]

    Args:
        health_check (bool | Unset): When true, performs a GET request to each agent's URL. Agents
            with reachable URLs (HTTP status < 500) and agents without a URL are returned; unreachable
            agents are filtered out. Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[AgentResponse]]
     """


    kwargs = _get_kwargs(
        health_check=health_check,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    health_check: bool | Unset = False,

) -> HTTPValidationError | list[AgentResponse] | None:
    r""" Get Agents

     Example usage:
    ```
    curl -X GET \"http://localhost:4000/v1/agents\"       -H \"Content-Type: application/json\"       -H
    \"Authorization: Bearer your-key\"     ```

    Pass `?health_check=true` to filter out agents whose URL is unreachable:
    ```
    curl -X GET \"http://localhost:4000/v1/agents?health_check=true\"       -H \"Content-Type:
    application/json\"       -H \"Authorization: Bearer your-key\"     ```

    Returns: List[AgentResponse]

    Args:
        health_check (bool | Unset): When true, performs a GET request to each agent's URL. Agents
            with reachable URLs (HTTP status < 500) and agents without a URL are returned; unreachable
            agents are filtered out. Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[AgentResponse]
     """


    return sync_detailed(
        client=client,
health_check=health_check,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    health_check: bool | Unset = False,

) -> Response[HTTPValidationError | list[AgentResponse]]:
    r""" Get Agents

     Example usage:
    ```
    curl -X GET \"http://localhost:4000/v1/agents\"       -H \"Content-Type: application/json\"       -H
    \"Authorization: Bearer your-key\"     ```

    Pass `?health_check=true` to filter out agents whose URL is unreachable:
    ```
    curl -X GET \"http://localhost:4000/v1/agents?health_check=true\"       -H \"Content-Type:
    application/json\"       -H \"Authorization: Bearer your-key\"     ```

    Returns: List[AgentResponse]

    Args:
        health_check (bool | Unset): When true, performs a GET request to each agent's URL. Agents
            with reachable URLs (HTTP status < 500) and agents without a URL are returned; unreachable
            agents are filtered out. Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[AgentResponse]]
     """


    kwargs = _get_kwargs(
        health_check=health_check,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    health_check: bool | Unset = False,

) -> HTTPValidationError | list[AgentResponse] | None:
    r""" Get Agents

     Example usage:
    ```
    curl -X GET \"http://localhost:4000/v1/agents\"       -H \"Content-Type: application/json\"       -H
    \"Authorization: Bearer your-key\"     ```

    Pass `?health_check=true` to filter out agents whose URL is unreachable:
    ```
    curl -X GET \"http://localhost:4000/v1/agents?health_check=true\"       -H \"Content-Type:
    application/json\"       -H \"Authorization: Bearer your-key\"     ```

    Returns: List[AgentResponse]

    Args:
        health_check (bool | Unset): When true, performs a GET request to each agent's URL. Agents
            with reachable URLs (HTTP status < 500) and agents without a URL are returned; unreachable
            agents are filtered out. Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[AgentResponse]
     """


    return (await asyncio_detailed(
        client=client,
health_check=health_check,

    )).parsed
