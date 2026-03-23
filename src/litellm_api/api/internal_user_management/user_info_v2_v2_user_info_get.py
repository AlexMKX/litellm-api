from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.user_info_v2_response import UserInfoV2Response
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    user_id: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_user_id: None | str | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/user/info",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | UserInfoV2Response | None:
    if response.status_code == 200:
        response_200 = UserInfoV2Response.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | UserInfoV2Response]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_id: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | UserInfoV2Response]:
    r""" User Info V2

     Lightweight endpoint to get user info. Returns only the user object — no keys, no teams objects.

    This is the v2 replacement for /user/info, designed to avoid the \"god endpoint\" problem
    where the old endpoint loaded all keys and teams into memory.

    Access control:
    - Proxy admins can query any user
    - Team admins can query users within their teams
    - Internal users can only query themselves (omit user_id or pass own)
    - Returns 404 for non-existent users or unauthorized access

    Example request:
    ```
    curl -X GET 'http://localhost:4000/v2/user/info?user_id=user123' \
    --header 'Authorization: Bearer sk-1234'
    ```

    Args:
        user_id (None | str | Unset): User ID in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserInfoV2Response]
     """


    kwargs = _get_kwargs(
        user_id=user_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    user_id: None | str | Unset = UNSET,

) -> HTTPValidationError | UserInfoV2Response | None:
    r""" User Info V2

     Lightweight endpoint to get user info. Returns only the user object — no keys, no teams objects.

    This is the v2 replacement for /user/info, designed to avoid the \"god endpoint\" problem
    where the old endpoint loaded all keys and teams into memory.

    Access control:
    - Proxy admins can query any user
    - Team admins can query users within their teams
    - Internal users can only query themselves (omit user_id or pass own)
    - Returns 404 for non-existent users or unauthorized access

    Example request:
    ```
    curl -X GET 'http://localhost:4000/v2/user/info?user_id=user123' \
    --header 'Authorization: Bearer sk-1234'
    ```

    Args:
        user_id (None | str | Unset): User ID in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserInfoV2Response
     """


    return sync_detailed(
        client=client,
user_id=user_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | UserInfoV2Response]:
    r""" User Info V2

     Lightweight endpoint to get user info. Returns only the user object — no keys, no teams objects.

    This is the v2 replacement for /user/info, designed to avoid the \"god endpoint\" problem
    where the old endpoint loaded all keys and teams into memory.

    Access control:
    - Proxy admins can query any user
    - Team admins can query users within their teams
    - Internal users can only query themselves (omit user_id or pass own)
    - Returns 404 for non-existent users or unauthorized access

    Example request:
    ```
    curl -X GET 'http://localhost:4000/v2/user/info?user_id=user123' \
    --header 'Authorization: Bearer sk-1234'
    ```

    Args:
        user_id (None | str | Unset): User ID in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserInfoV2Response]
     """


    kwargs = _get_kwargs(
        user_id=user_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: None | str | Unset = UNSET,

) -> HTTPValidationError | UserInfoV2Response | None:
    r""" User Info V2

     Lightweight endpoint to get user info. Returns only the user object — no keys, no teams objects.

    This is the v2 replacement for /user/info, designed to avoid the \"god endpoint\" problem
    where the old endpoint loaded all keys and teams into memory.

    Access control:
    - Proxy admins can query any user
    - Team admins can query users within their teams
    - Internal users can only query themselves (omit user_id or pass own)
    - Returns 404 for non-existent users or unauthorized access

    Example request:
    ```
    curl -X GET 'http://localhost:4000/v2/user/info?user_id=user123' \
    --header 'Authorization: Bearer sk-1234'
    ```

    Args:
        user_id (None | str | Unset): User ID in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserInfoV2Response
     """


    return (await asyncio_detailed(
        client=client,
user_id=user_id,

    )).parsed
