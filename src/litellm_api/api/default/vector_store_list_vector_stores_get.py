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
    *,
    after: None | str | Unset = UNSET,
    before: None | str | Unset = UNSET,
    limit: int | None | Unset = 20,
    order: None | str | Unset = 'desc',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

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

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_order: None | str | Unset
    if isinstance(order, Unset):
        json_order = UNSET
    else:
        json_order = order
    params["order"] = json_order


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/vector_stores",
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
    after: None | str | Unset = UNSET,
    before: None | str | Unset = UNSET,
    limit: int | None | Unset = 20,
    order: None | str | Unset = 'desc',

) -> Response[Any | HTTPValidationError]:
    """ Vector Store List

     List vector stores.

    API Reference:
    https://platform.openai.com/docs/api-reference/vector-stores/list

    Args:
        after (None | str | Unset):
        before (None | str | Unset):
        limit (int | None | Unset):  Default: 20.
        order (None | str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        after=after,
before=before,
limit=limit,
order=order,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    after: None | str | Unset = UNSET,
    before: None | str | Unset = UNSET,
    limit: int | None | Unset = 20,
    order: None | str | Unset = 'desc',

) -> Any | HTTPValidationError | None:
    """ Vector Store List

     List vector stores.

    API Reference:
    https://platform.openai.com/docs/api-reference/vector-stores/list

    Args:
        after (None | str | Unset):
        before (None | str | Unset):
        limit (int | None | Unset):  Default: 20.
        order (None | str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
after=after,
before=before,
limit=limit,
order=order,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    after: None | str | Unset = UNSET,
    before: None | str | Unset = UNSET,
    limit: int | None | Unset = 20,
    order: None | str | Unset = 'desc',

) -> Response[Any | HTTPValidationError]:
    """ Vector Store List

     List vector stores.

    API Reference:
    https://platform.openai.com/docs/api-reference/vector-stores/list

    Args:
        after (None | str | Unset):
        before (None | str | Unset):
        limit (int | None | Unset):  Default: 20.
        order (None | str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        after=after,
before=before,
limit=limit,
order=order,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    after: None | str | Unset = UNSET,
    before: None | str | Unset = UNSET,
    limit: int | None | Unset = 20,
    order: None | str | Unset = 'desc',

) -> Any | HTTPValidationError | None:
    """ Vector Store List

     List vector stores.

    API Reference:
    https://platform.openai.com/docs/api-reference/vector-stores/list

    Args:
        after (None | str | Unset):
        before (None | str | Unset):
        limit (int | None | Unset):  Default: 20.
        order (None | str | Unset):  Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
after=after,
before=before,
limit=limit,
order=order,

    )).parsed
