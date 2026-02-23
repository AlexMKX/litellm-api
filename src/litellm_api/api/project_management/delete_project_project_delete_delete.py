from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_project_request import DeleteProjectRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llm_project_table import LiteLLMProjectTable
from typing import cast



def _get_kwargs(
    *,
    body: DeleteProjectRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/project/delete",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | list[LiteLLMProjectTable] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = LiteLLMProjectTable.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | list[LiteLLMProjectTable]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DeleteProjectRequest,

) -> Response[HTTPValidationError | list[LiteLLMProjectTable]]:
    r""" Delete Project

     Delete projects

    Parameters:
    - project_ids: *List[str]* - List of project ids to delete

    Example:
    ```bash
    curl --location --request DELETE 'http://0.0.0.0:4000/project/delete' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_ids\": [\"project-123\", \"project-456\"]
    }'
    ```

    Args:
        body (DeleteProjectRequest): Request model for DELETE /project/delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LiteLLMProjectTable]]
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
    body: DeleteProjectRequest,

) -> HTTPValidationError | list[LiteLLMProjectTable] | None:
    r""" Delete Project

     Delete projects

    Parameters:
    - project_ids: *List[str]* - List of project ids to delete

    Example:
    ```bash
    curl --location --request DELETE 'http://0.0.0.0:4000/project/delete' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_ids\": [\"project-123\", \"project-456\"]
    }'
    ```

    Args:
        body (DeleteProjectRequest): Request model for DELETE /project/delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LiteLLMProjectTable]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DeleteProjectRequest,

) -> Response[HTTPValidationError | list[LiteLLMProjectTable]]:
    r""" Delete Project

     Delete projects

    Parameters:
    - project_ids: *List[str]* - List of project ids to delete

    Example:
    ```bash
    curl --location --request DELETE 'http://0.0.0.0:4000/project/delete' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_ids\": [\"project-123\", \"project-456\"]
    }'
    ```

    Args:
        body (DeleteProjectRequest): Request model for DELETE /project/delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LiteLLMProjectTable]]
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
    body: DeleteProjectRequest,

) -> HTTPValidationError | list[LiteLLMProjectTable] | None:
    r""" Delete Project

     Delete projects

    Parameters:
    - project_ids: *List[str]* - List of project ids to delete

    Example:
    ```bash
    curl --location --request DELETE 'http://0.0.0.0:4000/project/delete' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_ids\": [\"project-123\", \"project-456\"]
    }'
    ```

    Args:
        body (DeleteProjectRequest): Request model for DELETE /project/delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LiteLLMProjectTable]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
