from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_user_request import DeleteUserRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: DeleteUserRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(litellm_changed_by, Unset):
        headers["litellm-changed-by"] = litellm_changed_by



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/user/delete",
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
    body: DeleteUserRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Delete User

     delete user and associated user keys

    ```
    curl --location 'http://0.0.0.0:4000/user/delete'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data-raw '{
        \"user_ids\": [\"45e3e396-ee08-4a61-a88e-16b3ce7e0849\"]
    }'
    ```

    Parameters:
    - user_ids: List[str] - The list of user id's to be deleted.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (DeleteUserRequest):

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
    body: DeleteUserRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Delete User

     delete user and associated user keys

    ```
    curl --location 'http://0.0.0.0:4000/user/delete'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data-raw '{
        \"user_ids\": [\"45e3e396-ee08-4a61-a88e-16b3ce7e0849\"]
    }'
    ```

    Parameters:
    - user_ids: List[str] - The list of user id's to be deleted.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (DeleteUserRequest):

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
    body: DeleteUserRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Delete User

     delete user and associated user keys

    ```
    curl --location 'http://0.0.0.0:4000/user/delete'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data-raw '{
        \"user_ids\": [\"45e3e396-ee08-4a61-a88e-16b3ce7e0849\"]
    }'
    ```

    Parameters:
    - user_ids: List[str] - The list of user id's to be deleted.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (DeleteUserRequest):

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
    body: DeleteUserRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Delete User

     delete user and associated user keys

    ```
    curl --location 'http://0.0.0.0:4000/user/delete'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data-raw '{
        \"user_ids\": [\"45e3e396-ee08-4a61-a88e-16b3ce7e0849\"]
    }'
    ```

    Parameters:
    - user_ids: List[str] - The list of user id's to be deleted.

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (DeleteUserRequest):

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
