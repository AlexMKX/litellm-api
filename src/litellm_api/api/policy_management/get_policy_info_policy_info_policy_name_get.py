from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.policy_info_response import PolicyInfoResponse
from typing import cast



def _get_kwargs(
    policy_name: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/policy/info/{policy_name}".format(policy_name=quote(str(policy_name), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | PolicyInfoResponse | None:
    if response.status_code == 200:
        response_200 = PolicyInfoResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | PolicyInfoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    policy_name: str,
    *,
    client: AuthenticatedClient,

) -> Response[HTTPValidationError | PolicyInfoResponse]:
    """ Get Policy Info

     Get detailed information about a specific policy.

    Returns:
    - Policy configuration
    - Resolved guardrails (after inheritance)
    - Inheritance chain

    Args:
        policy_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyInfoResponse]
     """


    kwargs = _get_kwargs(
        policy_name=policy_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    policy_name: str,
    *,
    client: AuthenticatedClient,

) -> HTTPValidationError | PolicyInfoResponse | None:
    """ Get Policy Info

     Get detailed information about a specific policy.

    Returns:
    - Policy configuration
    - Resolved guardrails (after inheritance)
    - Inheritance chain

    Args:
        policy_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyInfoResponse
     """


    return sync_detailed(
        policy_name=policy_name,
client=client,

    ).parsed

async def asyncio_detailed(
    policy_name: str,
    *,
    client: AuthenticatedClient,

) -> Response[HTTPValidationError | PolicyInfoResponse]:
    """ Get Policy Info

     Get detailed information about a specific policy.

    Returns:
    - Policy configuration
    - Resolved guardrails (after inheritance)
    - Inheritance chain

    Args:
        policy_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyInfoResponse]
     """


    kwargs = _get_kwargs(
        policy_name=policy_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    policy_name: str,
    *,
    client: AuthenticatedClient,

) -> HTTPValidationError | PolicyInfoResponse | None:
    """ Get Policy Info

     Get detailed information about a specific policy.

    Returns:
    - Policy configuration
    - Resolved guardrails (after inheritance)
    - Inheritance chain

    Args:
        policy_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyInfoResponse
     """


    return (await asyncio_detailed(
        policy_name=policy_name,
client=client,

    )).parsed
