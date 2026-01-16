from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cloud_zero_export_request import CloudZeroExportRequest
from ...models.cloud_zero_export_response import CloudZeroExportResponse
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    *,
    body: CloudZeroExportRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloudzero/dry-run",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CloudZeroExportResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CloudZeroExportResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CloudZeroExportResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CloudZeroExportRequest,

) -> Response[CloudZeroExportResponse | HTTPValidationError]:
    """ Cloudzero Dry Run Export

     Perform a dry run export using the CloudZero logger.

    This endpoint uses the CloudZero logger to perform a dry run export,
    which returns the data that would be exported without actually sending it to CloudZero.

    Parameters:
    - limit: Optional limit on number of records to process (default: 10000)

    Returns:
    - usage_data: Sample of the raw usage data (first 50 records)
    - cbf_data: CloudZero CBF formatted data ready for export
    - summary: Statistics including total cost, tokens, and record counts

    Only admin users can perform CloudZero exports.

    Args:
        body (CloudZeroExportRequest): Request model for CloudZero export operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudZeroExportResponse | HTTPValidationError]
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
    body: CloudZeroExportRequest,

) -> CloudZeroExportResponse | HTTPValidationError | None:
    """ Cloudzero Dry Run Export

     Perform a dry run export using the CloudZero logger.

    This endpoint uses the CloudZero logger to perform a dry run export,
    which returns the data that would be exported without actually sending it to CloudZero.

    Parameters:
    - limit: Optional limit on number of records to process (default: 10000)

    Returns:
    - usage_data: Sample of the raw usage data (first 50 records)
    - cbf_data: CloudZero CBF formatted data ready for export
    - summary: Statistics including total cost, tokens, and record counts

    Only admin users can perform CloudZero exports.

    Args:
        body (CloudZeroExportRequest): Request model for CloudZero export operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudZeroExportResponse | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CloudZeroExportRequest,

) -> Response[CloudZeroExportResponse | HTTPValidationError]:
    """ Cloudzero Dry Run Export

     Perform a dry run export using the CloudZero logger.

    This endpoint uses the CloudZero logger to perform a dry run export,
    which returns the data that would be exported without actually sending it to CloudZero.

    Parameters:
    - limit: Optional limit on number of records to process (default: 10000)

    Returns:
    - usage_data: Sample of the raw usage data (first 50 records)
    - cbf_data: CloudZero CBF formatted data ready for export
    - summary: Statistics including total cost, tokens, and record counts

    Only admin users can perform CloudZero exports.

    Args:
        body (CloudZeroExportRequest): Request model for CloudZero export operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudZeroExportResponse | HTTPValidationError]
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
    body: CloudZeroExportRequest,

) -> CloudZeroExportResponse | HTTPValidationError | None:
    """ Cloudzero Dry Run Export

     Perform a dry run export using the CloudZero logger.

    This endpoint uses the CloudZero logger to perform a dry run export,
    which returns the data that would be exported without actually sending it to CloudZero.

    Parameters:
    - limit: Optional limit on number of records to process (default: 10000)

    Returns:
    - usage_data: Sample of the raw usage data (first 50 records)
    - cbf_data: CloudZero CBF formatted data ready for export
    - summary: Statistics including total cost, tokens, and record counts

    Only admin users can perform CloudZero exports.

    Args:
        body (CloudZeroExportRequest): Request model for CloudZero export operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudZeroExportResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
