from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.block_key_request import BlockKeyRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: BlockKeyRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(litellm_changed_by, Unset):
        headers["litellm-changed-by"] = litellm_changed_by



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/key/unblock",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BlockKeyRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Unblock Key

     Unblock a Virtual key to allow it to make requests again.

    Parameters:
    - key: str - The key to unblock. Can be either the unhashed key (sk-...) or the hashed key value

    Example:
    ```bash
    curl --location 'http://0.0.0.0:4000/key/unblock'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"key\": \"sk-Fn8Ej39NxjAXrvpUGKghGw\"
    }'
    ```

    Note: This is an admin-only endpoint. Only proxy admins can unblock keys.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BlockKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: BlockKeyRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Unblock Key

     Unblock a Virtual key to allow it to make requests again.

    Parameters:
    - key: str - The key to unblock. Can be either the unhashed key (sk-...) or the hashed key value

    Example:
    ```bash
    curl --location 'http://0.0.0.0:4000/key/unblock'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"key\": \"sk-Fn8Ej39NxjAXrvpUGKghGw\"
    }'
    ```

    Note: This is an admin-only endpoint. Only proxy admins can unblock keys.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BlockKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BlockKeyRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Unblock Key

     Unblock a Virtual key to allow it to make requests again.

    Parameters:
    - key: str - The key to unblock. Can be either the unhashed key (sk-...) or the hashed key value

    Example:
    ```bash
    curl --location 'http://0.0.0.0:4000/key/unblock'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"key\": \"sk-Fn8Ej39NxjAXrvpUGKghGw\"
    }'
    ```

    Note: This is an admin-only endpoint. Only proxy admins can unblock keys.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BlockKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: BlockKeyRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Unblock Key

     Unblock a Virtual key to allow it to make requests again.

    Parameters:
    - key: str - The key to unblock. Can be either the unhashed key (sk-...) or the hashed key value

    Example:
    ```bash
    curl --location 'http://0.0.0.0:4000/key/unblock'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"key\": \"sk-Fn8Ej39NxjAXrvpUGKghGw\"
    }'
    ```

    Note: This is an admin-only endpoint. Only proxy admins can unblock keys.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (BlockKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    )).parsed
