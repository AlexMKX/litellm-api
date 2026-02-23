from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llm_project_table import LiteLLMProjectTable
from typing import cast



def _get_kwargs(
    *,
    project_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["project_id"] = project_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/project/info",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | LiteLLMProjectTable | None:
    if response.status_code == 200:
        response_200 = LiteLLMProjectTable.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | LiteLLMProjectTable]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    project_id: str,

) -> Response[HTTPValidationError | LiteLLMProjectTable]:
    r""" Project Info

     Get information about a specific project

    Parameters:
    - project_id: *str* - The project id to fetch info for

    Example:
    ```bash
    curl --location 'http://0.0.0.0:4000/project/info?project_id=project-123' \
    --header 'Authorization: Bearer sk-1234'
    ```

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiteLLMProjectTable]
     """


    kwargs = _get_kwargs(
        project_id=project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    project_id: str,

) -> HTTPValidationError | LiteLLMProjectTable | None:
    r""" Project Info

     Get information about a specific project

    Parameters:
    - project_id: *str* - The project id to fetch info for

    Example:
    ```bash
    curl --location 'http://0.0.0.0:4000/project/info?project_id=project-123' \
    --header 'Authorization: Bearer sk-1234'
    ```

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiteLLMProjectTable
     """


    return sync_detailed(
        client=client,
project_id=project_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project_id: str,

) -> Response[HTTPValidationError | LiteLLMProjectTable]:
    r""" Project Info

     Get information about a specific project

    Parameters:
    - project_id: *str* - The project id to fetch info for

    Example:
    ```bash
    curl --location 'http://0.0.0.0:4000/project/info?project_id=project-123' \
    --header 'Authorization: Bearer sk-1234'
    ```

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiteLLMProjectTable]
     """


    kwargs = _get_kwargs(
        project_id=project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    project_id: str,

) -> HTTPValidationError | LiteLLMProjectTable | None:
    r""" Project Info

     Get information about a specific project

    Parameters:
    - project_id: *str* - The project id to fetch info for

    Example:
    ```bash
    curl --location 'http://0.0.0.0:4000/project/info?project_id=project-123' \
    --header 'Authorization: Bearer sk-1234'
    ```

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiteLLMProjectTable
     """


    return (await asyncio_detailed(
        client=client,
project_id=project_id,

    )).parsed
