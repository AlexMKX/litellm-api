from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mcp_semantic_filter_settings_response import MCPSemanticFilterSettingsResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/get/mcp_semantic_filter_settings",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MCPSemanticFilterSettingsResponse | None:
    if response.status_code == 200:
        response_200 = MCPSemanticFilterSettingsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MCPSemanticFilterSettingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[MCPSemanticFilterSettingsResponse]:
    """ Get Mcp Semantic Filter Settings

     Get MCP semantic filter configuration.
    Returns current settings for semantic tool filtering.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MCPSemanticFilterSettingsResponse]
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

) -> MCPSemanticFilterSettingsResponse | None:
    """ Get Mcp Semantic Filter Settings

     Get MCP semantic filter configuration.
    Returns current settings for semantic tool filtering.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MCPSemanticFilterSettingsResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[MCPSemanticFilterSettingsResponse]:
    """ Get Mcp Semantic Filter Settings

     Get MCP semantic filter configuration.
    Returns current settings for semantic tool filtering.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MCPSemanticFilterSettingsResponse]
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

) -> MCPSemanticFilterSettingsResponse | None:
    """ Get Mcp Semantic Filter Settings

     Get MCP semantic filter configuration.
    Returns current settings for semantic tool filtering.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MCPSemanticFilterSettingsResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
