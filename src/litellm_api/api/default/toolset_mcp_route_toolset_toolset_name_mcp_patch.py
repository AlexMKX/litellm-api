from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    toolset_name: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/toolset/{toolset_name}/mcp".format(toolset_name=quote(str(toolset_name), safe=""),),
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
    toolset_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | HTTPValidationError]:
    """ Toolset Mcp Route

     Namespace a toolset as its own MCP endpoint.

    Connecting to /toolset/<name>/mcp exposes exactly the tools defined in
    the toolset. Access is enforced: non-admin API keys must have the toolset
    listed in their object_permission.mcp_toolsets grant list, or the request
    will be rejected with a 403.

    Args:
        toolset_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        toolset_name=toolset_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    toolset_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | HTTPValidationError | None:
    """ Toolset Mcp Route

     Namespace a toolset as its own MCP endpoint.

    Connecting to /toolset/<name>/mcp exposes exactly the tools defined in
    the toolset. Access is enforced: non-admin API keys must have the toolset
    listed in their object_permission.mcp_toolsets grant list, or the request
    will be rejected with a 403.

    Args:
        toolset_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        toolset_name=toolset_name,
client=client,

    ).parsed

async def asyncio_detailed(
    toolset_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | HTTPValidationError]:
    """ Toolset Mcp Route

     Namespace a toolset as its own MCP endpoint.

    Connecting to /toolset/<name>/mcp exposes exactly the tools defined in
    the toolset. Access is enforced: non-admin API keys must have the toolset
    listed in their object_permission.mcp_toolsets grant list, or the request
    will be rejected with a 403.

    Args:
        toolset_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        toolset_name=toolset_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    toolset_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | HTTPValidationError | None:
    """ Toolset Mcp Route

     Namespace a toolset as its own MCP endpoint.

    Connecting to /toolset/<name>/mcp exposes exactly the tools defined in
    the toolset. Access is enforced: non-admin API keys must have the toolset
    listed in their object_permission.mcp_toolsets grant list, or the request
    will be rejected with a 403.

    Args:
        toolset_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        toolset_name=toolset_name,
client=client,

    )).parsed
