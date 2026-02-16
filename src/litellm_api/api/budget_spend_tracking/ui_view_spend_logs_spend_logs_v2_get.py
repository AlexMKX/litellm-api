from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.ui_view_spend_logs_spend_logs_v2_get_response_200_ui_view_spend_logs_spend_logs_v2_get import UiViewSpendLogsSpendLogsV2GetResponse200UiViewSpendLogsSpendLogsV2Get
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    api_key: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    request_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    min_spend: float | None | Unset = UNSET,
    max_spend: float | None | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    status_filter: None | str | Unset = UNSET,
    model: None | str | Unset = UNSET,
    model_id: None | str | Unset = UNSET,
    key_alias: None | str | Unset = UNSET,
    end_user: None | str | Unset = UNSET,
    error_code: None | str | Unset = UNSET,
    error_message: None | str | Unset = UNSET,
    sort_by: str | Unset = 'startTime',
    sort_order: None | str | Unset = 'desc',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_api_key: None | str | Unset
    if isinstance(api_key, Unset):
        json_api_key = UNSET
    else:
        json_api_key = api_key
    params["api_key"] = json_api_key

    json_user_id: None | str | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    json_request_id: None | str | Unset
    if isinstance(request_id, Unset):
        json_request_id = UNSET
    else:
        json_request_id = request_id
    params["request_id"] = json_request_id

    json_team_id: None | str | Unset
    if isinstance(team_id, Unset):
        json_team_id = UNSET
    else:
        json_team_id = team_id
    params["team_id"] = json_team_id

    json_min_spend: float | None | Unset
    if isinstance(min_spend, Unset):
        json_min_spend = UNSET
    else:
        json_min_spend = min_spend
    params["min_spend"] = json_min_spend

    json_max_spend: float | None | Unset
    if isinstance(max_spend, Unset):
        json_max_spend = UNSET
    else:
        json_max_spend = max_spend
    params["max_spend"] = json_max_spend

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

    params["page"] = page

    params["page_size"] = page_size

    json_status_filter: None | str | Unset
    if isinstance(status_filter, Unset):
        json_status_filter = UNSET
    else:
        json_status_filter = status_filter
    params["status_filter"] = json_status_filter

    json_model: None | str | Unset
    if isinstance(model, Unset):
        json_model = UNSET
    else:
        json_model = model
    params["model"] = json_model

    json_model_id: None | str | Unset
    if isinstance(model_id, Unset):
        json_model_id = UNSET
    else:
        json_model_id = model_id
    params["model_id"] = json_model_id

    json_key_alias: None | str | Unset
    if isinstance(key_alias, Unset):
        json_key_alias = UNSET
    else:
        json_key_alias = key_alias
    params["key_alias"] = json_key_alias

    json_end_user: None | str | Unset
    if isinstance(end_user, Unset):
        json_end_user = UNSET
    else:
        json_end_user = end_user
    params["end_user"] = json_end_user

    json_error_code: None | str | Unset
    if isinstance(error_code, Unset):
        json_error_code = UNSET
    else:
        json_error_code = error_code
    params["error_code"] = json_error_code

    json_error_message: None | str | Unset
    if isinstance(error_message, Unset):
        json_error_message = UNSET
    else:
        json_error_message = error_message
    params["error_message"] = json_error_message

    params["sort_by"] = sort_by

    json_sort_order: None | str | Unset
    if isinstance(sort_order, Unset):
        json_sort_order = UNSET
    else:
        json_sort_order = sort_order
    params["sort_order"] = json_sort_order


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/spend/logs/v2",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | UiViewSpendLogsSpendLogsV2GetResponse200UiViewSpendLogsSpendLogsV2Get | None:
    if response.status_code == 200:
        response_200 = UiViewSpendLogsSpendLogsV2GetResponse200UiViewSpendLogsSpendLogsV2Get.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | UiViewSpendLogsSpendLogsV2GetResponse200UiViewSpendLogsSpendLogsV2Get]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    api_key: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    request_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    min_spend: float | None | Unset = UNSET,
    max_spend: float | None | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    status_filter: None | str | Unset = UNSET,
    model: None | str | Unset = UNSET,
    model_id: None | str | Unset = UNSET,
    key_alias: None | str | Unset = UNSET,
    end_user: None | str | Unset = UNSET,
    error_code: None | str | Unset = UNSET,
    error_message: None | str | Unset = UNSET,
    sort_by: str | Unset = 'startTime',
    sort_order: None | str | Unset = 'desc',

) -> Response[HTTPValidationError | UiViewSpendLogsSpendLogsV2GetResponse200UiViewSpendLogsSpendLogsV2Get]:
    r""" Ui View Spend Logs

     View spend logs with pagination support.
    Available at both `/spend/logs/v2` (public API) and `/spend/logs/ui` (internal UI).

    Returns paginated response with data, total, page, page_size, and total_pages.

    Example:
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs/v2?start_date=2025-11-25%2000:00:00&end_date=2025-11-
    26%2023:59:59&page=1&page_size=50\" -H \"Authorization: Bearer sk-1234\"
    ```

    Args:
        api_key (None | str | Unset): Get spend logs based on api key
        user_id (None | str | Unset): Get spend logs based on user_id
        request_id (None | str | Unset): request_id to get spend logs for specific request_id
        team_id (None | str | Unset): Filter spend logs by team_id
        min_spend (float | None | Unset): Filter logs with spend greater than or equal to this
            value
        max_spend (float | None | Unset): Filter logs with spend less than or equal to this value
        start_date (None | str | Unset): Time from which to start viewing key spend
        end_date (None | str | Unset): Time till which to view key spend
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Number of items per page Default: 50.
        status_filter (None | str | Unset): Filter logs by status (e.g., success, failure)
        model (None | str | Unset): Filter logs by model
        model_id (None | str | Unset): Filter logs by model ID (litellm model deployment id)
        key_alias (None | str | Unset): Filter logs by key alias
        end_user (None | str | Unset): Filter logs by end user
        error_code (None | str | Unset): Filter logs by error code (e.g., '404', '500')
        error_message (None | str | Unset): Filter logs by error message (partial string match)
        sort_by (str | Unset): Sort logs by field: spend, total_tokens, startTime, or endTime
            Default: 'startTime'.
        sort_order (None | str | Unset): Sort order: asc or desc Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UiViewSpendLogsSpendLogsV2GetResponse200UiViewSpendLogsSpendLogsV2Get]
     """


    kwargs = _get_kwargs(
        api_key=api_key,
user_id=user_id,
request_id=request_id,
team_id=team_id,
min_spend=min_spend,
max_spend=max_spend,
start_date=start_date,
end_date=end_date,
page=page,
page_size=page_size,
status_filter=status_filter,
model=model,
model_id=model_id,
key_alias=key_alias,
end_user=end_user,
error_code=error_code,
error_message=error_message,
sort_by=sort_by,
sort_order=sort_order,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    api_key: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    request_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    min_spend: float | None | Unset = UNSET,
    max_spend: float | None | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    status_filter: None | str | Unset = UNSET,
    model: None | str | Unset = UNSET,
    model_id: None | str | Unset = UNSET,
    key_alias: None | str | Unset = UNSET,
    end_user: None | str | Unset = UNSET,
    error_code: None | str | Unset = UNSET,
    error_message: None | str | Unset = UNSET,
    sort_by: str | Unset = 'startTime',
    sort_order: None | str | Unset = 'desc',

) -> HTTPValidationError | UiViewSpendLogsSpendLogsV2GetResponse200UiViewSpendLogsSpendLogsV2Get | None:
    r""" Ui View Spend Logs

     View spend logs with pagination support.
    Available at both `/spend/logs/v2` (public API) and `/spend/logs/ui` (internal UI).

    Returns paginated response with data, total, page, page_size, and total_pages.

    Example:
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs/v2?start_date=2025-11-25%2000:00:00&end_date=2025-11-
    26%2023:59:59&page=1&page_size=50\" -H \"Authorization: Bearer sk-1234\"
    ```

    Args:
        api_key (None | str | Unset): Get spend logs based on api key
        user_id (None | str | Unset): Get spend logs based on user_id
        request_id (None | str | Unset): request_id to get spend logs for specific request_id
        team_id (None | str | Unset): Filter spend logs by team_id
        min_spend (float | None | Unset): Filter logs with spend greater than or equal to this
            value
        max_spend (float | None | Unset): Filter logs with spend less than or equal to this value
        start_date (None | str | Unset): Time from which to start viewing key spend
        end_date (None | str | Unset): Time till which to view key spend
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Number of items per page Default: 50.
        status_filter (None | str | Unset): Filter logs by status (e.g., success, failure)
        model (None | str | Unset): Filter logs by model
        model_id (None | str | Unset): Filter logs by model ID (litellm model deployment id)
        key_alias (None | str | Unset): Filter logs by key alias
        end_user (None | str | Unset): Filter logs by end user
        error_code (None | str | Unset): Filter logs by error code (e.g., '404', '500')
        error_message (None | str | Unset): Filter logs by error message (partial string match)
        sort_by (str | Unset): Sort logs by field: spend, total_tokens, startTime, or endTime
            Default: 'startTime'.
        sort_order (None | str | Unset): Sort order: asc or desc Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UiViewSpendLogsSpendLogsV2GetResponse200UiViewSpendLogsSpendLogsV2Get
     """


    return sync_detailed(
        client=client,
api_key=api_key,
user_id=user_id,
request_id=request_id,
team_id=team_id,
min_spend=min_spend,
max_spend=max_spend,
start_date=start_date,
end_date=end_date,
page=page,
page_size=page_size,
status_filter=status_filter,
model=model,
model_id=model_id,
key_alias=key_alias,
end_user=end_user,
error_code=error_code,
error_message=error_message,
sort_by=sort_by,
sort_order=sort_order,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    api_key: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    request_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    min_spend: float | None | Unset = UNSET,
    max_spend: float | None | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    status_filter: None | str | Unset = UNSET,
    model: None | str | Unset = UNSET,
    model_id: None | str | Unset = UNSET,
    key_alias: None | str | Unset = UNSET,
    end_user: None | str | Unset = UNSET,
    error_code: None | str | Unset = UNSET,
    error_message: None | str | Unset = UNSET,
    sort_by: str | Unset = 'startTime',
    sort_order: None | str | Unset = 'desc',

) -> Response[HTTPValidationError | UiViewSpendLogsSpendLogsV2GetResponse200UiViewSpendLogsSpendLogsV2Get]:
    r""" Ui View Spend Logs

     View spend logs with pagination support.
    Available at both `/spend/logs/v2` (public API) and `/spend/logs/ui` (internal UI).

    Returns paginated response with data, total, page, page_size, and total_pages.

    Example:
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs/v2?start_date=2025-11-25%2000:00:00&end_date=2025-11-
    26%2023:59:59&page=1&page_size=50\" -H \"Authorization: Bearer sk-1234\"
    ```

    Args:
        api_key (None | str | Unset): Get spend logs based on api key
        user_id (None | str | Unset): Get spend logs based on user_id
        request_id (None | str | Unset): request_id to get spend logs for specific request_id
        team_id (None | str | Unset): Filter spend logs by team_id
        min_spend (float | None | Unset): Filter logs with spend greater than or equal to this
            value
        max_spend (float | None | Unset): Filter logs with spend less than or equal to this value
        start_date (None | str | Unset): Time from which to start viewing key spend
        end_date (None | str | Unset): Time till which to view key spend
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Number of items per page Default: 50.
        status_filter (None | str | Unset): Filter logs by status (e.g., success, failure)
        model (None | str | Unset): Filter logs by model
        model_id (None | str | Unset): Filter logs by model ID (litellm model deployment id)
        key_alias (None | str | Unset): Filter logs by key alias
        end_user (None | str | Unset): Filter logs by end user
        error_code (None | str | Unset): Filter logs by error code (e.g., '404', '500')
        error_message (None | str | Unset): Filter logs by error message (partial string match)
        sort_by (str | Unset): Sort logs by field: spend, total_tokens, startTime, or endTime
            Default: 'startTime'.
        sort_order (None | str | Unset): Sort order: asc or desc Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UiViewSpendLogsSpendLogsV2GetResponse200UiViewSpendLogsSpendLogsV2Get]
     """


    kwargs = _get_kwargs(
        api_key=api_key,
user_id=user_id,
request_id=request_id,
team_id=team_id,
min_spend=min_spend,
max_spend=max_spend,
start_date=start_date,
end_date=end_date,
page=page,
page_size=page_size,
status_filter=status_filter,
model=model,
model_id=model_id,
key_alias=key_alias,
end_user=end_user,
error_code=error_code,
error_message=error_message,
sort_by=sort_by,
sort_order=sort_order,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    api_key: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    request_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    min_spend: float | None | Unset = UNSET,
    max_spend: float | None | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    status_filter: None | str | Unset = UNSET,
    model: None | str | Unset = UNSET,
    model_id: None | str | Unset = UNSET,
    key_alias: None | str | Unset = UNSET,
    end_user: None | str | Unset = UNSET,
    error_code: None | str | Unset = UNSET,
    error_message: None | str | Unset = UNSET,
    sort_by: str | Unset = 'startTime',
    sort_order: None | str | Unset = 'desc',

) -> HTTPValidationError | UiViewSpendLogsSpendLogsV2GetResponse200UiViewSpendLogsSpendLogsV2Get | None:
    r""" Ui View Spend Logs

     View spend logs with pagination support.
    Available at both `/spend/logs/v2` (public API) and `/spend/logs/ui` (internal UI).

    Returns paginated response with data, total, page, page_size, and total_pages.

    Example:
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs/v2?start_date=2025-11-25%2000:00:00&end_date=2025-11-
    26%2023:59:59&page=1&page_size=50\" -H \"Authorization: Bearer sk-1234\"
    ```

    Args:
        api_key (None | str | Unset): Get spend logs based on api key
        user_id (None | str | Unset): Get spend logs based on user_id
        request_id (None | str | Unset): request_id to get spend logs for specific request_id
        team_id (None | str | Unset): Filter spend logs by team_id
        min_spend (float | None | Unset): Filter logs with spend greater than or equal to this
            value
        max_spend (float | None | Unset): Filter logs with spend less than or equal to this value
        start_date (None | str | Unset): Time from which to start viewing key spend
        end_date (None | str | Unset): Time till which to view key spend
        page (int | Unset): Page number for pagination Default: 1.
        page_size (int | Unset): Number of items per page Default: 50.
        status_filter (None | str | Unset): Filter logs by status (e.g., success, failure)
        model (None | str | Unset): Filter logs by model
        model_id (None | str | Unset): Filter logs by model ID (litellm model deployment id)
        key_alias (None | str | Unset): Filter logs by key alias
        end_user (None | str | Unset): Filter logs by end user
        error_code (None | str | Unset): Filter logs by error code (e.g., '404', '500')
        error_message (None | str | Unset): Filter logs by error message (partial string match)
        sort_by (str | Unset): Sort logs by field: spend, total_tokens, startTime, or endTime
            Default: 'startTime'.
        sort_order (None | str | Unset): Sort order: asc or desc Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UiViewSpendLogsSpendLogsV2GetResponse200UiViewSpendLogsSpendLogsV2Get
     """


    return (await asyncio_detailed(
        client=client,
api_key=api_key,
user_id=user_id,
request_id=request_id,
team_id=team_id,
min_spend=min_spend,
max_spend=max_spend,
start_date=start_date,
end_date=end_date,
page=page,
page_size=page_size,
status_filter=status_filter,
model=model,
model_id=model_id,
key_alias=key_alias,
end_user=end_user,
error_code=error_code,
error_message=error_message,
sort_by=sort_by,
sort_order=sort_order,

    )).parsed
