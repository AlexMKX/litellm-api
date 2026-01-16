from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.body_test_model_connection_health_test_connection_post import BodyTestModelConnectionHealthTestConnectionPost
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: BodyTestModelConnectionHealthTestConnectionPost | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/health/test_connection",
    }

    
    if not isinstance(body, Unset):
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
    body: BodyTestModelConnectionHealthTestConnectionPost | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Test Model Connection

     Test a direct connection to a specific model.

    This endpoint allows you to verify if your proxy can successfully connect to a specific model.
    It's useful for troubleshooting model connectivity issues without going through the full proxy
    routing.

    Example:
    ```bash
    # If model is configured in proxy_config.yaml, you only need to specify the model name:
    curl -X POST 'http://localhost:4000/health/test_connection' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"litellm_params\": {
            \"model\": \"gpt-4o\"
        },
        \"mode\": \"chat\"
      }'

    # The endpoint will automatically use api_key, api_base, etc. from proxy_config.yaml

    # You can also override specific params or test with custom credentials:
    curl -X POST 'http://localhost:4000/health/test_connection' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"litellm_params\": {
            \"model\": \"azure/gpt-4o\",
            \"api_key\": \"os.environ/AZURE_OPENAI_API_KEY\",
            \"api_base\": \"os.environ/AZURE_OPENAI_ENDPOINT\",
            \"api_version\": \"2024-10-21\"
        },
        \"mode\": \"chat\"
      }'
    ```

    Note:
    - If the model is configured in proxy_config.yaml, credentials (api_key, api_base, etc.)
      will be automatically loaded from the config (with resolved environment variables).
    - You can override specific params by including them in the request.
    - You can use `os.environ/VARIABLE_NAME` syntax to reference environment variables,
      which will be resolved automatically (same as in proxy_config.yaml).

    Returns:
        dict: A dictionary containing the health check result with either success information or error
    details.

    Args:
        body (BodyTestModelConnectionHealthTestConnectionPost | Unset):

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
    body: BodyTestModelConnectionHealthTestConnectionPost | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Test Model Connection

     Test a direct connection to a specific model.

    This endpoint allows you to verify if your proxy can successfully connect to a specific model.
    It's useful for troubleshooting model connectivity issues without going through the full proxy
    routing.

    Example:
    ```bash
    # If model is configured in proxy_config.yaml, you only need to specify the model name:
    curl -X POST 'http://localhost:4000/health/test_connection' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"litellm_params\": {
            \"model\": \"gpt-4o\"
        },
        \"mode\": \"chat\"
      }'

    # The endpoint will automatically use api_key, api_base, etc. from proxy_config.yaml

    # You can also override specific params or test with custom credentials:
    curl -X POST 'http://localhost:4000/health/test_connection' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"litellm_params\": {
            \"model\": \"azure/gpt-4o\",
            \"api_key\": \"os.environ/AZURE_OPENAI_API_KEY\",
            \"api_base\": \"os.environ/AZURE_OPENAI_ENDPOINT\",
            \"api_version\": \"2024-10-21\"
        },
        \"mode\": \"chat\"
      }'
    ```

    Note:
    - If the model is configured in proxy_config.yaml, credentials (api_key, api_base, etc.)
      will be automatically loaded from the config (with resolved environment variables).
    - You can override specific params by including them in the request.
    - You can use `os.environ/VARIABLE_NAME` syntax to reference environment variables,
      which will be resolved automatically (same as in proxy_config.yaml).

    Returns:
        dict: A dictionary containing the health check result with either success information or error
    details.

    Args:
        body (BodyTestModelConnectionHealthTestConnectionPost | Unset):

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
    body: BodyTestModelConnectionHealthTestConnectionPost | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Test Model Connection

     Test a direct connection to a specific model.

    This endpoint allows you to verify if your proxy can successfully connect to a specific model.
    It's useful for troubleshooting model connectivity issues without going through the full proxy
    routing.

    Example:
    ```bash
    # If model is configured in proxy_config.yaml, you only need to specify the model name:
    curl -X POST 'http://localhost:4000/health/test_connection' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"litellm_params\": {
            \"model\": \"gpt-4o\"
        },
        \"mode\": \"chat\"
      }'

    # The endpoint will automatically use api_key, api_base, etc. from proxy_config.yaml

    # You can also override specific params or test with custom credentials:
    curl -X POST 'http://localhost:4000/health/test_connection' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"litellm_params\": {
            \"model\": \"azure/gpt-4o\",
            \"api_key\": \"os.environ/AZURE_OPENAI_API_KEY\",
            \"api_base\": \"os.environ/AZURE_OPENAI_ENDPOINT\",
            \"api_version\": \"2024-10-21\"
        },
        \"mode\": \"chat\"
      }'
    ```

    Note:
    - If the model is configured in proxy_config.yaml, credentials (api_key, api_base, etc.)
      will be automatically loaded from the config (with resolved environment variables).
    - You can override specific params by including them in the request.
    - You can use `os.environ/VARIABLE_NAME` syntax to reference environment variables,
      which will be resolved automatically (same as in proxy_config.yaml).

    Returns:
        dict: A dictionary containing the health check result with either success information or error
    details.

    Args:
        body (BodyTestModelConnectionHealthTestConnectionPost | Unset):

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
    body: BodyTestModelConnectionHealthTestConnectionPost | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Test Model Connection

     Test a direct connection to a specific model.

    This endpoint allows you to verify if your proxy can successfully connect to a specific model.
    It's useful for troubleshooting model connectivity issues without going through the full proxy
    routing.

    Example:
    ```bash
    # If model is configured in proxy_config.yaml, you only need to specify the model name:
    curl -X POST 'http://localhost:4000/health/test_connection' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"litellm_params\": {
            \"model\": \"gpt-4o\"
        },
        \"mode\": \"chat\"
      }'

    # The endpoint will automatically use api_key, api_base, etc. from proxy_config.yaml

    # You can also override specific params or test with custom credentials:
    curl -X POST 'http://localhost:4000/health/test_connection' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"litellm_params\": {
            \"model\": \"azure/gpt-4o\",
            \"api_key\": \"os.environ/AZURE_OPENAI_API_KEY\",
            \"api_base\": \"os.environ/AZURE_OPENAI_ENDPOINT\",
            \"api_version\": \"2024-10-21\"
        },
        \"mode\": \"chat\"
      }'
    ```

    Note:
    - If the model is configured in proxy_config.yaml, credentials (api_key, api_base, etc.)
      will be automatically loaded from the config (with resolved environment variables).
    - You can override specific params by including them in the request.
    - You can use `os.environ/VARIABLE_NAME` syntax to reference environment variables,
      which will be resolved automatically (same as in proxy_config.yaml).

    Returns:
        dict: A dictionary containing the health check result with either success information or error
    details.

    Args:
        body (BodyTestModelConnectionHealthTestConnectionPost | Unset):

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
