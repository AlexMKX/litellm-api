from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_search_tools_response import ListSearchToolsResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/search_tools/list",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListSearchToolsResponse | None:
    if response.status_code == 200:
        response_200 = ListSearchToolsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListSearchToolsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[ListSearchToolsResponse]:
    r""" List Search Tools

     List all search tools that are available in the database.

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/search_tools/list\" -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"search_tools\": [
            {
                \"search_tool_id\": \"123e4567-e89b-12d3-a456-426614174000\",
                \"search_tool_name\": \"litellm-search\",
                \"litellm_params\": {
                    \"search_provider\": \"perplexity\",
                    \"api_key\": \"sk-***\",
                    \"api_base\": \"https://api.perplexity.ai\"
                },
                \"search_tool_info\": {
                    \"description\": \"Perplexity search tool\"
                },
                \"created_at\": \"2023-11-09T12:34:56.789Z\",
                \"updated_at\": \"2023-11-09T12:34:56.789Z\"
            }
        ]
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSearchToolsResponse]
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

) -> ListSearchToolsResponse | None:
    r""" List Search Tools

     List all search tools that are available in the database.

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/search_tools/list\" -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"search_tools\": [
            {
                \"search_tool_id\": \"123e4567-e89b-12d3-a456-426614174000\",
                \"search_tool_name\": \"litellm-search\",
                \"litellm_params\": {
                    \"search_provider\": \"perplexity\",
                    \"api_key\": \"sk-***\",
                    \"api_base\": \"https://api.perplexity.ai\"
                },
                \"search_tool_info\": {
                    \"description\": \"Perplexity search tool\"
                },
                \"created_at\": \"2023-11-09T12:34:56.789Z\",
                \"updated_at\": \"2023-11-09T12:34:56.789Z\"
            }
        ]
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSearchToolsResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[ListSearchToolsResponse]:
    r""" List Search Tools

     List all search tools that are available in the database.

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/search_tools/list\" -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"search_tools\": [
            {
                \"search_tool_id\": \"123e4567-e89b-12d3-a456-426614174000\",
                \"search_tool_name\": \"litellm-search\",
                \"litellm_params\": {
                    \"search_provider\": \"perplexity\",
                    \"api_key\": \"sk-***\",
                    \"api_base\": \"https://api.perplexity.ai\"
                },
                \"search_tool_info\": {
                    \"description\": \"Perplexity search tool\"
                },
                \"created_at\": \"2023-11-09T12:34:56.789Z\",
                \"updated_at\": \"2023-11-09T12:34:56.789Z\"
            }
        ]
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListSearchToolsResponse]
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

) -> ListSearchToolsResponse | None:
    r""" List Search Tools

     List all search tools that are available in the database.

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/search_tools/list\" -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"search_tools\": [
            {
                \"search_tool_id\": \"123e4567-e89b-12d3-a456-426614174000\",
                \"search_tool_name\": \"litellm-search\",
                \"litellm_params\": {
                    \"search_provider\": \"perplexity\",
                    \"api_key\": \"sk-***\",
                    \"api_base\": \"https://api.perplexity.ai\"
                },
                \"search_tool_info\": {
                    \"description\": \"Perplexity search tool\"
                },
                \"created_at\": \"2023-11-09T12:34:56.789Z\",
                \"updated_at\": \"2023-11-09T12:34:56.789Z\"
            }
        ]
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListSearchToolsResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
