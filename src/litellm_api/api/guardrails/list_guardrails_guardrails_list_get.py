from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_guardrails_response import ListGuardrailsResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/guardrails/list",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListGuardrailsResponse | None:
    if response.status_code == 200:
        response_200 = ListGuardrailsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListGuardrailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[ListGuardrailsResponse]:
    r""" List Guardrails

     List the guardrails that are available on the proxy server

    👉 [Guardrail docs](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/guardrails/list\" -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"guardrails\": [
            {
            \"guardrail_name\": \"bedrock-pre-guard\",
            \"guardrail_info\": {
                \"params\": [
                {
                    \"name\": \"toxicity_score\",
                    \"type\": \"float\",
                    \"description\": \"Score between 0-1 indicating content toxicity level\"
                },
                {
                    \"name\": \"pii_detection\",
                    \"type\": \"boolean\"
                }
                ]
            }
            }
        ]
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListGuardrailsResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> ListGuardrailsResponse | None:
    r""" List Guardrails

     List the guardrails that are available on the proxy server

    👉 [Guardrail docs](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/guardrails/list\" -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"guardrails\": [
            {
            \"guardrail_name\": \"bedrock-pre-guard\",
            \"guardrail_info\": {
                \"params\": [
                {
                    \"name\": \"toxicity_score\",
                    \"type\": \"float\",
                    \"description\": \"Score between 0-1 indicating content toxicity level\"
                },
                {
                    \"name\": \"pii_detection\",
                    \"type\": \"boolean\"
                }
                ]
            }
            }
        ]
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListGuardrailsResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[ListGuardrailsResponse]:
    r""" List Guardrails

     List the guardrails that are available on the proxy server

    👉 [Guardrail docs](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/guardrails/list\" -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"guardrails\": [
            {
            \"guardrail_name\": \"bedrock-pre-guard\",
            \"guardrail_info\": {
                \"params\": [
                {
                    \"name\": \"toxicity_score\",
                    \"type\": \"float\",
                    \"description\": \"Score between 0-1 indicating content toxicity level\"
                },
                {
                    \"name\": \"pii_detection\",
                    \"type\": \"boolean\"
                }
                ]
            }
            }
        ]
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListGuardrailsResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> ListGuardrailsResponse | None:
    r""" List Guardrails

     List the guardrails that are available on the proxy server

    👉 [Guardrail docs](https://docs.litellm.ai/docs/proxy/guardrails/quick_start)

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/guardrails/list\" -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"guardrails\": [
            {
            \"guardrail_name\": \"bedrock-pre-guard\",
            \"guardrail_info\": {
                \"params\": [
                {
                    \"name\": \"toxicity_score\",
                    \"type\": \"float\",
                    \"description\": \"Score between 0-1 indicating content toxicity level\"
                },
                {
                    \"name\": \"pii_detection\",
                    \"type\": \"boolean\"
                }
                ]
            }
            }
        ]
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListGuardrailsResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
