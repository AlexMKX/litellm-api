from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_search_tool_request import CreateSearchToolRequest
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    *,
    body: CreateSearchToolRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/search_tools",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSearchToolRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Create Search Tool

     Create a new search tool.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/search_tools\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"search_tool\": {
                \"search_tool_name\": \"litellm-search\",
                \"litellm_params\": {
                    \"search_provider\": \"perplexity\",
                    \"api_key\": \"sk-...\"
                },
                \"search_tool_info\": {
                    \"description\": \"Perplexity search tool\"
                }
            }
        }'
    ```

    Example Response:
    ```json
    {
        \"search_tool_id\": \"123e4567-e89b-12d3-a456-426614174000\",
        \"search_tool_name\": \"litellm-search\",
        \"litellm_params\": {
            \"search_provider\": \"perplexity\",
            \"api_key\": \"sk-...\"
        },
        \"search_tool_info\": {
            \"description\": \"Perplexity search tool\"
        },
        \"created_at\": \"2023-11-09T12:34:56.789Z\",
        \"updated_at\": \"2023-11-09T12:34:56.789Z\"
    }
    ```

    Args:
        body (CreateSearchToolRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: CreateSearchToolRequest,

) -> Any | HTTPValidationError | None:
    r""" Create Search Tool

     Create a new search tool.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/search_tools\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"search_tool\": {
                \"search_tool_name\": \"litellm-search\",
                \"litellm_params\": {
                    \"search_provider\": \"perplexity\",
                    \"api_key\": \"sk-...\"
                },
                \"search_tool_info\": {
                    \"description\": \"Perplexity search tool\"
                }
            }
        }'
    ```

    Example Response:
    ```json
    {
        \"search_tool_id\": \"123e4567-e89b-12d3-a456-426614174000\",
        \"search_tool_name\": \"litellm-search\",
        \"litellm_params\": {
            \"search_provider\": \"perplexity\",
            \"api_key\": \"sk-...\"
        },
        \"search_tool_info\": {
            \"description\": \"Perplexity search tool\"
        },
        \"created_at\": \"2023-11-09T12:34:56.789Z\",
        \"updated_at\": \"2023-11-09T12:34:56.789Z\"
    }
    ```

    Args:
        body (CreateSearchToolRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateSearchToolRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Create Search Tool

     Create a new search tool.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/search_tools\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"search_tool\": {
                \"search_tool_name\": \"litellm-search\",
                \"litellm_params\": {
                    \"search_provider\": \"perplexity\",
                    \"api_key\": \"sk-...\"
                },
                \"search_tool_info\": {
                    \"description\": \"Perplexity search tool\"
                }
            }
        }'
    ```

    Example Response:
    ```json
    {
        \"search_tool_id\": \"123e4567-e89b-12d3-a456-426614174000\",
        \"search_tool_name\": \"litellm-search\",
        \"litellm_params\": {
            \"search_provider\": \"perplexity\",
            \"api_key\": \"sk-...\"
        },
        \"search_tool_info\": {
            \"description\": \"Perplexity search tool\"
        },
        \"created_at\": \"2023-11-09T12:34:56.789Z\",
        \"updated_at\": \"2023-11-09T12:34:56.789Z\"
    }
    ```

    Args:
        body (CreateSearchToolRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: CreateSearchToolRequest,

) -> Any | HTTPValidationError | None:
    r""" Create Search Tool

     Create a new search tool.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/search_tools\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"search_tool\": {
                \"search_tool_name\": \"litellm-search\",
                \"litellm_params\": {
                    \"search_provider\": \"perplexity\",
                    \"api_key\": \"sk-...\"
                },
                \"search_tool_info\": {
                    \"description\": \"Perplexity search tool\"
                }
            }
        }'
    ```

    Example Response:
    ```json
    {
        \"search_tool_id\": \"123e4567-e89b-12d3-a456-426614174000\",
        \"search_tool_name\": \"litellm-search\",
        \"litellm_params\": {
            \"search_provider\": \"perplexity\",
            \"api_key\": \"sk-...\"
        },
        \"search_tool_info\": {
            \"description\": \"Perplexity search tool\"
        },
        \"created_at\": \"2023-11-09T12:34:56.789Z\",
        \"updated_at\": \"2023-11-09T12:34:56.789Z\"
    }
    ```

    Args:
        body (CreateSearchToolRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
