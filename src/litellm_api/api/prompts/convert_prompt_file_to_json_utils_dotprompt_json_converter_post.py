from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.body_convert_prompt_file_to_json_utils_dotprompt_json_converter_post import BodyConvertPromptFileToJsonUtilsDotpromptJsonConverterPost
from ...models.convert_prompt_file_to_json_utils_dotprompt_json_converter_post_response_convert_prompt_file_to_json_utils_dotprompt_json_converter_post import ConvertPromptFileToJsonUtilsDotpromptJsonConverterPostResponseConvertPromptFileToJsonUtilsDotpromptJsonConverterPost
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    *,
    body: BodyConvertPromptFileToJsonUtilsDotpromptJsonConverterPost,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/utils/dotprompt_json_converter",
    }

    _kwargs["files"] = body.to_multipart()



    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConvertPromptFileToJsonUtilsDotpromptJsonConverterPostResponseConvertPromptFileToJsonUtilsDotpromptJsonConverterPost | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ConvertPromptFileToJsonUtilsDotpromptJsonConverterPostResponseConvertPromptFileToJsonUtilsDotpromptJsonConverterPost.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConvertPromptFileToJsonUtilsDotpromptJsonConverterPostResponseConvertPromptFileToJsonUtilsDotpromptJsonConverterPost | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyConvertPromptFileToJsonUtilsDotpromptJsonConverterPost,

) -> Response[ConvertPromptFileToJsonUtilsDotpromptJsonConverterPostResponseConvertPromptFileToJsonUtilsDotpromptJsonConverterPost | HTTPValidationError]:
    """ Convert Prompt File To Json

     Convert a .prompt file to JSON format.

    This endpoint accepts a .prompt file upload and returns the equivalent JSON representation
    that can be stored in a database or used programmatically.

    Returns the JSON structure with 'content' and 'metadata' fields.

    Args:
        body (BodyConvertPromptFileToJsonUtilsDotpromptJsonConverterPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConvertPromptFileToJsonUtilsDotpromptJsonConverterPostResponseConvertPromptFileToJsonUtilsDotpromptJsonConverterPost | HTTPValidationError]
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
    body: BodyConvertPromptFileToJsonUtilsDotpromptJsonConverterPost,

) -> ConvertPromptFileToJsonUtilsDotpromptJsonConverterPostResponseConvertPromptFileToJsonUtilsDotpromptJsonConverterPost | HTTPValidationError | None:
    """ Convert Prompt File To Json

     Convert a .prompt file to JSON format.

    This endpoint accepts a .prompt file upload and returns the equivalent JSON representation
    that can be stored in a database or used programmatically.

    Returns the JSON structure with 'content' and 'metadata' fields.

    Args:
        body (BodyConvertPromptFileToJsonUtilsDotpromptJsonConverterPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConvertPromptFileToJsonUtilsDotpromptJsonConverterPostResponseConvertPromptFileToJsonUtilsDotpromptJsonConverterPost | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyConvertPromptFileToJsonUtilsDotpromptJsonConverterPost,

) -> Response[ConvertPromptFileToJsonUtilsDotpromptJsonConverterPostResponseConvertPromptFileToJsonUtilsDotpromptJsonConverterPost | HTTPValidationError]:
    """ Convert Prompt File To Json

     Convert a .prompt file to JSON format.

    This endpoint accepts a .prompt file upload and returns the equivalent JSON representation
    that can be stored in a database or used programmatically.

    Returns the JSON structure with 'content' and 'metadata' fields.

    Args:
        body (BodyConvertPromptFileToJsonUtilsDotpromptJsonConverterPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConvertPromptFileToJsonUtilsDotpromptJsonConverterPostResponseConvertPromptFileToJsonUtilsDotpromptJsonConverterPost | HTTPValidationError]
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
    body: BodyConvertPromptFileToJsonUtilsDotpromptJsonConverterPost,

) -> ConvertPromptFileToJsonUtilsDotpromptJsonConverterPostResponseConvertPromptFileToJsonUtilsDotpromptJsonConverterPost | HTTPValidationError | None:
    """ Convert Prompt File To Json

     Convert a .prompt file to JSON format.

    This endpoint accepts a .prompt file upload and returns the equivalent JSON representation
    that can be stored in a database or used programmatically.

    Returns the JSON structure with 'content' and 'metadata' fields.

    Args:
        body (BodyConvertPromptFileToJsonUtilsDotpromptJsonConverterPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConvertPromptFileToJsonUtilsDotpromptJsonConverterPostResponseConvertPromptFileToJsonUtilsDotpromptJsonConverterPost | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
