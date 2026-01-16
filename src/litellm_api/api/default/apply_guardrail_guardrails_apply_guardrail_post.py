from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.apply_guardrail_request import ApplyGuardrailRequest
from ...models.apply_guardrail_response import ApplyGuardrailResponse
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    *,
    body: ApplyGuardrailRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/guardrails/apply_guardrail",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApplyGuardrailResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ApplyGuardrailResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApplyGuardrailResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ApplyGuardrailRequest,

) -> Response[ApplyGuardrailResponse | HTTPValidationError]:
    """ Apply Guardrail

     Apply a guardrail to text input and return the processed result.

    This endpoint allows testing guardrails by applying them to custom text inputs.

    Args:
        body (ApplyGuardrailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplyGuardrailResponse | HTTPValidationError]
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
    body: ApplyGuardrailRequest,

) -> ApplyGuardrailResponse | HTTPValidationError | None:
    """ Apply Guardrail

     Apply a guardrail to text input and return the processed result.

    This endpoint allows testing guardrails by applying them to custom text inputs.

    Args:
        body (ApplyGuardrailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplyGuardrailResponse | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ApplyGuardrailRequest,

) -> Response[ApplyGuardrailResponse | HTTPValidationError]:
    """ Apply Guardrail

     Apply a guardrail to text input and return the processed result.

    This endpoint allows testing guardrails by applying them to custom text inputs.

    Args:
        body (ApplyGuardrailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplyGuardrailResponse | HTTPValidationError]
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
    body: ApplyGuardrailRequest,

) -> ApplyGuardrailResponse | HTTPValidationError | None:
    """ Apply Guardrail

     Apply a guardrail to text input and return the processed result.

    This endpoint allows testing guardrails by applying them to custom text inputs.

    Args:
        body (ApplyGuardrailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplyGuardrailResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
