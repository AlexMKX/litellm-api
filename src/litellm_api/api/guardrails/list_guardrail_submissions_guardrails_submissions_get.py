from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.list_guardrail_submissions_response import ListGuardrailSubmissionsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    status: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_team_id: None | str | Unset
    if isinstance(team_id, Unset):
        json_team_id = UNSET
    else:
        json_team_id = team_id
    params["team_id"] = json_team_id

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/guardrails/submissions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | ListGuardrailSubmissionsResponse | None:
    if response.status_code == 200:
        response_200 = ListGuardrailSubmissionsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | ListGuardrailSubmissionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | ListGuardrailSubmissionsResponse]:
    """ List Guardrail Submissions

     List team guardrail submissions. Returns only guardrails with a team_id.

    Admins see all submissions. Non-admin users see submissions for teams they are
    a member of.

    Status values: pending_review (team-registered, awaiting approval), active (approved), rejected.

    Optional filters:
    - status: pending_review | active | rejected
    - team_id: filter by specific team (non-admins must be a member of that team)
    - search: name/description

    Args:
        status (None | str | Unset):
        team_id (None | str | Unset):
        search (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListGuardrailSubmissionsResponse]
     """


    kwargs = _get_kwargs(
        status=status,
team_id=team_id,
search=search,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    status: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,

) -> HTTPValidationError | ListGuardrailSubmissionsResponse | None:
    """ List Guardrail Submissions

     List team guardrail submissions. Returns only guardrails with a team_id.

    Admins see all submissions. Non-admin users see submissions for teams they are
    a member of.

    Status values: pending_review (team-registered, awaiting approval), active (approved), rejected.

    Optional filters:
    - status: pending_review | active | rejected
    - team_id: filter by specific team (non-admins must be a member of that team)
    - search: name/description

    Args:
        status (None | str | Unset):
        team_id (None | str | Unset):
        search (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListGuardrailSubmissionsResponse
     """


    return sync_detailed(
        client=client,
status=status,
team_id=team_id,
search=search,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    status: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | ListGuardrailSubmissionsResponse]:
    """ List Guardrail Submissions

     List team guardrail submissions. Returns only guardrails with a team_id.

    Admins see all submissions. Non-admin users see submissions for teams they are
    a member of.

    Status values: pending_review (team-registered, awaiting approval), active (approved), rejected.

    Optional filters:
    - status: pending_review | active | rejected
    - team_id: filter by specific team (non-admins must be a member of that team)
    - search: name/description

    Args:
        status (None | str | Unset):
        team_id (None | str | Unset):
        search (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListGuardrailSubmissionsResponse]
     """


    kwargs = _get_kwargs(
        status=status,
team_id=team_id,
search=search,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    status: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,

) -> HTTPValidationError | ListGuardrailSubmissionsResponse | None:
    """ List Guardrail Submissions

     List team guardrail submissions. Returns only guardrails with a team_id.

    Admins see all submissions. Non-admin users see submissions for teams they are
    a member of.

    Status values: pending_review (team-registered, awaiting approval), active (approved), rejected.

    Optional filters:
    - status: pending_review | active | rejected
    - team_id: filter by specific team (non-admins must be a member of that team)
    - search: name/description

    Args:
        status (None | str | Unset):
        team_id (None | str | Unset):
        search (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListGuardrailSubmissionsResponse
     """


    return (await asyncio_detailed(
        client=client,
status=status,
team_id=team_id,
search=search,

    )).parsed
