from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.embeddings_embeddings_post_body import EmbeddingsEmbeddingsPostBody
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    *,
    body: EmbeddingsEmbeddingsPostBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/embeddings",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: EmbeddingsEmbeddingsPostBody,

) -> Response[Any | HTTPValidationError]:
    r""" Embeddings

     Follows the exact same API spec as `OpenAI's Embeddings API https://platform.openai.com/docs/api-
    reference/embeddings`

    ```bash
    curl -X POST http://localhost:4000/v1/embeddings
    -H \"Content-Type: application/json\"
    -H \"Authorization: Bearer sk-1234\"
    -d '{
        \"model\": \"text-embedding-ada-002\",
        \"input\": \"The quick brown fox jumps over the lazy dog\"
    }'
    ```

    Args:
        body (EmbeddingsEmbeddingsPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: EmbeddingsEmbeddingsPostBody,

) -> Any | HTTPValidationError | None:
    r""" Embeddings

     Follows the exact same API spec as `OpenAI's Embeddings API https://platform.openai.com/docs/api-
    reference/embeddings`

    ```bash
    curl -X POST http://localhost:4000/v1/embeddings
    -H \"Content-Type: application/json\"
    -H \"Authorization: Bearer sk-1234\"
    -d '{
        \"model\": \"text-embedding-ada-002\",
        \"input\": \"The quick brown fox jumps over the lazy dog\"
    }'
    ```

    Args:
        body (EmbeddingsEmbeddingsPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EmbeddingsEmbeddingsPostBody,

) -> Response[Any | HTTPValidationError]:
    r""" Embeddings

     Follows the exact same API spec as `OpenAI's Embeddings API https://platform.openai.com/docs/api-
    reference/embeddings`

    ```bash
    curl -X POST http://localhost:4000/v1/embeddings
    -H \"Content-Type: application/json\"
    -H \"Authorization: Bearer sk-1234\"
    -d '{
        \"model\": \"text-embedding-ada-002\",
        \"input\": \"The quick brown fox jumps over the lazy dog\"
    }'
    ```

    Args:
        body (EmbeddingsEmbeddingsPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: EmbeddingsEmbeddingsPostBody,

) -> Any | HTTPValidationError | None:
    r""" Embeddings

     Follows the exact same API spec as `OpenAI's Embeddings API https://platform.openai.com/docs/api-
    reference/embeddings`

    ```bash
    curl -X POST http://localhost:4000/v1/embeddings
    -H \"Content-Type: application/json\"
    -H \"Authorization: Bearer sk-1234\"
    -d '{
        \"model\": \"text-embedding-ada-002\",
        \"input\": \"The quick brown fox jumps over the lazy dog\"
    }'
    ```

    Args:
        body (EmbeddingsEmbeddingsPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
