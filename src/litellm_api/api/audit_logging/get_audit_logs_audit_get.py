from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.paginated_audit_log_response import PaginatedAuditLogResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    changed_by: None | str | Unset = UNSET,
    changed_by_api_key: None | str | Unset = UNSET,
    action: None | str | Unset = UNSET,
    table_name: None | str | Unset = UNSET,
    object_id: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'desc',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    json_changed_by: None | str | Unset
    if isinstance(changed_by, Unset):
        json_changed_by = UNSET
    else:
        json_changed_by = changed_by
    params["changed_by"] = json_changed_by

    json_changed_by_api_key: None | str | Unset
    if isinstance(changed_by_api_key, Unset):
        json_changed_by_api_key = UNSET
    else:
        json_changed_by_api_key = changed_by_api_key
    params["changed_by_api_key"] = json_changed_by_api_key

    json_action: None | str | Unset
    if isinstance(action, Unset):
        json_action = UNSET
    else:
        json_action = action
    params["action"] = json_action

    json_table_name: None | str | Unset
    if isinstance(table_name, Unset):
        json_table_name = UNSET
    else:
        json_table_name = table_name
    params["table_name"] = json_table_name

    json_object_id: None | str | Unset
    if isinstance(object_id, Unset):
        json_object_id = UNSET
    else:
        json_object_id = object_id
    params["object_id"] = json_object_id

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

    json_sort_by: None | str | Unset
    if isinstance(sort_by, Unset):
        json_sort_by = UNSET
    else:
        json_sort_by = sort_by
    params["sort_by"] = json_sort_by

    params["sort_order"] = sort_order


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/audit",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | PaginatedAuditLogResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedAuditLogResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | PaginatedAuditLogResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    changed_by: None | str | Unset = UNSET,
    changed_by_api_key: None | str | Unset = UNSET,
    action: None | str | Unset = UNSET,
    table_name: None | str | Unset = UNSET,
    object_id: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'desc',

) -> Response[HTTPValidationError | PaginatedAuditLogResponse]:
    """ Get Audit Logs

     Get all audit logs with filtering and pagination.

    Returns a paginated response of audit logs matching the specified filters.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 10.
        changed_by (None | str | Unset): Filter by user or system that performed the action
        changed_by_api_key (None | str | Unset): Filter by API key hash that performed the action
        action (None | str | Unset): Filter by action type (create, update, delete)
        table_name (None | str | Unset): Filter by table name that was modified
        object_id (None | str | Unset): Filter by ID of the object that was modified
        start_date (None | str | Unset): Filter logs after this date
        end_date (None | str | Unset): Filter logs before this date
        sort_by (None | str | Unset): Column to sort by (e.g. 'updated_at', 'action',
            'table_name')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PaginatedAuditLogResponse]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
changed_by=changed_by,
changed_by_api_key=changed_by_api_key,
action=action,
table_name=table_name,
object_id=object_id,
start_date=start_date,
end_date=end_date,
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
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    changed_by: None | str | Unset = UNSET,
    changed_by_api_key: None | str | Unset = UNSET,
    action: None | str | Unset = UNSET,
    table_name: None | str | Unset = UNSET,
    object_id: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'desc',

) -> HTTPValidationError | PaginatedAuditLogResponse | None:
    """ Get Audit Logs

     Get all audit logs with filtering and pagination.

    Returns a paginated response of audit logs matching the specified filters.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 10.
        changed_by (None | str | Unset): Filter by user or system that performed the action
        changed_by_api_key (None | str | Unset): Filter by API key hash that performed the action
        action (None | str | Unset): Filter by action type (create, update, delete)
        table_name (None | str | Unset): Filter by table name that was modified
        object_id (None | str | Unset): Filter by ID of the object that was modified
        start_date (None | str | Unset): Filter logs after this date
        end_date (None | str | Unset): Filter logs before this date
        sort_by (None | str | Unset): Column to sort by (e.g. 'updated_at', 'action',
            'table_name')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PaginatedAuditLogResponse
     """


    return sync_detailed(
        client=client,
page=page,
page_size=page_size,
changed_by=changed_by,
changed_by_api_key=changed_by_api_key,
action=action,
table_name=table_name,
object_id=object_id,
start_date=start_date,
end_date=end_date,
sort_by=sort_by,
sort_order=sort_order,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    changed_by: None | str | Unset = UNSET,
    changed_by_api_key: None | str | Unset = UNSET,
    action: None | str | Unset = UNSET,
    table_name: None | str | Unset = UNSET,
    object_id: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'desc',

) -> Response[HTTPValidationError | PaginatedAuditLogResponse]:
    """ Get Audit Logs

     Get all audit logs with filtering and pagination.

    Returns a paginated response of audit logs matching the specified filters.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 10.
        changed_by (None | str | Unset): Filter by user or system that performed the action
        changed_by_api_key (None | str | Unset): Filter by API key hash that performed the action
        action (None | str | Unset): Filter by action type (create, update, delete)
        table_name (None | str | Unset): Filter by table name that was modified
        object_id (None | str | Unset): Filter by ID of the object that was modified
        start_date (None | str | Unset): Filter logs after this date
        end_date (None | str | Unset): Filter logs before this date
        sort_by (None | str | Unset): Column to sort by (e.g. 'updated_at', 'action',
            'table_name')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PaginatedAuditLogResponse]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
changed_by=changed_by,
changed_by_api_key=changed_by_api_key,
action=action,
table_name=table_name,
object_id=object_id,
start_date=start_date,
end_date=end_date,
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
    page: int | Unset = 1,
    page_size: int | Unset = 10,
    changed_by: None | str | Unset = UNSET,
    changed_by_api_key: None | str | Unset = UNSET,
    action: None | str | Unset = UNSET,
    table_name: None | str | Unset = UNSET,
    object_id: None | str | Unset = UNSET,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    sort_order: str | Unset = 'desc',

) -> HTTPValidationError | PaginatedAuditLogResponse | None:
    """ Get Audit Logs

     Get all audit logs with filtering and pagination.

    Returns a paginated response of audit logs matching the specified filters.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 10.
        changed_by (None | str | Unset): Filter by user or system that performed the action
        changed_by_api_key (None | str | Unset): Filter by API key hash that performed the action
        action (None | str | Unset): Filter by action type (create, update, delete)
        table_name (None | str | Unset): Filter by table name that was modified
        object_id (None | str | Unset): Filter by ID of the object that was modified
        start_date (None | str | Unset): Filter logs after this date
        end_date (None | str | Unset): Filter logs before this date
        sort_by (None | str | Unset): Column to sort by (e.g. 'updated_at', 'action',
            'table_name')
        sort_order (str | Unset): Sort order ('asc' or 'desc') Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PaginatedAuditLogResponse
     """


    return (await asyncio_detailed(
        client=client,
page=page,
page_size=page_size,
changed_by=changed_by,
changed_by_api_key=changed_by_api_key,
action=action,
table_name=table_name,
object_id=object_id,
start_date=start_date,
end_date=end_date,
sort_by=sort_by,
sort_order=sort_order,

    )).parsed
