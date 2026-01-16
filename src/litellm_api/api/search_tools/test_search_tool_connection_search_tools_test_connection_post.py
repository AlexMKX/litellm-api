from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.test_search_tool_connection_request import TestSearchToolConnectionRequest
from typing import cast



def _get_kwargs(
    *,
    body: TestSearchToolConnectionRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/search_tools/test_connection",
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
    body: TestSearchToolConnectionRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Test Search Tool Connection

     Test connection to a search provider with the given configuration.

    Makes a simple test search query to verify the API key and configuration are valid.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/search_tools/test_connection\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"litellm_params\": {
                \"search_provider\": \"perplexity\",
                \"api_key\": \"sk-...\"
            }
        }'
    ```

    Example Response (Success):
    ```json
    {
        \"status\": \"success\",
        \"message\": \"Successfully connected to perplexity search provider\",
        \"test_query\": \"test\",
        \"results_count\": 5
    }
    ```

    Example Response (Failure):
    ```json
    {
        \"status\": \"error\",
        \"message\": \"Authentication failed: Invalid API key\",
        \"error_type\": \"AuthenticationError\"
    }
    ```

    Args:
        body (TestSearchToolConnectionRequest):

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
    body: TestSearchToolConnectionRequest,

) -> Any | HTTPValidationError | None:
    r""" Test Search Tool Connection

     Test connection to a search provider with the given configuration.

    Makes a simple test search query to verify the API key and configuration are valid.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/search_tools/test_connection\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"litellm_params\": {
                \"search_provider\": \"perplexity\",
                \"api_key\": \"sk-...\"
            }
        }'
    ```

    Example Response (Success):
    ```json
    {
        \"status\": \"success\",
        \"message\": \"Successfully connected to perplexity search provider\",
        \"test_query\": \"test\",
        \"results_count\": 5
    }
    ```

    Example Response (Failure):
    ```json
    {
        \"status\": \"error\",
        \"message\": \"Authentication failed: Invalid API key\",
        \"error_type\": \"AuthenticationError\"
    }
    ```

    Args:
        body (TestSearchToolConnectionRequest):

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
    body: TestSearchToolConnectionRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Test Search Tool Connection

     Test connection to a search provider with the given configuration.

    Makes a simple test search query to verify the API key and configuration are valid.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/search_tools/test_connection\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"litellm_params\": {
                \"search_provider\": \"perplexity\",
                \"api_key\": \"sk-...\"
            }
        }'
    ```

    Example Response (Success):
    ```json
    {
        \"status\": \"success\",
        \"message\": \"Successfully connected to perplexity search provider\",
        \"test_query\": \"test\",
        \"results_count\": 5
    }
    ```

    Example Response (Failure):
    ```json
    {
        \"status\": \"error\",
        \"message\": \"Authentication failed: Invalid API key\",
        \"error_type\": \"AuthenticationError\"
    }
    ```

    Args:
        body (TestSearchToolConnectionRequest):

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
    body: TestSearchToolConnectionRequest,

) -> Any | HTTPValidationError | None:
    r""" Test Search Tool Connection

     Test connection to a search provider with the given configuration.

    Makes a simple test search query to verify the API key and configuration are valid.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/search_tools/test_connection\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"litellm_params\": {
                \"search_provider\": \"perplexity\",
                \"api_key\": \"sk-...\"
            }
        }'
    ```

    Example Response (Success):
    ```json
    {
        \"status\": \"success\",
        \"message\": \"Successfully connected to perplexity search provider\",
        \"test_query\": \"test\",
        \"results_count\": 5
    }
    ```

    Example Response (Failure):
    ```json
    {
        \"status\": \"error\",
        \"message\": \"Authentication failed: Invalid API key\",
        \"error_type\": \"AuthenticationError\"
    }
    ```

    Args:
        body (TestSearchToolConnectionRequest):

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
