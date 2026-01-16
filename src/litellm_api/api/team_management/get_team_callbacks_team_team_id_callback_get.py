from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    team_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/team/{team_id}/callback".format(team_id=quote(str(team_id), safe=""),),
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
    team_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | HTTPValidationError]:
    r""" Get Team Callbacks

     Get the success/failure callbacks and variables for a team

    Parameters:
    - team_id (str, required): The unique identifier for the team

    Example curl:
    ```
    curl -X GET 'http://localhost:4000/team/dbe2f686-a686-4896-864a-4c3924458709/callback'         -H
    'Authorization: Bearer sk-1234'
    ```

    This will return the callback settings for the team with id dbe2f686-a686-4896-864a-4c3924458709

    Returns {
            \"status\": \"success\",
            \"data\": {
                \"team_id\": team_id,
                \"success_callbacks\": team_callback_settings_obj.success_callback,
                \"failure_callbacks\": team_callback_settings_obj.failure_callback,
                \"callback_vars\": team_callback_settings_obj.callback_vars,
            },
        }

    Args:
        team_id (str):

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
    team_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | HTTPValidationError | None:
    r""" Get Team Callbacks

     Get the success/failure callbacks and variables for a team

    Parameters:
    - team_id (str, required): The unique identifier for the team

    Example curl:
    ```
    curl -X GET 'http://localhost:4000/team/dbe2f686-a686-4896-864a-4c3924458709/callback'         -H
    'Authorization: Bearer sk-1234'
    ```

    This will return the callback settings for the team with id dbe2f686-a686-4896-864a-4c3924458709

    Returns {
            \"status\": \"success\",
            \"data\": {
                \"team_id\": team_id,
                \"success_callbacks\": team_callback_settings_obj.success_callback,
                \"failure_callbacks\": team_callback_settings_obj.failure_callback,
                \"callback_vars\": team_callback_settings_obj.callback_vars,
            },
        }

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        team_id=team_id,
client=client,

    ).parsed

async def asyncio_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | HTTPValidationError]:
    r""" Get Team Callbacks

     Get the success/failure callbacks and variables for a team

    Parameters:
    - team_id (str, required): The unique identifier for the team

    Example curl:
    ```
    curl -X GET 'http://localhost:4000/team/dbe2f686-a686-4896-864a-4c3924458709/callback'         -H
    'Authorization: Bearer sk-1234'
    ```

    This will return the callback settings for the team with id dbe2f686-a686-4896-864a-4c3924458709

    Returns {
            \"status\": \"success\",
            \"data\": {
                \"team_id\": team_id,
                \"success_callbacks\": team_callback_settings_obj.success_callback,
                \"failure_callbacks\": team_callback_settings_obj.failure_callback,
                \"callback_vars\": team_callback_settings_obj.callback_vars,
            },
        }

    Args:
        team_id (str):

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
    team_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | HTTPValidationError | None:
    r""" Get Team Callbacks

     Get the success/failure callbacks and variables for a team

    Parameters:
    - team_id (str, required): The unique identifier for the team

    Example curl:
    ```
    curl -X GET 'http://localhost:4000/team/dbe2f686-a686-4896-864a-4c3924458709/callback'         -H
    'Authorization: Bearer sk-1234'
    ```

    This will return the callback settings for the team with id dbe2f686-a686-4896-864a-4c3924458709

    Returns {
            \"status\": \"success\",
            \"data\": {
                \"team_id\": team_id,
                \"success_callbacks\": team_callback_settings_obj.success_callback,
                \"failure_callbacks\": team_callback_settings_obj.failure_callback,
                \"callback_vars\": team_callback_settings_obj.callback_vars,
            },
        }

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        team_id=team_id,
client=client,

    )).parsed
