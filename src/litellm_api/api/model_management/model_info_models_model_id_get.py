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
    model_id: str,
    *,
    team_id: None | str | Unset = UNSET,
    healthy_only: bool | None | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_team_id: None | str | Unset
    if isinstance(team_id, Unset):
        json_team_id = UNSET
    else:
        json_team_id = team_id
    params["team_id"] = json_team_id

    json_healthy_only: bool | None | Unset
    if isinstance(healthy_only, Unset):
        json_healthy_only = UNSET
    else:
        json_healthy_only = healthy_only
    params["healthy_only"] = json_healthy_only


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/models/{model_id}".format(model_id=quote(str(model_id), safe=""),),
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
    model_id: str,
    *,
    client: AuthenticatedClient,
    team_id: None | str | Unset = UNSET,
    healthy_only: bool | None | Unset = False,

) -> Response[Any | HTTPValidationError]:
    """ Model Info

     Retrieve information about a specific model accessible to your API key.

    Returns model details only if the model is available to your API key/team.
    Returns 404 if the model doesn't exist or is not accessible.

    Follows OpenAI API specification for individual model retrieval.
    https://platform.openai.com/docs/api-reference/models/retrieve

    Query parameters mirror `/v1/models` so the same caller context (team
    scoping, health filtering, paused deployments) drives both endpoints; the
    listing's public id must resolve to the same internal deployment here.

    Args:
        model_id (str):
        team_id (None | str | Unset):
        healthy_only (bool | None | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        model_id=model_id,
team_id=team_id,
healthy_only=healthy_only,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    model_id: str,
    *,
    client: AuthenticatedClient,
    team_id: None | str | Unset = UNSET,
    healthy_only: bool | None | Unset = False,

) -> Any | HTTPValidationError | None:
    """ Model Info

     Retrieve information about a specific model accessible to your API key.

    Returns model details only if the model is available to your API key/team.
    Returns 404 if the model doesn't exist or is not accessible.

    Follows OpenAI API specification for individual model retrieval.
    https://platform.openai.com/docs/api-reference/models/retrieve

    Query parameters mirror `/v1/models` so the same caller context (team
    scoping, health filtering, paused deployments) drives both endpoints; the
    listing's public id must resolve to the same internal deployment here.

    Args:
        model_id (str):
        team_id (None | str | Unset):
        healthy_only (bool | None | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        model_id=model_id,
client=client,
team_id=team_id,
healthy_only=healthy_only,

    ).parsed

async def asyncio_detailed(
    model_id: str,
    *,
    client: AuthenticatedClient,
    team_id: None | str | Unset = UNSET,
    healthy_only: bool | None | Unset = False,

) -> Response[Any | HTTPValidationError]:
    """ Model Info

     Retrieve information about a specific model accessible to your API key.

    Returns model details only if the model is available to your API key/team.
    Returns 404 if the model doesn't exist or is not accessible.

    Follows OpenAI API specification for individual model retrieval.
    https://platform.openai.com/docs/api-reference/models/retrieve

    Query parameters mirror `/v1/models` so the same caller context (team
    scoping, health filtering, paused deployments) drives both endpoints; the
    listing's public id must resolve to the same internal deployment here.

    Args:
        model_id (str):
        team_id (None | str | Unset):
        healthy_only (bool | None | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        model_id=model_id,
team_id=team_id,
healthy_only=healthy_only,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    model_id: str,
    *,
    client: AuthenticatedClient,
    team_id: None | str | Unset = UNSET,
    healthy_only: bool | None | Unset = False,

) -> Any | HTTPValidationError | None:
    """ Model Info

     Retrieve information about a specific model accessible to your API key.

    Returns model details only if the model is available to your API key/team.
    Returns 404 if the model doesn't exist or is not accessible.

    Follows OpenAI API specification for individual model retrieval.
    https://platform.openai.com/docs/api-reference/models/retrieve

    Query parameters mirror `/v1/models` so the same caller context (team
    scoping, health filtering, paused deployments) drives both endpoints; the
    listing's public id must resolve to the same internal deployment here.

    Args:
        model_id (str):
        team_id (None | str | Unset):
        healthy_only (bool | None | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        model_id=model_id,
client=client,
team_id=team_id,
healthy_only=healthy_only,

    )).parsed
