from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_model_group_response import DeleteModelGroupResponse
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    access_group: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/access_group/{access_group}/delete".format(access_group=quote(str(access_group), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteModelGroupResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DeleteModelGroupResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteModelGroupResponse | HTTPValidationError]:
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

) -> Response[DeleteModelGroupResponse | HTTPValidationError]:
    r""" Delete Access Group

     Delete an access group.

    Removes the access group from all deployments that have it.

    Example:
    ```bash
    curl -X DELETE 'http://localhost:4000/access_group/production-models/delete' \
      -H 'Authorization: Bearer sk-1234'
    ```

    Parameters:
    - access_group: str - The access group name (URL path parameter)

    Returns:
    - DeleteModelGroupResponse with deletion details

    Raises:
    - HTTPException 404: If access group not found

    Args:
        access_group (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteModelGroupResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        access_group=access_group,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    access_group: str,
    *,
    client: AuthenticatedClient,

) -> DeleteModelGroupResponse | HTTPValidationError | None:
    r""" Delete Access Group

     Delete an access group.

    Removes the access group from all deployments that have it.

    Example:
    ```bash
    curl -X DELETE 'http://localhost:4000/access_group/production-models/delete' \
      -H 'Authorization: Bearer sk-1234'
    ```

    Parameters:
    - access_group: str - The access group name (URL path parameter)

    Returns:
    - DeleteModelGroupResponse with deletion details

    Raises:
    - HTTPException 404: If access group not found

    Args:
        access_group (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteModelGroupResponse | HTTPValidationError
     """


    return sync_detailed(
        access_group=access_group,
client=client,

    ).parsed

async def asyncio_detailed(
    access_group: str,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteModelGroupResponse | HTTPValidationError]:
    r""" Delete Access Group

     Delete an access group.

    Removes the access group from all deployments that have it.

    Example:
    ```bash
    curl -X DELETE 'http://localhost:4000/access_group/production-models/delete' \
      -H 'Authorization: Bearer sk-1234'
    ```

    Parameters:
    - access_group: str - The access group name (URL path parameter)

    Returns:
    - DeleteModelGroupResponse with deletion details

    Raises:
    - HTTPException 404: If access group not found

    Args:
        access_group (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteModelGroupResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        access_group=access_group,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    access_group: str,
    *,
    client: AuthenticatedClient,

) -> DeleteModelGroupResponse | HTTPValidationError | None:
    r""" Delete Access Group

     Delete an access group.

    Removes the access group from all deployments that have it.

    Example:
    ```bash
    curl -X DELETE 'http://localhost:4000/access_group/production-models/delete' \
      -H 'Authorization: Bearer sk-1234'
    ```

    Parameters:
    - access_group: str - The access group name (URL path parameter)

    Returns:
    - DeleteModelGroupResponse with deletion details

    Raises:
    - HTTPException 404: If access group not found

    Args:
        access_group (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteModelGroupResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        access_group=access_group,
client=client,

    )).parsed
