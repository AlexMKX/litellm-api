from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llm_spend_logs import LiteLLMSpendLogs
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    api_key: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    request_id: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    summarize: bool | Unset = True,

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

    params["summarize"] = summarize


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/spend/logs",
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
    api_key: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    request_id: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    summarize: bool | Unset = True,

) -> Response[HTTPValidationError | list[LiteLLMSpendLogs]]:
    r""" View Spend Logs

     [DEPRECATED] This endpoint is not paginated and can cause performance issues.
    Please use `/spend/logs/v2` instead for paginated access to spend logs.

    View all spend logs, if request_id is provided, only logs for that request_id will be returned

    When start_date and end_date are provided:
    - summarize=true (default): Returns aggregated spend data grouped by date (maintains backward
    compatibility)
    - summarize=false: Returns filtered individual log entries within the date range

    Example Request for all logs
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs\" -H \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific request_id
    ```
    curl -X GET
    \"http://0.0.0.0:8000/spend/logs?request_id=chatcmpl-6dcb2540-d3d7-4e49-bb27-291f863f112e\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific api_key
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?api_key=sk-test-example-key-123\" -H \"Authorization:
    Bearer sk-1234\"
    ```

    Example Request for specific user_id
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?user_id=ishaan@berri.ai\" -H \"Authorization: Bearer
    sk-1234\"
    ```

    Example Request for date range with individual logs (unsummarized)
    ```
    curl -X GET
    \"http://0.0.0.0:8000/spend/logs?start_date=2024-01-01&end_date=2024-01-02&summarize=false\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Args:
        api_key (None | str | Unset): Get spend logs based on api key
        user_id (None | str | Unset): Get spend logs based on user_id
        request_id (None | str | Unset): request_id to get spend logs for specific request_id. If
            none passed then pass spend logs for all requests
        start_date (None | str | Unset): Time from which to start viewing key spend
        end_date (None | str | Unset): Time till which to view key spend
        summarize (bool | Unset): When start_date and end_date are provided, summarize=true
            returns aggregated data by date (legacy behavior), summarize=false returns filtered
            individual logs Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LiteLLMSpendLogs]]
     """


    kwargs = _get_kwargs(
        api_key=api_key,
user_id=user_id,
request_id=request_id,
start_date=start_date,
end_date=end_date,
summarize=summarize,

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
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    summarize: bool | Unset = True,

) -> HTTPValidationError | list[LiteLLMSpendLogs] | None:
    r""" View Spend Logs

     [DEPRECATED] This endpoint is not paginated and can cause performance issues.
    Please use `/spend/logs/v2` instead for paginated access to spend logs.

    View all spend logs, if request_id is provided, only logs for that request_id will be returned

    When start_date and end_date are provided:
    - summarize=true (default): Returns aggregated spend data grouped by date (maintains backward
    compatibility)
    - summarize=false: Returns filtered individual log entries within the date range

    Example Request for all logs
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs\" -H \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific request_id
    ```
    curl -X GET
    \"http://0.0.0.0:8000/spend/logs?request_id=chatcmpl-6dcb2540-d3d7-4e49-bb27-291f863f112e\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific api_key
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?api_key=sk-test-example-key-123\" -H \"Authorization:
    Bearer sk-1234\"
    ```

    Example Request for specific user_id
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?user_id=ishaan@berri.ai\" -H \"Authorization: Bearer
    sk-1234\"
    ```

    Example Request for date range with individual logs (unsummarized)
    ```
    curl -X GET
    \"http://0.0.0.0:8000/spend/logs?start_date=2024-01-01&end_date=2024-01-02&summarize=false\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Args:
        api_key (None | str | Unset): Get spend logs based on api key
        user_id (None | str | Unset): Get spend logs based on user_id
        request_id (None | str | Unset): request_id to get spend logs for specific request_id. If
            none passed then pass spend logs for all requests
        start_date (None | str | Unset): Time from which to start viewing key spend
        end_date (None | str | Unset): Time till which to view key spend
        summarize (bool | Unset): When start_date and end_date are provided, summarize=true
            returns aggregated data by date (legacy behavior), summarize=false returns filtered
            individual logs Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LiteLLMSpendLogs]
     """


    return sync_detailed(
        client=client,
api_key=api_key,
user_id=user_id,
request_id=request_id,
start_date=start_date,
end_date=end_date,
summarize=summarize,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    api_key: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    request_id: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    summarize: bool | Unset = True,

) -> Response[HTTPValidationError | list[LiteLLMSpendLogs]]:
    r""" View Spend Logs

     [DEPRECATED] This endpoint is not paginated and can cause performance issues.
    Please use `/spend/logs/v2` instead for paginated access to spend logs.

    View all spend logs, if request_id is provided, only logs for that request_id will be returned

    When start_date and end_date are provided:
    - summarize=true (default): Returns aggregated spend data grouped by date (maintains backward
    compatibility)
    - summarize=false: Returns filtered individual log entries within the date range

    Example Request for all logs
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs\" -H \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific request_id
    ```
    curl -X GET
    \"http://0.0.0.0:8000/spend/logs?request_id=chatcmpl-6dcb2540-d3d7-4e49-bb27-291f863f112e\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific api_key
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?api_key=sk-test-example-key-123\" -H \"Authorization:
    Bearer sk-1234\"
    ```

    Example Request for specific user_id
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?user_id=ishaan@berri.ai\" -H \"Authorization: Bearer
    sk-1234\"
    ```

    Example Request for date range with individual logs (unsummarized)
    ```
    curl -X GET
    \"http://0.0.0.0:8000/spend/logs?start_date=2024-01-01&end_date=2024-01-02&summarize=false\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Args:
        api_key (None | str | Unset): Get spend logs based on api key
        user_id (None | str | Unset): Get spend logs based on user_id
        request_id (None | str | Unset): request_id to get spend logs for specific request_id. If
            none passed then pass spend logs for all requests
        start_date (None | str | Unset): Time from which to start viewing key spend
        end_date (None | str | Unset): Time till which to view key spend
        summarize (bool | Unset): When start_date and end_date are provided, summarize=true
            returns aggregated data by date (legacy behavior), summarize=false returns filtered
            individual logs Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LiteLLMSpendLogs]]
     """


    kwargs = _get_kwargs(
        api_key=api_key,
user_id=user_id,
request_id=request_id,
start_date=start_date,
end_date=end_date,
summarize=summarize,

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
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    summarize: bool | Unset = True,

) -> HTTPValidationError | list[LiteLLMSpendLogs] | None:
    r""" View Spend Logs

     [DEPRECATED] This endpoint is not paginated and can cause performance issues.
    Please use `/spend/logs/v2` instead for paginated access to spend logs.

    View all spend logs, if request_id is provided, only logs for that request_id will be returned

    When start_date and end_date are provided:
    - summarize=true (default): Returns aggregated spend data grouped by date (maintains backward
    compatibility)
    - summarize=false: Returns filtered individual log entries within the date range

    Example Request for all logs
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs\" -H \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific request_id
    ```
    curl -X GET
    \"http://0.0.0.0:8000/spend/logs?request_id=chatcmpl-6dcb2540-d3d7-4e49-bb27-291f863f112e\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Example Request for specific api_key
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?api_key=sk-test-example-key-123\" -H \"Authorization:
    Bearer sk-1234\"
    ```

    Example Request for specific user_id
    ```
    curl -X GET \"http://0.0.0.0:8000/spend/logs?user_id=ishaan@berri.ai\" -H \"Authorization: Bearer
    sk-1234\"
    ```

    Example Request for date range with individual logs (unsummarized)
    ```
    curl -X GET
    \"http://0.0.0.0:8000/spend/logs?start_date=2024-01-01&end_date=2024-01-02&summarize=false\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Args:
        api_key (None | str | Unset): Get spend logs based on api key
        user_id (None | str | Unset): Get spend logs based on user_id
        request_id (None | str | Unset): request_id to get spend logs for specific request_id. If
            none passed then pass spend logs for all requests
        start_date (None | str | Unset): Time from which to start viewing key spend
        end_date (None | str | Unset): Time till which to view key spend
        summarize (bool | Unset): When start_date and end_date are provided, summarize=true
            returns aggregated data by date (legacy behavior), summarize=false returns filtered
            individual logs Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LiteLLMSpendLogs]
     """


    return (await asyncio_detailed(
        client=client,
api_key=api_key,
user_id=user_id,
request_id=request_id,
start_date=start_date,
end_date=end_date,
summarize=summarize,

    )).parsed
