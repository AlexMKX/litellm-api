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
    attachment_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/policies/attachments/{attachment_id}".format(attachment_id=quote(str(attachment_id), safe=""),),
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
    attachment_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | HTTPValidationError]:
    r""" Delete Policy Attachment

     Delete a policy attachment.

    Example Request:
    ```bash
    curl -X DELETE \"http://localhost:4000/policies/attachments/123e4567-e89b-12d3-a456-426614174000\" \
        -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"message\": \"Attachment 123e4567-e89b-12d3-a456-426614174000 deleted successfully\"
    }
    ```

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        attachment_id=attachment_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    attachment_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | HTTPValidationError | None:
    r""" Delete Policy Attachment

     Delete a policy attachment.

    Example Request:
    ```bash
    curl -X DELETE \"http://localhost:4000/policies/attachments/123e4567-e89b-12d3-a456-426614174000\" \
        -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"message\": \"Attachment 123e4567-e89b-12d3-a456-426614174000 deleted successfully\"
    }
    ```

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        attachment_id=attachment_id,
client=client,

    ).parsed

async def asyncio_detailed(
    attachment_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | HTTPValidationError]:
    r""" Delete Policy Attachment

     Delete a policy attachment.

    Example Request:
    ```bash
    curl -X DELETE \"http://localhost:4000/policies/attachments/123e4567-e89b-12d3-a456-426614174000\" \
        -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"message\": \"Attachment 123e4567-e89b-12d3-a456-426614174000 deleted successfully\"
    }
    ```

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        attachment_id=attachment_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    attachment_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | HTTPValidationError | None:
    r""" Delete Policy Attachment

     Delete a policy attachment.

    Example Request:
    ```bash
    curl -X DELETE \"http://localhost:4000/policies/attachments/123e4567-e89b-12d3-a456-426614174000\" \
        -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"message\": \"Attachment 123e4567-e89b-12d3-a456-426614174000 deleted successfully\"
    }
    ```

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        attachment_id=attachment_id,
client=client,

    )).parsed
