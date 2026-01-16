from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.update_search_tool_request import UpdateSearchToolRequest
from typing import cast



def _get_kwargs(
    search_tool_id: str,
    *,
    body: UpdateSearchToolRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/search_tools/{search_tool_id}".format(search_tool_id=quote(str(search_tool_id), safe=""),),
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
    search_tool_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSearchToolRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Update Search Tool

     Update an existing search tool.

    Example Request:
    ```bash
    curl -X PUT \"http://localhost:4000/search_tools/123e4567-e89b-12d3-a456-426614174000\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"search_tool\": {
                \"search_tool_name\": \"updated-search\",
                \"litellm_params\": {
                    \"search_provider\": \"perplexity\",
                    \"api_key\": \"sk-new-key\"
                },
                \"search_tool_info\": {
                    \"description\": \"Updated search tool\"
                }
            }
        }'
    ```

    Example Response:
    ```json
    {
        \"search_tool_id\": \"123e4567-e89b-12d3-a456-426614174000\",
        \"search_tool_name\": \"updated-search\",
        \"litellm_params\": {
            \"search_provider\": \"perplexity\",
            \"api_key\": \"sk-new-key\"
        },
        \"search_tool_info\": {
            \"description\": \"Updated search tool\"
        },
        \"created_at\": \"2023-11-09T12:34:56.789Z\",
        \"updated_at\": \"2023-11-09T13:45:12.345Z\"
    }
    ```

    Args:
        search_tool_id (str):
        body (UpdateSearchToolRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        search_tool_id=search_tool_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    search_tool_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSearchToolRequest,

) -> Any | HTTPValidationError | None:
    r""" Update Search Tool

     Update an existing search tool.

    Example Request:
    ```bash
    curl -X PUT \"http://localhost:4000/search_tools/123e4567-e89b-12d3-a456-426614174000\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"search_tool\": {
                \"search_tool_name\": \"updated-search\",
                \"litellm_params\": {
                    \"search_provider\": \"perplexity\",
                    \"api_key\": \"sk-new-key\"
                },
                \"search_tool_info\": {
                    \"description\": \"Updated search tool\"
                }
            }
        }'
    ```

    Example Response:
    ```json
    {
        \"search_tool_id\": \"123e4567-e89b-12d3-a456-426614174000\",
        \"search_tool_name\": \"updated-search\",
        \"litellm_params\": {
            \"search_provider\": \"perplexity\",
            \"api_key\": \"sk-new-key\"
        },
        \"search_tool_info\": {
            \"description\": \"Updated search tool\"
        },
        \"created_at\": \"2023-11-09T12:34:56.789Z\",
        \"updated_at\": \"2023-11-09T13:45:12.345Z\"
    }
    ```

    Args:
        search_tool_id (str):
        body (UpdateSearchToolRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        search_tool_id=search_tool_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    search_tool_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSearchToolRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Update Search Tool

     Update an existing search tool.

    Example Request:
    ```bash
    curl -X PUT \"http://localhost:4000/search_tools/123e4567-e89b-12d3-a456-426614174000\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"search_tool\": {
                \"search_tool_name\": \"updated-search\",
                \"litellm_params\": {
                    \"search_provider\": \"perplexity\",
                    \"api_key\": \"sk-new-key\"
                },
                \"search_tool_info\": {
                    \"description\": \"Updated search tool\"
                }
            }
        }'
    ```

    Example Response:
    ```json
    {
        \"search_tool_id\": \"123e4567-e89b-12d3-a456-426614174000\",
        \"search_tool_name\": \"updated-search\",
        \"litellm_params\": {
            \"search_provider\": \"perplexity\",
            \"api_key\": \"sk-new-key\"
        },
        \"search_tool_info\": {
            \"description\": \"Updated search tool\"
        },
        \"created_at\": \"2023-11-09T12:34:56.789Z\",
        \"updated_at\": \"2023-11-09T13:45:12.345Z\"
    }
    ```

    Args:
        search_tool_id (str):
        body (UpdateSearchToolRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        search_tool_id=search_tool_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    search_tool_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSearchToolRequest,

) -> Any | HTTPValidationError | None:
    r""" Update Search Tool

     Update an existing search tool.

    Example Request:
    ```bash
    curl -X PUT \"http://localhost:4000/search_tools/123e4567-e89b-12d3-a456-426614174000\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"search_tool\": {
                \"search_tool_name\": \"updated-search\",
                \"litellm_params\": {
                    \"search_provider\": \"perplexity\",
                    \"api_key\": \"sk-new-key\"
                },
                \"search_tool_info\": {
                    \"description\": \"Updated search tool\"
                }
            }
        }'
    ```

    Example Response:
    ```json
    {
        \"search_tool_id\": \"123e4567-e89b-12d3-a456-426614174000\",
        \"search_tool_name\": \"updated-search\",
        \"litellm_params\": {
            \"search_provider\": \"perplexity\",
            \"api_key\": \"sk-new-key\"
        },
        \"search_tool_info\": {
            \"description\": \"Updated search tool\"
        },
        \"created_at\": \"2023-11-09T12:34:56.789Z\",
        \"updated_at\": \"2023-11-09T13:45:12.345Z\"
    }
    ```

    Args:
        search_tool_id (str):
        body (UpdateSearchToolRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        search_tool_id=search_tool_id,
client=client,
body=body,

    )).parsed
