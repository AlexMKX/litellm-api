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
    client_id: str,
    redirect_uri: str,
    state: str | Unset = '',
    mcp_server_name: None | str | Unset = UNSET,
    code_challenge: None | str | Unset = UNSET,
    code_challenge_method: None | str | Unset = UNSET,
    response_type: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["client_id"] = client_id

    params["redirect_uri"] = redirect_uri

    params["state"] = state

    json_mcp_server_name: None | str | Unset
    if isinstance(mcp_server_name, Unset):
        json_mcp_server_name = UNSET
    else:
        json_mcp_server_name = mcp_server_name
    params["mcp_server_name"] = json_mcp_server_name

    json_code_challenge: None | str | Unset
    if isinstance(code_challenge, Unset):
        json_code_challenge = UNSET
    else:
        json_code_challenge = code_challenge
    params["code_challenge"] = json_code_challenge

    json_code_challenge_method: None | str | Unset
    if isinstance(code_challenge_method, Unset):
        json_code_challenge_method = UNSET
    else:
        json_code_challenge_method = code_challenge_method
    params["code_challenge_method"] = json_code_challenge_method

    json_response_type: None | str | Unset
    if isinstance(response_type, Unset):
        json_response_type = UNSET
    else:
        json_response_type = response_type
    params["response_type"] = json_response_type

    json_scope: None | str | Unset
    if isinstance(scope, Unset):
        json_scope = UNSET
    else:
        json_scope = scope
    params["scope"] = json_scope


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/authorize",
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
    client: AuthenticatedClient | Client,
    client_id: str,
    redirect_uri: str,
    state: str | Unset = '',
    mcp_server_name: None | str | Unset = UNSET,
    code_challenge: None | str | Unset = UNSET,
    code_challenge_method: None | str | Unset = UNSET,
    response_type: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Authorize

    Args:
        client_id (str):
        redirect_uri (str):
        state (str | Unset):  Default: ''.
        mcp_server_name (None | str | Unset):
        code_challenge (None | str | Unset):
        code_challenge_method (None | str | Unset):
        response_type (None | str | Unset):
        scope (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
redirect_uri=redirect_uri,
state=state,
mcp_server_name=mcp_server_name,
code_challenge=code_challenge,
code_challenge_method=code_challenge_method,
response_type=response_type,
scope=scope,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    client_id: str,
    redirect_uri: str,
    state: str | Unset = '',
    mcp_server_name: None | str | Unset = UNSET,
    code_challenge: None | str | Unset = UNSET,
    code_challenge_method: None | str | Unset = UNSET,
    response_type: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Authorize

    Args:
        client_id (str):
        redirect_uri (str):
        state (str | Unset):  Default: ''.
        mcp_server_name (None | str | Unset):
        code_challenge (None | str | Unset):
        code_challenge_method (None | str | Unset):
        response_type (None | str | Unset):
        scope (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
client_id=client_id,
redirect_uri=redirect_uri,
state=state,
mcp_server_name=mcp_server_name,
code_challenge=code_challenge,
code_challenge_method=code_challenge_method,
response_type=response_type,
scope=scope,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    client_id: str,
    redirect_uri: str,
    state: str | Unset = '',
    mcp_server_name: None | str | Unset = UNSET,
    code_challenge: None | str | Unset = UNSET,
    code_challenge_method: None | str | Unset = UNSET,
    response_type: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Authorize

    Args:
        client_id (str):
        redirect_uri (str):
        state (str | Unset):  Default: ''.
        mcp_server_name (None | str | Unset):
        code_challenge (None | str | Unset):
        code_challenge_method (None | str | Unset):
        response_type (None | str | Unset):
        scope (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
redirect_uri=redirect_uri,
state=state,
mcp_server_name=mcp_server_name,
code_challenge=code_challenge,
code_challenge_method=code_challenge_method,
response_type=response_type,
scope=scope,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    client_id: str,
    redirect_uri: str,
    state: str | Unset = '',
    mcp_server_name: None | str | Unset = UNSET,
    code_challenge: None | str | Unset = UNSET,
    code_challenge_method: None | str | Unset = UNSET,
    response_type: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Authorize

    Args:
        client_id (str):
        redirect_uri (str):
        state (str | Unset):  Default: ''.
        mcp_server_name (None | str | Unset):
        code_challenge (None | str | Unset):
        code_challenge_method (None | str | Unset):
        response_type (None | str | Unset):
        scope (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
client_id=client_id,
redirect_uri=redirect_uri,
state=state,
mcp_server_name=mcp_server_name,
code_challenge=code_challenge,
code_challenge_method=code_challenge_method,
response_type=response_type,
scope=scope,

    )).parsed
