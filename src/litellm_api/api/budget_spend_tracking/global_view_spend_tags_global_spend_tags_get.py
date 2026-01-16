from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llm_spend_logs import LiteLLMSpendLogs
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    tags: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_start_date: None | str | Unset
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: None | str | Unset
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date

    json_tags: None | str | Unset
    if isinstance(tags, Unset):
        json_tags = UNSET
    else:
        json_tags = tags
    params["tags"] = json_tags


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/global/spend/tags",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | list[LiteLLMSpendLogs] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = LiteLLMSpendLogs.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | list[LiteLLMSpendLogs]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    tags: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | list[LiteLLMSpendLogs]]:
    r""" Global View Spend Tags

     LiteLLM Enterprise - View Spend Per Request Tag. Used by LiteLLM UI

    Example Request:
    ```
    curl -X GET \"http://0.0.0.0:4000/spend/tags\" -H \"Authorization: Bearer sk-1234\"
    ```

    Spend with Start Date and End Date
    ```
    curl -X GET \"http://0.0.0.0:4000/spend/tags?start_date=2022-01-01&end_date=2022-02-01\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Args:
        start_date (None | str | Unset): Time from which to start viewing key spend
        end_date (None | str | Unset): Time till which to view key spend
        tags (None | str | Unset): comman separated tags to filter on

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LiteLLMSpendLogs]]
     """


    kwargs = _get_kwargs(
        start_date=start_date,
end_date=end_date,
tags=tags,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    tags: None | str | Unset = UNSET,

) -> HTTPValidationError | list[LiteLLMSpendLogs] | None:
    r""" Global View Spend Tags

     LiteLLM Enterprise - View Spend Per Request Tag. Used by LiteLLM UI

    Example Request:
    ```
    curl -X GET \"http://0.0.0.0:4000/spend/tags\" -H \"Authorization: Bearer sk-1234\"
    ```

    Spend with Start Date and End Date
    ```
    curl -X GET \"http://0.0.0.0:4000/spend/tags?start_date=2022-01-01&end_date=2022-02-01\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Args:
        start_date (None | str | Unset): Time from which to start viewing key spend
        end_date (None | str | Unset): Time till which to view key spend
        tags (None | str | Unset): comman separated tags to filter on

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LiteLLMSpendLogs]
     """


    return sync_detailed(
        client=client,
start_date=start_date,
end_date=end_date,
tags=tags,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    tags: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | list[LiteLLMSpendLogs]]:
    r""" Global View Spend Tags

     LiteLLM Enterprise - View Spend Per Request Tag. Used by LiteLLM UI

    Example Request:
    ```
    curl -X GET \"http://0.0.0.0:4000/spend/tags\" -H \"Authorization: Bearer sk-1234\"
    ```

    Spend with Start Date and End Date
    ```
    curl -X GET \"http://0.0.0.0:4000/spend/tags?start_date=2022-01-01&end_date=2022-02-01\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Args:
        start_date (None | str | Unset): Time from which to start viewing key spend
        end_date (None | str | Unset): Time till which to view key spend
        tags (None | str | Unset): comman separated tags to filter on

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LiteLLMSpendLogs]]
     """


    kwargs = _get_kwargs(
        start_date=start_date,
end_date=end_date,
tags=tags,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    tags: None | str | Unset = UNSET,

) -> HTTPValidationError | list[LiteLLMSpendLogs] | None:
    r""" Global View Spend Tags

     LiteLLM Enterprise - View Spend Per Request Tag. Used by LiteLLM UI

    Example Request:
    ```
    curl -X GET \"http://0.0.0.0:4000/spend/tags\" -H \"Authorization: Bearer sk-1234\"
    ```

    Spend with Start Date and End Date
    ```
    curl -X GET \"http://0.0.0.0:4000/spend/tags?start_date=2022-01-01&end_date=2022-02-01\" -H
    \"Authorization: Bearer sk-1234\"
    ```

    Args:
        start_date (None | str | Unset): Time from which to start viewing key spend
        end_date (None | str | Unset): Time till which to view key spend
        tags (None | str | Unset): comman separated tags to filter on

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LiteLLMSpendLogs]
     """


    return (await asyncio_detailed(
        client=client,
start_date=start_date,
end_date=end_date,
tags=tags,

    )).parsed
