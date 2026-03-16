from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.tool_policy_update_request import ToolPolicyUpdateRequest
from ...models.tool_policy_update_response import ToolPolicyUpdateResponse
from typing import cast



def _get_kwargs(
    *,
    body: ToolPolicyUpdateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tool/policy",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | ToolPolicyUpdateResponse | None:
    if response.status_code == 200:
        response_200 = ToolPolicyUpdateResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | ToolPolicyUpdateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ToolPolicyUpdateRequest,

) -> Response[HTTPValidationError | ToolPolicyUpdateResponse]:
    r""" Update Tool Policy

     Set the input_policy and/or output_policy for a tool (global), or block for a specific team/key
    (override).

    Parameters:
    - tool_name: str - The tool to update
    - input_policy: optional - \"trusted\" | \"untrusted\" | \"blocked\"
    - output_policy: optional - \"trusted\" | \"untrusted\"
    - team_id: optional - if set, create/update override for this team only
    - key_hash: optional - if set, create/update override for this key only

    Args:
        body (ToolPolicyUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ToolPolicyUpdateResponse]
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
    body: ToolPolicyUpdateRequest,

) -> HTTPValidationError | ToolPolicyUpdateResponse | None:
    r""" Update Tool Policy

     Set the input_policy and/or output_policy for a tool (global), or block for a specific team/key
    (override).

    Parameters:
    - tool_name: str - The tool to update
    - input_policy: optional - \"trusted\" | \"untrusted\" | \"blocked\"
    - output_policy: optional - \"trusted\" | \"untrusted\"
    - team_id: optional - if set, create/update override for this team only
    - key_hash: optional - if set, create/update override for this key only

    Args:
        body (ToolPolicyUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ToolPolicyUpdateResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ToolPolicyUpdateRequest,

) -> Response[HTTPValidationError | ToolPolicyUpdateResponse]:
    r""" Update Tool Policy

     Set the input_policy and/or output_policy for a tool (global), or block for a specific team/key
    (override).

    Parameters:
    - tool_name: str - The tool to update
    - input_policy: optional - \"trusted\" | \"untrusted\" | \"blocked\"
    - output_policy: optional - \"trusted\" | \"untrusted\"
    - team_id: optional - if set, create/update override for this team only
    - key_hash: optional - if set, create/update override for this key only

    Args:
        body (ToolPolicyUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ToolPolicyUpdateResponse]
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
    body: ToolPolicyUpdateRequest,

) -> HTTPValidationError | ToolPolicyUpdateResponse | None:
    r""" Update Tool Policy

     Set the input_policy and/or output_policy for a tool (global), or block for a specific team/key
    (override).

    Parameters:
    - tool_name: str - The tool to update
    - input_policy: optional - \"trusted\" | \"untrusted\" | \"blocked\"
    - output_policy: optional - \"trusted\" | \"untrusted\"
    - team_id: optional - if set, create/update override for this team only
    - key_hash: optional - if set, create/update override for this key only

    Args:
        body (ToolPolicyUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ToolPolicyUpdateResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
