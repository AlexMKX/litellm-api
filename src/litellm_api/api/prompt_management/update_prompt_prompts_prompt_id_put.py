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
    prompt_id: str,
    *,
    body: Prompt,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/prompts/{prompt_id}".format(prompt_id=quote(str(prompt_id), safe=""),),
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
    prompt_id: str,
    *,
    client: AuthenticatedClient,
    body: Prompt,

) -> Response[Any | HTTPValidationError]:
    r""" Update Prompt

     Update an existing prompt

    👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

    Example Request:
    ```bash
    curl -X PUT \"http://localhost:4000/prompts/my_prompt_id\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"prompt_id\": \"my_prompt\",
            \"litellm_params\": {
                \"prompt_id\": \"my_prompt\",
                    \"prompt_integration\": \"dotprompt\",
                    \"prompt_directory\": \"/path/to/prompts\"
                },
                \"prompt_info\": {
                    \"prompt_type\": \"config\"
                }
            }
        }'
    ```

    Args:
        prompt_id (str):
        body (Prompt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        prompt_id=prompt_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    prompt_id: str,
    *,
    client: AuthenticatedClient,
    body: Prompt,

) -> Any | HTTPValidationError | None:
    r""" Update Prompt

     Update an existing prompt

    👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

    Example Request:
    ```bash
    curl -X PUT \"http://localhost:4000/prompts/my_prompt_id\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"prompt_id\": \"my_prompt\",
            \"litellm_params\": {
                \"prompt_id\": \"my_prompt\",
                    \"prompt_integration\": \"dotprompt\",
                    \"prompt_directory\": \"/path/to/prompts\"
                },
                \"prompt_info\": {
                    \"prompt_type\": \"config\"
                }
            }
        }'
    ```

    Args:
        prompt_id (str):
        body (Prompt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        prompt_id=prompt_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    prompt_id: str,
    *,
    client: AuthenticatedClient,
    body: Prompt,

) -> Response[Any | HTTPValidationError]:
    r""" Update Prompt

     Update an existing prompt

    👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

    Example Request:
    ```bash
    curl -X PUT \"http://localhost:4000/prompts/my_prompt_id\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"prompt_id\": \"my_prompt\",
            \"litellm_params\": {
                \"prompt_id\": \"my_prompt\",
                    \"prompt_integration\": \"dotprompt\",
                    \"prompt_directory\": \"/path/to/prompts\"
                },
                \"prompt_info\": {
                    \"prompt_type\": \"config\"
                }
            }
        }'
    ```

    Args:
        prompt_id (str):
        body (Prompt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        prompt_id=prompt_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    prompt_id: str,
    *,
    client: AuthenticatedClient,
    body: Prompt,

) -> Any | HTTPValidationError | None:
    r""" Update Prompt

     Update an existing prompt

    👉 [Prompt docs](https://docs.litellm.ai/docs/proxy/prompt_management)

    Example Request:
    ```bash
    curl -X PUT \"http://localhost:4000/prompts/my_prompt_id\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"prompt_id\": \"my_prompt\",
            \"litellm_params\": {
                \"prompt_id\": \"my_prompt\",
                    \"prompt_integration\": \"dotprompt\",
                    \"prompt_directory\": \"/path/to/prompts\"
                },
                \"prompt_info\": {
                    \"prompt_type\": \"config\"
                }
            }
        }'
    ```

    Args:
        prompt_id (str):
        body (Prompt):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        prompt_id=prompt_id,
client=client,
body=body,

    )).parsed
