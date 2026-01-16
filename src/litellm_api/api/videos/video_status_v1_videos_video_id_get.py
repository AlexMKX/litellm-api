from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    video_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/videos/{video_id}".format(video_id=quote(str(video_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    video_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | HTTPValidationError]:
    r""" Video Status

     Video status endpoint for retrieving video status and metadata.

    Follows the OpenAI Videos API spec:
    https://platform.openai.com/docs/api-reference/videos

    Example:
    ```bash
    curl -X GET \"http://localhost:4000/v1/videos/video_123\"         -H \"Authorization: Bearer
    sk-1234\"
    ```

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        video_id=video_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    video_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | HTTPValidationError | None:
    r""" Video Status

     Video status endpoint for retrieving video status and metadata.

    Follows the OpenAI Videos API spec:
    https://platform.openai.com/docs/api-reference/videos

    Example:
    ```bash
    curl -X GET \"http://localhost:4000/v1/videos/video_123\"         -H \"Authorization: Bearer
    sk-1234\"
    ```

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        video_id=video_id,
client=client,

    ).parsed

async def asyncio_detailed(
    video_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | HTTPValidationError]:
    r""" Video Status

     Video status endpoint for retrieving video status and metadata.

    Follows the OpenAI Videos API spec:
    https://platform.openai.com/docs/api-reference/videos

    Example:
    ```bash
    curl -X GET \"http://localhost:4000/v1/videos/video_123\"         -H \"Authorization: Bearer
    sk-1234\"
    ```

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        video_id=video_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    video_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | HTTPValidationError | None:
    r""" Video Status

     Video status endpoint for retrieving video status and metadata.

    Follows the OpenAI Videos API spec:
    https://platform.openai.com/docs/api-reference/videos

    Example:
    ```bash
    curl -X GET \"http://localhost:4000/v1/videos/video_123\"         -H \"Authorization: Bearer
    sk-1234\"
    ```

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        video_id=video_id,
client=client,

    )).parsed
