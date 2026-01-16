from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llm_end_user_table import LiteLLMEndUserTable
from typing import cast



def _get_kwargs(
    *,
    end_user_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["end_user_id"] = end_user_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/customer/info",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | LiteLLMEndUserTable | None:
    if response.status_code == 200:
        response_200 = LiteLLMEndUserTable.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | LiteLLMEndUserTable]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    end_user_id: str,

) -> Response[HTTPValidationError | LiteLLMEndUserTable]:
    """ End User Info

     Get information about an end-user. An `end_user` is a customer (external user) of the proxy.

    Parameters:
    - end_user_id (str, required): The unique identifier for the end-user

    Example curl:
    ```
    curl -X GET 'http://localhost:4000/customer/info?end_user_id=test-litellm-user-4'         -H
    'Authorization: Bearer sk-1234'
    ```

    Args:
        end_user_id (str): End User ID in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiteLLMEndUserTable]
     """


    kwargs = _get_kwargs(
        end_user_id=end_user_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    end_user_id: str,

) -> HTTPValidationError | LiteLLMEndUserTable | None:
    """ End User Info

     Get information about an end-user. An `end_user` is a customer (external user) of the proxy.

    Parameters:
    - end_user_id (str, required): The unique identifier for the end-user

    Example curl:
    ```
    curl -X GET 'http://localhost:4000/customer/info?end_user_id=test-litellm-user-4'         -H
    'Authorization: Bearer sk-1234'
    ```

    Args:
        end_user_id (str): End User ID in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiteLLMEndUserTable
     """


    return sync_detailed(
        client=client,
end_user_id=end_user_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    end_user_id: str,

) -> Response[HTTPValidationError | LiteLLMEndUserTable]:
    """ End User Info

     Get information about an end-user. An `end_user` is a customer (external user) of the proxy.

    Parameters:
    - end_user_id (str, required): The unique identifier for the end-user

    Example curl:
    ```
    curl -X GET 'http://localhost:4000/customer/info?end_user_id=test-litellm-user-4'         -H
    'Authorization: Bearer sk-1234'
    ```

    Args:
        end_user_id (str): End User ID in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiteLLMEndUserTable]
     """


    kwargs = _get_kwargs(
        end_user_id=end_user_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    end_user_id: str,

) -> HTTPValidationError | LiteLLMEndUserTable | None:
    """ End User Info

     Get information about an end-user. An `end_user` is a customer (external user) of the proxy.

    Parameters:
    - end_user_id (str, required): The unique identifier for the end-user

    Example curl:
    ```
    curl -X GET 'http://localhost:4000/customer/info?end_user_id=test-litellm-user-4'         -H
    'Authorization: Bearer sk-1234'
    ```

    Args:
        end_user_id (str): End User ID in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiteLLMEndUserTable
     """


    return (await asyncio_detailed(
        client=client,
end_user_id=end_user_id,

    )).parsed
