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
    team_id: str,
    *,
    litellm_changed_by: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(litellm_changed_by, Unset):
        headers["litellm-changed-by"] = litellm_changed_by



    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/team/{team_id}".format(team_id=quote(str(team_id), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | None:
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError]:
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
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[HTTPValidationError]:
    r""" Patch Team

     Partially update a team using RFC 7386 JSON Merge Patch semantics.

    `team_id` is taken from the path. `metadata` is merged with the team's stored
    metadata rather than replacing it: an omitted key is preserved, `key: null`
    deletes it, and any other value overwrites (recursing into nested objects).
    Every other field behaves exactly like `POST /team/update` (omitted preserves,
    a value overwrites). Returns the full updated team.

    ```
    curl --location --request PATCH 'http://0.0.0.0:4000/team/8d916b1c-510d-4894-a334-1c16a93344f5'
    --header 'Authorization: Bearer sk-1234'     --header 'Content-Type: application/json'     --data-
    raw '{
        \"metadata\": {\"cost_center\": \"1234\", \"deprecated_key\": null}
    }'
    ```

    Args:
        team_id (str):
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
litellm_changed_by=litellm_changed_by,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    team_id: str,
    *,
    client: AuthenticatedClient,
    litellm_changed_by: None | str | Unset = UNSET,

) -> HTTPValidationError | None:
    r""" Patch Team

     Partially update a team using RFC 7386 JSON Merge Patch semantics.

    `team_id` is taken from the path. `metadata` is merged with the team's stored
    metadata rather than replacing it: an omitted key is preserved, `key: null`
    deletes it, and any other value overwrites (recursing into nested objects).
    Every other field behaves exactly like `POST /team/update` (omitted preserves,
    a value overwrites). Returns the full updated team.

    ```
    curl --location --request PATCH 'http://0.0.0.0:4000/team/8d916b1c-510d-4894-a334-1c16a93344f5'
    --header 'Authorization: Bearer sk-1234'     --header 'Content-Type: application/json'     --data-
    raw '{
        \"metadata\": {\"cost_center\": \"1234\", \"deprecated_key\": null}
    }'
    ```

    Args:
        team_id (str):
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
     """


    return sync_detailed(
        team_id=team_id,
client=client,
litellm_changed_by=litellm_changed_by,

    ).parsed

async def asyncio_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[HTTPValidationError]:
    r""" Patch Team

     Partially update a team using RFC 7386 JSON Merge Patch semantics.

    `team_id` is taken from the path. `metadata` is merged with the team's stored
    metadata rather than replacing it: an omitted key is preserved, `key: null`
    deletes it, and any other value overwrites (recursing into nested objects).
    Every other field behaves exactly like `POST /team/update` (omitted preserves,
    a value overwrites). Returns the full updated team.

    ```
    curl --location --request PATCH 'http://0.0.0.0:4000/team/8d916b1c-510d-4894-a334-1c16a93344f5'
    --header 'Authorization: Bearer sk-1234'     --header 'Content-Type: application/json'     --data-
    raw '{
        \"metadata\": {\"cost_center\": \"1234\", \"deprecated_key\": null}
    }'
    ```

    Args:
        team_id (str):
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
litellm_changed_by=litellm_changed_by,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    team_id: str,
    *,
    client: AuthenticatedClient,
    litellm_changed_by: None | str | Unset = UNSET,

) -> HTTPValidationError | None:
    r""" Patch Team

     Partially update a team using RFC 7386 JSON Merge Patch semantics.

    `team_id` is taken from the path. `metadata` is merged with the team's stored
    metadata rather than replacing it: an omitted key is preserved, `key: null`
    deletes it, and any other value overwrites (recursing into nested objects).
    Every other field behaves exactly like `POST /team/update` (omitted preserves,
    a value overwrites). Returns the full updated team.

    ```
    curl --location --request PATCH 'http://0.0.0.0:4000/team/8d916b1c-510d-4894-a334-1c16a93344f5'
    --header 'Authorization: Bearer sk-1234'     --header 'Content-Type: application/json'     --data-
    raw '{
        \"metadata\": {\"cost_center\": \"1234\", \"deprecated_key\": null}
    }'
    ```

    Args:
        team_id (str):
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
     """


    return (await asyncio_detailed(
        team_id=team_id,
client=client,
litellm_changed_by=litellm_changed_by,

    )).parsed
