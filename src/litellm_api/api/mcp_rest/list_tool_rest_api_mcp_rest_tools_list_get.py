from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.list_tool_rest_api_mcp_rest_tools_list_get_response_list_tool_rest_api_mcp_rest_tools_list_get import ListToolRestApiMcpRestToolsListGetResponseListToolRestApiMcpRestToolsListGet
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    server_id: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_server_id: None | str | Unset
    if isinstance(server_id, Unset):
        json_server_id = UNSET
    else:
        json_server_id = server_id
    params["server_id"] = json_server_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/mcp-rest/tools/list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | ListToolRestApiMcpRestToolsListGetResponseListToolRestApiMcpRestToolsListGet | None:
    if response.status_code == 200:
        response_200 = ListToolRestApiMcpRestToolsListGetResponseListToolRestApiMcpRestToolsListGet.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | ListToolRestApiMcpRestToolsListGetResponseListToolRestApiMcpRestToolsListGet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    server_id: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | ListToolRestApiMcpRestToolsListGetResponseListToolRestApiMcpRestToolsListGet]:
    r""" List Tool Rest Api

     List all available tools with information about the server they belong to.

    Example response:
    {
        \"tools\": [
            {
                \"name\": \"create_zap\",
                \"description\": \"Create a new zap\",
                \"inputSchema\": \"tool_input_schema\",
                \"mcp_info\": {
                    \"server_name\": \"zapier\",
                    \"logo_url\": \"https://www.zapier.com/logo.png\",
                }
            }
        ],
        \"error\": null,
        \"message\": \"Successfully retrieved tools\"
    }

    Args:
        server_id (None | str | Unset): The server id to list tools for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListToolRestApiMcpRestToolsListGetResponseListToolRestApiMcpRestToolsListGet]
     """


    kwargs = _get_kwargs(
        server_id=server_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    server_id: None | str | Unset = UNSET,

) -> HTTPValidationError | ListToolRestApiMcpRestToolsListGetResponseListToolRestApiMcpRestToolsListGet | None:
    r""" List Tool Rest Api

     List all available tools with information about the server they belong to.

    Example response:
    {
        \"tools\": [
            {
                \"name\": \"create_zap\",
                \"description\": \"Create a new zap\",
                \"inputSchema\": \"tool_input_schema\",
                \"mcp_info\": {
                    \"server_name\": \"zapier\",
                    \"logo_url\": \"https://www.zapier.com/logo.png\",
                }
            }
        ],
        \"error\": null,
        \"message\": \"Successfully retrieved tools\"
    }

    Args:
        server_id (None | str | Unset): The server id to list tools for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListToolRestApiMcpRestToolsListGetResponseListToolRestApiMcpRestToolsListGet
     """


    return sync_detailed(
        client=client,
server_id=server_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    server_id: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | ListToolRestApiMcpRestToolsListGetResponseListToolRestApiMcpRestToolsListGet]:
    r""" List Tool Rest Api

     List all available tools with information about the server they belong to.

    Example response:
    {
        \"tools\": [
            {
                \"name\": \"create_zap\",
                \"description\": \"Create a new zap\",
                \"inputSchema\": \"tool_input_schema\",
                \"mcp_info\": {
                    \"server_name\": \"zapier\",
                    \"logo_url\": \"https://www.zapier.com/logo.png\",
                }
            }
        ],
        \"error\": null,
        \"message\": \"Successfully retrieved tools\"
    }

    Args:
        server_id (None | str | Unset): The server id to list tools for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListToolRestApiMcpRestToolsListGetResponseListToolRestApiMcpRestToolsListGet]
     """


    kwargs = _get_kwargs(
        server_id=server_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    server_id: None | str | Unset = UNSET,

) -> HTTPValidationError | ListToolRestApiMcpRestToolsListGetResponseListToolRestApiMcpRestToolsListGet | None:
    r""" List Tool Rest Api

     List all available tools with information about the server they belong to.

    Example response:
    {
        \"tools\": [
            {
                \"name\": \"create_zap\",
                \"description\": \"Create a new zap\",
                \"inputSchema\": \"tool_input_schema\",
                \"mcp_info\": {
                    \"server_name\": \"zapier\",
                    \"logo_url\": \"https://www.zapier.com/logo.png\",
                }
            }
        ],
        \"error\": null,
        \"message\": \"Successfully retrieved tools\"
    }

    Args:
        server_id (None | str | Unset): The server id to list tools for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListToolRestApiMcpRestToolsListGetResponseListToolRestApiMcpRestToolsListGet
     """


    return (await asyncio_detailed(
        client=client,
server_id=server_id,

    )).parsed
