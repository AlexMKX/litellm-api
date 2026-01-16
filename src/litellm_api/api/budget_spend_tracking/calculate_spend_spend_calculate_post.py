from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.spend_calculate_request import SpendCalculateRequest
from typing import cast



def _get_kwargs(
    *,
    body: SpendCalculateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/spend/calculate",
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
    body: SpendCalculateRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Calculate Spend

     Accepts all the params of completion_cost.

    Calculate spend **before** making call:

    Note: If you see a spend of $0.0 you need to set custom_pricing for your model:
    https://docs.litellm.ai/docs/proxy/custom_pricing

    ```
    curl --location 'http://localhost:4000/spend/calculate'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"model\": \"anthropic.claude-v2\",
        \"messages\": [{\"role\": \"user\", \"content\": \"Hey, how'''s it going?\"}]
    }'
    ```

    Calculate spend **after** making call:

    ```
    curl --location 'http://localhost:4000/spend/calculate'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"completion_response\": {
            \"id\": \"chatcmpl-123\",
            \"object\": \"chat.completion\",
            \"created\": 1677652288,
            \"model\": \"gpt-3.5-turbo-0125\",
            \"system_fingerprint\": \"fp_44709d6fcb\",
            \"choices\": [{
                \"index\": 0,
                \"message\": {
                    \"role\": \"assistant\",
                    \"content\": \"Hello there, how may I assist you today?\"
                },
                \"logprobs\": null,
                \"finish_reason\": \"stop\"
            }]
            \"usage\": {
                \"prompt_tokens\": 9,
                \"completion_tokens\": 12,
                \"total_tokens\": 21
            }
        }
    }'
    ```

    Args:
        body (SpendCalculateRequest):

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
    body: SpendCalculateRequest,

) -> Any | HTTPValidationError | None:
    r""" Calculate Spend

     Accepts all the params of completion_cost.

    Calculate spend **before** making call:

    Note: If you see a spend of $0.0 you need to set custom_pricing for your model:
    https://docs.litellm.ai/docs/proxy/custom_pricing

    ```
    curl --location 'http://localhost:4000/spend/calculate'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"model\": \"anthropic.claude-v2\",
        \"messages\": [{\"role\": \"user\", \"content\": \"Hey, how'''s it going?\"}]
    }'
    ```

    Calculate spend **after** making call:

    ```
    curl --location 'http://localhost:4000/spend/calculate'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"completion_response\": {
            \"id\": \"chatcmpl-123\",
            \"object\": \"chat.completion\",
            \"created\": 1677652288,
            \"model\": \"gpt-3.5-turbo-0125\",
            \"system_fingerprint\": \"fp_44709d6fcb\",
            \"choices\": [{
                \"index\": 0,
                \"message\": {
                    \"role\": \"assistant\",
                    \"content\": \"Hello there, how may I assist you today?\"
                },
                \"logprobs\": null,
                \"finish_reason\": \"stop\"
            }]
            \"usage\": {
                \"prompt_tokens\": 9,
                \"completion_tokens\": 12,
                \"total_tokens\": 21
            }
        }
    }'
    ```

    Args:
        body (SpendCalculateRequest):

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
    body: SpendCalculateRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Calculate Spend

     Accepts all the params of completion_cost.

    Calculate spend **before** making call:

    Note: If you see a spend of $0.0 you need to set custom_pricing for your model:
    https://docs.litellm.ai/docs/proxy/custom_pricing

    ```
    curl --location 'http://localhost:4000/spend/calculate'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"model\": \"anthropic.claude-v2\",
        \"messages\": [{\"role\": \"user\", \"content\": \"Hey, how'''s it going?\"}]
    }'
    ```

    Calculate spend **after** making call:

    ```
    curl --location 'http://localhost:4000/spend/calculate'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"completion_response\": {
            \"id\": \"chatcmpl-123\",
            \"object\": \"chat.completion\",
            \"created\": 1677652288,
            \"model\": \"gpt-3.5-turbo-0125\",
            \"system_fingerprint\": \"fp_44709d6fcb\",
            \"choices\": [{
                \"index\": 0,
                \"message\": {
                    \"role\": \"assistant\",
                    \"content\": \"Hello there, how may I assist you today?\"
                },
                \"logprobs\": null,
                \"finish_reason\": \"stop\"
            }]
            \"usage\": {
                \"prompt_tokens\": 9,
                \"completion_tokens\": 12,
                \"total_tokens\": 21
            }
        }
    }'
    ```

    Args:
        body (SpendCalculateRequest):

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
    body: SpendCalculateRequest,

) -> Any | HTTPValidationError | None:
    r""" Calculate Spend

     Accepts all the params of completion_cost.

    Calculate spend **before** making call:

    Note: If you see a spend of $0.0 you need to set custom_pricing for your model:
    https://docs.litellm.ai/docs/proxy/custom_pricing

    ```
    curl --location 'http://localhost:4000/spend/calculate'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"model\": \"anthropic.claude-v2\",
        \"messages\": [{\"role\": \"user\", \"content\": \"Hey, how'''s it going?\"}]
    }'
    ```

    Calculate spend **after** making call:

    ```
    curl --location 'http://localhost:4000/spend/calculate'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"completion_response\": {
            \"id\": \"chatcmpl-123\",
            \"object\": \"chat.completion\",
            \"created\": 1677652288,
            \"model\": \"gpt-3.5-turbo-0125\",
            \"system_fingerprint\": \"fp_44709d6fcb\",
            \"choices\": [{
                \"index\": 0,
                \"message\": {
                    \"role\": \"assistant\",
                    \"content\": \"Hello there, how may I assist you today?\"
                },
                \"logprobs\": null,
                \"finish_reason\": \"stop\"
            }]
            \"usage\": {
                \"prompt_tokens\": 9,
                \"completion_tokens\": 12,
                \"total_tokens\": 21
            }
        }
    }'
    ```

    Args:
        body (SpendCalculateRequest):

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
