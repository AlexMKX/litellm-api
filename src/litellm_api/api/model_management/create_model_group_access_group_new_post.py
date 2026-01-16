from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.new_model_group_request import NewModelGroupRequest
from ...models.new_model_group_response import NewModelGroupResponse
from typing import cast



def _get_kwargs(
    *,
    body: NewModelGroupRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/access_group/new",
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
    *,
    client: AuthenticatedClient,
    body: NewModelGroupRequest,

) -> Response[HTTPValidationError | NewModelGroupResponse]:
    r""" Create Model Group

     Create a new access group containing multiple model names.

    An access group is a named collection of model groups that can be referenced
    by teams/keys for simplified access control.

    Example:
    ```bash
    curl -X POST 'http://localhost:4000/access_group/new' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"access_group\": \"production-models\",
        \"model_names\": [\"gpt-4\", \"claude-3-opus\", \"gemini-pro\"]
      }'
    ```

    Parameters:
    - access_group: str - The access group name (e.g., \"production-models\")
    - model_names: List[str] - List of existing model groups to include

    Returns:
    - NewModelGroupResponse with the created access group details

    Raises:
    - HTTPException 400: If any model names don't exist
    - HTTPException 500: If database operations fail

    Args:
        body (NewModelGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NewModelGroupResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: NewModelGroupRequest,

) -> HTTPValidationError | NewModelGroupResponse | None:
    r""" Create Model Group

     Create a new access group containing multiple model names.

    An access group is a named collection of model groups that can be referenced
    by teams/keys for simplified access control.

    Example:
    ```bash
    curl -X POST 'http://localhost:4000/access_group/new' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"access_group\": \"production-models\",
        \"model_names\": [\"gpt-4\", \"claude-3-opus\", \"gemini-pro\"]
      }'
    ```

    Parameters:
    - access_group: str - The access group name (e.g., \"production-models\")
    - model_names: List[str] - List of existing model groups to include

    Returns:
    - NewModelGroupResponse with the created access group details

    Raises:
    - HTTPException 400: If any model names don't exist
    - HTTPException 500: If database operations fail

    Args:
        body (NewModelGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NewModelGroupResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewModelGroupRequest,

) -> Response[HTTPValidationError | NewModelGroupResponse]:
    r""" Create Model Group

     Create a new access group containing multiple model names.

    An access group is a named collection of model groups that can be referenced
    by teams/keys for simplified access control.

    Example:
    ```bash
    curl -X POST 'http://localhost:4000/access_group/new' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"access_group\": \"production-models\",
        \"model_names\": [\"gpt-4\", \"claude-3-opus\", \"gemini-pro\"]
      }'
    ```

    Parameters:
    - access_group: str - The access group name (e.g., \"production-models\")
    - model_names: List[str] - List of existing model groups to include

    Returns:
    - NewModelGroupResponse with the created access group details

    Raises:
    - HTTPException 400: If any model names don't exist
    - HTTPException 500: If database operations fail

    Args:
        body (NewModelGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NewModelGroupResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NewModelGroupRequest,

) -> HTTPValidationError | NewModelGroupResponse | None:
    r""" Create Model Group

     Create a new access group containing multiple model names.

    An access group is a named collection of model groups that can be referenced
    by teams/keys for simplified access control.

    Example:
    ```bash
    curl -X POST 'http://localhost:4000/access_group/new' \
      -H 'Authorization: Bearer sk-1234' \
      -H 'Content-Type: application/json' \
      -d '{
        \"access_group\": \"production-models\",
        \"model_names\": [\"gpt-4\", \"claude-3-opus\", \"gemini-pro\"]
      }'
    ```

    Parameters:
    - access_group: str - The access group name (e.g., \"production-models\")
    - model_names: List[str] - List of existing model groups to include

    Returns:
    - NewModelGroupResponse with the created access group details

    Raises:
    - HTTPException 400: If any model names don't exist
    - HTTPException 500: If database operations fail

    Args:
        body (NewModelGroupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NewModelGroupResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
