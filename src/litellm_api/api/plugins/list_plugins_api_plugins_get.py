from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_plugins_api_plugins_get_response_200_item import ListPluginsApiPluginsGetResponse200Item
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/plugins",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[ListPluginsApiPluginsGetResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ListPluginsApiPluginsGetResponse200Item.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[ListPluginsApiPluginsGetResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[list[ListPluginsApiPluginsGetResponse200Item]]:
    """ List Plugins

     Return registered plugins for authenticated UI callers.

    plugin_key is never returned — the browser never needs it (the proxy injects
    it server-side from the registry), and exposing it here would leak the
    credential into React state and DevTools.  Admin key management goes through
    the redacted /config/field/info path instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListPluginsApiPluginsGetResponse200Item]]
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

) -> list[ListPluginsApiPluginsGetResponse200Item] | None:
    """ List Plugins

     Return registered plugins for authenticated UI callers.

    plugin_key is never returned — the browser never needs it (the proxy injects
    it server-side from the registry), and exposing it here would leak the
    credential into React state and DevTools.  Admin key management goes through
    the redacted /config/field/info path instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListPluginsApiPluginsGetResponse200Item]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[list[ListPluginsApiPluginsGetResponse200Item]]:
    """ List Plugins

     Return registered plugins for authenticated UI callers.

    plugin_key is never returned — the browser never needs it (the proxy injects
    it server-side from the registry), and exposing it here would leak the
    credential into React state and DevTools.  Admin key management goes through
    the redacted /config/field/info path instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ListPluginsApiPluginsGetResponse200Item]]
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

) -> list[ListPluginsApiPluginsGetResponse200Item] | None:
    """ List Plugins

     Return registered plugins for authenticated UI callers.

    plugin_key is never returned — the browser never needs it (the proxy injects
    it server-side from the registry), and exposing it here would leak the
    credential into React state and DevTools.  Admin key management goes through
    the redacted /config/field/info path instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ListPluginsApiPluginsGetResponse200Item]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
