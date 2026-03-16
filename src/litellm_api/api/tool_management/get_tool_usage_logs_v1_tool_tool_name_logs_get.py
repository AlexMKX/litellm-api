from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.tool_usage_logs_response import ToolUsageLogsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    tool_name: str,
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

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
        "url": "/v1/tool/{tool_name}/logs".format(tool_name=quote(str(tool_name), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | ToolUsageLogsResponse | None:
    if response.status_code == 200:
        response_200 = ToolUsageLogsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | ToolUsageLogsResponse]:
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
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | ToolUsageLogsResponse]:
    """ Get Tool Usage Logs

     Return paginated spend logs for requests that used this tool (from SpendLogToolIndex).

    Args:
        tool_name (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        start_date (None | str | Unset): YYYY-MM-DD
        end_date (None | str | Unset): YYYY-MM-DD

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ToolUsageLogsResponse]
     """


    kwargs = _get_kwargs(
        tool_name=tool_name,
page=page,
page_size=page_size,
start_date=start_date,
end_date=end_date,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    tool_name: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,

) -> HTTPValidationError | ToolUsageLogsResponse | None:
    """ Get Tool Usage Logs

     Return paginated spend logs for requests that used this tool (from SpendLogToolIndex).

    Args:
        tool_name (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        start_date (None | str | Unset): YYYY-MM-DD
        end_date (None | str | Unset): YYYY-MM-DD

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ToolUsageLogsResponse
     """


    return sync_detailed(
        tool_name=tool_name,
client=client,
page=page,
page_size=page_size,
start_date=start_date,
end_date=end_date,

    ).parsed

async def asyncio_detailed(
    tool_name: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | ToolUsageLogsResponse]:
    """ Get Tool Usage Logs

     Return paginated spend logs for requests that used this tool (from SpendLogToolIndex).

    Args:
        tool_name (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        start_date (None | str | Unset): YYYY-MM-DD
        end_date (None | str | Unset): YYYY-MM-DD

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ToolUsageLogsResponse]
     """


    kwargs = _get_kwargs(
        tool_name=tool_name,
page=page,
page_size=page_size,
start_date=start_date,
end_date=end_date,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    tool_name: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,

) -> HTTPValidationError | ToolUsageLogsResponse | None:
    """ Get Tool Usage Logs

     Return paginated spend logs for requests that used this tool (from SpendLogToolIndex).

    Args:
        tool_name (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        start_date (None | str | Unset): YYYY-MM-DD
        end_date (None | str | Unset): YYYY-MM-DD

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ToolUsageLogsResponse
     """


    return (await asyncio_detailed(
        tool_name=tool_name,
client=client,
page=page,
page_size=page_size,
start_date=start_date,
end_date=end_date,

    )).parsed
