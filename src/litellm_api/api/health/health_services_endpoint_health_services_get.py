from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.health_services_endpoint_health_services_get_service_type_0 import HealthServicesEndpointHealthServicesGetServiceType0
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    *,
    service: HealthServicesEndpointHealthServicesGetServiceType0 | str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_service: str
    if isinstance(service, HealthServicesEndpointHealthServicesGetServiceType0):
        json_service = service.value
    else:
        json_service = service
    params["service"] = json_service


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/health/services",
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
    client: AuthenticatedClient,
    service: HealthServicesEndpointHealthServicesGetServiceType0 | str,

) -> Response[Any | HTTPValidationError]:
    """ Health Services Endpoint

     Use this admin-only endpoint to check if the service is healthy.

    Example:
    ```
    curl -L -X GET 'http://0.0.0.0:4000/health/services?service=datadog'     -H 'Authorization: Bearer
    sk-1234'
    ```

    Args:
        service (HealthServicesEndpointHealthServicesGetServiceType0 | str): Specify the service
            being hit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        service=service,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    service: HealthServicesEndpointHealthServicesGetServiceType0 | str,

) -> Any | HTTPValidationError | None:
    """ Health Services Endpoint

     Use this admin-only endpoint to check if the service is healthy.

    Example:
    ```
    curl -L -X GET 'http://0.0.0.0:4000/health/services?service=datadog'     -H 'Authorization: Bearer
    sk-1234'
    ```

    Args:
        service (HealthServicesEndpointHealthServicesGetServiceType0 | str): Specify the service
            being hit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
service=service,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    service: HealthServicesEndpointHealthServicesGetServiceType0 | str,

) -> Response[Any | HTTPValidationError]:
    """ Health Services Endpoint

     Use this admin-only endpoint to check if the service is healthy.

    Example:
    ```
    curl -L -X GET 'http://0.0.0.0:4000/health/services?service=datadog'     -H 'Authorization: Bearer
    sk-1234'
    ```

    Args:
        service (HealthServicesEndpointHealthServicesGetServiceType0 | str): Specify the service
            being hit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        service=service,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    service: HealthServicesEndpointHealthServicesGetServiceType0 | str,

) -> Any | HTTPValidationError | None:
    """ Health Services Endpoint

     Use this admin-only endpoint to check if the service is healthy.

    Example:
    ```
    curl -L -X GET 'http://0.0.0.0:4000/health/services?service=datadog'     -H 'Authorization: Bearer
    sk-1234'
    ```

    Args:
        service (HealthServicesEndpointHealthServicesGetServiceType0 | str): Specify the service
            being hit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
service=service,

    )).parsed
