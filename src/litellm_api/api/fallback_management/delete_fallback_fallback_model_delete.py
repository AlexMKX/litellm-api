from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_fallback_fallback_model_delete_fallback_type import DeleteFallbackFallbackModelDeleteFallbackType
from ...models.fallback_delete_response import FallbackDeleteResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    model: str,
    *,
    fallback_type: DeleteFallbackFallbackModelDeleteFallbackType | Unset = DeleteFallbackFallbackModelDeleteFallbackType.GENERAL,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_fallback_type: str | Unset = UNSET
    if not isinstance(fallback_type, Unset):
        json_fallback_type = fallback_type.value

    params["fallback_type"] = json_fallback_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/fallback/{model}".format(model=quote(str(model), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FallbackDeleteResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FallbackDeleteResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FallbackDeleteResponse | HTTPValidationError]:
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
    fallback_type: DeleteFallbackFallbackModelDeleteFallbackType | Unset = DeleteFallbackFallbackModelDeleteFallbackType.GENERAL,

) -> Response[FallbackDeleteResponse | HTTPValidationError]:
    """ Delete Fallback

     Delete fallback configuration for a specific model.

    **Parameters:**
    - `model`: The model name to delete fallbacks for
    - `fallback_type`: Type of fallback to delete (query parameter)

    **Example:**
    ```
    DELETE /fallback/gpt-3.5-turbo?fallback_type=general
    ```

    Args:
        model (str):
        fallback_type (DeleteFallbackFallbackModelDeleteFallbackType | Unset):  Default:
            DeleteFallbackFallbackModelDeleteFallbackType.GENERAL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FallbackDeleteResponse | HTTPValidationError]
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
    fallback_type: DeleteFallbackFallbackModelDeleteFallbackType | Unset = DeleteFallbackFallbackModelDeleteFallbackType.GENERAL,

) -> FallbackDeleteResponse | HTTPValidationError | None:
    """ Delete Fallback

     Delete fallback configuration for a specific model.

    **Parameters:**
    - `model`: The model name to delete fallbacks for
    - `fallback_type`: Type of fallback to delete (query parameter)

    **Example:**
    ```
    DELETE /fallback/gpt-3.5-turbo?fallback_type=general
    ```

    Args:
        model (str):
        fallback_type (DeleteFallbackFallbackModelDeleteFallbackType | Unset):  Default:
            DeleteFallbackFallbackModelDeleteFallbackType.GENERAL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FallbackDeleteResponse | HTTPValidationError
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
    fallback_type: DeleteFallbackFallbackModelDeleteFallbackType | Unset = DeleteFallbackFallbackModelDeleteFallbackType.GENERAL,

) -> Response[FallbackDeleteResponse | HTTPValidationError]:
    """ Delete Fallback

     Delete fallback configuration for a specific model.

    **Parameters:**
    - `model`: The model name to delete fallbacks for
    - `fallback_type`: Type of fallback to delete (query parameter)

    **Example:**
    ```
    DELETE /fallback/gpt-3.5-turbo?fallback_type=general
    ```

    Args:
        model (str):
        fallback_type (DeleteFallbackFallbackModelDeleteFallbackType | Unset):  Default:
            DeleteFallbackFallbackModelDeleteFallbackType.GENERAL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FallbackDeleteResponse | HTTPValidationError]
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
    fallback_type: DeleteFallbackFallbackModelDeleteFallbackType | Unset = DeleteFallbackFallbackModelDeleteFallbackType.GENERAL,

) -> FallbackDeleteResponse | HTTPValidationError | None:
    """ Delete Fallback

     Delete fallback configuration for a specific model.

    **Parameters:**
    - `model`: The model name to delete fallbacks for
    - `fallback_type`: Type of fallback to delete (query parameter)

    **Example:**
    ```
    DELETE /fallback/gpt-3.5-turbo?fallback_type=general
    ```

    Args:
        model (str):
        fallback_type (DeleteFallbackFallbackModelDeleteFallbackType | Unset):  Default:
            DeleteFallbackFallbackModelDeleteFallbackType.GENERAL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FallbackDeleteResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        model=model,
client=client,
fallback_type=fallback_type,

    )).parsed
