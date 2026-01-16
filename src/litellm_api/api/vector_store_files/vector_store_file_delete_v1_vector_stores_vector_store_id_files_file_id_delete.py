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
    vector_store_id: str,
    file_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/vector_stores/{vector_store_id}/files/{file_id}".format(vector_store_id=quote(str(vector_store_id), safe=""),file_id=quote(str(file_id), safe=""),),
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
    vector_store_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | HTTPValidationError]:
    """ Vector Store File Delete

    Args:
        vector_store_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        vector_store_id=vector_store_id,
file_id=file_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    vector_store_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | HTTPValidationError | None:
    """ Vector Store File Delete

    Args:
        vector_store_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        vector_store_id=vector_store_id,
file_id=file_id,
client=client,

    ).parsed

async def asyncio_detailed(
    vector_store_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | HTTPValidationError]:
    """ Vector Store File Delete

    Args:
        vector_store_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        vector_store_id=vector_store_id,
file_id=file_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    vector_store_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | HTTPValidationError | None:
    """ Vector Store File Delete

    Args:
        vector_store_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        vector_store_id=vector_store_id,
file_id=file_id,
client=client,

    )).parsed
