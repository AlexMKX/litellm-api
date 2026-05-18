from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.mcp_user_credential_request import MCPUserCredentialRequest
from ...models.mcp_user_credential_response import MCPUserCredentialResponse
from typing import cast



def _get_kwargs(
    server_id: str,
    *,
    body: MCPUserCredentialRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/mcp/server/{server_id}/user-credential".format(server_id=quote(str(server_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | MCPUserCredentialResponse | None:
    if response.status_code == 200:
        response_200 = MCPUserCredentialResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | MCPUserCredentialResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    server_id: str,
    *,
    client: AuthenticatedClient,
    body: MCPUserCredentialRequest,

) -> Response[HTTPValidationError | MCPUserCredentialResponse]:
    """ Store Mcp User Credential

     Store or update the calling user's API key for a BYOK MCP server

    Args:
        server_id (str):
        body (MCPUserCredentialRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MCPUserCredentialResponse]
     """


    kwargs = _get_kwargs(
        server_id=server_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    server_id: str,
    *,
    client: AuthenticatedClient,
    body: MCPUserCredentialRequest,

) -> HTTPValidationError | MCPUserCredentialResponse | None:
    """ Store Mcp User Credential

     Store or update the calling user's API key for a BYOK MCP server

    Args:
        server_id (str):
        body (MCPUserCredentialRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MCPUserCredentialResponse
     """


    return sync_detailed(
        server_id=server_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    server_id: str,
    *,
    client: AuthenticatedClient,
    body: MCPUserCredentialRequest,

) -> Response[HTTPValidationError | MCPUserCredentialResponse]:
    """ Store Mcp User Credential

     Store or update the calling user's API key for a BYOK MCP server

    Args:
        server_id (str):
        body (MCPUserCredentialRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MCPUserCredentialResponse]
     """


    kwargs = _get_kwargs(
        server_id=server_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    server_id: str,
    *,
    client: AuthenticatedClient,
    body: MCPUserCredentialRequest,

) -> HTTPValidationError | MCPUserCredentialResponse | None:
    """ Store Mcp User Credential

     Store or update the calling user's API key for a BYOK MCP server

    Args:
        server_id (str):
        body (MCPUserCredentialRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MCPUserCredentialResponse
     """


    return (await asyncio_detailed(
        server_id=server_id,
client=client,
body=body,

    )).parsed
