from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.fallback_create_request import FallbackCreateRequest
from ...models.fallback_response import FallbackResponse
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    *,
    body: FallbackCreateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fallback",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FallbackResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FallbackResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FallbackResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: FallbackCreateRequest,

) -> Response[FallbackResponse | HTTPValidationError]:
    r""" Create Fallback

     Create or update fallbacks for a specific model.

    This endpoint allows you to configure fallback models separately from the general config.
    Fallbacks are triggered when a model call fails after retries.

    **Example Request:**
    ```json
    {
        \"model\": \"gpt-3.5-turbo\",
        \"fallback_models\": [\"gpt-4\", \"claude-3-haiku\"],
        \"fallback_type\": \"general\"
    }
    ```

    **Fallback Types:**
    - `general`: Standard fallbacks for any error (default)
    - `context_window`: Fallbacks specifically for context window exceeded errors
    - `content_policy`: Fallbacks specifically for content policy violations

    Args:
        body (FallbackCreateRequest): Request model for creating/updating fallbacks

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FallbackResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: FallbackCreateRequest,

) -> FallbackResponse | HTTPValidationError | None:
    r""" Create Fallback

     Create or update fallbacks for a specific model.

    This endpoint allows you to configure fallback models separately from the general config.
    Fallbacks are triggered when a model call fails after retries.

    **Example Request:**
    ```json
    {
        \"model\": \"gpt-3.5-turbo\",
        \"fallback_models\": [\"gpt-4\", \"claude-3-haiku\"],
        \"fallback_type\": \"general\"
    }
    ```

    **Fallback Types:**
    - `general`: Standard fallbacks for any error (default)
    - `context_window`: Fallbacks specifically for context window exceeded errors
    - `content_policy`: Fallbacks specifically for content policy violations

    Args:
        body (FallbackCreateRequest): Request model for creating/updating fallbacks

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FallbackResponse | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: FallbackCreateRequest,

) -> Response[FallbackResponse | HTTPValidationError]:
    r""" Create Fallback

     Create or update fallbacks for a specific model.

    This endpoint allows you to configure fallback models separately from the general config.
    Fallbacks are triggered when a model call fails after retries.

    **Example Request:**
    ```json
    {
        \"model\": \"gpt-3.5-turbo\",
        \"fallback_models\": [\"gpt-4\", \"claude-3-haiku\"],
        \"fallback_type\": \"general\"
    }
    ```

    **Fallback Types:**
    - `general`: Standard fallbacks for any error (default)
    - `context_window`: Fallbacks specifically for context window exceeded errors
    - `content_policy`: Fallbacks specifically for content policy violations

    Args:
        body (FallbackCreateRequest): Request model for creating/updating fallbacks

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FallbackResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: FallbackCreateRequest,

) -> FallbackResponse | HTTPValidationError | None:
    r""" Create Fallback

     Create or update fallbacks for a specific model.

    This endpoint allows you to configure fallback models separately from the general config.
    Fallbacks are triggered when a model call fails after retries.

    **Example Request:**
    ```json
    {
        \"model\": \"gpt-3.5-turbo\",
        \"fallback_models\": [\"gpt-4\", \"claude-3-haiku\"],
        \"fallback_type\": \"general\"
    }
    ```

    **Fallback Types:**
    - `general`: Standard fallbacks for any error (default)
    - `context_window`: Fallbacks specifically for context window exceeded errors
    - `content_policy`: Fallbacks specifically for content policy violations

    Args:
        body (FallbackCreateRequest): Request model for creating/updating fallbacks

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FallbackResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
