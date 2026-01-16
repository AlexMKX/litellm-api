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
    team_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["team_id"] = team_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/team/info",
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
    team_id: str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Team Info

     get info on team + related keys

    Parameters:
    - team_id: str - Required. The unique identifier of the team to get info on.

    ```
    curl --location 'http://localhost:4000/team/info?team_id=your_team_id_here'     --header
    'Authorization: Bearer your_api_key_here'
    ```

    Args:
        team_id (str | Unset): Team ID in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        team_id=team_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    team_id: str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Team Info

     get info on team + related keys

    Parameters:
    - team_id: str - Required. The unique identifier of the team to get info on.

    ```
    curl --location 'http://localhost:4000/team/info?team_id=your_team_id_here'     --header
    'Authorization: Bearer your_api_key_here'
    ```

    Args:
        team_id (str | Unset): Team ID in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
team_id=team_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    team_id: str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    """ Team Info

     get info on team + related keys

    Parameters:
    - team_id: str - Required. The unique identifier of the team to get info on.

    ```
    curl --location 'http://localhost:4000/team/info?team_id=your_team_id_here'     --header
    'Authorization: Bearer your_api_key_here'
    ```

    Args:
        team_id (str | Unset): Team ID in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        team_id=team_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    team_id: str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    """ Team Info

     get info on team + related keys

    Parameters:
    - team_id: str - Required. The unique identifier of the team to get info on.

    ```
    curl --location 'http://localhost:4000/team/info?team_id=your_team_id_here'     --header
    'Authorization: Bearer your_api_key_here'
    ```

    Args:
        team_id (str | Unset): Team ID in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
team_id=team_id,

    )).parsed
