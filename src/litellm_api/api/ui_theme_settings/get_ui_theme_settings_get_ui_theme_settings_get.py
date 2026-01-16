from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ui_theme_settings_response import UIThemeSettingsResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/get/ui_theme_settings",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UIThemeSettingsResponse | None:
    if response.status_code == 200:
        response_200 = UIThemeSettingsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UIThemeSettingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[UIThemeSettingsResponse]:
    """ Get Ui Theme Settings

     Get UI theme configuration from the litellm_settings.
    Returns current logo settings for UI customization.

    Note: This endpoint is public (no authentication required) so all users can see custom branding.
    Only the /update/ui_theme_settings endpoint requires authentication for admins to change settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UIThemeSettingsResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> UIThemeSettingsResponse | None:
    """ Get Ui Theme Settings

     Get UI theme configuration from the litellm_settings.
    Returns current logo settings for UI customization.

    Note: This endpoint is public (no authentication required) so all users can see custom branding.
    Only the /update/ui_theme_settings endpoint requires authentication for admins to change settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UIThemeSettingsResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[UIThemeSettingsResponse]:
    """ Get Ui Theme Settings

     Get UI theme configuration from the litellm_settings.
    Returns current logo settings for UI customization.

    Note: This endpoint is public (no authentication required) so all users can see custom branding.
    Only the /update/ui_theme_settings endpoint requires authentication for admins to change settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UIThemeSettingsResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> UIThemeSettingsResponse | None:
    """ Get Ui Theme Settings

     Get UI theme configuration from the litellm_settings.
    Returns current logo settings for UI customization.

    Note: This endpoint is public (no authentication required) so all users can see custom branding.
    Only the /update/ui_theme_settings endpoint requires authentication for admins to change settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UIThemeSettingsResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
