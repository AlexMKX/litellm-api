from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.retrieve_fine_tuning_job_v1_fine_tuning_jobs_fine_tuning_job_id_get_custom_llm_provider_type_0 import RetrieveFineTuningJobV1FineTuningJobsFineTuningJobIdGetCustomLlmProviderType0
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    fine_tuning_job_id: str,
    *,
    custom_llm_provider: None | RetrieveFineTuningJobV1FineTuningJobsFineTuningJobIdGetCustomLlmProviderType0 | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_custom_llm_provider: None | str | Unset
    if isinstance(custom_llm_provider, Unset):
        json_custom_llm_provider = UNSET
    elif isinstance(custom_llm_provider, RetrieveFineTuningJobV1FineTuningJobsFineTuningJobIdGetCustomLlmProviderType0):
        json_custom_llm_provider = custom_llm_provider.value
    else:
        json_custom_llm_provider = custom_llm_provider
    params["custom_llm_provider"] = json_custom_llm_provider


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/fine_tuning/jobs/{fine_tuning_job_id}".format(fine_tuning_job_id=quote(str(fine_tuning_job_id), safe=""),),
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
    fine_tuning_job_id: str,
    *,
    client: AuthenticatedClient,
    custom_llm_provider: None | RetrieveFineTuningJobV1FineTuningJobsFineTuningJobIdGetCustomLlmProviderType0 | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ ✨ (Enterprise) Retrieve Fine-Tuning Job

     Retrieves a fine-tuning job.
    This is the equivalent of GET https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}

    Supported Query Params:
    - `custom_llm_provider`: Name of the LiteLLM provider
    - `fine_tuning_job_id`: The ID of the fine-tuning job to retrieve.

    Args:
        fine_tuning_job_id (str):
        custom_llm_provider (None |
            RetrieveFineTuningJobV1FineTuningJobsFineTuningJobIdGetCustomLlmProviderType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        fine_tuning_job_id=fine_tuning_job_id,
custom_llm_provider=custom_llm_provider,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    fine_tuning_job_id: str,
    *,
    client: AuthenticatedClient,
    custom_llm_provider: None | RetrieveFineTuningJobV1FineTuningJobsFineTuningJobIdGetCustomLlmProviderType0 | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ ✨ (Enterprise) Retrieve Fine-Tuning Job

     Retrieves a fine-tuning job.
    This is the equivalent of GET https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}

    Supported Query Params:
    - `custom_llm_provider`: Name of the LiteLLM provider
    - `fine_tuning_job_id`: The ID of the fine-tuning job to retrieve.

    Args:
        fine_tuning_job_id (str):
        custom_llm_provider (None |
            RetrieveFineTuningJobV1FineTuningJobsFineTuningJobIdGetCustomLlmProviderType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        fine_tuning_job_id=fine_tuning_job_id,
client=client,
custom_llm_provider=custom_llm_provider,

    ).parsed

async def asyncio_detailed(
    fine_tuning_job_id: str,
    *,
    client: AuthenticatedClient,
    custom_llm_provider: None | RetrieveFineTuningJobV1FineTuningJobsFineTuningJobIdGetCustomLlmProviderType0 | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ ✨ (Enterprise) Retrieve Fine-Tuning Job

     Retrieves a fine-tuning job.
    This is the equivalent of GET https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}

    Supported Query Params:
    - `custom_llm_provider`: Name of the LiteLLM provider
    - `fine_tuning_job_id`: The ID of the fine-tuning job to retrieve.

    Args:
        fine_tuning_job_id (str):
        custom_llm_provider (None |
            RetrieveFineTuningJobV1FineTuningJobsFineTuningJobIdGetCustomLlmProviderType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        fine_tuning_job_id=fine_tuning_job_id,
custom_llm_provider=custom_llm_provider,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    fine_tuning_job_id: str,
    *,
    client: AuthenticatedClient,
    custom_llm_provider: None | RetrieveFineTuningJobV1FineTuningJobsFineTuningJobIdGetCustomLlmProviderType0 | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ ✨ (Enterprise) Retrieve Fine-Tuning Job

     Retrieves a fine-tuning job.
    This is the equivalent of GET https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}

    Supported Query Params:
    - `custom_llm_provider`: Name of the LiteLLM provider
    - `fine_tuning_job_id`: The ID of the fine-tuning job to retrieve.

    Args:
        fine_tuning_job_id (str):
        custom_llm_provider (None |
            RetrieveFineTuningJobV1FineTuningJobsFineTuningJobIdGetCustomLlmProviderType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        fine_tuning_job_id=fine_tuning_job_id,
client=client,
custom_llm_provider=custom_llm_provider,

    )).parsed
