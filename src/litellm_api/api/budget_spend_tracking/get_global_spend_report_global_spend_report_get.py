from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_global_spend_report_global_spend_report_get_group_by_type_0 import GetGlobalSpendReportGlobalSpendReportGetGroupByType0
from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llm_spend_logs import LiteLLMSpendLogs
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    group_by: GetGlobalSpendReportGlobalSpendReportGetGroupByType0 | None | Unset = GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM,
    api_key: None | str | Unset = UNSET,
    internal_user_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    customer_id: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

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

    json_group_by: None | str | Unset
    if isinstance(group_by, Unset):
        json_group_by = UNSET
    elif isinstance(group_by, GetGlobalSpendReportGlobalSpendReportGetGroupByType0):
        json_group_by = group_by.value
    else:
        json_group_by = group_by
    params["group_by"] = json_group_by

    json_api_key: None | str | Unset
    if isinstance(api_key, Unset):
        json_api_key = UNSET
    else:
        json_api_key = api_key
    params["api_key"] = json_api_key

    json_internal_user_id: None | str | Unset
    if isinstance(internal_user_id, Unset):
        json_internal_user_id = UNSET
    else:
        json_internal_user_id = internal_user_id
    params["internal_user_id"] = json_internal_user_id

    json_team_id: None | str | Unset
    if isinstance(team_id, Unset):
        json_team_id = UNSET
    else:
        json_team_id = team_id
    params["team_id"] = json_team_id

    json_customer_id: None | str | Unset
    if isinstance(customer_id, Unset):
        json_customer_id = UNSET
    else:
        json_customer_id = customer_id
    params["customer_id"] = json_customer_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/global/spend/report",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | list[LiteLLMSpendLogs] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = LiteLLMSpendLogs.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | list[LiteLLMSpendLogs]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    group_by: GetGlobalSpendReportGlobalSpendReportGetGroupByType0 | None | Unset = GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM,
    api_key: None | str | Unset = UNSET,
    internal_user_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    customer_id: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | list[LiteLLMSpendLogs]]:
    r""" Get Global Spend Report

     Get Daily Spend per Team, based on specific startTime and endTime. Per team, view usage by each key,
    model
    [
        {
            \"group-by-day\": \"2024-05-10\",
            \"teams\": [
                {
                    \"team_name\": \"team-1\"
                    \"spend\": 10,
                    \"keys\": [
                        \"key\": \"1213\",
                        \"usage\": {
                            \"model-1\": {
                                    \"cost\": 12.50,
                                    \"input_tokens\": 1000,
                                    \"output_tokens\": 5000,
                                    \"requests\": 100
                                },
                                \"audio-modelname1\": {
                                \"cost\": 25.50,
                                \"seconds\": 25,
                                \"requests\": 50
                        },
                        }
                    }
            ]
        ]
    }

    Args:
        start_date (None | str | Unset): Time from which to start viewing spend
        end_date (None | str | Unset): Time till which to view spend
        group_by (GetGlobalSpendReportGlobalSpendReportGetGroupByType0 | None | Unset): Group
            spend by internal team or customer or api_key Default:
            GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM.
        api_key (None | str | Unset): View spend for a specific api_key. Example api_key='sk-1234
        internal_user_id (None | str | Unset): View spend for a specific internal_user_id. Example
            internal_user_id='1234
        team_id (None | str | Unset): View spend for a specific team_id. Example team_id='1234
        customer_id (None | str | Unset): View spend for a specific customer_id. Example
            customer_id='1234. Can be used in conjunction with team_id as well.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LiteLLMSpendLogs]]
     """


    kwargs = _get_kwargs(
        start_date=start_date,
end_date=end_date,
group_by=group_by,
api_key=api_key,
internal_user_id=internal_user_id,
team_id=team_id,
customer_id=customer_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    group_by: GetGlobalSpendReportGlobalSpendReportGetGroupByType0 | None | Unset = GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM,
    api_key: None | str | Unset = UNSET,
    internal_user_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    customer_id: None | str | Unset = UNSET,

) -> HTTPValidationError | list[LiteLLMSpendLogs] | None:
    r""" Get Global Spend Report

     Get Daily Spend per Team, based on specific startTime and endTime. Per team, view usage by each key,
    model
    [
        {
            \"group-by-day\": \"2024-05-10\",
            \"teams\": [
                {
                    \"team_name\": \"team-1\"
                    \"spend\": 10,
                    \"keys\": [
                        \"key\": \"1213\",
                        \"usage\": {
                            \"model-1\": {
                                    \"cost\": 12.50,
                                    \"input_tokens\": 1000,
                                    \"output_tokens\": 5000,
                                    \"requests\": 100
                                },
                                \"audio-modelname1\": {
                                \"cost\": 25.50,
                                \"seconds\": 25,
                                \"requests\": 50
                        },
                        }
                    }
            ]
        ]
    }

    Args:
        start_date (None | str | Unset): Time from which to start viewing spend
        end_date (None | str | Unset): Time till which to view spend
        group_by (GetGlobalSpendReportGlobalSpendReportGetGroupByType0 | None | Unset): Group
            spend by internal team or customer or api_key Default:
            GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM.
        api_key (None | str | Unset): View spend for a specific api_key. Example api_key='sk-1234
        internal_user_id (None | str | Unset): View spend for a specific internal_user_id. Example
            internal_user_id='1234
        team_id (None | str | Unset): View spend for a specific team_id. Example team_id='1234
        customer_id (None | str | Unset): View spend for a specific customer_id. Example
            customer_id='1234. Can be used in conjunction with team_id as well.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LiteLLMSpendLogs]
     """


    return sync_detailed(
        client=client,
start_date=start_date,
end_date=end_date,
group_by=group_by,
api_key=api_key,
internal_user_id=internal_user_id,
team_id=team_id,
customer_id=customer_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    group_by: GetGlobalSpendReportGlobalSpendReportGetGroupByType0 | None | Unset = GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM,
    api_key: None | str | Unset = UNSET,
    internal_user_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    customer_id: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | list[LiteLLMSpendLogs]]:
    r""" Get Global Spend Report

     Get Daily Spend per Team, based on specific startTime and endTime. Per team, view usage by each key,
    model
    [
        {
            \"group-by-day\": \"2024-05-10\",
            \"teams\": [
                {
                    \"team_name\": \"team-1\"
                    \"spend\": 10,
                    \"keys\": [
                        \"key\": \"1213\",
                        \"usage\": {
                            \"model-1\": {
                                    \"cost\": 12.50,
                                    \"input_tokens\": 1000,
                                    \"output_tokens\": 5000,
                                    \"requests\": 100
                                },
                                \"audio-modelname1\": {
                                \"cost\": 25.50,
                                \"seconds\": 25,
                                \"requests\": 50
                        },
                        }
                    }
            ]
        ]
    }

    Args:
        start_date (None | str | Unset): Time from which to start viewing spend
        end_date (None | str | Unset): Time till which to view spend
        group_by (GetGlobalSpendReportGlobalSpendReportGetGroupByType0 | None | Unset): Group
            spend by internal team or customer or api_key Default:
            GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM.
        api_key (None | str | Unset): View spend for a specific api_key. Example api_key='sk-1234
        internal_user_id (None | str | Unset): View spend for a specific internal_user_id. Example
            internal_user_id='1234
        team_id (None | str | Unset): View spend for a specific team_id. Example team_id='1234
        customer_id (None | str | Unset): View spend for a specific customer_id. Example
            customer_id='1234. Can be used in conjunction with team_id as well.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LiteLLMSpendLogs]]
     """


    kwargs = _get_kwargs(
        start_date=start_date,
end_date=end_date,
group_by=group_by,
api_key=api_key,
internal_user_id=internal_user_id,
team_id=team_id,
customer_id=customer_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    group_by: GetGlobalSpendReportGlobalSpendReportGetGroupByType0 | None | Unset = GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM,
    api_key: None | str | Unset = UNSET,
    internal_user_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    customer_id: None | str | Unset = UNSET,

) -> HTTPValidationError | list[LiteLLMSpendLogs] | None:
    r""" Get Global Spend Report

     Get Daily Spend per Team, based on specific startTime and endTime. Per team, view usage by each key,
    model
    [
        {
            \"group-by-day\": \"2024-05-10\",
            \"teams\": [
                {
                    \"team_name\": \"team-1\"
                    \"spend\": 10,
                    \"keys\": [
                        \"key\": \"1213\",
                        \"usage\": {
                            \"model-1\": {
                                    \"cost\": 12.50,
                                    \"input_tokens\": 1000,
                                    \"output_tokens\": 5000,
                                    \"requests\": 100
                                },
                                \"audio-modelname1\": {
                                \"cost\": 25.50,
                                \"seconds\": 25,
                                \"requests\": 50
                        },
                        }
                    }
            ]
        ]
    }

    Args:
        start_date (None | str | Unset): Time from which to start viewing spend
        end_date (None | str | Unset): Time till which to view spend
        group_by (GetGlobalSpendReportGlobalSpendReportGetGroupByType0 | None | Unset): Group
            spend by internal team or customer or api_key Default:
            GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM.
        api_key (None | str | Unset): View spend for a specific api_key. Example api_key='sk-1234
        internal_user_id (None | str | Unset): View spend for a specific internal_user_id. Example
            internal_user_id='1234
        team_id (None | str | Unset): View spend for a specific team_id. Example team_id='1234
        customer_id (None | str | Unset): View spend for a specific customer_id. Example
            customer_id='1234. Can be used in conjunction with team_id as well.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LiteLLMSpendLogs]
     """


    return (await asyncio_detailed(
        client=client,
start_date=start_date,
end_date=end_date,
group_by=group_by,
api_key=api_key,
internal_user_id=internal_user_id,
team_id=team_id,
customer_id=customer_id,

    )).parsed
