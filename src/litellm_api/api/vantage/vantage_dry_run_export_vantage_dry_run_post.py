from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.vantage_dry_run_request import VantageDryRunRequest
from ...models.vantage_export_response import VantageExportResponse
from typing import cast



def _get_kwargs(
    *,
    body: VantageDryRunRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/vantage/dry-run",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | VantageExportResponse | None:
    if response.status_code == 200:
        response_200 = VantageExportResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | VantageExportResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: VantageDryRunRequest,

) -> Response[HTTPValidationError | VantageExportResponse]:
    """ Vantage Dry Run Export

     Perform a dry run export using the Vantage logger.

    Returns the data that would be exported without actually sending it to Vantage.

    Parameters:
    - limit: Limit on number of records to preview (default: 500)

    Only admin users can perform Vantage exports.

    Args:
        body (VantageDryRunRequest): Request model for Vantage dry-run operations (capped for
            preview)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | VantageExportResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: VantageDryRunRequest,

) -> HTTPValidationError | VantageExportResponse | None:
    """ Vantage Dry Run Export

     Perform a dry run export using the Vantage logger.

    Returns the data that would be exported without actually sending it to Vantage.

    Parameters:
    - limit: Limit on number of records to preview (default: 500)

    Only admin users can perform Vantage exports.

    Args:
        body (VantageDryRunRequest): Request model for Vantage dry-run operations (capped for
            preview)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | VantageExportResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: VantageDryRunRequest,

) -> Response[HTTPValidationError | VantageExportResponse]:
    """ Vantage Dry Run Export

     Perform a dry run export using the Vantage logger.

    Returns the data that would be exported without actually sending it to Vantage.

    Parameters:
    - limit: Limit on number of records to preview (default: 500)

    Only admin users can perform Vantage exports.

    Args:
        body (VantageDryRunRequest): Request model for Vantage dry-run operations (capped for
            preview)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | VantageExportResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: VantageDryRunRequest,

) -> HTTPValidationError | VantageExportResponse | None:
    """ Vantage Dry Run Export

     Perform a dry run export using the Vantage logger.

    Returns the data that would be exported without actually sending it to Vantage.

    Parameters:
    - limit: Limit on number of records to preview (default: 500)

    Only admin users can perform Vantage exports.

    Args:
        body (VantageDryRunRequest): Request model for Vantage dry-run operations (capped for
            preview)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | VantageExportResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
