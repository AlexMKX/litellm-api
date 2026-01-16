from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/settings",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    r""" Active Callbacks

     Returns a list of litellm level settings

    This is useful for debugging and ensuring the proxy server is configured correctly.

    Response schema:
    ```
    {
        \"alerting\": _alerting,
        \"litellm.callbacks\": litellm_callbacks,
        \"litellm.input_callback\": litellm_input_callbacks,
        \"litellm.failure_callback\": litellm_failure_callbacks,
        \"litellm.success_callback\": litellm_success_callbacks,
        \"litellm._async_success_callback\": litellm_async_success_callbacks,
        \"litellm._async_failure_callback\": litellm_async_failure_callbacks,
        \"litellm._async_input_callback\": litellm_async_input_callbacks,
        \"all_litellm_callbacks\": all_litellm_callbacks,
        \"num_callbacks\": len(all_litellm_callbacks),
        \"num_alerting\": _num_alerting,
        \"litellm.request_timeout\": litellm.request_timeout,
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    r""" Active Callbacks

     Returns a list of litellm level settings

    This is useful for debugging and ensuring the proxy server is configured correctly.

    Response schema:
    ```
    {
        \"alerting\": _alerting,
        \"litellm.callbacks\": litellm_callbacks,
        \"litellm.input_callback\": litellm_input_callbacks,
        \"litellm.failure_callback\": litellm_failure_callbacks,
        \"litellm.success_callback\": litellm_success_callbacks,
        \"litellm._async_success_callback\": litellm_async_success_callbacks,
        \"litellm._async_failure_callback\": litellm_async_failure_callbacks,
        \"litellm._async_input_callback\": litellm_async_input_callbacks,
        \"all_litellm_callbacks\": all_litellm_callbacks,
        \"num_callbacks\": len(all_litellm_callbacks),
        \"num_alerting\": _num_alerting,
        \"litellm.request_timeout\": litellm.request_timeout,
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

