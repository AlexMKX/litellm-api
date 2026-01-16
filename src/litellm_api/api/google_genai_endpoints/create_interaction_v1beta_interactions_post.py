from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1beta/interactions",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    r""" Create Interaction

     Create a new interaction using Google's Interactions API.

    Per OpenAPI spec: POST /{api_version}/interactions

    Supports both model interactions and agent interactions:
    - Model: Provide `model` parameter (e.g., \"gemini-2.5-flash\")
    - Agent: Provide `agent` parameter (e.g., \"deep-research-pro-preview-12-2025\")

    Example:
    ```bash
    curl -X POST \"http://localhost:4000/v1beta/interactions\"         -H \"Authorization: Bearer
    sk-1234\"         -H \"Content-Type: application/json\"         -d '{
            \"model\": \"gemini/gemini-2.5-flash\",
            \"input\": \"Hello, how are you?\"
        }'
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    r""" Create Interaction

     Create a new interaction using Google's Interactions API.

    Per OpenAPI spec: POST /{api_version}/interactions

    Supports both model interactions and agent interactions:
    - Model: Provide `model` parameter (e.g., \"gemini-2.5-flash\")
    - Agent: Provide `agent` parameter (e.g., \"deep-research-pro-preview-12-2025\")

    Example:
    ```bash
    curl -X POST \"http://localhost:4000/v1beta/interactions\"         -H \"Authorization: Bearer
    sk-1234\"         -H \"Content-Type: application/json\"         -d '{
            \"model\": \"gemini/gemini-2.5-flash\",
            \"input\": \"Hello, how are you?\"
        }'
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

