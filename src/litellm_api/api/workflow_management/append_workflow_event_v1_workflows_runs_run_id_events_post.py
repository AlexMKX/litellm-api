from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.workflow_event_create_request import WorkflowEventCreateRequest
from typing import cast



def _get_kwargs(
    run_id: str,
    *,
    body: WorkflowEventCreateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/workflows/runs/{run_id}/events".format(run_id=quote(str(run_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    run_id: str,
    *,
    client: AuthenticatedClient,
    body: WorkflowEventCreateRequest,

) -> Response[Any | HTTPValidationError]:
    """ Append Workflow Event

     Append an event to the run's event log. Also updates run.status if event_type maps to a status.

    Sequence numbers use optimistic concurrency: on a unique-constraint collision
    (concurrent append), retries up to _MAX_SEQUENCE_RETRIES times with a fresh MAX+1.
    The event+status update is atomic in a single DB transaction.

    Args:
        run_id (str):
        body (WorkflowEventCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        run_id=run_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    run_id: str,
    *,
    client: AuthenticatedClient,
    body: WorkflowEventCreateRequest,

) -> Any | HTTPValidationError | None:
    """ Append Workflow Event

     Append an event to the run's event log. Also updates run.status if event_type maps to a status.

    Sequence numbers use optimistic concurrency: on a unique-constraint collision
    (concurrent append), retries up to _MAX_SEQUENCE_RETRIES times with a fresh MAX+1.
    The event+status update is atomic in a single DB transaction.

    Args:
        run_id (str):
        body (WorkflowEventCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        run_id=run_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
    body: WorkflowEventCreateRequest,

) -> Response[Any | HTTPValidationError]:
    """ Append Workflow Event

     Append an event to the run's event log. Also updates run.status if event_type maps to a status.

    Sequence numbers use optimistic concurrency: on a unique-constraint collision
    (concurrent append), retries up to _MAX_SEQUENCE_RETRIES times with a fresh MAX+1.
    The event+status update is atomic in a single DB transaction.

    Args:
        run_id (str):
        body (WorkflowEventCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        run_id=run_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient,
    body: WorkflowEventCreateRequest,

) -> Any | HTTPValidationError | None:
    """ Append Workflow Event

     Append an event to the run's event log. Also updates run.status if event_type maps to a status.

    Sequence numbers use optimistic concurrency: on a unique-constraint collision
    (concurrent append), retries up to _MAX_SEQUENCE_RETRIES times with a fresh MAX+1.
    The event+status update is atomic in a single DB transaction.

    Args:
        run_id (str):
        body (WorkflowEventCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        run_id=run_id,
client=client,
body=body,

    )).parsed
