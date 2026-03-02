from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.policy_db_response import PolicyDBResponse
from ...models.policy_version_create_request import PolicyVersionCreateRequest
from typing import cast



def _get_kwargs(
    policy_name: str,
    *,
    body: PolicyVersionCreateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/policies/name/{policy_name}/versions".format(policy_name=quote(str(policy_name), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | PolicyDBResponse | None:
    if response.status_code == 200:
        response_200 = PolicyDBResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | PolicyDBResponse]:
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
    body: PolicyVersionCreateRequest,

) -> Response[HTTPValidationError | PolicyDBResponse]:
    """ Create Policy Version

     Create a new draft version of a policy. Copies all fields from the source.
    Source is current production if source_policy_id is not provided.

    Args:
        policy_name (str):
        body (PolicyVersionCreateRequest): Request body for creating a new policy version (draft).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyDBResponse]
     """


    kwargs = _get_kwargs(
        policy_name=policy_name,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    policy_name: str,
    *,
    client: AuthenticatedClient,
    body: PolicyVersionCreateRequest,

) -> HTTPValidationError | PolicyDBResponse | None:
    """ Create Policy Version

     Create a new draft version of a policy. Copies all fields from the source.
    Source is current production if source_policy_id is not provided.

    Args:
        policy_name (str):
        body (PolicyVersionCreateRequest): Request body for creating a new policy version (draft).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyDBResponse
     """


    return sync_detailed(
        policy_name=policy_name,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    policy_name: str,
    *,
    client: AuthenticatedClient,
    body: PolicyVersionCreateRequest,

) -> Response[HTTPValidationError | PolicyDBResponse]:
    """ Create Policy Version

     Create a new draft version of a policy. Copies all fields from the source.
    Source is current production if source_policy_id is not provided.

    Args:
        policy_name (str):
        body (PolicyVersionCreateRequest): Request body for creating a new policy version (draft).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyDBResponse]
     """


    kwargs = _get_kwargs(
        policy_name=policy_name,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    policy_name: str,
    *,
    client: AuthenticatedClient,
    body: PolicyVersionCreateRequest,

) -> HTTPValidationError | PolicyDBResponse | None:
    """ Create Policy Version

     Create a new draft version of a policy. Copies all fields from the source.
    Source is current production if source_policy_id is not provided.

    Args:
        policy_name (str):
        body (PolicyVersionCreateRequest): Request body for creating a new policy version (draft).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyDBResponse
     """


    return (await asyncio_detailed(
        policy_name=policy_name,
client=client,
body=body,

    )).parsed
