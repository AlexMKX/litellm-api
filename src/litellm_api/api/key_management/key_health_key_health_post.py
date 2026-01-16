from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.key_health_response import KeyHealthResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/key/health",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> KeyHealthResponse | None:
    if response.status_code == 200:
        response_200 = KeyHealthResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[KeyHealthResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[KeyHealthResponse]:
    r""" Key Health

     Check the health of the key

    Checks:
    - If key based logging is configured correctly - sends a test log

    Usage

    Pass the key in the request header

    ```bash
    curl -X POST \"http://localhost:4000/key/health\"      -H \"Authorization: Bearer sk-1234\"      -H
    \"Content-Type: application/json\"
    ```

    Response when logging callbacks are setup correctly:

    ```json
    {
      \"key\": \"healthy\",
      \"logging_callbacks\": {
        \"callbacks\": [
          \"gcs_bucket\"
        ],
        \"status\": \"healthy\",
        \"details\": \"No logger exceptions triggered, system is healthy. Manually check if logs were
    sent to ['gcs_bucket']\"
      }
    }
    ```


    Response when logging callbacks are not setup correctly:
    ```json
    {
      \"key\": \"unhealthy\",
      \"logging_callbacks\": {
        \"callbacks\": [
          \"gcs_bucket\"
        ],
        \"status\": \"unhealthy\",
        \"details\": \"Logger exceptions triggered, system is unhealthy: Failed to load vertex
    credentials. Check to see if credentials containing partial/invalid information.\"
      }
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KeyHealthResponse]
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

) -> KeyHealthResponse | None:
    r""" Key Health

     Check the health of the key

    Checks:
    - If key based logging is configured correctly - sends a test log

    Usage

    Pass the key in the request header

    ```bash
    curl -X POST \"http://localhost:4000/key/health\"      -H \"Authorization: Bearer sk-1234\"      -H
    \"Content-Type: application/json\"
    ```

    Response when logging callbacks are setup correctly:

    ```json
    {
      \"key\": \"healthy\",
      \"logging_callbacks\": {
        \"callbacks\": [
          \"gcs_bucket\"
        ],
        \"status\": \"healthy\",
        \"details\": \"No logger exceptions triggered, system is healthy. Manually check if logs were
    sent to ['gcs_bucket']\"
      }
    }
    ```


    Response when logging callbacks are not setup correctly:
    ```json
    {
      \"key\": \"unhealthy\",
      \"logging_callbacks\": {
        \"callbacks\": [
          \"gcs_bucket\"
        ],
        \"status\": \"unhealthy\",
        \"details\": \"Logger exceptions triggered, system is unhealthy: Failed to load vertex
    credentials. Check to see if credentials containing partial/invalid information.\"
      }
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KeyHealthResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[KeyHealthResponse]:
    r""" Key Health

     Check the health of the key

    Checks:
    - If key based logging is configured correctly - sends a test log

    Usage

    Pass the key in the request header

    ```bash
    curl -X POST \"http://localhost:4000/key/health\"      -H \"Authorization: Bearer sk-1234\"      -H
    \"Content-Type: application/json\"
    ```

    Response when logging callbacks are setup correctly:

    ```json
    {
      \"key\": \"healthy\",
      \"logging_callbacks\": {
        \"callbacks\": [
          \"gcs_bucket\"
        ],
        \"status\": \"healthy\",
        \"details\": \"No logger exceptions triggered, system is healthy. Manually check if logs were
    sent to ['gcs_bucket']\"
      }
    }
    ```


    Response when logging callbacks are not setup correctly:
    ```json
    {
      \"key\": \"unhealthy\",
      \"logging_callbacks\": {
        \"callbacks\": [
          \"gcs_bucket\"
        ],
        \"status\": \"unhealthy\",
        \"details\": \"Logger exceptions triggered, system is unhealthy: Failed to load vertex
    credentials. Check to see if credentials containing partial/invalid information.\"
      }
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KeyHealthResponse]
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

) -> KeyHealthResponse | None:
    r""" Key Health

     Check the health of the key

    Checks:
    - If key based logging is configured correctly - sends a test log

    Usage

    Pass the key in the request header

    ```bash
    curl -X POST \"http://localhost:4000/key/health\"      -H \"Authorization: Bearer sk-1234\"      -H
    \"Content-Type: application/json\"
    ```

    Response when logging callbacks are setup correctly:

    ```json
    {
      \"key\": \"healthy\",
      \"logging_callbacks\": {
        \"callbacks\": [
          \"gcs_bucket\"
        ],
        \"status\": \"healthy\",
        \"details\": \"No logger exceptions triggered, system is healthy. Manually check if logs were
    sent to ['gcs_bucket']\"
      }
    }
    ```


    Response when logging callbacks are not setup correctly:
    ```json
    {
      \"key\": \"unhealthy\",
      \"logging_callbacks\": {
        \"callbacks\": [
          \"gcs_bucket\"
        ],
        \"status\": \"unhealthy\",
        \"details\": \"Logger exceptions triggered, system is unhealthy: Failed to load vertex
    credentials. Check to see if credentials containing partial/invalid information.\"
      }
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KeyHealthResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
