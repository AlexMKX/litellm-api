from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.policy_match_context import PolicyMatchContext
from ...models.policy_test_response import PolicyTestResponse
from typing import cast



def _get_kwargs(
    *,
    body: PolicyMatchContext,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/policy/test",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | PolicyTestResponse | None:
    if response.status_code == 200:
        response_200 = PolicyTestResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | PolicyTestResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PolicyMatchContext,

) -> Response[HTTPValidationError | PolicyTestResponse]:
    r""" Test Policy Matching

     Test which policies would match a given request context.

    This is useful for debugging and understanding policy behavior.

    Request body:
    ```json
    {
        \"team_alias\": \"healthcare-team\",
        \"key_alias\": \"my-api-key\",
        \"model\": \"gpt-4\"
    }
    ```

    Returns:
    - matching_policies: List of policy names that match
    - resolved_guardrails: Final list of guardrails that would be applied

    Args:
        body (PolicyMatchContext): Context used to match a request against policies.

            Contains the team alias, key alias, and model from the incoming request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyTestResponse]
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
    body: PolicyMatchContext,

) -> HTTPValidationError | PolicyTestResponse | None:
    r""" Test Policy Matching

     Test which policies would match a given request context.

    This is useful for debugging and understanding policy behavior.

    Request body:
    ```json
    {
        \"team_alias\": \"healthcare-team\",
        \"key_alias\": \"my-api-key\",
        \"model\": \"gpt-4\"
    }
    ```

    Returns:
    - matching_policies: List of policy names that match
    - resolved_guardrails: Final list of guardrails that would be applied

    Args:
        body (PolicyMatchContext): Context used to match a request against policies.

            Contains the team alias, key alias, and model from the incoming request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyTestResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PolicyMatchContext,

) -> Response[HTTPValidationError | PolicyTestResponse]:
    r""" Test Policy Matching

     Test which policies would match a given request context.

    This is useful for debugging and understanding policy behavior.

    Request body:
    ```json
    {
        \"team_alias\": \"healthcare-team\",
        \"key_alias\": \"my-api-key\",
        \"model\": \"gpt-4\"
    }
    ```

    Returns:
    - matching_policies: List of policy names that match
    - resolved_guardrails: Final list of guardrails that would be applied

    Args:
        body (PolicyMatchContext): Context used to match a request against policies.

            Contains the team alias, key alias, and model from the incoming request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyTestResponse]
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
    body: PolicyMatchContext,

) -> HTTPValidationError | PolicyTestResponse | None:
    r""" Test Policy Matching

     Test which policies would match a given request context.

    This is useful for debugging and understanding policy behavior.

    Request body:
    ```json
    {
        \"team_alias\": \"healthcare-team\",
        \"key_alias\": \"my-api-key\",
        \"model\": \"gpt-4\"
    }
    ```

    Returns:
    - matching_policies: List of policy names that match
    - resolved_guardrails: Final list of guardrails that would be applied

    Args:
        body (PolicyMatchContext): Context used to match a request against policies.

            Contains the team alias, key alias, and model from the incoming request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyTestResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
