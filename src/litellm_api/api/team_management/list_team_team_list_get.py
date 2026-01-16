from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    user_id: None | str | Unset = UNSET,
    organization_id: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_user_id: None | str | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    json_organization_id: None | str | Unset
    if isinstance(organization_id, Unset):
        json_organization_id = UNSET
    else:
        json_organization_id = organization_id
    params["organization_id"] = json_organization_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/team/list",
        "params": params,
    }


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
    user_id: None | str | Unset = UNSET,
    organization_id: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ List Team

     ```
    curl --location --request GET 'http://0.0.0.0:4000/team/list'         --header 'Authorization:
    Bearer sk-1234'
    ```

    Parameters:
    - user_id: str - Optional. If passed will only return teams that the user_id is a member of.
    - organization_id: str - Optional. If passed will only return teams that belong to the
    organization_id. Pass 'default_organization' to get all teams without organization_id.

    Args:
        user_id (None | str | Unset): Only return teams which this 'user_id' belongs to
        organization_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    user_id: None | str | Unset = UNSET,
    organization_id: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ List Team

     ```
    curl --location --request GET 'http://0.0.0.0:4000/team/list'         --header 'Authorization:
    Bearer sk-1234'
    ```

    Parameters:
    - user_id: str - Optional. If passed will only return teams that the user_id is a member of.
    - organization_id: str - Optional. If passed will only return teams that belong to the
    organization_id. Pass 'default_organization' to get all teams without organization_id.

    Args:
        user_id (None | str | Unset): Only return teams which this 'user_id' belongs to
        organization_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
user_id=user_id,
organization_id=organization_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: None | str | Unset = UNSET,
    organization_id: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ List Team

     ```
    curl --location --request GET 'http://0.0.0.0:4000/team/list'         --header 'Authorization:
    Bearer sk-1234'
    ```

    Parameters:
    - user_id: str - Optional. If passed will only return teams that the user_id is a member of.
    - organization_id: str - Optional. If passed will only return teams that belong to the
    organization_id. Pass 'default_organization' to get all teams without organization_id.

    Args:
        user_id (None | str | Unset): Only return teams which this 'user_id' belongs to
        organization_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: None | str | Unset = UNSET,
    organization_id: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ List Team

     ```
    curl --location --request GET 'http://0.0.0.0:4000/team/list'         --header 'Authorization:
    Bearer sk-1234'
    ```

    Parameters:
    - user_id: str - Optional. If passed will only return teams that the user_id is a member of.
    - organization_id: str - Optional. If passed will only return teams that belong to the
    organization_id. Pass 'default_organization' to get all teams without organization_id.

    Args:
        user_id (None | str | Unset): Only return teams which this 'user_id' belongs to
        organization_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
user_id=user_id,
organization_id=organization_id,

    )).parsed
