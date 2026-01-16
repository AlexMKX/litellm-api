from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    search_tool_name: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_search_tool_name: None | str | Unset
    if isinstance(search_tool_name, Unset):
        json_search_tool_name = UNSET
    else:
        json_search_tool_name = search_tool_name
    params["search_tool_name"] = json_search_tool_name


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/search",
        "params": params,
    }


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
    search_tool_name: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Search

     Search endpoint for performing web searches.

    Follows the Perplexity Search API spec:
    https://docs.perplexity.ai/api-reference/search-post

    The search_tool_name can be passed either:
    1. In the URL path: /v1/search/{search_tool_name}
    2. In the request body: {\"search_tool_name\": \"...\"}

    Example with search_tool_name in URL (recommended - keeps body Perplexity-compatible):
    ```bash
    curl -X POST \"http://localhost:4000/v1/search/litellm-search\"         -H \"Authorization: Bearer
    sk-1234\"         -H \"Content-Type: application/json\"         -d '{
            \"query\": \"latest AI developments 2024\",
            \"max_results\": 5,
            \"search_domain_filter\": [\"arxiv.org\", \"nature.com\"],
            \"country\": \"US\"
        }'
    ```

    Example with search_tool_name in body:
    ```bash
    curl -X POST \"http://localhost:4000/v1/search\"         -H \"Authorization: Bearer sk-1234\"
    -H \"Content-Type: application/json\"         -d '{
            \"search_tool_name\": \"litellm-search\",
            \"query\": \"latest AI developments 2024\",
            \"max_results\": 5,
            \"search_domain_filter\": [\"arxiv.org\", \"nature.com\"],
            \"country\": \"US\"
        }'
    ```

    Request Body Parameters (when search_tool_name not in URL):
    - search_tool_name (str, required if not in URL): Name of the search tool configured in router
    - query (str or list[str], required): Search query
    - max_results (int, optional): Maximum number of results (1-20), default 10
    - search_domain_filter (list[str], optional): List of domains to filter (max 20)
    - max_tokens_per_page (int, optional): Max tokens per page, default 1024
    - country (str, optional): Country code filter (e.g., 'US', 'GB', 'DE')

    When using URL path parameter, only Perplexity-compatible parameters are needed in body:
    - query (str or list[str], required): Search query
    - max_results (int, optional): Maximum number of results (1-20), default 10
    - search_domain_filter (list[str], optional): List of domains to filter (max 20)
    - max_tokens_per_page (int, optional): Max tokens per page, default 1024
    - country (str, optional): Country code filter (e.g., 'US', 'GB', 'DE')

    Response follows Perplexity Search API format:
    ```json
    {
        \"object\": \"search\",
        \"results\": [
            {
                \"title\": \"Result title\",
                \"url\": \"https://example.com\",
                \"snippet\": \"Result snippet...\",
                \"date\": \"2024-01-01\",
                \"last_updated\": \"2024-01-01\"
            }
        ]
    }
    ```

    Args:
        search_tool_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        search_tool_name=search_tool_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    search_tool_name: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Search

     Search endpoint for performing web searches.

    Follows the Perplexity Search API spec:
    https://docs.perplexity.ai/api-reference/search-post

    The search_tool_name can be passed either:
    1. In the URL path: /v1/search/{search_tool_name}
    2. In the request body: {\"search_tool_name\": \"...\"}

    Example with search_tool_name in URL (recommended - keeps body Perplexity-compatible):
    ```bash
    curl -X POST \"http://localhost:4000/v1/search/litellm-search\"         -H \"Authorization: Bearer
    sk-1234\"         -H \"Content-Type: application/json\"         -d '{
            \"query\": \"latest AI developments 2024\",
            \"max_results\": 5,
            \"search_domain_filter\": [\"arxiv.org\", \"nature.com\"],
            \"country\": \"US\"
        }'
    ```

    Example with search_tool_name in body:
    ```bash
    curl -X POST \"http://localhost:4000/v1/search\"         -H \"Authorization: Bearer sk-1234\"
    -H \"Content-Type: application/json\"         -d '{
            \"search_tool_name\": \"litellm-search\",
            \"query\": \"latest AI developments 2024\",
            \"max_results\": 5,
            \"search_domain_filter\": [\"arxiv.org\", \"nature.com\"],
            \"country\": \"US\"
        }'
    ```

    Request Body Parameters (when search_tool_name not in URL):
    - search_tool_name (str, required if not in URL): Name of the search tool configured in router
    - query (str or list[str], required): Search query
    - max_results (int, optional): Maximum number of results (1-20), default 10
    - search_domain_filter (list[str], optional): List of domains to filter (max 20)
    - max_tokens_per_page (int, optional): Max tokens per page, default 1024
    - country (str, optional): Country code filter (e.g., 'US', 'GB', 'DE')

    When using URL path parameter, only Perplexity-compatible parameters are needed in body:
    - query (str or list[str], required): Search query
    - max_results (int, optional): Maximum number of results (1-20), default 10
    - search_domain_filter (list[str], optional): List of domains to filter (max 20)
    - max_tokens_per_page (int, optional): Max tokens per page, default 1024
    - country (str, optional): Country code filter (e.g., 'US', 'GB', 'DE')

    Response follows Perplexity Search API format:
    ```json
    {
        \"object\": \"search\",
        \"results\": [
            {
                \"title\": \"Result title\",
                \"url\": \"https://example.com\",
                \"snippet\": \"Result snippet...\",
                \"date\": \"2024-01-01\",
                \"last_updated\": \"2024-01-01\"
            }
        ]
    }
    ```

    Args:
        search_tool_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
search_tool_name=search_tool_name,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    search_tool_name: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Search

     Search endpoint for performing web searches.

    Follows the Perplexity Search API spec:
    https://docs.perplexity.ai/api-reference/search-post

    The search_tool_name can be passed either:
    1. In the URL path: /v1/search/{search_tool_name}
    2. In the request body: {\"search_tool_name\": \"...\"}

    Example with search_tool_name in URL (recommended - keeps body Perplexity-compatible):
    ```bash
    curl -X POST \"http://localhost:4000/v1/search/litellm-search\"         -H \"Authorization: Bearer
    sk-1234\"         -H \"Content-Type: application/json\"         -d '{
            \"query\": \"latest AI developments 2024\",
            \"max_results\": 5,
            \"search_domain_filter\": [\"arxiv.org\", \"nature.com\"],
            \"country\": \"US\"
        }'
    ```

    Example with search_tool_name in body:
    ```bash
    curl -X POST \"http://localhost:4000/v1/search\"         -H \"Authorization: Bearer sk-1234\"
    -H \"Content-Type: application/json\"         -d '{
            \"search_tool_name\": \"litellm-search\",
            \"query\": \"latest AI developments 2024\",
            \"max_results\": 5,
            \"search_domain_filter\": [\"arxiv.org\", \"nature.com\"],
            \"country\": \"US\"
        }'
    ```

    Request Body Parameters (when search_tool_name not in URL):
    - search_tool_name (str, required if not in URL): Name of the search tool configured in router
    - query (str or list[str], required): Search query
    - max_results (int, optional): Maximum number of results (1-20), default 10
    - search_domain_filter (list[str], optional): List of domains to filter (max 20)
    - max_tokens_per_page (int, optional): Max tokens per page, default 1024
    - country (str, optional): Country code filter (e.g., 'US', 'GB', 'DE')

    When using URL path parameter, only Perplexity-compatible parameters are needed in body:
    - query (str or list[str], required): Search query
    - max_results (int, optional): Maximum number of results (1-20), default 10
    - search_domain_filter (list[str], optional): List of domains to filter (max 20)
    - max_tokens_per_page (int, optional): Max tokens per page, default 1024
    - country (str, optional): Country code filter (e.g., 'US', 'GB', 'DE')

    Response follows Perplexity Search API format:
    ```json
    {
        \"object\": \"search\",
        \"results\": [
            {
                \"title\": \"Result title\",
                \"url\": \"https://example.com\",
                \"snippet\": \"Result snippet...\",
                \"date\": \"2024-01-01\",
                \"last_updated\": \"2024-01-01\"
            }
        ]
    }
    ```

    Args:
        search_tool_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        search_tool_name=search_tool_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    search_tool_name: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Search

     Search endpoint for performing web searches.

    Follows the Perplexity Search API spec:
    https://docs.perplexity.ai/api-reference/search-post

    The search_tool_name can be passed either:
    1. In the URL path: /v1/search/{search_tool_name}
    2. In the request body: {\"search_tool_name\": \"...\"}

    Example with search_tool_name in URL (recommended - keeps body Perplexity-compatible):
    ```bash
    curl -X POST \"http://localhost:4000/v1/search/litellm-search\"         -H \"Authorization: Bearer
    sk-1234\"         -H \"Content-Type: application/json\"         -d '{
            \"query\": \"latest AI developments 2024\",
            \"max_results\": 5,
            \"search_domain_filter\": [\"arxiv.org\", \"nature.com\"],
            \"country\": \"US\"
        }'
    ```

    Example with search_tool_name in body:
    ```bash
    curl -X POST \"http://localhost:4000/v1/search\"         -H \"Authorization: Bearer sk-1234\"
    -H \"Content-Type: application/json\"         -d '{
            \"search_tool_name\": \"litellm-search\",
            \"query\": \"latest AI developments 2024\",
            \"max_results\": 5,
            \"search_domain_filter\": [\"arxiv.org\", \"nature.com\"],
            \"country\": \"US\"
        }'
    ```

    Request Body Parameters (when search_tool_name not in URL):
    - search_tool_name (str, required if not in URL): Name of the search tool configured in router
    - query (str or list[str], required): Search query
    - max_results (int, optional): Maximum number of results (1-20), default 10
    - search_domain_filter (list[str], optional): List of domains to filter (max 20)
    - max_tokens_per_page (int, optional): Max tokens per page, default 1024
    - country (str, optional): Country code filter (e.g., 'US', 'GB', 'DE')

    When using URL path parameter, only Perplexity-compatible parameters are needed in body:
    - query (str or list[str], required): Search query
    - max_results (int, optional): Maximum number of results (1-20), default 10
    - search_domain_filter (list[str], optional): List of domains to filter (max 20)
    - max_tokens_per_page (int, optional): Max tokens per page, default 1024
    - country (str, optional): Country code filter (e.g., 'US', 'GB', 'DE')

    Response follows Perplexity Search API format:
    ```json
    {
        \"object\": \"search\",
        \"results\": [
            {
                \"title\": \"Result title\",
                \"url\": \"https://example.com\",
                \"snippet\": \"Result snippet...\",
                \"date\": \"2024-01-01\",
                \"last_updated\": \"2024-01-01\"
            }
        ]
    }
    ```

    Args:
        search_tool_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
search_tool_name=search_tool_name,

    )).parsed
