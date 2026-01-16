from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llm_fine_tuning_job_create import LiteLLMFineTuningJobCreate
from typing import cast



def _get_kwargs(
    *,
    body: LiteLLMFineTuningJobCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/fine_tuning/jobs",
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
    body: LiteLLMFineTuningJobCreate,

) -> Response[Any | HTTPValidationError]:
    r""" ✨ (Enterprise) Create Fine-Tuning Job

     Creates a fine-tuning job which begins the process of creating a new model from a given dataset.
    This is the equivalent of POST https://api.openai.com/v1/fine_tuning/jobs

    Supports Identical Params as: https://platform.openai.com/docs/api-reference/fine-tuning/create

    Example Curl:
    ```
    curl http://localhost:4000/v1/fine_tuning/jobs       -H \"Content-Type: application/json\"       -H
    \"Authorization: Bearer sk-1234\"       -d '{
        \"model\": \"gpt-3.5-turbo\",
        \"training_file\": \"file-abc123\",
        \"hyperparameters\": {
          \"n_epochs\": 4
        }
      }'
    ```

    Args:
        body (LiteLLMFineTuningJobCreate):

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
    body: LiteLLMFineTuningJobCreate,

) -> Any | HTTPValidationError | None:
    r""" ✨ (Enterprise) Create Fine-Tuning Job

     Creates a fine-tuning job which begins the process of creating a new model from a given dataset.
    This is the equivalent of POST https://api.openai.com/v1/fine_tuning/jobs

    Supports Identical Params as: https://platform.openai.com/docs/api-reference/fine-tuning/create

    Example Curl:
    ```
    curl http://localhost:4000/v1/fine_tuning/jobs       -H \"Content-Type: application/json\"       -H
    \"Authorization: Bearer sk-1234\"       -d '{
        \"model\": \"gpt-3.5-turbo\",
        \"training_file\": \"file-abc123\",
        \"hyperparameters\": {
          \"n_epochs\": 4
        }
      }'
    ```

    Args:
        body (LiteLLMFineTuningJobCreate):

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
    body: LiteLLMFineTuningJobCreate,

) -> Response[Any | HTTPValidationError]:
    r""" ✨ (Enterprise) Create Fine-Tuning Job

     Creates a fine-tuning job which begins the process of creating a new model from a given dataset.
    This is the equivalent of POST https://api.openai.com/v1/fine_tuning/jobs

    Supports Identical Params as: https://platform.openai.com/docs/api-reference/fine-tuning/create

    Example Curl:
    ```
    curl http://localhost:4000/v1/fine_tuning/jobs       -H \"Content-Type: application/json\"       -H
    \"Authorization: Bearer sk-1234\"       -d '{
        \"model\": \"gpt-3.5-turbo\",
        \"training_file\": \"file-abc123\",
        \"hyperparameters\": {
          \"n_epochs\": 4
        }
      }'
    ```

    Args:
        body (LiteLLMFineTuningJobCreate):

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
    body: LiteLLMFineTuningJobCreate,

) -> Any | HTTPValidationError | None:
    r""" ✨ (Enterprise) Create Fine-Tuning Job

     Creates a fine-tuning job which begins the process of creating a new model from a given dataset.
    This is the equivalent of POST https://api.openai.com/v1/fine_tuning/jobs

    Supports Identical Params as: https://platform.openai.com/docs/api-reference/fine-tuning/create

    Example Curl:
    ```
    curl http://localhost:4000/v1/fine_tuning/jobs       -H \"Content-Type: application/json\"       -H
    \"Authorization: Bearer sk-1234\"       -d '{
        \"model\": \"gpt-3.5-turbo\",
        \"training_file\": \"file-abc123\",
        \"hyperparameters\": {
          \"n_epochs\": 4
        }
      }'
    ```

    Args:
        body (LiteLLMFineTuningJobCreate):

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
