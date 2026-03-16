from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.register_guardrail_request import RegisterGuardrailRequest
from ...models.register_guardrail_response import RegisterGuardrailResponse
from typing import cast



def _get_kwargs(
    *,
    body: RegisterGuardrailRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/guardrails/register",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | RegisterGuardrailResponse | None:
    if response.status_code == 200:
        response_200 = RegisterGuardrailResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | RegisterGuardrailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RegisterGuardrailRequest,

) -> Response[HTTPValidationError | RegisterGuardrailResponse]:
    """ Register Guardrail

     Register a guardrail for onboarding (team submission).

    Accepts a guardrail config in the
    [Generic Guardrail API](https://docs.litellm.ai/docs/adding_provider/generic_guardrail_api) format.
    The submission is stored with status `pending_review` until an admin approves it.

    Args:
        body (RegisterGuardrailRequest): Request body for POST /guardrails/register. Follows
            Generic Guardrail API config.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RegisterGuardrailResponse]
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
    body: RegisterGuardrailRequest,

) -> HTTPValidationError | RegisterGuardrailResponse | None:
    """ Register Guardrail

     Register a guardrail for onboarding (team submission).

    Accepts a guardrail config in the
    [Generic Guardrail API](https://docs.litellm.ai/docs/adding_provider/generic_guardrail_api) format.
    The submission is stored with status `pending_review` until an admin approves it.

    Args:
        body (RegisterGuardrailRequest): Request body for POST /guardrails/register. Follows
            Generic Guardrail API config.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RegisterGuardrailResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RegisterGuardrailRequest,

) -> Response[HTTPValidationError | RegisterGuardrailResponse]:
    """ Register Guardrail

     Register a guardrail for onboarding (team submission).

    Accepts a guardrail config in the
    [Generic Guardrail API](https://docs.litellm.ai/docs/adding_provider/generic_guardrail_api) format.
    The submission is stored with status `pending_review` until an admin approves it.

    Args:
        body (RegisterGuardrailRequest): Request body for POST /guardrails/register. Follows
            Generic Guardrail API config.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RegisterGuardrailResponse]
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
    body: RegisterGuardrailRequest,

) -> HTTPValidationError | RegisterGuardrailResponse | None:
    """ Register Guardrail

     Register a guardrail for onboarding (team submission).

    Accepts a guardrail config in the
    [Generic Guardrail API](https://docs.litellm.ai/docs/adding_provider/generic_guardrail_api) format.
    The submission is stored with status `pending_review` until an admin approves it.

    Args:
        body (RegisterGuardrailRequest): Request body for POST /guardrails/register. Follows
            Generic Guardrail API config.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RegisterGuardrailResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
