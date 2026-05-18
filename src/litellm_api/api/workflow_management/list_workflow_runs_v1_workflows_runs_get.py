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
    *,
    workflow_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    limit: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_workflow_type: None | str | Unset
    if isinstance(workflow_type, Unset):
        json_workflow_type = UNSET
    else:
        json_workflow_type = workflow_type
    params["workflow_type"] = json_workflow_type

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/workflows/runs",
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
    *,
    client: AuthenticatedClient,
    workflow_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    limit: int | Unset = 50,

) -> Response[Any | HTTPValidationError]:
    """ List Workflow Runs

     List workflow runs. Filter by workflow_type and/or status.

    Non-admin callers only see runs created by their own API key.

    Args:
        workflow_type (None | str | Unset):
        status (None | str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        workflow_type=workflow_type,
status=status,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    workflow_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    limit: int | Unset = 50,

) -> Any | HTTPValidationError | None:
    """ List Workflow Runs

     List workflow runs. Filter by workflow_type and/or status.

    Non-admin callers only see runs created by their own API key.

    Args:
        workflow_type (None | str | Unset):
        status (None | str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
workflow_type=workflow_type,
status=status,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workflow_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    limit: int | Unset = 50,

) -> Response[Any | HTTPValidationError]:
    """ List Workflow Runs

     List workflow runs. Filter by workflow_type and/or status.

    Non-admin callers only see runs created by their own API key.

    Args:
        workflow_type (None | str | Unset):
        status (None | str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        workflow_type=workflow_type,
status=status,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    workflow_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    limit: int | Unset = 50,

) -> Any | HTTPValidationError | None:
    """ List Workflow Runs

     List workflow runs. Filter by workflow_type and/or status.

    Non-admin callers only see runs created by their own API key.

    Args:
        workflow_type (None | str | Unset):
        status (None | str | Unset):
        limit (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
workflow_type=workflow_type,
status=status,
limit=limit,

    )).parsed
