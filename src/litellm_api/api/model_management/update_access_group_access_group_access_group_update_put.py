from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.new_model_group_response import NewModelGroupResponse
from ...models.update_model_group_request import UpdateModelGroupRequest
from typing import cast



def _get_kwargs(
    access_group: str,
    *,
    body: UpdateModelGroupRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/access_group/{access_group}/update".format(access_group=quote(str(access_group), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | NewModelGroupResponse | None:
    if response.status_code == 200:
        response_200 = NewModelGroupResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | NewModelGroupResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    access_group: str,
    *,
    client: AuthenticatedClient,
    body: UpdateModelGroupRequest,

) -> Response[HTTPValidationError | NewModelGroupResponse]:
    r""" Update Access Group

     Update an access group's model names.

    This will:
    1. Remove the access group from all current deployments
    2. Add the access group to all deployments for the new model_names list

    Example:
    ```bash
    curl -X PUT 'http://localhost:4000/access_group/production-models/update' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"model_names\": [\"gpt-4\", \"claude-3-sonnet\"]
      }'
    ```

    Parameters:
    - access_group: str - The access group name (URL path parameter)
    - model_names: List[str] - New list of model groups to include

    Returns:
    - NewModelGroupResponse with the updated access group details

    Raises:
    - HTTPException 400: If any model names don't exist
    - HTTPException 404: If access group not found

    Args:
        access_group (str):
        body (UpdateModelGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NewModelGroupResponse]
     """


    kwargs = _get_kwargs(
        access_group=access_group,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    access_group: str,
    *,
    client: AuthenticatedClient,
    body: UpdateModelGroupRequest,

) -> HTTPValidationError | NewModelGroupResponse | None:
    r""" Update Access Group

     Update an access group's model names.

    This will:
    1. Remove the access group from all current deployments
    2. Add the access group to all deployments for the new model_names list

    Example:
    ```bash
    curl -X PUT 'http://localhost:4000/access_group/production-models/update' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"model_names\": [\"gpt-4\", \"claude-3-sonnet\"]
      }'
    ```

    Parameters:
    - access_group: str - The access group name (URL path parameter)
    - model_names: List[str] - New list of model groups to include

    Returns:
    - NewModelGroupResponse with the updated access group details

    Raises:
    - HTTPException 400: If any model names don't exist
    - HTTPException 404: If access group not found

    Args:
        access_group (str):
        body (UpdateModelGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NewModelGroupResponse
     """


    return sync_detailed(
        access_group=access_group,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    access_group: str,
    *,
    client: AuthenticatedClient,
    body: UpdateModelGroupRequest,

) -> Response[HTTPValidationError | NewModelGroupResponse]:
    r""" Update Access Group

     Update an access group's model names.

    This will:
    1. Remove the access group from all current deployments
    2. Add the access group to all deployments for the new model_names list

    Example:
    ```bash
    curl -X PUT 'http://localhost:4000/access_group/production-models/update' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"model_names\": [\"gpt-4\", \"claude-3-sonnet\"]
      }'
    ```

    Parameters:
    - access_group: str - The access group name (URL path parameter)
    - model_names: List[str] - New list of model groups to include

    Returns:
    - NewModelGroupResponse with the updated access group details

    Raises:
    - HTTPException 400: If any model names don't exist
    - HTTPException 404: If access group not found

    Args:
        access_group (str):
        body (UpdateModelGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NewModelGroupResponse]
     """


    kwargs = _get_kwargs(
        access_group=access_group,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    access_group: str,
    *,
    client: AuthenticatedClient,
    body: UpdateModelGroupRequest,

) -> HTTPValidationError | NewModelGroupResponse | None:
    r""" Update Access Group

     Update an access group's model names.

    This will:
    1. Remove the access group from all current deployments
    2. Add the access group to all deployments for the new model_names list

    Example:
    ```bash
    curl -X PUT 'http://localhost:4000/access_group/production-models/update' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"model_names\": [\"gpt-4\", \"claude-3-sonnet\"]
      }'
    ```

    Parameters:
    - access_group: str - The access group name (URL path parameter)
    - model_names: List[str] - New list of model groups to include

    Returns:
    - NewModelGroupResponse with the updated access group details

    Raises:
    - HTTPException 400: If any model names don't exist
    - HTTPException 404: If access group not found

    Args:
        access_group (str):
        body (UpdateModelGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NewModelGroupResponse
     """


    return (await asyncio_detailed(
        access_group=access_group,
client=client,
body=body,

    )).parsed
