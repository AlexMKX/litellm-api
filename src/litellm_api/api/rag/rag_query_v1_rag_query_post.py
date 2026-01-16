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
        "method": "post",
        "url": "/v1/rag/query",
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
    r""" Rag Query

     RAG Query endpoint - search vector store, optionally rerank, and generate LLM response.

    This endpoint:
    1. Extracts the query from the last user message
    2. Searches the vector store for relevant context
    3. Optionally reranks the results
    4. Generates an LLM response with the retrieved context

    ## Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/v1/rag/query\" \
        -H \"Authorization: Bearer sk-1234\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"model\": \"gpt-4o-mini\",
            \"messages\": [{\"role\": \"user\", \"content\": \"What is LiteLLM?\"}],
            \"retrieval_config\": {
                \"vector_store_id\": \"vs_abc123\",
                \"custom_llm_provider\": \"openai\",
                \"top_k\": 5
            }
        }'
    ```

    ## With Reranking:
    ```bash
    curl -X POST \"http://localhost:4000/v1/rag/query\" \
        -H \"Authorization: Bearer sk-1234\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"model\": \"gpt-4o-mini\",
            \"messages\": [{\"role\": \"user\", \"content\": \"What is LiteLLM?\"}],
            \"retrieval_config\": {
                \"vector_store_id\": \"vs_abc123\",
                \"custom_llm_provider\": \"openai\",
                \"top_k\": 10
            },
            \"rerank\": {
                \"enabled\": true,
                \"model\": \"cohere/rerank-english-v3.0\",
                \"top_n\": 3
            }
        }'
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
    r""" Rag Query

     RAG Query endpoint - search vector store, optionally rerank, and generate LLM response.

    This endpoint:
    1. Extracts the query from the last user message
    2. Searches the vector store for relevant context
    3. Optionally reranks the results
    4. Generates an LLM response with the retrieved context

    ## Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/v1/rag/query\" \
        -H \"Authorization: Bearer sk-1234\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"model\": \"gpt-4o-mini\",
            \"messages\": [{\"role\": \"user\", \"content\": \"What is LiteLLM?\"}],
            \"retrieval_config\": {
                \"vector_store_id\": \"vs_abc123\",
                \"custom_llm_provider\": \"openai\",
                \"top_k\": 5
            }
        }'
    ```

    ## With Reranking:
    ```bash
    curl -X POST \"http://localhost:4000/v1/rag/query\" \
        -H \"Authorization: Bearer sk-1234\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"model\": \"gpt-4o-mini\",
            \"messages\": [{\"role\": \"user\", \"content\": \"What is LiteLLM?\"}],
            \"retrieval_config\": {
                \"vector_store_id\": \"vs_abc123\",
                \"custom_llm_provider\": \"openai\",
                \"top_k\": 10
            },
            \"rerank\": {
                \"enabled\": true,
                \"model\": \"cohere/rerank-english-v3.0\",
                \"top_n\": 3
            }
        }'
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

