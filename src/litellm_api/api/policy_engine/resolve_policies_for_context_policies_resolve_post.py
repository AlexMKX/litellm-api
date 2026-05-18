from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.policy_resolve_request import PolicyResolveRequest
from ...models.policy_resolve_response import PolicyResolveResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: PolicyResolveRequest,
    force_sync: bool | Unset = False,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["force_sync"] = force_sync


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/policies/resolve",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | PolicyResolveResponse | None:
    if response.status_code == 200:
        response_200 = PolicyResolveResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | PolicyResolveResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PolicyResolveRequest,
    force_sync: bool | Unset = False,

) -> Response[HTTPValidationError | PolicyResolveResponse]:
    r""" Resolve Policies For Context

     Resolve which policies and guardrails apply for a given context.

    Use this endpoint to debug \"what guardrails would apply to a request
    with this team/key/model/tags combination?\"

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/resolve\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"tags\": [\"healthcare\"],
            \"model\": \"gpt-4\"
        }'
    ```

    Args:
        force_sync (bool | Unset): Force a DB sync before resolving. Default uses in-memory cache.
            Default: False.
        body (PolicyResolveRequest): Request body for resolving effective policies/guardrails for
            a context.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyResolveResponse]
     """


    kwargs = _get_kwargs(
        body=body,
force_sync=force_sync,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: PolicyResolveRequest,
    force_sync: bool | Unset = False,

) -> HTTPValidationError | PolicyResolveResponse | None:
    r""" Resolve Policies For Context

     Resolve which policies and guardrails apply for a given context.

    Use this endpoint to debug \"what guardrails would apply to a request
    with this team/key/model/tags combination?\"

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/resolve\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"tags\": [\"healthcare\"],
            \"model\": \"gpt-4\"
        }'
    ```

    Args:
        force_sync (bool | Unset): Force a DB sync before resolving. Default uses in-memory cache.
            Default: False.
        body (PolicyResolveRequest): Request body for resolving effective policies/guardrails for
            a context.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyResolveResponse
     """


    return sync_detailed(
        client=client,
body=body,
force_sync=force_sync,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PolicyResolveRequest,
    force_sync: bool | Unset = False,

) -> Response[HTTPValidationError | PolicyResolveResponse]:
    r""" Resolve Policies For Context

     Resolve which policies and guardrails apply for a given context.

    Use this endpoint to debug \"what guardrails would apply to a request
    with this team/key/model/tags combination?\"

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/resolve\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"tags\": [\"healthcare\"],
            \"model\": \"gpt-4\"
        }'
    ```

    Args:
        force_sync (bool | Unset): Force a DB sync before resolving. Default uses in-memory cache.
            Default: False.
        body (PolicyResolveRequest): Request body for resolving effective policies/guardrails for
            a context.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyResolveResponse]
     """


    kwargs = _get_kwargs(
        body=body,
force_sync=force_sync,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PolicyResolveRequest,
    force_sync: bool | Unset = False,

) -> HTTPValidationError | PolicyResolveResponse | None:
    r""" Resolve Policies For Context

     Resolve which policies and guardrails apply for a given context.

    Use this endpoint to debug \"what guardrails would apply to a request
    with this team/key/model/tags combination?\"

    Example Request:
    ```bash
    curl -X POST \"http://localhost:4000/policies/resolve\" \
        -H \"Authorization: Bearer <your_api_key>\" \
        -H \"Content-Type: application/json\" \
        -d '{
            \"tags\": [\"healthcare\"],
            \"model\": \"gpt-4\"
        }'
    ```

    Args:
        force_sync (bool | Unset): Force a DB sync before resolving. Default uses in-memory cache.
            Default: False.
        body (PolicyResolveRequest): Request body for resolving effective policies/guardrails for
            a context.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyResolveResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
force_sync=force_sync,

    )).parsed
