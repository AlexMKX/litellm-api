from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.token_count_details_response import TokenCountDetailsResponse
from typing import cast



def _get_kwargs(
    model_name: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1beta/models/{model_name}:countTokens".format(model_name=quote(str(model_name), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | TokenCountDetailsResponse | None:
    if response.status_code == 200:
        response_200 = TokenCountDetailsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | TokenCountDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_name: str,
    *,
    client: AuthenticatedClient,

) -> Response[HTTPValidationError | TokenCountDetailsResponse]:
    r""" Google Count Tokens

     ```json
    return {
        \"totalTokens\": 31,
        \"totalBillableCharacters\": 96,
        \"promptTokensDetails\": [
            {
            \"modality\": \"TEXT\",
            \"tokenCount\": 31
            }
        ]
    }
    ```

    Args:
        model_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TokenCountDetailsResponse]
     """


    kwargs = _get_kwargs(
        model_name=model_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    model_name: str,
    *,
    client: AuthenticatedClient,

) -> HTTPValidationError | TokenCountDetailsResponse | None:
    r""" Google Count Tokens

     ```json
    return {
        \"totalTokens\": 31,
        \"totalBillableCharacters\": 96,
        \"promptTokensDetails\": [
            {
            \"modality\": \"TEXT\",
            \"tokenCount\": 31
            }
        ]
    }
    ```

    Args:
        model_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TokenCountDetailsResponse
     """


    return sync_detailed(
        model_name=model_name,
client=client,

    ).parsed

async def asyncio_detailed(
    model_name: str,
    *,
    client: AuthenticatedClient,

) -> Response[HTTPValidationError | TokenCountDetailsResponse]:
    r""" Google Count Tokens

     ```json
    return {
        \"totalTokens\": 31,
        \"totalBillableCharacters\": 96,
        \"promptTokensDetails\": [
            {
            \"modality\": \"TEXT\",
            \"tokenCount\": 31
            }
        ]
    }
    ```

    Args:
        model_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TokenCountDetailsResponse]
     """


    kwargs = _get_kwargs(
        model_name=model_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    model_name: str,
    *,
    client: AuthenticatedClient,

) -> HTTPValidationError | TokenCountDetailsResponse | None:
    r""" Google Count Tokens

     ```json
    return {
        \"totalTokens\": 31,
        \"totalBillableCharacters\": 96,
        \"promptTokensDetails\": [
            {
            \"modality\": \"TEXT\",
            \"tokenCount\": 31
            }
        ]
    }
    ```

    Args:
        model_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TokenCountDetailsResponse
     """


    return (await asyncio_detailed(
        model_name=model_name,
client=client,

    )).parsed
