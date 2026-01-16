from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    response_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/openai/v1/responses/{response_id}".format(response_id=quote(str(response_id), safe=""),),
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
    response_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | HTTPValidationError]:
    r""" Delete Response

     Delete a response by ID.

    Supports both:
    - Polling IDs (litellm_poll_*): Deletes from Redis cache
    - Provider response IDs: Passes through to provider API

    Follows the OpenAI Responses API spec: https://platform.openai.com/docs/api-
    reference/responses/delete

    ```bash
    curl -X DELETE http://localhost:4000/v1/responses/resp_abc123     -H \"Authorization: Bearer
    sk-1234\"
    ```

    Args:
        response_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        response_id=response_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    response_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | HTTPValidationError | None:
    r""" Delete Response

     Delete a response by ID.

    Supports both:
    - Polling IDs (litellm_poll_*): Deletes from Redis cache
    - Provider response IDs: Passes through to provider API

    Follows the OpenAI Responses API spec: https://platform.openai.com/docs/api-
    reference/responses/delete

    ```bash
    curl -X DELETE http://localhost:4000/v1/responses/resp_abc123     -H \"Authorization: Bearer
    sk-1234\"
    ```

    Args:
        response_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        response_id=response_id,
client=client,

    ).parsed

async def asyncio_detailed(
    response_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | HTTPValidationError]:
    r""" Delete Response

     Delete a response by ID.

    Supports both:
    - Polling IDs (litellm_poll_*): Deletes from Redis cache
    - Provider response IDs: Passes through to provider API

    Follows the OpenAI Responses API spec: https://platform.openai.com/docs/api-
    reference/responses/delete

    ```bash
    curl -X DELETE http://localhost:4000/v1/responses/resp_abc123     -H \"Authorization: Bearer
    sk-1234\"
    ```

    Args:
        response_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        response_id=response_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    response_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | HTTPValidationError | None:
    r""" Delete Response

     Delete a response by ID.

    Supports both:
    - Polling IDs (litellm_poll_*): Deletes from Redis cache
    - Provider response IDs: Passes through to provider API

    Follows the OpenAI Responses API spec: https://platform.openai.com/docs/api-
    reference/responses/delete

    ```bash
    curl -X DELETE http://localhost:4000/v1/responses/resp_abc123     -H \"Authorization: Bearer
    sk-1234\"
    ```

    Args:
        response_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        response_id=response_id,
client=client,

    )).parsed
