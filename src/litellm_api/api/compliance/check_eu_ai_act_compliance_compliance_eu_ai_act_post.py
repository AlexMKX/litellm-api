from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_check_request import ComplianceCheckRequest
from ...models.compliance_response import ComplianceResponse
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    *,
    body: ComplianceCheckRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/compliance/eu-ai-act",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ComplianceResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ComplianceResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ComplianceResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ComplianceCheckRequest,

) -> Response[ComplianceResponse | HTTPValidationError]:
    """ Check Eu Ai Act Compliance

     Check EU AI Act compliance for a spend log entry.

    Checks:
    - Art. 9: Guardrails applied (any guardrail)
    - Art. 5: Content screened before LLM (pre-call guardrails)
    - Art. 12: Audit record complete (user_id, model, timestamp, guardrail_results)

    Args:
        body (ComplianceCheckRequest): Request payload for compliance check endpoints.

            Mirrors the spend log fields needed for compliance evaluation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComplianceResponse | HTTPValidationError]
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
    body: ComplianceCheckRequest,

) -> ComplianceResponse | HTTPValidationError | None:
    """ Check Eu Ai Act Compliance

     Check EU AI Act compliance for a spend log entry.

    Checks:
    - Art. 9: Guardrails applied (any guardrail)
    - Art. 5: Content screened before LLM (pre-call guardrails)
    - Art. 12: Audit record complete (user_id, model, timestamp, guardrail_results)

    Args:
        body (ComplianceCheckRequest): Request payload for compliance check endpoints.

            Mirrors the spend log fields needed for compliance evaluation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComplianceResponse | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ComplianceCheckRequest,

) -> Response[ComplianceResponse | HTTPValidationError]:
    """ Check Eu Ai Act Compliance

     Check EU AI Act compliance for a spend log entry.

    Checks:
    - Art. 9: Guardrails applied (any guardrail)
    - Art. 5: Content screened before LLM (pre-call guardrails)
    - Art. 12: Audit record complete (user_id, model, timestamp, guardrail_results)

    Args:
        body (ComplianceCheckRequest): Request payload for compliance check endpoints.

            Mirrors the spend log fields needed for compliance evaluation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComplianceResponse | HTTPValidationError]
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
    body: ComplianceCheckRequest,

) -> ComplianceResponse | HTTPValidationError | None:
    """ Check Eu Ai Act Compliance

     Check EU AI Act compliance for a spend log entry.

    Checks:
    - Art. 9: Guardrails applied (any guardrail)
    - Art. 5: Content screened before LLM (pre-call guardrails)
    - Art. 12: Audit record complete (user_id, model, timestamp, guardrail_results)

    Args:
        body (ComplianceCheckRequest): Request payload for compliance check endpoints.

            Mirrors the spend log fields needed for compliance evaluation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComplianceResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
