from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.pipeline_test_request import PipelineTestRequest
from typing import cast



def _get_kwargs(
    *,
    body: PipelineTestRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/policies/test-pipeline",
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
    body: PipelineTestRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Test Pipeline

     Test a guardrail pipeline with sample messages.

    Executes the pipeline steps against the provided test messages and returns
    step-by-step results showing which guardrails passed/failed, actions taken,
    and timing information.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/test-pipeline\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"pipeline\": {
                \"mode\": \"pre_call\",
                \"steps\": [
                    {\"guardrail\": \"pii-guard\", \"on_pass\": \"next\", \"on_fail\": \"block\"}
                ]
            },
            \"test_messages\": [{\"role\": \"user\", \"content\": \"My SSN is 123-45-6789\"}]
        }'
    ```

    Args:
        body (PipelineTestRequest): Request body for testing a guardrail pipeline with sample
            messages.

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
    body: PipelineTestRequest,

) -> Any | HTTPValidationError | None:
    r""" Test Pipeline

     Test a guardrail pipeline with sample messages.

    Executes the pipeline steps against the provided test messages and returns
    step-by-step results showing which guardrails passed/failed, actions taken,
    and timing information.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/test-pipeline\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"pipeline\": {
                \"mode\": \"pre_call\",
                \"steps\": [
                    {\"guardrail\": \"pii-guard\", \"on_pass\": \"next\", \"on_fail\": \"block\"}
                ]
            },
            \"test_messages\": [{\"role\": \"user\", \"content\": \"My SSN is 123-45-6789\"}]
        }'
    ```

    Args:
        body (PipelineTestRequest): Request body for testing a guardrail pipeline with sample
            messages.

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
    body: PipelineTestRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Test Pipeline

     Test a guardrail pipeline with sample messages.

    Executes the pipeline steps against the provided test messages and returns
    step-by-step results showing which guardrails passed/failed, actions taken,
    and timing information.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/test-pipeline\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"pipeline\": {
                \"mode\": \"pre_call\",
                \"steps\": [
                    {\"guardrail\": \"pii-guard\", \"on_pass\": \"next\", \"on_fail\": \"block\"}
                ]
            },
            \"test_messages\": [{\"role\": \"user\", \"content\": \"My SSN is 123-45-6789\"}]
        }'
    ```

    Args:
        body (PipelineTestRequest): Request body for testing a guardrail pipeline with sample
            messages.

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
    body: PipelineTestRequest,

) -> Any | HTTPValidationError | None:
    r""" Test Pipeline

     Test a guardrail pipeline with sample messages.

    Executes the pipeline steps against the provided test messages and returns
    step-by-step results showing which guardrails passed/failed, actions taken,
    and timing information.

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/test-pipeline\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"pipeline\": {
                \"mode\": \"pre_call\",
                \"steps\": [
                    {\"guardrail\": \"pii-guard\", \"on_pass\": \"next\", \"on_fail\": \"block\"}
                ]
            },
            \"test_messages\": [{\"role\": \"user\", \"content\": \"My SSN is 123-45-6789\"}]
        }'
    ```

    Args:
        body (PipelineTestRequest): Request body for testing a guardrail pipeline with sample
            messages.

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
