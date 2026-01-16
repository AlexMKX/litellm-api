from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.lite_llm_end_user_table import LiteLLMEndUserTable
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/customer/list",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[LiteLLMEndUserTable] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = LiteLLMEndUserTable.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[LiteLLMEndUserTable]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[list[LiteLLMEndUserTable]]:
    """ List End User

     [Admin-only] List all available customers

    Example curl:
    ```
    curl --location --request GET 'http://0.0.0.0:4000/customer/list'         --header 'Authorization:
    Bearer sk-1234'
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[LiteLLMEndUserTable]]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> list[LiteLLMEndUserTable] | None:
    """ List End User

     [Admin-only] List all available customers

    Example curl:
    ```
    curl --location --request GET 'http://0.0.0.0:4000/customer/list'         --header 'Authorization:
    Bearer sk-1234'
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[LiteLLMEndUserTable]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[list[LiteLLMEndUserTable]]:
    """ List End User

     [Admin-only] List all available customers

    Example curl:
    ```
    curl --location --request GET 'http://0.0.0.0:4000/customer/list'         --header 'Authorization:
    Bearer sk-1234'
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[LiteLLMEndUserTable]]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> list[LiteLLMEndUserTable] | None:
    """ List End User

     [Admin-only] List all available customers

    Example curl:
    ```
    curl --location --request GET 'http://0.0.0.0:4000/customer/list'         --header 'Authorization:
    Bearer sk-1234'
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[LiteLLMEndUserTable]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
