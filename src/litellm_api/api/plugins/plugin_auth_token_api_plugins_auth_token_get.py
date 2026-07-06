from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.plugin_auth_token_api_plugins_auth_token_get_response_plugin_auth_token_api_plugins_auth_token_get import PluginAuthTokenApiPluginsAuthTokenGetResponsePluginAuthTokenApiPluginsAuthTokenGet
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    plugin_name: str | Unset = 'litellm-platform-plugin',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["plugin_name"] = plugin_name


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/plugins/auth-token",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | PluginAuthTokenApiPluginsAuthTokenGetResponsePluginAuthTokenApiPluginsAuthTokenGet | None:
    if response.status_code == 200:
        response_200 = PluginAuthTokenApiPluginsAuthTokenGetResponsePluginAuthTokenApiPluginsAuthTokenGet.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | PluginAuthTokenApiPluginsAuthTokenGetResponsePluginAuthTokenApiPluginsAuthTokenGet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    plugin_name: str | Unset = 'litellm-platform-plugin',

) -> Response[HTTPValidationError | PluginAuthTokenApiPluginsAuthTokenGetResponsePluginAuthTokenApiPluginsAuthTokenGet]:
    """ Plugin Auth Token

     Issue a short-lived, audience-scoped plugin session claim.

    The claim contains {user_id, user_role, plugin, exp}.  It does NOT
    contain the caller's litellm bearer token — a compromised plugin can
    only learn the caller's identity, not impersonate them against the proxy.

    Encrypted with a key derived from HMAC(LITELLM_SALT_KEY, plugin_name),
    so each plugin holds only its own key and cannot forge claims for others.

    Requires LITELLM_SALT_KEY to be set; returns 503 otherwise.

    Args:
        plugin_name (str | Unset):  Default: 'litellm-platform-plugin'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PluginAuthTokenApiPluginsAuthTokenGetResponsePluginAuthTokenApiPluginsAuthTokenGet]
     """


    kwargs = _get_kwargs(
        plugin_name=plugin_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    plugin_name: str | Unset = 'litellm-platform-plugin',

) -> HTTPValidationError | PluginAuthTokenApiPluginsAuthTokenGetResponsePluginAuthTokenApiPluginsAuthTokenGet | None:
    """ Plugin Auth Token

     Issue a short-lived, audience-scoped plugin session claim.

    The claim contains {user_id, user_role, plugin, exp}.  It does NOT
    contain the caller's litellm bearer token — a compromised plugin can
    only learn the caller's identity, not impersonate them against the proxy.

    Encrypted with a key derived from HMAC(LITELLM_SALT_KEY, plugin_name),
    so each plugin holds only its own key and cannot forge claims for others.

    Requires LITELLM_SALT_KEY to be set; returns 503 otherwise.

    Args:
        plugin_name (str | Unset):  Default: 'litellm-platform-plugin'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PluginAuthTokenApiPluginsAuthTokenGetResponsePluginAuthTokenApiPluginsAuthTokenGet
     """


    return sync_detailed(
        client=client,
plugin_name=plugin_name,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    plugin_name: str | Unset = 'litellm-platform-plugin',

) -> Response[HTTPValidationError | PluginAuthTokenApiPluginsAuthTokenGetResponsePluginAuthTokenApiPluginsAuthTokenGet]:
    """ Plugin Auth Token

     Issue a short-lived, audience-scoped plugin session claim.

    The claim contains {user_id, user_role, plugin, exp}.  It does NOT
    contain the caller's litellm bearer token — a compromised plugin can
    only learn the caller's identity, not impersonate them against the proxy.

    Encrypted with a key derived from HMAC(LITELLM_SALT_KEY, plugin_name),
    so each plugin holds only its own key and cannot forge claims for others.

    Requires LITELLM_SALT_KEY to be set; returns 503 otherwise.

    Args:
        plugin_name (str | Unset):  Default: 'litellm-platform-plugin'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PluginAuthTokenApiPluginsAuthTokenGetResponsePluginAuthTokenApiPluginsAuthTokenGet]
     """


    kwargs = _get_kwargs(
        plugin_name=plugin_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    plugin_name: str | Unset = 'litellm-platform-plugin',

) -> HTTPValidationError | PluginAuthTokenApiPluginsAuthTokenGetResponsePluginAuthTokenApiPluginsAuthTokenGet | None:
    """ Plugin Auth Token

     Issue a short-lived, audience-scoped plugin session claim.

    The claim contains {user_id, user_role, plugin, exp}.  It does NOT
    contain the caller's litellm bearer token — a compromised plugin can
    only learn the caller's identity, not impersonate them against the proxy.

    Encrypted with a key derived from HMAC(LITELLM_SALT_KEY, plugin_name),
    so each plugin holds only its own key and cannot forge claims for others.

    Requires LITELLM_SALT_KEY to be set; returns 503 otherwise.

    Args:
        plugin_name (str | Unset):  Default: 'litellm-platform-plugin'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PluginAuthTokenApiPluginsAuthTokenGetResponsePluginAuthTokenApiPluginsAuthTokenGet
     """


    return (await asyncio_detailed(
        client=client,
plugin_name=plugin_name,

    )).parsed
