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
    model: None | str | Unset = UNSET,
    model_id: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_model: None | str | Unset
    if isinstance(model, Unset):
        json_model = UNSET
    else:
        json_model = model
    params["model"] = json_model

    json_model_id: None | str | Unset
    if isinstance(model_id, Unset):
        json_model_id = UNSET
    else:
        json_model_id = model_id
    params["model_id"] = json_model_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/health",
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
    model: None | str | Unset = UNSET,
    model_id: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Health Endpoint

     🚨 USE `/health/liveliness` to health check the proxy 🚨

    See more 👉 https://docs.litellm.ai/docs/proxy/health


    Check the health of all the endpoints in config.yaml

    To run health checks in the background, add this to config.yaml:
    ```
    general_settings:
        # ... other settings
        background_health_checks: True
    ```
    else, the health checks will be run on models when /health is called.

    Args:
        model (None | str | Unset): Specify the model name (optional)
        model_id (None | str | Unset): Specify the model ID (optional)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        model=model,
model_id=model_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    model: None | str | Unset = UNSET,
    model_id: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Health Endpoint

     🚨 USE `/health/liveliness` to health check the proxy 🚨

    See more 👉 https://docs.litellm.ai/docs/proxy/health


    Check the health of all the endpoints in config.yaml

    To run health checks in the background, add this to config.yaml:
    ```
    general_settings:
        # ... other settings
        background_health_checks: True
    ```
    else, the health checks will be run on models when /health is called.

    Args:
        model (None | str | Unset): Specify the model name (optional)
        model_id (None | str | Unset): Specify the model ID (optional)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
model=model,
model_id=model_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    model: None | str | Unset = UNSET,
    model_id: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Health Endpoint

     🚨 USE `/health/liveliness` to health check the proxy 🚨

    See more 👉 https://docs.litellm.ai/docs/proxy/health


    Check the health of all the endpoints in config.yaml

    To run health checks in the background, add this to config.yaml:
    ```
    general_settings:
        # ... other settings
        background_health_checks: True
    ```
    else, the health checks will be run on models when /health is called.

    Args:
        model (None | str | Unset): Specify the model name (optional)
        model_id (None | str | Unset): Specify the model ID (optional)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        model=model,
model_id=model_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    model: None | str | Unset = UNSET,
    model_id: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Health Endpoint

     🚨 USE `/health/liveliness` to health check the proxy 🚨

    See more 👉 https://docs.litellm.ai/docs/proxy/health


    Check the health of all the endpoints in config.yaml

    To run health checks in the background, add this to config.yaml:
    ```
    general_settings:
        # ... other settings
        background_health_checks: True
    ```
    else, the health checks will be run on models when /health is called.

    Args:
        model (None | str | Unset): Specify the model name (optional)
        model_id (None | str | Unset): Specify the model ID (optional)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
model=model,
model_id=model_id,

    )).parsed
