from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.policy_version_compare_response import PolicyVersionCompareResponse
from typing import cast



def _get_kwargs(
    *,
    version_a: str,
    version_b: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["version_a"] = version_a

    params["version_b"] = version_b


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/policies/compare",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | PolicyVersionCompareResponse | None:
    if response.status_code == 200:
        response_200 = PolicyVersionCompareResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | PolicyVersionCompareResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    version_a: str,
    version_b: str,

) -> Response[HTTPValidationError | PolicyVersionCompareResponse]:
    """ Compare Policy Versions

     Compare two policy versions. Query params: version_a, version_b (policy version IDs).

    Args:
        version_a (str):
        version_b (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyVersionCompareResponse]
     """


    kwargs = _get_kwargs(
        version_a=version_a,
version_b=version_b,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    version_a: str,
    version_b: str,

) -> HTTPValidationError | PolicyVersionCompareResponse | None:
    """ Compare Policy Versions

     Compare two policy versions. Query params: version_a, version_b (policy version IDs).

    Args:
        version_a (str):
        version_b (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyVersionCompareResponse
     """


    return sync_detailed(
        client=client,
version_a=version_a,
version_b=version_b,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    version_a: str,
    version_b: str,

) -> Response[HTTPValidationError | PolicyVersionCompareResponse]:
    """ Compare Policy Versions

     Compare two policy versions. Query params: version_a, version_b (policy version IDs).

    Args:
        version_a (str):
        version_b (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyVersionCompareResponse]
     """


    kwargs = _get_kwargs(
        version_a=version_a,
version_b=version_b,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    version_a: str,
    version_b: str,

) -> HTTPValidationError | PolicyVersionCompareResponse | None:
    """ Compare Policy Versions

     Compare two policy versions. Query params: version_a, version_b (policy version IDs).

    Args:
        version_a (str):
        version_b (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyVersionCompareResponse
     """


    return (await asyncio_detailed(
        client=client,
version_a=version_a,
version_b=version_b,

    )).parsed
