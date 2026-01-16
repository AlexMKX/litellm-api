from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.body_video_generation_videos_post import BodyVideoGenerationVideosPost
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: BodyVideoGenerationVideosPost | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/videos",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()



    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient,
    body: BodyVideoGenerationVideosPost | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Video Generation

     Video generation endpoint for creating videos from text prompts.

    Follows the OpenAI Videos API spec:
    https://platform.openai.com/docs/api-reference/videos

    Example:
    ```bash
    curl -X POST \"http://localhost:4000/v1/videos\"         -H \"Authorization: Bearer sk-1234\"
    -H \"Content-Type: application/json\"         -d '{
            \"model\": \"sora-2\",
            \"prompt\": \"A beautiful sunset over the ocean\"
        }'
    ```

    Args:
        body (BodyVideoGenerationVideosPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: BodyVideoGenerationVideosPost | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Video Generation

     Video generation endpoint for creating videos from text prompts.

    Follows the OpenAI Videos API spec:
    https://platform.openai.com/docs/api-reference/videos

    Example:
    ```bash
    curl -X POST \"http://localhost:4000/v1/videos\"         -H \"Authorization: Bearer sk-1234\"
    -H \"Content-Type: application/json\"         -d '{
            \"model\": \"sora-2\",
            \"prompt\": \"A beautiful sunset over the ocean\"
        }'
    ```

    Args:
        body (BodyVideoGenerationVideosPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyVideoGenerationVideosPost | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Video Generation

     Video generation endpoint for creating videos from text prompts.

    Follows the OpenAI Videos API spec:
    https://platform.openai.com/docs/api-reference/videos

    Example:
    ```bash
    curl -X POST \"http://localhost:4000/v1/videos\"         -H \"Authorization: Bearer sk-1234\"
    -H \"Content-Type: application/json\"         -d '{
            \"model\": \"sora-2\",
            \"prompt\": \"A beautiful sunset over the ocean\"
        }'
    ```

    Args:
        body (BodyVideoGenerationVideosPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: BodyVideoGenerationVideosPost | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Video Generation

     Video generation endpoint for creating videos from text prompts.

    Follows the OpenAI Videos API spec:
    https://platform.openai.com/docs/api-reference/videos

    Example:
    ```bash
    curl -X POST \"http://localhost:4000/v1/videos\"         -H \"Authorization: Bearer sk-1234\"
    -H \"Content-Type: application/json\"         -d '{
            \"model\": \"sora-2\",
            \"prompt\": \"A beautiful sunset over the ocean\"
        }'
    ```

    Args:
        body (BodyVideoGenerationVideosPost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
