from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.list_fine_tuning_jobs_v1_fine_tuning_jobs_get_custom_llm_provider_type_0 import ListFineTuningJobsV1FineTuningJobsGetCustomLlmProviderType0
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    custom_llm_provider: ListFineTuningJobsV1FineTuningJobsGetCustomLlmProviderType0 | None | Unset = UNSET,
    target_model_names: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
    limit: int | None | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_custom_llm_provider: None | str | Unset
    if isinstance(custom_llm_provider, Unset):
        json_custom_llm_provider = UNSET
    elif isinstance(custom_llm_provider, ListFineTuningJobsV1FineTuningJobsGetCustomLlmProviderType0):
        json_custom_llm_provider = custom_llm_provider.value
    else:
        json_custom_llm_provider = custom_llm_provider
    params["custom_llm_provider"] = json_custom_llm_provider

    json_target_model_names: None | str | Unset
    if isinstance(target_model_names, Unset):
        json_target_model_names = UNSET
    else:
        json_target_model_names = target_model_names
    params["target_model_names"] = json_target_model_names

    json_after: None | str | Unset
    if isinstance(after, Unset):
        json_after = UNSET
    else:
        json_after = after
    params["after"] = json_after

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/fine_tuning/jobs",
        "params": params,
    }


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
    custom_llm_provider: ListFineTuningJobsV1FineTuningJobsGetCustomLlmProviderType0 | None | Unset = UNSET,
    target_model_names: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
    limit: int | None | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ ✨ (Enterprise) List Fine-Tuning Jobs

     Lists fine-tuning jobs for the organization.
    This is the equivalent of GET https://api.openai.com/v1/fine_tuning/jobs

    Supported Query Params:
    - `custom_llm_provider`: Name of the LiteLLM provider
    - `after`: Identifier for the last job from the previous pagination request.
    - `limit`: Number of fine-tuning jobs to retrieve (default is 20).

    Args:
        custom_llm_provider (ListFineTuningJobsV1FineTuningJobsGetCustomLlmProviderType0 | None |
            Unset):
        target_model_names (None | str | Unset): Comma separated list of model names to filter by.
            Example: 'gpt-4o,gpt-4o-mini'
        after (None | str | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        custom_llm_provider=custom_llm_provider,
target_model_names=target_model_names,
after=after,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    custom_llm_provider: ListFineTuningJobsV1FineTuningJobsGetCustomLlmProviderType0 | None | Unset = UNSET,
    target_model_names: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
    limit: int | None | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ ✨ (Enterprise) List Fine-Tuning Jobs

     Lists fine-tuning jobs for the organization.
    This is the equivalent of GET https://api.openai.com/v1/fine_tuning/jobs

    Supported Query Params:
    - `custom_llm_provider`: Name of the LiteLLM provider
    - `after`: Identifier for the last job from the previous pagination request.
    - `limit`: Number of fine-tuning jobs to retrieve (default is 20).

    Args:
        custom_llm_provider (ListFineTuningJobsV1FineTuningJobsGetCustomLlmProviderType0 | None |
            Unset):
        target_model_names (None | str | Unset): Comma separated list of model names to filter by.
            Example: 'gpt-4o,gpt-4o-mini'
        after (None | str | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
custom_llm_provider=custom_llm_provider,
target_model_names=target_model_names,
after=after,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    custom_llm_provider: ListFineTuningJobsV1FineTuningJobsGetCustomLlmProviderType0 | None | Unset = UNSET,
    target_model_names: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
    limit: int | None | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ ✨ (Enterprise) List Fine-Tuning Jobs

     Lists fine-tuning jobs for the organization.
    This is the equivalent of GET https://api.openai.com/v1/fine_tuning/jobs

    Supported Query Params:
    - `custom_llm_provider`: Name of the LiteLLM provider
    - `after`: Identifier for the last job from the previous pagination request.
    - `limit`: Number of fine-tuning jobs to retrieve (default is 20).

    Args:
        custom_llm_provider (ListFineTuningJobsV1FineTuningJobsGetCustomLlmProviderType0 | None |
            Unset):
        target_model_names (None | str | Unset): Comma separated list of model names to filter by.
            Example: 'gpt-4o,gpt-4o-mini'
        after (None | str | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        custom_llm_provider=custom_llm_provider,
target_model_names=target_model_names,
after=after,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    custom_llm_provider: ListFineTuningJobsV1FineTuningJobsGetCustomLlmProviderType0 | None | Unset = UNSET,
    target_model_names: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
    limit: int | None | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ ✨ (Enterprise) List Fine-Tuning Jobs

     Lists fine-tuning jobs for the organization.
    This is the equivalent of GET https://api.openai.com/v1/fine_tuning/jobs

    Supported Query Params:
    - `custom_llm_provider`: Name of the LiteLLM provider
    - `after`: Identifier for the last job from the previous pagination request.
    - `limit`: Number of fine-tuning jobs to retrieve (default is 20).

    Args:
        custom_llm_provider (ListFineTuningJobsV1FineTuningJobsGetCustomLlmProviderType0 | None |
            Unset):
        target_model_names (None | str | Unset): Comma separated list of model names to filter by.
            Example: 'gpt-4o,gpt-4o-mini'
        after (None | str | Unset):
        limit (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
custom_llm_provider=custom_llm_provider,
target_model_names=target_model_names,
after=after,
limit=limit,

    )).parsed
