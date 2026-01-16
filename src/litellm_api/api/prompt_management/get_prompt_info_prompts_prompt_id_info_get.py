from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.prompt_info_response import PromptInfoResponse
from typing import cast



def _get_kwargs(
    prompt_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/prompts/{prompt_id}/info".format(prompt_id=quote(str(prompt_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | PromptInfoResponse | None:
    if response.status_code == 200:
        response_200 = PromptInfoResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | PromptInfoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    prompt_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[HTTPValidationError | PromptInfoResponse]:
    r""" Get Prompt Info

     Get detailed information about a specific prompt by ID, including prompt content

        👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

        Example Request:
        ```bash
        curl -X GET \"http://localhost:4000/prompts/my_prompt_id/info\" \
            -H \"Authorization: Bearer <your_api_key>\"
        ```

        Example Response:
        ```json
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
            \"updated_at\": \"2023-11-09T12:34:56.789Z\",
            \"content\": \"System: You are a helpful assistant.

    User: {{user_message}}\"
        }
        ```

    Args:
        prompt_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PromptInfoResponse]
     """


    kwargs = _get_kwargs(
        prompt_id=prompt_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    prompt_id: str,
    *,
    client: AuthenticatedClient,

) -> HTTPValidationError | PromptInfoResponse | None:
    r""" Get Prompt Info

     Get detailed information about a specific prompt by ID, including prompt content

        👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

        Example Request:
        ```bash
        curl -X GET \"http://localhost:4000/prompts/my_prompt_id/info\" \
            -H \"Authorization: Bearer <your_api_key>\"
        ```

        Example Response:
        ```json
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
            \"updated_at\": \"2023-11-09T12:34:56.789Z\",
            \"content\": \"System: You are a helpful assistant.

    User: {{user_message}}\"
        }
        ```

    Args:
        prompt_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PromptInfoResponse
     """


    return sync_detailed(
        prompt_id=prompt_id,
client=client,

    ).parsed

async def asyncio_detailed(
    prompt_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[HTTPValidationError | PromptInfoResponse]:
    r""" Get Prompt Info

     Get detailed information about a specific prompt by ID, including prompt content

        👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

        Example Request:
        ```bash
        curl -X GET \"http://localhost:4000/prompts/my_prompt_id/info\" \
            -H \"Authorization: Bearer <your_api_key>\"
        ```

        Example Response:
        ```json
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
            \"updated_at\": \"2023-11-09T12:34:56.789Z\",
            \"content\": \"System: You are a helpful assistant.

    User: {{user_message}}\"
        }
        ```

    Args:
        prompt_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PromptInfoResponse]
     """


    kwargs = _get_kwargs(
        prompt_id=prompt_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    prompt_id: str,
    *,
    client: AuthenticatedClient,

) -> HTTPValidationError | PromptInfoResponse | None:
    r""" Get Prompt Info

     Get detailed information about a specific prompt by ID, including prompt content

        👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

        Example Request:
        ```bash
        curl -X GET \"http://localhost:4000/prompts/my_prompt_id/info\" \
            -H \"Authorization: Bearer <your_api_key>\"
        ```

        Example Response:
        ```json
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
            \"updated_at\": \"2023-11-09T12:34:56.789Z\",
            \"content\": \"System: You are a helpful assistant.

    User: {{user_message}}\"
        }
        ```

    Args:
        prompt_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PromptInfoResponse
     """


    return (await asyncio_detailed(
        prompt_id=prompt_id,
client=client,

    )).parsed
