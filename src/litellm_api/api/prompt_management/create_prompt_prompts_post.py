from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.prompt import Prompt
from typing import cast



def _get_kwargs(
    *,
    body: Prompt,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/prompts",
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
    body: Prompt,

) -> Response[Any | HTTPValidationError]:
    r""" Create Prompt

     Create a new prompt

    👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/prompts\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"prompt_id\": \"my_prompt\",
            \"litellm_params\": {
                \"prompt_id\": \"json_prompt\",
                \"prompt_integration\": \"dotprompt\",
                ### EITHER prompt_directory OR prompt_data MUST BE PROVIDED
                \"prompt_directory\": \"/path/to/dotprompt/folder\",
                \"prompt_data\": {\"json_prompt\": {\"content\": \"This is a prompt\", \"metadata\":
    {\"model\": \"gpt-4\"}}}
            },
            \"prompt_info\": {
                \"prompt_type\": \"config\"
            }
        }'
    ```

    Args:
        body (Prompt):

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
    body: Prompt,

) -> Any | HTTPValidationError | None:
    r""" Create Prompt

     Create a new prompt

    👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/prompts\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"prompt_id\": \"my_prompt\",
            \"litellm_params\": {
                \"prompt_id\": \"json_prompt\",
                \"prompt_integration\": \"dotprompt\",
                ### EITHER prompt_directory OR prompt_data MUST BE PROVIDED
                \"prompt_directory\": \"/path/to/dotprompt/folder\",
                \"prompt_data\": {\"json_prompt\": {\"content\": \"This is a prompt\", \"metadata\":
    {\"model\": \"gpt-4\"}}}
            },
            \"prompt_info\": {
                \"prompt_type\": \"config\"
            }
        }'
    ```

    Args:
        body (Prompt):

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
    body: Prompt,

) -> Response[Any | HTTPValidationError]:
    r""" Create Prompt

     Create a new prompt

    👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/prompts\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"prompt_id\": \"my_prompt\",
            \"litellm_params\": {
                \"prompt_id\": \"json_prompt\",
                \"prompt_integration\": \"dotprompt\",
                ### EITHER prompt_directory OR prompt_data MUST BE PROVIDED
                \"prompt_directory\": \"/path/to/dotprompt/folder\",
                \"prompt_data\": {\"json_prompt\": {\"content\": \"This is a prompt\", \"metadata\":
    {\"model\": \"gpt-4\"}}}
            },
            \"prompt_info\": {
                \"prompt_type\": \"config\"
            }
        }'
    ```

    Args:
        body (Prompt):

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
    body: Prompt,

) -> Any | HTTPValidationError | None:
    r""" Create Prompt

     Create a new prompt

    👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/prompts\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"prompt_id\": \"my_prompt\",
            \"litellm_params\": {
                \"prompt_id\": \"json_prompt\",
                \"prompt_integration\": \"dotprompt\",
                ### EITHER prompt_directory OR prompt_data MUST BE PROVIDED
                \"prompt_directory\": \"/path/to/dotprompt/folder\",
                \"prompt_data\": {\"json_prompt\": {\"content\": \"This is a prompt\", \"metadata\":
    {\"model\": \"gpt-4\"}}}
            },
            \"prompt_info\": {
                \"prompt_type\": \"config\"
            }
        }'
    ```

    Args:
        body (Prompt):

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
