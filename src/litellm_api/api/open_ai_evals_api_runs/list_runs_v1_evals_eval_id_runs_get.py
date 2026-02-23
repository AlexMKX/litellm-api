from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.list_runs_response import ListRunsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    eval_id: str,
    *,
    limit: int | None | Unset = 20,
    after: None | str | Unset = UNSET,
    before: None | str | Unset = UNSET,
    order: None | str | Unset = UNSET,
    custom_llm_provider: None | str | Unset = 'openai',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_after: None | str | Unset
    if isinstance(after, Unset):
        json_after = UNSET
    else:
        json_after = after
    params["after"] = json_after

    json_before: None | str | Unset
    if isinstance(before, Unset):
        json_before = UNSET
    else:
        json_before = before
    params["before"] = json_before

    json_order: None | str | Unset
    if isinstance(order, Unset):
        json_order = UNSET
    else:
        json_order = order
    params["order"] = json_order

    json_custom_llm_provider: None | str | Unset
    if isinstance(custom_llm_provider, Unset):
        json_custom_llm_provider = UNSET
    else:
        json_custom_llm_provider = custom_llm_provider
    params["custom_llm_provider"] = json_custom_llm_provider


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/evals/{eval_id}/runs".format(eval_id=quote(str(eval_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | ListRunsResponse | None:
    if response.status_code == 200:
        response_200 = ListRunsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | ListRunsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    eval_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = 20,
    after: None | str | Unset = UNSET,
    before: None | str | Unset = UNSET,
    order: None | str | Unset = UNSET,
    custom_llm_provider: None | str | Unset = 'openai',

) -> Response[HTTPValidationError | ListRunsResponse]:
    r""" List Runs

     List all runs for an evaluation with pagination.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: gpt-4-account-1`
    - Pass model via query: `?model=gpt-4-account-1`

    Example usage:
    ```bash
    curl \"http://localhost:4000/v1/evals/eval_123/runs?limit=10\"       -H \"Authorization: Bearer
    your-key\"
    ```

    Returns: ListRunsResponse with list of runs

    Args:
        eval_id (str):
        limit (int | None | Unset):  Default: 20.
        after (None | str | Unset):
        before (None | str | Unset):
        order (None | str | Unset):
        custom_llm_provider (None | str | Unset):  Default: 'openai'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListRunsResponse]
     """


    kwargs = _get_kwargs(
        eval_id=eval_id,
limit=limit,
after=after,
before=before,
order=order,
custom_llm_provider=custom_llm_provider,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    eval_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = 20,
    after: None | str | Unset = UNSET,
    before: None | str | Unset = UNSET,
    order: None | str | Unset = UNSET,
    custom_llm_provider: None | str | Unset = 'openai',

) -> HTTPValidationError | ListRunsResponse | None:
    r""" List Runs

     List all runs for an evaluation with pagination.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: gpt-4-account-1`
    - Pass model via query: `?model=gpt-4-account-1`

    Example usage:
    ```bash
    curl \"http://localhost:4000/v1/evals/eval_123/runs?limit=10\"       -H \"Authorization: Bearer
    your-key\"
    ```

    Returns: ListRunsResponse with list of runs

    Args:
        eval_id (str):
        limit (int | None | Unset):  Default: 20.
        after (None | str | Unset):
        before (None | str | Unset):
        order (None | str | Unset):
        custom_llm_provider (None | str | Unset):  Default: 'openai'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListRunsResponse
     """


    return sync_detailed(
        eval_id=eval_id,
client=client,
limit=limit,
after=after,
before=before,
order=order,
custom_llm_provider=custom_llm_provider,

    ).parsed

async def asyncio_detailed(
    eval_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = 20,
    after: None | str | Unset = UNSET,
    before: None | str | Unset = UNSET,
    order: None | str | Unset = UNSET,
    custom_llm_provider: None | str | Unset = 'openai',

) -> Response[HTTPValidationError | ListRunsResponse]:
    r""" List Runs

     List all runs for an evaluation with pagination.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: gpt-4-account-1`
    - Pass model via query: `?model=gpt-4-account-1`

    Example usage:
    ```bash
    curl \"http://localhost:4000/v1/evals/eval_123/runs?limit=10\"       -H \"Authorization: Bearer
    your-key\"
    ```

    Returns: ListRunsResponse with list of runs

    Args:
        eval_id (str):
        limit (int | None | Unset):  Default: 20.
        after (None | str | Unset):
        before (None | str | Unset):
        order (None | str | Unset):
        custom_llm_provider (None | str | Unset):  Default: 'openai'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListRunsResponse]
     """


    kwargs = _get_kwargs(
        eval_id=eval_id,
limit=limit,
after=after,
before=before,
order=order,
custom_llm_provider=custom_llm_provider,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    eval_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = 20,
    after: None | str | Unset = UNSET,
    before: None | str | Unset = UNSET,
    order: None | str | Unset = UNSET,
    custom_llm_provider: None | str | Unset = 'openai',

) -> HTTPValidationError | ListRunsResponse | None:
    r""" List Runs

     List all runs for an evaluation with pagination.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: gpt-4-account-1`
    - Pass model via query: `?model=gpt-4-account-1`

    Example usage:
    ```bash
    curl \"http://localhost:4000/v1/evals/eval_123/runs?limit=10\"       -H \"Authorization: Bearer
    your-key\"
    ```

    Returns: ListRunsResponse with list of runs

    Args:
        eval_id (str):
        limit (int | None | Unset):  Default: 20.
        after (None | str | Unset):
        before (None | str | Unset):
        order (None | str | Unset):
        custom_llm_provider (None | str | Unset):  Default: 'openai'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListRunsResponse
     """


    return (await asyncio_detailed(
        eval_id=eval_id,
client=client,
limit=limit,
after=after,
before=before,
order=order,
custom_llm_provider=custom_llm_provider,

    )).parsed
