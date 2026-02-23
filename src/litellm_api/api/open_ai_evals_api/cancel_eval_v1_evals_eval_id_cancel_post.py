from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cancel_eval_response import CancelEvalResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    eval_id: str,
    *,
    custom_llm_provider: None | str | Unset = 'openai',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_custom_llm_provider: None | str | Unset
    if isinstance(custom_llm_provider, Unset):
        json_custom_llm_provider = UNSET
    else:
        json_custom_llm_provider = custom_llm_provider
    params["custom_llm_provider"] = json_custom_llm_provider


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/evals/{eval_id}/cancel".format(eval_id=quote(str(eval_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CancelEvalResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CancelEvalResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CancelEvalResponse | HTTPValidationError]:
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
    custom_llm_provider: None | str | Unset = 'openai',

) -> Response[CancelEvalResponse | HTTPValidationError]:
    r""" Cancel Eval

     Cancel a running evaluation.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: gpt-4-account-1`
    - Pass model via query: `?model=gpt-4-account-1`
    - Pass model via body: `{\"model\": \"gpt-4-account-1\"}`

    Example usage:
    ```bash
    curl -X POST \"http://localhost:4000/v1/evals/eval_123/cancel\"       -H \"Authorization: Bearer
    your-key\"
    ```

    Returns: CancelEvalResponse with cancellation confirmation

    Args:
        eval_id (str):
        custom_llm_provider (None | str | Unset):  Default: 'openai'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelEvalResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        eval_id=eval_id,
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
    custom_llm_provider: None | str | Unset = 'openai',

) -> CancelEvalResponse | HTTPValidationError | None:
    r""" Cancel Eval

     Cancel a running evaluation.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: gpt-4-account-1`
    - Pass model via query: `?model=gpt-4-account-1`
    - Pass model via body: `{\"model\": \"gpt-4-account-1\"}`

    Example usage:
    ```bash
    curl -X POST \"http://localhost:4000/v1/evals/eval_123/cancel\"       -H \"Authorization: Bearer
    your-key\"
    ```

    Returns: CancelEvalResponse with cancellation confirmation

    Args:
        eval_id (str):
        custom_llm_provider (None | str | Unset):  Default: 'openai'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelEvalResponse | HTTPValidationError
     """


    return sync_detailed(
        eval_id=eval_id,
client=client,
custom_llm_provider=custom_llm_provider,

    ).parsed

async def asyncio_detailed(
    eval_id: str,
    *,
    client: AuthenticatedClient,
    custom_llm_provider: None | str | Unset = 'openai',

) -> Response[CancelEvalResponse | HTTPValidationError]:
    r""" Cancel Eval

     Cancel a running evaluation.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: gpt-4-account-1`
    - Pass model via query: `?model=gpt-4-account-1`
    - Pass model via body: `{\"model\": \"gpt-4-account-1\"}`

    Example usage:
    ```bash
    curl -X POST \"http://localhost:4000/v1/evals/eval_123/cancel\"       -H \"Authorization: Bearer
    your-key\"
    ```

    Returns: CancelEvalResponse with cancellation confirmation

    Args:
        eval_id (str):
        custom_llm_provider (None | str | Unset):  Default: 'openai'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelEvalResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        eval_id=eval_id,
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
    custom_llm_provider: None | str | Unset = 'openai',

) -> CancelEvalResponse | HTTPValidationError | None:
    r""" Cancel Eval

     Cancel a running evaluation.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: gpt-4-account-1`
    - Pass model via query: `?model=gpt-4-account-1`
    - Pass model via body: `{\"model\": \"gpt-4-account-1\"}`

    Example usage:
    ```bash
    curl -X POST \"http://localhost:4000/v1/evals/eval_123/cancel\"       -H \"Authorization: Bearer
    your-key\"
    ```

    Returns: CancelEvalResponse with cancellation confirmation

    Args:
        eval_id (str):
        custom_llm_provider (None | str | Unset):  Default: 'openai'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelEvalResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        eval_id=eval_id,
client=client,
custom_llm_provider=custom_llm_provider,

    )).parsed
