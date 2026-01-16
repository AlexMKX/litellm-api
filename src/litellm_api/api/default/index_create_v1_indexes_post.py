from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.index_create_request import IndexCreateRequest
from typing import cast



def _get_kwargs(
    *,
    body: IndexCreateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/indexes",
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
    body: IndexCreateRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Index Create

     Create an index. Just writes the index to the database.

    ```bash
    curl -L -X POST 'http://0.0.0.0:4000/indexes/create'         -H 'Content-Type: application/json'
    -H 'Authorization: Bearer sk-1234'         -H 'LiteLLM-Beta: indexes_beta=v1'         -d '{
            \"index_name\": \"dall-e-3\",
            \"vector_store_index\": \"real-index-name\",
            \"vector_store_name\": \"azure-ai-search\"
        }'
    ```

    Args:
        body (IndexCreateRequest):

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
    body: IndexCreateRequest,

) -> Any | HTTPValidationError | None:
    r""" Index Create

     Create an index. Just writes the index to the database.

    ```bash
    curl -L -X POST 'http://0.0.0.0:4000/indexes/create'         -H 'Content-Type: application/json'
    -H 'Authorization: Bearer sk-1234'         -H 'LiteLLM-Beta: indexes_beta=v1'         -d '{
            \"index_name\": \"dall-e-3\",
            \"vector_store_index\": \"real-index-name\",
            \"vector_store_name\": \"azure-ai-search\"
        }'
    ```

    Args:
        body (IndexCreateRequest):

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
    body: IndexCreateRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Index Create

     Create an index. Just writes the index to the database.

    ```bash
    curl -L -X POST 'http://0.0.0.0:4000/indexes/create'         -H 'Content-Type: application/json'
    -H 'Authorization: Bearer sk-1234'         -H 'LiteLLM-Beta: indexes_beta=v1'         -d '{
            \"index_name\": \"dall-e-3\",
            \"vector_store_index\": \"real-index-name\",
            \"vector_store_name\": \"azure-ai-search\"
        }'
    ```

    Args:
        body (IndexCreateRequest):

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
    body: IndexCreateRequest,

) -> Any | HTTPValidationError | None:
    r""" Index Create

     Create an index. Just writes the index to the database.

    ```bash
    curl -L -X POST 'http://0.0.0.0:4000/indexes/create'         -H 'Content-Type: application/json'
    -H 'Authorization: Bearer sk-1234'         -H 'LiteLLM-Beta: indexes_beta=v1'         -d '{
            \"index_name\": \"dall-e-3\",
            \"vector_store_index\": \"real-index-name\",
            \"vector_store_name\": \"azure-ai-search\"
        }'
    ```

    Args:
        body (IndexCreateRequest):

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
