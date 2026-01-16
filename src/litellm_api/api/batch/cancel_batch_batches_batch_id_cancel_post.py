from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    batch_id: str,
    *,
    provider: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_provider: None | str | Unset
    if isinstance(provider, Unset):
        json_provider = UNSET
    else:
        json_provider = provider
    params["provider"] = json_provider


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/batches/{batch_id}/cancel".format(batch_id=quote(str(batch_id), safe=""),),
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
    batch_id: str,
    *,
    client: AuthenticatedClient,
    provider: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Cancel Batch

     Cancel a batch.
    This is the equivalent of POST https://api.openai.com/v1/batches/{batch_id}/cancel

    Supports Identical Params as: https://platform.openai.com/docs/api-reference/batch/cancel

    Example Curl
    ```
    curl http://localhost:4000/v1/batches/batch_abc123/cancel         -H \"Authorization: Bearer
    sk-1234\"         -H \"Content-Type: application/json\"         -X POST

    ```

    Args:
        batch_id (str):
        provider (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        batch_id=batch_id,
provider=provider,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    provider: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Cancel Batch

     Cancel a batch.
    This is the equivalent of POST https://api.openai.com/v1/batches/{batch_id}/cancel

    Supports Identical Params as: https://platform.openai.com/docs/api-reference/batch/cancel

    Example Curl
    ```
    curl http://localhost:4000/v1/batches/batch_abc123/cancel         -H \"Authorization: Bearer
    sk-1234\"         -H \"Content-Type: application/json\"         -X POST

    ```

    Args:
        batch_id (str):
        provider (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        batch_id=batch_id,
client=client,
provider=provider,

    ).parsed

async def asyncio_detailed(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    provider: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Cancel Batch

     Cancel a batch.
    This is the equivalent of POST https://api.openai.com/v1/batches/{batch_id}/cancel

    Supports Identical Params as: https://platform.openai.com/docs/api-reference/batch/cancel

    Example Curl
    ```
    curl http://localhost:4000/v1/batches/batch_abc123/cancel         -H \"Authorization: Bearer
    sk-1234\"         -H \"Content-Type: application/json\"         -X POST

    ```

    Args:
        batch_id (str):
        provider (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        batch_id=batch_id,
provider=provider,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    provider: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Cancel Batch

     Cancel a batch.
    This is the equivalent of POST https://api.openai.com/v1/batches/{batch_id}/cancel

    Supports Identical Params as: https://platform.openai.com/docs/api-reference/batch/cancel

    Example Curl
    ```
    curl http://localhost:4000/v1/batches/batch_abc123/cancel         -H \"Authorization: Bearer
    sk-1234\"         -H \"Content-Type: application/json\"         -X POST

    ```

    Args:
        batch_id (str):
        provider (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        batch_id=batch_id,
client=client,
provider=provider,

    )).parsed
