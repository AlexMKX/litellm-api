from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.list_prompts_response import ListPromptsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    environment: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_environment: None | str | Unset
    if isinstance(environment, Unset):
        json_environment = UNSET
    else:
        json_environment = environment
    params["environment"] = json_environment


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/prompts/list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | ListPromptsResponse | None:
    if response.status_code == 200:
        response_200 = ListPromptsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | ListPromptsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    environment: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | ListPromptsResponse]:
    r""" List Prompts

     List the prompts that are available on the proxy server

    👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/prompts/list\" -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"prompts\": [
            {
                \"prompt_id\": \"my_prompt_id\",
                \"litellm_params\": {
                    \"prompt_id\": \"my_prompt_id\",
                    \"prompt_integration\": \"dotprompt\",
                    \"prompt_directory\": \"/path/to/prompts\"
                },
                \"prompt_info\": {
                    \"prompt_type\": \"config\"
                },
                \"created_at\": \"2023-11-09T12:34:56.789Z\",
                \"updated_at\": \"2023-11-09T12:34:56.789Z\"
            }
        ]
    }
    ```

    Args:
        environment (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListPromptsResponse]
     """


    kwargs = _get_kwargs(
        environment=environment,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    environment: None | str | Unset = UNSET,

) -> HTTPValidationError | ListPromptsResponse | None:
    r""" List Prompts

     List the prompts that are available on the proxy server

    👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/prompts/list\" -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"prompts\": [
            {
                \"prompt_id\": \"my_prompt_id\",
                \"litellm_params\": {
                    \"prompt_id\": \"my_prompt_id\",
                    \"prompt_integration\": \"dotprompt\",
                    \"prompt_directory\": \"/path/to/prompts\"
                },
                \"prompt_info\": {
                    \"prompt_type\": \"config\"
                },
                \"created_at\": \"2023-11-09T12:34:56.789Z\",
                \"updated_at\": \"2023-11-09T12:34:56.789Z\"
            }
        ]
    }
    ```

    Args:
        environment (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListPromptsResponse
     """


    return sync_detailed(
        client=client,
environment=environment,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    environment: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | ListPromptsResponse]:
    r""" List Prompts

     List the prompts that are available on the proxy server

    👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/prompts/list\" -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"prompts\": [
            {
                \"prompt_id\": \"my_prompt_id\",
                \"litellm_params\": {
                    \"prompt_id\": \"my_prompt_id\",
                    \"prompt_integration\": \"dotprompt\",
                    \"prompt_directory\": \"/path/to/prompts\"
                },
                \"prompt_info\": {
                    \"prompt_type\": \"config\"
                },
                \"created_at\": \"2023-11-09T12:34:56.789Z\",
                \"updated_at\": \"2023-11-09T12:34:56.789Z\"
            }
        ]
    }
    ```

    Args:
        environment (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListPromptsResponse]
     """


    kwargs = _get_kwargs(
        environment=environment,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    environment: None | str | Unset = UNSET,

) -> HTTPValidationError | ListPromptsResponse | None:
    r""" List Prompts

     List the prompts that are available on the proxy server

    👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/prompts/list\" -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"prompts\": [
            {
                \"prompt_id\": \"my_prompt_id\",
                \"litellm_params\": {
                    \"prompt_id\": \"my_prompt_id\",
                    \"prompt_integration\": \"dotprompt\",
                    \"prompt_directory\": \"/path/to/prompts\"
                },
                \"prompt_info\": {
                    \"prompt_type\": \"config\"
                },
                \"created_at\": \"2023-11-09T12:34:56.789Z\",
                \"updated_at\": \"2023-11-09T12:34:56.789Z\"
            }
        ]
    }
    ```

    Args:
        environment (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListPromptsResponse
     """


    return (await asyncio_detailed(
        client=client,
environment=environment,

    )).parsed
