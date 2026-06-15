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
        "url": "/health/drain",
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
    client: AuthenticatedClient | Client,

) -> Response[Any]:
    """ Health Drain

     Graceful-drain probe for Kubernetes ``preStop`` hooks.

    Disabled by default and returns 404 unless ``general_settings`` sets
    ``enable_drain_endpoint: true``. Calling it flips a process-wide
    shutting-down flag, so a successful call permanently takes the worker out
    of rotation until the pod restarts.

    Because the kubelet calls preStop hooks without proxy credentials, the
    endpoint does not require ``user_api_key_auth``. To prevent any
    pod-reachable caller from triggering shutdown, set
    ``general_settings.drain_endpoint_token`` (or the ``DRAIN_ENDPOINT_TOKEN``
    env var) and supply the same value on the ``X-Drain-Token`` header from
    the preStop hook. Calls without the header (or with a wrong value) get a
    401 and have no side effect.

    When enabled, it marks the worker as shutting down (so /health/readiness
    and /health/liveliness immediately start returning 503, removing the pod
    from service) and blocks until the in-flight request counter drains to
    zero or ``GRACEFUL_SHUTDOWN_TIMEOUT`` elapses. Unlike a fixed ``sleep``,
    this returns as soon as real in-flight work is done.

    Wire it up as:

    ```yaml
    lifecycle:
      preStop:
        httpGet:
          path: /health/drain
          port: 4000
          httpHeaders:
            - name: X-Drain-Token
              value: <same value as drain_endpoint_token>
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
    client: AuthenticatedClient | Client,

) -> Response[Any]:
    """ Health Drain

     Graceful-drain probe for Kubernetes ``preStop`` hooks.

    Disabled by default and returns 404 unless ``general_settings`` sets
    ``enable_drain_endpoint: true``. Calling it flips a process-wide
    shutting-down flag, so a successful call permanently takes the worker out
    of rotation until the pod restarts.

    Because the kubelet calls preStop hooks without proxy credentials, the
    endpoint does not require ``user_api_key_auth``. To prevent any
    pod-reachable caller from triggering shutdown, set
    ``general_settings.drain_endpoint_token`` (or the ``DRAIN_ENDPOINT_TOKEN``
    env var) and supply the same value on the ``X-Drain-Token`` header from
    the preStop hook. Calls without the header (or with a wrong value) get a
    401 and have no side effect.

    When enabled, it marks the worker as shutting down (so /health/readiness
    and /health/liveliness immediately start returning 503, removing the pod
    from service) and blocks until the in-flight request counter drains to
    zero or ``GRACEFUL_SHUTDOWN_TIMEOUT`` elapses. Unlike a fixed ``sleep``,
    this returns as soon as real in-flight work is done.

    Wire it up as:

    ```yaml
    lifecycle:
      preStop:
        httpGet:
          path: /health/drain
          port: 4000
          httpHeaders:
            - name: X-Drain-Token
              value: <same value as drain_endpoint_token>
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

