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
        "method": "get",
        "url": "/search/tools",
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
    r""" List Search Tools

     List all available search tools configured in the router.

    This endpoint returns the search tools that are currently loaded and available
    for use with the /v1/search endpoint.

    Example:
    ```bash
    curl -X GET \"http://localhost:4000/v1/search/tools\"         -H \"Authorization: Bearer sk-1234\"
    ```

    Response:
    ```json
    {
        \"object\": \"list\",
        \"data\": [
            {
                \"search_tool_name\": \"litellm-search\",
                \"search_provider\": \"perplexity\",
                \"description\": \"Perplexity search tool\"
            }
        ]
    }
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
    r""" List Search Tools

     List all available search tools configured in the router.

    This endpoint returns the search tools that are currently loaded and available
    for use with the /v1/search endpoint.

    Example:
    ```bash
    curl -X GET \"http://localhost:4000/v1/search/tools\"         -H \"Authorization: Bearer sk-1234\"
    ```

    Response:
    ```json
    {
        \"object\": \"list\",
        \"data\": [
            {
                \"search_tool_name\": \"litellm-search\",
                \"search_provider\": \"perplexity\",
                \"description\": \"Perplexity search tool\"
            }
        ]
    }
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

