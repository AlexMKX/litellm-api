from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.mcpo_auth_user_credential_request import MCPOAuthUserCredentialRequest
from ...models.mcpo_auth_user_credential_status import MCPOAuthUserCredentialStatus
from typing import cast



def _get_kwargs(
    server_id: str,
    *,
    body: MCPOAuthUserCredentialRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/mcp/server/{server_id}/oauth-user-credential".format(server_id=quote(str(server_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | MCPOAuthUserCredentialStatus | None:
    if response.status_code == 200:
        response_200 = MCPOAuthUserCredentialStatus.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | MCPOAuthUserCredentialStatus]:
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
    body: MCPOAuthUserCredentialRequest,

) -> Response[HTTPValidationError | MCPOAuthUserCredentialStatus]:
    """ Store Mcp Oauth User Credential

     Store the calling user's OAuth2 token for an OpenAPI MCP server

    Args:
        server_id (str):
        body (MCPOAuthUserCredentialRequest): Stores a user's OAuth2 token for an OpenAPI MCP
            server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MCPOAuthUserCredentialStatus]
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
    body: MCPOAuthUserCredentialRequest,

) -> HTTPValidationError | MCPOAuthUserCredentialStatus | None:
    """ Store Mcp Oauth User Credential

     Store the calling user's OAuth2 token for an OpenAPI MCP server

    Args:
        server_id (str):
        body (MCPOAuthUserCredentialRequest): Stores a user's OAuth2 token for an OpenAPI MCP
            server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MCPOAuthUserCredentialStatus
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
    body: MCPOAuthUserCredentialRequest,

) -> Response[HTTPValidationError | MCPOAuthUserCredentialStatus]:
    """ Store Mcp Oauth User Credential

     Store the calling user's OAuth2 token for an OpenAPI MCP server

    Args:
        server_id (str):
        body (MCPOAuthUserCredentialRequest): Stores a user's OAuth2 token for an OpenAPI MCP
            server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MCPOAuthUserCredentialStatus]
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
    body: MCPOAuthUserCredentialRequest,

) -> HTTPValidationError | MCPOAuthUserCredentialStatus | None:
    """ Store Mcp Oauth User Credential

     Store the calling user's OAuth2 token for an OpenAPI MCP server

    Args:
        server_id (str):
        body (MCPOAuthUserCredentialRequest): Stores a user's OAuth2 token for an OpenAPI MCP
            server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MCPOAuthUserCredentialStatus
     """


    return (await asyncio_detailed(
        server_id=server_id,
client=client,
body=body,

    )).parsed
