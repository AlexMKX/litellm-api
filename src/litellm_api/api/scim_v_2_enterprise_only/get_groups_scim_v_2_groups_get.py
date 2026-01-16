from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.scim_list_response import SCIMListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_index: int | Unset = 1,
    count: int | Unset = 10,
    filter_: None | str | Unset = UNSET,
    feature: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startIndex"] = start_index

    params["count"] = count

    json_filter_: None | str | Unset
    if isinstance(filter_, Unset):
        json_filter_ = UNSET
    else:
        json_filter_ = filter_
    params["filter"] = json_filter_

    json_feature: None | str | Unset
    if isinstance(feature, Unset):
        json_feature = UNSET
    else:
        json_feature = feature
    params["feature"] = json_feature


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/scim/v2/Groups",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | SCIMListResponse | None:
    if response.status_code == 200:
        response_200 = SCIMListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | SCIMListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_index: int | Unset = 1,
    count: int | Unset = 10,
    filter_: None | str | Unset = UNSET,
    feature: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | SCIMListResponse]:
    """ Get Groups

     Get a list of groups according to SCIM v2 protocol

    Args:
        start_index (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        filter_ (None | str | Unset):
        feature (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SCIMListResponse]
     """


    kwargs = _get_kwargs(
        start_index=start_index,
count=count,
filter_=filter_,
feature=feature,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start_index: int | Unset = 1,
    count: int | Unset = 10,
    filter_: None | str | Unset = UNSET,
    feature: None | str | Unset = UNSET,

) -> HTTPValidationError | SCIMListResponse | None:
    """ Get Groups

     Get a list of groups according to SCIM v2 protocol

    Args:
        start_index (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        filter_ (None | str | Unset):
        feature (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SCIMListResponse
     """


    return sync_detailed(
        client=client,
start_index=start_index,
count=count,
filter_=filter_,
feature=feature,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_index: int | Unset = 1,
    count: int | Unset = 10,
    filter_: None | str | Unset = UNSET,
    feature: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | SCIMListResponse]:
    """ Get Groups

     Get a list of groups according to SCIM v2 protocol

    Args:
        start_index (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        filter_ (None | str | Unset):
        feature (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SCIMListResponse]
     """


    kwargs = _get_kwargs(
        start_index=start_index,
count=count,
filter_=filter_,
feature=feature,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start_index: int | Unset = 1,
    count: int | Unset = 10,
    filter_: None | str | Unset = UNSET,
    feature: None | str | Unset = UNSET,

) -> HTTPValidationError | SCIMListResponse | None:
    """ Get Groups

     Get a list of groups according to SCIM v2 protocol

    Args:
        start_index (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        filter_ (None | str | Unset):
        feature (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SCIMListResponse
     """


    return (await asyncio_detailed(
        client=client,
start_index=start_index,
count=count,
filter_=filter_,
feature=feature,

    )).parsed
