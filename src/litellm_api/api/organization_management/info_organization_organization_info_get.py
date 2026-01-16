from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llm_organization_table_with_members import LiteLLMOrganizationTableWithMembers
from typing import cast



def _get_kwargs(
    *,
    organization_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["organization_id"] = organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/organization/info",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | LiteLLMOrganizationTableWithMembers | None:
    if response.status_code == 200:
        response_200 = LiteLLMOrganizationTableWithMembers.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | LiteLLMOrganizationTableWithMembers]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    organization_id: str,

) -> Response[HTTPValidationError | LiteLLMOrganizationTableWithMembers]:
    """ Info Organization

     Get the org specific information

    Args:
        organization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiteLLMOrganizationTableWithMembers]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    organization_id: str,

) -> HTTPValidationError | LiteLLMOrganizationTableWithMembers | None:
    """ Info Organization

     Get the org specific information

    Args:
        organization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiteLLMOrganizationTableWithMembers
     """


    return sync_detailed(
        client=client,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    organization_id: str,

) -> Response[HTTPValidationError | LiteLLMOrganizationTableWithMembers]:
    """ Info Organization

     Get the org specific information

    Args:
        organization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiteLLMOrganizationTableWithMembers]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    organization_id: str,

) -> HTTPValidationError | LiteLLMOrganizationTableWithMembers | None:
    """ Info Organization

     Get the org specific information

    Args:
        organization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiteLLMOrganizationTableWithMembers
     """


    return (await asyncio_detailed(
        client=client,
organization_id=organization_id,

    )).parsed
