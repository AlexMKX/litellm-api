from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.body_token_endpoint_token_post import BodyTokenEndpointTokenPost
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: BodyTokenEndpointTokenPost,
    mcp_server_name: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_mcp_server_name: None | str | Unset
    if isinstance(mcp_server_name, Unset):
        json_mcp_server_name = UNSET
    else:
        json_mcp_server_name = mcp_server_name
    params["mcp_server_name"] = json_mcp_server_name


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/token",
        "params": params,
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

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
    client: AuthenticatedClient | Client,
    body: BodyTokenEndpointTokenPost,
    mcp_server_name: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Token Endpoint

     Accept the authorization code from client and exchange it for OAuth token.
    Supports PKCE flow by forwarding code_verifier to upstream provider.

    1. Call the token endpoint with PKCE parameters
    2. Store the user's token in the db - and generate a LiteLLM virtual key
    3. Return the token
    4. Return a virtual key in this response

    Args:
        mcp_server_name (None | str | Unset):
        body (BodyTokenEndpointTokenPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        body=body,
mcp_server_name=mcp_server_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BodyTokenEndpointTokenPost,
    mcp_server_name: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Token Endpoint

     Accept the authorization code from client and exchange it for OAuth token.
    Supports PKCE flow by forwarding code_verifier to upstream provider.

    1. Call the token endpoint with PKCE parameters
    2. Store the user's token in the db - and generate a LiteLLM virtual key
    3. Return the token
    4. Return a virtual key in this response

    Args:
        mcp_server_name (None | str | Unset):
        body (BodyTokenEndpointTokenPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,
mcp_server_name=mcp_server_name,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyTokenEndpointTokenPost,
    mcp_server_name: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Token Endpoint

     Accept the authorization code from client and exchange it for OAuth token.
    Supports PKCE flow by forwarding code_verifier to upstream provider.

    1. Call the token endpoint with PKCE parameters
    2. Store the user's token in the db - and generate a LiteLLM virtual key
    3. Return the token
    4. Return a virtual key in this response

    Args:
        mcp_server_name (None | str | Unset):
        body (BodyTokenEndpointTokenPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        body=body,
mcp_server_name=mcp_server_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BodyTokenEndpointTokenPost,
    mcp_server_name: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Token Endpoint

     Accept the authorization code from client and exchange it for OAuth token.
    Supports PKCE flow by forwarding code_verifier to upstream provider.

    1. Call the token endpoint with PKCE parameters
    2. Store the user's token in the db - and generate a LiteLLM virtual key
    3. Return the token
    4. Return a virtual key in this response

    Args:
        mcp_server_name (None | str | Unset):
        body (BodyTokenEndpointTokenPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,
mcp_server_name=mcp_server_name,

    )).parsed
