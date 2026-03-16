from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.list_tools_v1_tool_list_get_input_policy_type_0 import ListToolsV1ToolListGetInputPolicyType0
from ...models.tool_list_response import ToolListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    input_policy: ListToolsV1ToolListGetInputPolicyType0 | None | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_input_policy: None | str | Unset
    if isinstance(input_policy, Unset):
        json_input_policy = UNSET
    elif isinstance(input_policy, ListToolsV1ToolListGetInputPolicyType0):
        json_input_policy = input_policy.value
    else:
        json_input_policy = input_policy
    params["input_policy"] = json_input_policy


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tool/list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | ToolListResponse | None:
    if response.status_code == 200:
        response_200 = ToolListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | ToolListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    input_policy: ListToolsV1ToolListGetInputPolicyType0 | None | Unset = UNSET,

) -> Response[HTTPValidationError | ToolListResponse]:
    r""" List Tools

     List all auto-discovered tools and their policies.

    Parameters:
    - input_policy: Optional filter — one of \"trusted\", \"untrusted\", \"blocked\"

    Args:
        input_policy (ListToolsV1ToolListGetInputPolicyType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ToolListResponse]
     """


    kwargs = _get_kwargs(
        input_policy=input_policy,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    input_policy: ListToolsV1ToolListGetInputPolicyType0 | None | Unset = UNSET,

) -> HTTPValidationError | ToolListResponse | None:
    r""" List Tools

     List all auto-discovered tools and their policies.

    Parameters:
    - input_policy: Optional filter — one of \"trusted\", \"untrusted\", \"blocked\"

    Args:
        input_policy (ListToolsV1ToolListGetInputPolicyType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ToolListResponse
     """


    return sync_detailed(
        client=client,
input_policy=input_policy,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    input_policy: ListToolsV1ToolListGetInputPolicyType0 | None | Unset = UNSET,

) -> Response[HTTPValidationError | ToolListResponse]:
    r""" List Tools

     List all auto-discovered tools and their policies.

    Parameters:
    - input_policy: Optional filter — one of \"trusted\", \"untrusted\", \"blocked\"

    Args:
        input_policy (ListToolsV1ToolListGetInputPolicyType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ToolListResponse]
     """


    kwargs = _get_kwargs(
        input_policy=input_policy,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    input_policy: ListToolsV1ToolListGetInputPolicyType0 | None | Unset = UNSET,

) -> HTTPValidationError | ToolListResponse | None:
    r""" List Tools

     List all auto-discovered tools and their policies.

    Parameters:
    - input_policy: Optional filter — one of \"trusted\", \"untrusted\", \"blocked\"

    Args:
        input_policy (ListToolsV1ToolListGetInputPolicyType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ToolListResponse
     """


    return (await asyncio_detailed(
        client=client,
input_policy=input_policy,

    )).parsed
