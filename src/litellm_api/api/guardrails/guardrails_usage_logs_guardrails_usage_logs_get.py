from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.usage_logs_response import UsageLogsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    guardrail_id: None | str | Unset = UNSET,
    policy_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    action: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_guardrail_id: None | str | Unset
    if isinstance(guardrail_id, Unset):
        json_guardrail_id = UNSET
    else:
        json_guardrail_id = guardrail_id
    params["guardrail_id"] = json_guardrail_id

    json_policy_id: None | str | Unset
    if isinstance(policy_id, Unset):
        json_policy_id = UNSET
    else:
        json_policy_id = policy_id
    params["policy_id"] = json_policy_id

    params["page"] = page

    params["page_size"] = page_size

    json_action: None | str | Unset
    if isinstance(action, Unset):
        json_action = UNSET
    else:
        json_action = action
    params["action"] = json_action

    json_start_date: None | str | Unset
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: None | str | Unset
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/guardrails/usage/logs",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | UsageLogsResponse | None:
    if response.status_code == 200:
        response_200 = UsageLogsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | UsageLogsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    guardrail_id: None | str | Unset = UNSET,
    policy_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    action: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | UsageLogsResponse]:
    """ Guardrails Usage Logs

     Return paginated run logs for a guardrail (or policy) from SpendLogs via index.

    Args:
        guardrail_id (None | str | Unset):
        policy_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        action (None | str | Unset):
        start_date (None | str | Unset):
        end_date (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UsageLogsResponse]
     """


    kwargs = _get_kwargs(
        guardrail_id=guardrail_id,
policy_id=policy_id,
page=page,
page_size=page_size,
action=action,
start_date=start_date,
end_date=end_date,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    guardrail_id: None | str | Unset = UNSET,
    policy_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    action: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,

) -> HTTPValidationError | UsageLogsResponse | None:
    """ Guardrails Usage Logs

     Return paginated run logs for a guardrail (or policy) from SpendLogs via index.

    Args:
        guardrail_id (None | str | Unset):
        policy_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        action (None | str | Unset):
        start_date (None | str | Unset):
        end_date (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UsageLogsResponse
     """


    return sync_detailed(
        client=client,
guardrail_id=guardrail_id,
policy_id=policy_id,
page=page,
page_size=page_size,
action=action,
start_date=start_date,
end_date=end_date,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    guardrail_id: None | str | Unset = UNSET,
    policy_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    action: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | UsageLogsResponse]:
    """ Guardrails Usage Logs

     Return paginated run logs for a guardrail (or policy) from SpendLogs via index.

    Args:
        guardrail_id (None | str | Unset):
        policy_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        action (None | str | Unset):
        start_date (None | str | Unset):
        end_date (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UsageLogsResponse]
     """


    kwargs = _get_kwargs(
        guardrail_id=guardrail_id,
policy_id=policy_id,
page=page,
page_size=page_size,
action=action,
start_date=start_date,
end_date=end_date,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    guardrail_id: None | str | Unset = UNSET,
    policy_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    action: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,

) -> HTTPValidationError | UsageLogsResponse | None:
    """ Guardrails Usage Logs

     Return paginated run logs for a guardrail (or policy) from SpendLogs via index.

    Args:
        guardrail_id (None | str | Unset):
        policy_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        action (None | str | Unset):
        start_date (None | str | Unset):
        end_date (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UsageLogsResponse
     """


    return (await asyncio_detailed(
        client=client,
guardrail_id=guardrail_id,
policy_id=policy_id,
page=page,
page_size=page_size,
action=action,
start_date=start_date,
end_date=end_date,

    )).parsed
