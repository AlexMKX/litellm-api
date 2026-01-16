from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cost_estimate_request import CostEstimateRequest
from ...models.cost_estimate_response import CostEstimateResponse
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    *,
    body: CostEstimateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cost/estimate",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CostEstimateResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CostEstimateResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CostEstimateResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CostEstimateRequest,

) -> Response[CostEstimateResponse | HTTPValidationError]:
    r""" Estimate Cost

     Estimate cost for a given model and token counts.

    This endpoint uses the same cost calculation logic as actual requests,
    including any configured margins and discounts.

    Parameters:
    - model: Model name (e.g., \"gpt-4\", \"claude-3-opus\")
    - input_tokens: Expected input tokens per request
    - output_tokens: Expected output tokens per request
    - num_requests_per_day: Number of requests per day (optional)
    - num_requests_per_month: Number of requests per month (optional)

    Returns cost breakdown including:
    - Per-request costs (input, output, margin)
    - Daily costs (if num_requests_per_day provided)
    - Monthly costs (if num_requests_per_month provided)

    Example:
    ```json
    {
        \"model\": \"gpt-4\",
        \"input_tokens\": 1000,
        \"output_tokens\": 500,
        \"num_requests_per_day\": 100,
        \"num_requests_per_month\": 3000
    }
    ```

    Args:
        body (CostEstimateRequest): Request body for /cost/estimate endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostEstimateResponse | HTTPValidationError]
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
    body: CostEstimateRequest,

) -> CostEstimateResponse | HTTPValidationError | None:
    r""" Estimate Cost

     Estimate cost for a given model and token counts.

    This endpoint uses the same cost calculation logic as actual requests,
    including any configured margins and discounts.

    Parameters:
    - model: Model name (e.g., \"gpt-4\", \"claude-3-opus\")
    - input_tokens: Expected input tokens per request
    - output_tokens: Expected output tokens per request
    - num_requests_per_day: Number of requests per day (optional)
    - num_requests_per_month: Number of requests per month (optional)

    Returns cost breakdown including:
    - Per-request costs (input, output, margin)
    - Daily costs (if num_requests_per_day provided)
    - Monthly costs (if num_requests_per_month provided)

    Example:
    ```json
    {
        \"model\": \"gpt-4\",
        \"input_tokens\": 1000,
        \"output_tokens\": 500,
        \"num_requests_per_day\": 100,
        \"num_requests_per_month\": 3000
    }
    ```

    Args:
        body (CostEstimateRequest): Request body for /cost/estimate endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostEstimateResponse | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CostEstimateRequest,

) -> Response[CostEstimateResponse | HTTPValidationError]:
    r""" Estimate Cost

     Estimate cost for a given model and token counts.

    This endpoint uses the same cost calculation logic as actual requests,
    including any configured margins and discounts.

    Parameters:
    - model: Model name (e.g., \"gpt-4\", \"claude-3-opus\")
    - input_tokens: Expected input tokens per request
    - output_tokens: Expected output tokens per request
    - num_requests_per_day: Number of requests per day (optional)
    - num_requests_per_month: Number of requests per month (optional)

    Returns cost breakdown including:
    - Per-request costs (input, output, margin)
    - Daily costs (if num_requests_per_day provided)
    - Monthly costs (if num_requests_per_month provided)

    Example:
    ```json
    {
        \"model\": \"gpt-4\",
        \"input_tokens\": 1000,
        \"output_tokens\": 500,
        \"num_requests_per_day\": 100,
        \"num_requests_per_month\": 3000
    }
    ```

    Args:
        body (CostEstimateRequest): Request body for /cost/estimate endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostEstimateResponse | HTTPValidationError]
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
    body: CostEstimateRequest,

) -> CostEstimateResponse | HTTPValidationError | None:
    r""" Estimate Cost

     Estimate cost for a given model and token counts.

    This endpoint uses the same cost calculation logic as actual requests,
    including any configured margins and discounts.

    Parameters:
    - model: Model name (e.g., \"gpt-4\", \"claude-3-opus\")
    - input_tokens: Expected input tokens per request
    - output_tokens: Expected output tokens per request
    - num_requests_per_day: Number of requests per day (optional)
    - num_requests_per_month: Number of requests per month (optional)

    Returns cost breakdown including:
    - Per-request costs (input, output, margin)
    - Daily costs (if num_requests_per_day provided)
    - Monthly costs (if num_requests_per_month provided)

    Example:
    ```json
    {
        \"model\": \"gpt-4\",
        \"input_tokens\": 1000,
        \"output_tokens\": 500,
        \"num_requests_per_day\": 100,
        \"num_requests_per_month\": 3000
    }
    ```

    Args:
        body (CostEstimateRequest): Request body for /cost/estimate endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostEstimateResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
