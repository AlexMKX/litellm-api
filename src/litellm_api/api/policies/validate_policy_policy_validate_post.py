from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.policy_validate_request import PolicyValidateRequest
from ...models.policy_validation_response import PolicyValidationResponse
from typing import cast



def _get_kwargs(
    *,
    body: PolicyValidateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/policy/validate",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | PolicyValidationResponse | None:
    if response.status_code == 200:
        response_200 = PolicyValidationResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | PolicyValidationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PolicyValidateRequest,

) -> Response[HTTPValidationError | PolicyValidationResponse]:
    r""" Validate Policy

     Validate a policy configuration before applying it.

    Checks:
    - All referenced guardrails exist in the guardrail registry
    - All non-wildcard team aliases exist in the database
    - All non-wildcard key aliases exist in the database
    - Inheritance chains are valid (no cycles, parents exist)
    - Scope patterns are syntactically valid

    Returns:
    - valid: True if the policy configuration is valid (no blocking errors)
    - errors: List of blocking validation errors
    - warnings: List of non-blocking validation warnings

    Example request:
    ```json
    {
        \"policies\": {
            \"global-baseline\": {
                \"guardrails\": {
                    \"add\": [\"pii_blocker\", \"phi_blocker\"]
                },
                \"scope\": {
                    \"teams\": [\"*\"],
                    \"keys\": [\"*\"],
                    \"models\": [\"*\"]
                }
            },
            \"healthcare-compliance\": {
                \"inherit\": \"global-baseline\",
                \"guardrails\": {
                    \"add\": [\"hipaa_audit\"]
                },
                \"scope\": {
                    \"teams\": [\"healthcare-team\"]
                }
            }
        }
    }
    ```

    Args:
        body (PolicyValidateRequest): Request body for the /policy/validate endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyValidationResponse]
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
    body: PolicyValidateRequest,

) -> HTTPValidationError | PolicyValidationResponse | None:
    r""" Validate Policy

     Validate a policy configuration before applying it.

    Checks:
    - All referenced guardrails exist in the guardrail registry
    - All non-wildcard team aliases exist in the database
    - All non-wildcard key aliases exist in the database
    - Inheritance chains are valid (no cycles, parents exist)
    - Scope patterns are syntactically valid

    Returns:
    - valid: True if the policy configuration is valid (no blocking errors)
    - errors: List of blocking validation errors
    - warnings: List of non-blocking validation warnings

    Example request:
    ```json
    {
        \"policies\": {
            \"global-baseline\": {
                \"guardrails\": {
                    \"add\": [\"pii_blocker\", \"phi_blocker\"]
                },
                \"scope\": {
                    \"teams\": [\"*\"],
                    \"keys\": [\"*\"],
                    \"models\": [\"*\"]
                }
            },
            \"healthcare-compliance\": {
                \"inherit\": \"global-baseline\",
                \"guardrails\": {
                    \"add\": [\"hipaa_audit\"]
                },
                \"scope\": {
                    \"teams\": [\"healthcare-team\"]
                }
            }
        }
    }
    ```

    Args:
        body (PolicyValidateRequest): Request body for the /policy/validate endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyValidationResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PolicyValidateRequest,

) -> Response[HTTPValidationError | PolicyValidationResponse]:
    r""" Validate Policy

     Validate a policy configuration before applying it.

    Checks:
    - All referenced guardrails exist in the guardrail registry
    - All non-wildcard team aliases exist in the database
    - All non-wildcard key aliases exist in the database
    - Inheritance chains are valid (no cycles, parents exist)
    - Scope patterns are syntactically valid

    Returns:
    - valid: True if the policy configuration is valid (no blocking errors)
    - errors: List of blocking validation errors
    - warnings: List of non-blocking validation warnings

    Example request:
    ```json
    {
        \"policies\": {
            \"global-baseline\": {
                \"guardrails\": {
                    \"add\": [\"pii_blocker\", \"phi_blocker\"]
                },
                \"scope\": {
                    \"teams\": [\"*\"],
                    \"keys\": [\"*\"],
                    \"models\": [\"*\"]
                }
            },
            \"healthcare-compliance\": {
                \"inherit\": \"global-baseline\",
                \"guardrails\": {
                    \"add\": [\"hipaa_audit\"]
                },
                \"scope\": {
                    \"teams\": [\"healthcare-team\"]
                }
            }
        }
    }
    ```

    Args:
        body (PolicyValidateRequest): Request body for the /policy/validate endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyValidationResponse]
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
    body: PolicyValidateRequest,

) -> HTTPValidationError | PolicyValidationResponse | None:
    r""" Validate Policy

     Validate a policy configuration before applying it.

    Checks:
    - All referenced guardrails exist in the guardrail registry
    - All non-wildcard team aliases exist in the database
    - All non-wildcard key aliases exist in the database
    - Inheritance chains are valid (no cycles, parents exist)
    - Scope patterns are syntactically valid

    Returns:
    - valid: True if the policy configuration is valid (no blocking errors)
    - errors: List of blocking validation errors
    - warnings: List of non-blocking validation warnings

    Example request:
    ```json
    {
        \"policies\": {
            \"global-baseline\": {
                \"guardrails\": {
                    \"add\": [\"pii_blocker\", \"phi_blocker\"]
                },
                \"scope\": {
                    \"teams\": [\"*\"],
                    \"keys\": [\"*\"],
                    \"models\": [\"*\"]
                }
            },
            \"healthcare-compliance\": {
                \"inherit\": \"global-baseline\",
                \"guardrails\": {
                    \"add\": [\"hipaa_audit\"]
                },
                \"scope\": {
                    \"teams\": [\"healthcare-team\"]
                }
            }
        }
    }
    ```

    Args:
        body (PolicyValidateRequest): Request body for the /policy/validate endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyValidationResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
