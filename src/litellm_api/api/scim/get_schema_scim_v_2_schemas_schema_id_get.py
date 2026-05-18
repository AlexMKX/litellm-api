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
    schema_id: str,
    *,
    feature: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_feature: None | str | Unset
    if isinstance(feature, Unset):
        json_feature = UNSET
    else:
        json_feature = feature
    params["feature"] = json_feature


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/scim/v2/Schemas/{schema_id}".format(schema_id=quote(str(schema_id), safe=""),),
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
    schema_id: str,
    *,
    client: AuthenticatedClient,
    feature: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Get Schema

     Get a single Schema by its URI per RFC 7643 Section 7.

    Args:
        schema_id (str):
        feature (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        schema_id=schema_id,
feature=feature,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    schema_id: str,
    *,
    client: AuthenticatedClient,
    feature: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Get Schema

     Get a single Schema by its URI per RFC 7643 Section 7.

    Args:
        schema_id (str):
        feature (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        schema_id=schema_id,
client=client,
feature=feature,

    ).parsed

async def asyncio_detailed(
    schema_id: str,
    *,
    client: AuthenticatedClient,
    feature: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Get Schema

     Get a single Schema by its URI per RFC 7643 Section 7.

    Args:
        schema_id (str):
        feature (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        schema_id=schema_id,
feature=feature,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    schema_id: str,
    *,
    client: AuthenticatedClient,
    feature: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Get Schema

     Get a single Schema by its URI per RFC 7643 Section 7.

    Args:
        schema_id (str):
        feature (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        schema_id=schema_id,
client=client,
feature=feature,

    )).parsed
