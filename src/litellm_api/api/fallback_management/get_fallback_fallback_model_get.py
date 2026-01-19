from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.fallback_get_response import FallbackGetResponse
from ...models.get_fallback_fallback_model_get_fallback_type import GetFallbackFallbackModelGetFallbackType
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    model: str,
    *,
    fallback_type: GetFallbackFallbackModelGetFallbackType | Unset = GetFallbackFallbackModelGetFallbackType.GENERAL,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_fallback_type: str | Unset = UNSET
    if not isinstance(fallback_type, Unset):
        json_fallback_type = fallback_type.value

    params["fallback_type"] = json_fallback_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fallback/{model}".format(model=quote(str(model), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FallbackGetResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FallbackGetResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FallbackGetResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model: str,
    *,
    client: AuthenticatedClient,
    fallback_type: GetFallbackFallbackModelGetFallbackType | Unset = GetFallbackFallbackModelGetFallbackType.GENERAL,

) -> Response[FallbackGetResponse | HTTPValidationError]:
    """ Get Fallback

     Get fallback configuration for a specific model.

    **Parameters:**
    - `model`: The model name to get fallbacks for
    - `fallback_type`: Type of fallback to retrieve (query parameter)

    **Example:**
    ```
    GET /fallback/gpt-3.5-turbo?fallback_type=general
    ```

    Args:
        model (str):
        fallback_type (GetFallbackFallbackModelGetFallbackType | Unset):  Default:
            GetFallbackFallbackModelGetFallbackType.GENERAL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FallbackGetResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        model=model,
fallback_type=fallback_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    model: str,
    *,
    client: AuthenticatedClient,
    fallback_type: GetFallbackFallbackModelGetFallbackType | Unset = GetFallbackFallbackModelGetFallbackType.GENERAL,

) -> FallbackGetResponse | HTTPValidationError | None:
    """ Get Fallback

     Get fallback configuration for a specific model.

    **Parameters:**
    - `model`: The model name to get fallbacks for
    - `fallback_type`: Type of fallback to retrieve (query parameter)

    **Example:**
    ```
    GET /fallback/gpt-3.5-turbo?fallback_type=general
    ```

    Args:
        model (str):
        fallback_type (GetFallbackFallbackModelGetFallbackType | Unset):  Default:
            GetFallbackFallbackModelGetFallbackType.GENERAL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FallbackGetResponse | HTTPValidationError
     """


    return sync_detailed(
        model=model,
client=client,
fallback_type=fallback_type,

    ).parsed

async def asyncio_detailed(
    model: str,
    *,
    client: AuthenticatedClient,
    fallback_type: GetFallbackFallbackModelGetFallbackType | Unset = GetFallbackFallbackModelGetFallbackType.GENERAL,

) -> Response[FallbackGetResponse | HTTPValidationError]:
    """ Get Fallback

     Get fallback configuration for a specific model.

    **Parameters:**
    - `model`: The model name to get fallbacks for
    - `fallback_type`: Type of fallback to retrieve (query parameter)

    **Example:**
    ```
    GET /fallback/gpt-3.5-turbo?fallback_type=general
    ```

    Args:
        model (str):
        fallback_type (GetFallbackFallbackModelGetFallbackType | Unset):  Default:
            GetFallbackFallbackModelGetFallbackType.GENERAL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FallbackGetResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        model=model,
fallback_type=fallback_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    model: str,
    *,
    client: AuthenticatedClient,
    fallback_type: GetFallbackFallbackModelGetFallbackType | Unset = GetFallbackFallbackModelGetFallbackType.GENERAL,

) -> FallbackGetResponse | HTTPValidationError | None:
    """ Get Fallback

     Get fallback configuration for a specific model.

    **Parameters:**
    - `model`: The model name to get fallbacks for
    - `fallback_type`: Type of fallback to retrieve (query parameter)

    **Example:**
    ```
    GET /fallback/gpt-3.5-turbo?fallback_type=general
    ```

    Args:
        model (str):
        fallback_type (GetFallbackFallbackModelGetFallbackType | Unset):  Default:
            GetFallbackFallbackModelGetFallbackType.GENERAL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FallbackGetResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        model=model,
client=client,
fallback_type=fallback_type,

    )).parsed
