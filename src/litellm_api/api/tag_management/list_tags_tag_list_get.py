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
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_start_date: None | str | Unset
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: None | str | Unset
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tag/list",
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
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ List Tags

     List all available tags with their budget information.

    Args:
        start_date (None | str | Unset): Optional start date (YYYY-MM-DD). When provided together
            with end_date, dynamic tags are limited to those active in the window. Stored tags are
            always returned.
        end_date (None | str | Unset): Optional end date (YYYY-MM-DD). Must be given with
            start_date.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        start_date=start_date,
end_date=end_date,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ List Tags

     List all available tags with their budget information.

    Args:
        start_date (None | str | Unset): Optional start date (YYYY-MM-DD). When provided together
            with end_date, dynamic tags are limited to those active in the window. Stored tags are
            always returned.
        end_date (None | str | Unset): Optional end date (YYYY-MM-DD). Must be given with
            start_date.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
start_date=start_date,
end_date=end_date,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ List Tags

     List all available tags with their budget information.

    Args:
        start_date (None | str | Unset): Optional start date (YYYY-MM-DD). When provided together
            with end_date, dynamic tags are limited to those active in the window. Stored tags are
            always returned.
        end_date (None | str | Unset): Optional end date (YYYY-MM-DD). Must be given with
            start_date.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        start_date=start_date,
end_date=end_date,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ List Tags

     List all available tags with their budget information.

    Args:
        start_date (None | str | Unset): Optional start date (YYYY-MM-DD). When provided together
            with end_date, dynamic tags are limited to those active in the window. Stored tags are
            always returned.
        end_date (None | str | Unset): Optional end date (YYYY-MM-DD). Must be given with
            start_date.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
start_date=start_date,
end_date=end_date,

    )).parsed
