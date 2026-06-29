from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.block_model_request import BlockModelRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llm_proxy_model_table import LiteLLMProxyModelTable
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: BlockModelRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(litellm_changed_by, Unset):
        headers["litellm-changed-by"] = litellm_changed_by



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/model/block",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | LiteLLMProxyModelTable | None | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> LiteLLMProxyModelTable | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = LiteLLMProxyModelTable.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiteLLMProxyModelTable | None, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | LiteLLMProxyModelTable | None]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BlockModelRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | LiteLLMProxyModelTable | None]:
    """ Block Model

     Block a DB-stored model deployment from serving requests.

    Parameters:
    - model_id: str - The model deployment id to block.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BlockModelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiteLLMProxyModelTable | None]
     """


    kwargs = _get_kwargs(
        body=body,
litellm_changed_by=litellm_changed_by,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: BlockModelRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> HTTPValidationError | LiteLLMProxyModelTable | None | None:
    """ Block Model

     Block a DB-stored model deployment from serving requests.

    Parameters:
    - model_id: str - The model deployment id to block.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BlockModelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiteLLMProxyModelTable | None
     """


    return sync_detailed(
        client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BlockModelRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | LiteLLMProxyModelTable | None]:
    """ Block Model

     Block a DB-stored model deployment from serving requests.

    Parameters:
    - model_id: str - The model deployment id to block.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BlockModelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiteLLMProxyModelTable | None]
     """


    kwargs = _get_kwargs(
        body=body,
litellm_changed_by=litellm_changed_by,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BlockModelRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> HTTPValidationError | LiteLLMProxyModelTable | None | None:
    """ Block Model

     Block a DB-stored model deployment from serving requests.

    Parameters:
    - model_id: str - The model deployment id to block.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BlockModelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiteLLMProxyModelTable | None
     """


    return (await asyncio_detailed(
        client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    )).parsed
