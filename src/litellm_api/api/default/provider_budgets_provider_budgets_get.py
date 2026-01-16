from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.provider_budget_response import ProviderBudgetResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/provider/budgets",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProviderBudgetResponse | None:
    if response.status_code == 200:
        response_200 = ProviderBudgetResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProviderBudgetResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[ProviderBudgetResponse]:
    r""" Provider Budgets

     Provider Budget Routing - Get Budget, Spend Details
    https://docs.litellm.ai/docs/proxy/provider_budget_routing

    Use this endpoint to check current budget, spend and budget reset time for a provider

    Example Request

    ```bash
    curl -X GET http://localhost:4000/provider/budgets     -H \"Content-Type: application/json\"     -H
    \"Authorization: Bearer sk-1234\"
    ```

    Example Response

    ```json
    {
        \"providers\": {
            \"openai\": {
                \"budget_limit\": 1e-12,
                \"time_period\": \"1d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            },
            \"azure\": {
                \"budget_limit\": 100.0,
                \"time_period\": \"1d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            },
            \"anthropic\": {
                \"budget_limit\": 100.0,
                \"time_period\": \"10d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            },
            \"vertex_ai\": {
                \"budget_limit\": 100.0,
                \"time_period\": \"12d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            }
        }
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProviderBudgetResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> ProviderBudgetResponse | None:
    r""" Provider Budgets

     Provider Budget Routing - Get Budget, Spend Details
    https://docs.litellm.ai/docs/proxy/provider_budget_routing

    Use this endpoint to check current budget, spend and budget reset time for a provider

    Example Request

    ```bash
    curl -X GET http://localhost:4000/provider/budgets     -H \"Content-Type: application/json\"     -H
    \"Authorization: Bearer sk-1234\"
    ```

    Example Response

    ```json
    {
        \"providers\": {
            \"openai\": {
                \"budget_limit\": 1e-12,
                \"time_period\": \"1d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            },
            \"azure\": {
                \"budget_limit\": 100.0,
                \"time_period\": \"1d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            },
            \"anthropic\": {
                \"budget_limit\": 100.0,
                \"time_period\": \"10d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            },
            \"vertex_ai\": {
                \"budget_limit\": 100.0,
                \"time_period\": \"12d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            }
        }
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProviderBudgetResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[ProviderBudgetResponse]:
    r""" Provider Budgets

     Provider Budget Routing - Get Budget, Spend Details
    https://docs.litellm.ai/docs/proxy/provider_budget_routing

    Use this endpoint to check current budget, spend and budget reset time for a provider

    Example Request

    ```bash
    curl -X GET http://localhost:4000/provider/budgets     -H \"Content-Type: application/json\"     -H
    \"Authorization: Bearer sk-1234\"
    ```

    Example Response

    ```json
    {
        \"providers\": {
            \"openai\": {
                \"budget_limit\": 1e-12,
                \"time_period\": \"1d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            },
            \"azure\": {
                \"budget_limit\": 100.0,
                \"time_period\": \"1d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            },
            \"anthropic\": {
                \"budget_limit\": 100.0,
                \"time_period\": \"10d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            },
            \"vertex_ai\": {
                \"budget_limit\": 100.0,
                \"time_period\": \"12d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            }
        }
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProviderBudgetResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> ProviderBudgetResponse | None:
    r""" Provider Budgets

     Provider Budget Routing - Get Budget, Spend Details
    https://docs.litellm.ai/docs/proxy/provider_budget_routing

    Use this endpoint to check current budget, spend and budget reset time for a provider

    Example Request

    ```bash
    curl -X GET http://localhost:4000/provider/budgets     -H \"Content-Type: application/json\"     -H
    \"Authorization: Bearer sk-1234\"
    ```

    Example Response

    ```json
    {
        \"providers\": {
            \"openai\": {
                \"budget_limit\": 1e-12,
                \"time_period\": \"1d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            },
            \"azure\": {
                \"budget_limit\": 100.0,
                \"time_period\": \"1d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            },
            \"anthropic\": {
                \"budget_limit\": 100.0,
                \"time_period\": \"10d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            },
            \"vertex_ai\": {
                \"budget_limit\": 100.0,
                \"time_period\": \"12d\",
                \"spend\": 0.0,
                \"budget_reset_at\": null
            }
        }
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProviderBudgetResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
