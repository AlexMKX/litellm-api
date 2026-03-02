from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.policy_db_response import PolicyDBResponse
from ...models.policy_version_status_update_request import PolicyVersionStatusUpdateRequest
from typing import cast



def _get_kwargs(
    policy_id: str,
    *,
    body: PolicyVersionStatusUpdateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/policies/{policy_id}/status".format(policy_id=quote(str(policy_id), safe=""),),
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
    policy_id: str,
    *,
    client: AuthenticatedClient,
    body: PolicyVersionStatusUpdateRequest,

) -> Response[HTTPValidationError | PolicyDBResponse]:
    """ Update Policy Version Status

     Update a policy version's status. Valid transitions:
    - draft -> published
    - published -> production (demotes current production to published)
    - production -> published (demotes, policy becomes inactive)

    Args:
        policy_id (str):
        body (PolicyVersionStatusUpdateRequest): Request body for updating a policy version's
            status.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyDBResponse]
     """


    kwargs = _get_kwargs(
        policy_id=policy_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    policy_id: str,
    *,
    client: AuthenticatedClient,
    body: PolicyVersionStatusUpdateRequest,

) -> HTTPValidationError | PolicyDBResponse | None:
    """ Update Policy Version Status

     Update a policy version's status. Valid transitions:
    - draft -> published
    - published -> production (demotes current production to published)
    - production -> published (demotes, policy becomes inactive)

    Args:
        policy_id (str):
        body (PolicyVersionStatusUpdateRequest): Request body for updating a policy version's
            status.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyDBResponse
     """


    return sync_detailed(
        policy_id=policy_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    policy_id: str,
    *,
    client: AuthenticatedClient,
    body: PolicyVersionStatusUpdateRequest,

) -> Response[HTTPValidationError | PolicyDBResponse]:
    """ Update Policy Version Status

     Update a policy version's status. Valid transitions:
    - draft -> published
    - published -> production (demotes current production to published)
    - production -> published (demotes, policy becomes inactive)

    Args:
        policy_id (str):
        body (PolicyVersionStatusUpdateRequest): Request body for updating a policy version's
            status.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyDBResponse]
     """


    kwargs = _get_kwargs(
        policy_id=policy_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    policy_id: str,
    *,
    client: AuthenticatedClient,
    body: PolicyVersionStatusUpdateRequest,

) -> HTTPValidationError | PolicyDBResponse | None:
    """ Update Policy Version Status

     Update a policy version's status. Valid transitions:
    - draft -> published
    - published -> production (demotes current production to published)
    - production -> published (demotes, policy becomes inactive)

    Args:
        policy_id (str):
        body (PolicyVersionStatusUpdateRequest): Request body for updating a policy version's
            status.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyDBResponse
     """


    return (await asyncio_detailed(
        policy_id=policy_id,
client=client,
body=body,

    )).parsed
