from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.guardrail_submission_item import GuardrailSubmissionItem
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    guardrail_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/guardrails/submissions/{guardrail_id}".format(guardrail_id=quote(str(guardrail_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GuardrailSubmissionItem | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = GuardrailSubmissionItem.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GuardrailSubmissionItem | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    guardrail_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[GuardrailSubmissionItem | HTTPValidationError]:
    """ Get Guardrail Submission

     Get a single guardrail submission by id (admin only).

    Args:
        guardrail_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GuardrailSubmissionItem | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        guardrail_id=guardrail_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    guardrail_id: str,
    *,
    client: AuthenticatedClient,

) -> GuardrailSubmissionItem | HTTPValidationError | None:
    """ Get Guardrail Submission

     Get a single guardrail submission by id (admin only).

    Args:
        guardrail_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GuardrailSubmissionItem | HTTPValidationError
     """


    return sync_detailed(
        guardrail_id=guardrail_id,
client=client,

    ).parsed

async def asyncio_detailed(
    guardrail_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[GuardrailSubmissionItem | HTTPValidationError]:
    """ Get Guardrail Submission

     Get a single guardrail submission by id (admin only).

    Args:
        guardrail_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GuardrailSubmissionItem | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        guardrail_id=guardrail_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    guardrail_id: str,
    *,
    client: AuthenticatedClient,

) -> GuardrailSubmissionItem | HTTPValidationError | None:
    """ Get Guardrail Submission

     Get a single guardrail submission by id (admin only).

    Args:
        guardrail_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GuardrailSubmissionItem | HTTPValidationError
     """


    return (await asyncio_detailed(
        guardrail_id=guardrail_id,
client=client,

    )).parsed
