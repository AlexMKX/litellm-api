from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.access_group_response import AccessGroupResponse
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    access_group_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/access_group/{access_group_id}".format(access_group_id=quote(str(access_group_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AccessGroupResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AccessGroupResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AccessGroupResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    access_group_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[AccessGroupResponse | HTTPValidationError]:
    """ Get Access Group

    Args:
        access_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccessGroupResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        access_group_id=access_group_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    access_group_id: str,
    *,
    client: AuthenticatedClient,

) -> AccessGroupResponse | HTTPValidationError | None:
    """ Get Access Group

    Args:
        access_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccessGroupResponse | HTTPValidationError
     """


    return sync_detailed(
        access_group_id=access_group_id,
client=client,

    ).parsed

async def asyncio_detailed(
    access_group_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[AccessGroupResponse | HTTPValidationError]:
    """ Get Access Group

    Args:
        access_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccessGroupResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        access_group_id=access_group_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    access_group_id: str,
    *,
    client: AuthenticatedClient,

) -> AccessGroupResponse | HTTPValidationError | None:
    """ Get Access Group

    Args:
        access_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccessGroupResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        access_group_id=access_group_id,
client=client,

    )).parsed
