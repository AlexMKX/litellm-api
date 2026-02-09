from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.reset_key_spend_fn_key_key_reset_spend_post_response_reset_key_spend_fn_key_key_reset_spend_post import ResetKeySpendFnKeyKeyResetSpendPostResponseResetKeySpendFnKeyKeyResetSpendPost
from ...models.reset_spend_request import ResetSpendRequest
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    key: str,
    *,
    body: ResetSpendRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(litellm_changed_by, Unset):
        headers["litellm-changed-by"] = litellm_changed_by



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/key/{key}/reset_spend".format(key=quote(str(key), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | ResetKeySpendFnKeyKeyResetSpendPostResponseResetKeySpendFnKeyKeyResetSpendPost | None:
    if response.status_code == 200:
        response_200 = ResetKeySpendFnKeyKeyResetSpendPostResponseResetKeySpendFnKeyKeyResetSpendPost.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | ResetKeySpendFnKeyKeyResetSpendPostResponseResetKeySpendFnKeyKeyResetSpendPost]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key: str,
    *,
    client: AuthenticatedClient,
    body: ResetSpendRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | ResetKeySpendFnKeyKeyResetSpendPostResponseResetKeySpendFnKeyKeyResetSpendPost]:
    """ Reset Key Spend Fn

    Args:
        key (str):
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (ResetSpendRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ResetKeySpendFnKeyKeyResetSpendPostResponseResetKeySpendFnKeyKeyResetSpendPost]
     """


    kwargs = _get_kwargs(
        key=key,
body=body,
litellm_changed_by=litellm_changed_by,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    key: str,
    *,
    client: AuthenticatedClient,
    body: ResetSpendRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> HTTPValidationError | ResetKeySpendFnKeyKeyResetSpendPostResponseResetKeySpendFnKeyKeyResetSpendPost | None:
    """ Reset Key Spend Fn

    Args:
        key (str):
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (ResetSpendRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ResetKeySpendFnKeyKeyResetSpendPostResponseResetKeySpendFnKeyKeyResetSpendPost
     """


    return sync_detailed(
        key=key,
client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    ).parsed

async def asyncio_detailed(
    key: str,
    *,
    client: AuthenticatedClient,
    body: ResetSpendRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | ResetKeySpendFnKeyKeyResetSpendPostResponseResetKeySpendFnKeyKeyResetSpendPost]:
    """ Reset Key Spend Fn

    Args:
        key (str):
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (ResetSpendRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ResetKeySpendFnKeyKeyResetSpendPostResponseResetKeySpendFnKeyKeyResetSpendPost]
     """


    kwargs = _get_kwargs(
        key=key,
body=body,
litellm_changed_by=litellm_changed_by,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    key: str,
    *,
    client: AuthenticatedClient,
    body: ResetSpendRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> HTTPValidationError | ResetKeySpendFnKeyKeyResetSpendPostResponseResetKeySpendFnKeyKeyResetSpendPost | None:
    """ Reset Key Spend Fn

    Args:
        key (str):
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (ResetSpendRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ResetKeySpendFnKeyKeyResetSpendPostResponseResetKeySpendFnKeyKeyResetSpendPost
     """


    return (await asyncio_detailed(
        key=key,
client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    )).parsed
