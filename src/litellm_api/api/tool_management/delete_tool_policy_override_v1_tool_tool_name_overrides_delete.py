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
    tool_name: str,
    *,
    team_id: None | str | Unset = UNSET,
    key_hash: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_team_id: None | str | Unset
    if isinstance(team_id, Unset):
        json_team_id = UNSET
    else:
        json_team_id = team_id
    params["team_id"] = json_team_id

    json_key_hash: None | str | Unset
    if isinstance(key_hash, Unset):
        json_key_hash = UNSET
    else:
        json_key_hash = key_hash
    params["key_hash"] = json_key_hash


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/tool/{tool_name}/overrides".format(tool_name=quote(str(tool_name), safe=""),),
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
    tool_name: str,
    *,
    client: AuthenticatedClient,
    team_id: None | str | Unset = UNSET,
    key_hash: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Delete Tool Policy Override

     Remove a policy override for a tool. Specify the override by team_id or key_hash
    (exactly one required).

    Args:
        tool_name (str):
        team_id (None | str | Unset): Team ID of the override to remove
        key_hash (None | str | Unset): Key hash of the override to remove

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        tool_name=tool_name,
team_id=team_id,
key_hash=key_hash,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    tool_name: str,
    *,
    client: AuthenticatedClient,
    team_id: None | str | Unset = UNSET,
    key_hash: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Delete Tool Policy Override

     Remove a policy override for a tool. Specify the override by team_id or key_hash
    (exactly one required).

    Args:
        tool_name (str):
        team_id (None | str | Unset): Team ID of the override to remove
        key_hash (None | str | Unset): Key hash of the override to remove

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        tool_name=tool_name,
client=client,
team_id=team_id,
key_hash=key_hash,

    ).parsed

async def asyncio_detailed(
    tool_name: str,
    *,
    client: AuthenticatedClient,
    team_id: None | str | Unset = UNSET,
    key_hash: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Delete Tool Policy Override

     Remove a policy override for a tool. Specify the override by team_id or key_hash
    (exactly one required).

    Args:
        tool_name (str):
        team_id (None | str | Unset): Team ID of the override to remove
        key_hash (None | str | Unset): Key hash of the override to remove

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        tool_name=tool_name,
team_id=team_id,
key_hash=key_hash,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    tool_name: str,
    *,
    client: AuthenticatedClient,
    team_id: None | str | Unset = UNSET,
    key_hash: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Delete Tool Policy Override

     Remove a policy override for a tool. Specify the override by team_id or key_hash
    (exactly one required).

    Args:
        tool_name (str):
        team_id (None | str | Unset): Team ID of the override to remove
        key_hash (None | str | Unset): Key hash of the override to remove

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        tool_name=tool_name,
client=client,
team_id=team_id,
key_hash=key_hash,

    )).parsed
