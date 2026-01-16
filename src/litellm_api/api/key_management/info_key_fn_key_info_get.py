from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    key: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_key: None | str | Unset
    if isinstance(key, Unset):
        json_key = UNSET
    else:
        json_key = key
    params["key"] = json_key


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/key/info",
        "params": params,
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
    *,
    client: AuthenticatedClient,
    key: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Info Key Fn

     Retrieve information about a key.
    Parameters:
        key: Optional[str] = Query parameter representing the key in the request
        user_api_key_dict: UserAPIKeyAuth = Dependency representing the user's API key
    Returns:
        Dict containing the key and its associated information

    Example Curl:
    ```
    curl -X GET \"http://0.0.0.0:4000/key/info?key=sk-test-example-key-123\" -H \"Authorization: Bearer
    sk-1234\"
    ```

    Example Curl - if no key is passed, it will use the Key Passed in Authorization Header
    ```
    curl -X GET \"http://0.0.0.0:4000/key/info\" -H \"Authorization: Bearer sk-test-example-key-123\"
    ```

    Args:
        key (None | str | Unset): Key in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        key=key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    key: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Info Key Fn

     Retrieve information about a key.
    Parameters:
        key: Optional[str] = Query parameter representing the key in the request
        user_api_key_dict: UserAPIKeyAuth = Dependency representing the user's API key
    Returns:
        Dict containing the key and its associated information

    Example Curl:
    ```
    curl -X GET \"http://0.0.0.0:4000/key/info?key=sk-test-example-key-123\" -H \"Authorization: Bearer
    sk-1234\"
    ```

    Example Curl - if no key is passed, it will use the Key Passed in Authorization Header
    ```
    curl -X GET \"http://0.0.0.0:4000/key/info\" -H \"Authorization: Bearer sk-test-example-key-123\"
    ```

    Args:
        key (None | str | Unset): Key in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
key=key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    key: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Info Key Fn

     Retrieve information about a key.
    Parameters:
        key: Optional[str] = Query parameter representing the key in the request
        user_api_key_dict: UserAPIKeyAuth = Dependency representing the user's API key
    Returns:
        Dict containing the key and its associated information

    Example Curl:
    ```
    curl -X GET \"http://0.0.0.0:4000/key/info?key=sk-test-example-key-123\" -H \"Authorization: Bearer
    sk-1234\"
    ```

    Example Curl - if no key is passed, it will use the Key Passed in Authorization Header
    ```
    curl -X GET \"http://0.0.0.0:4000/key/info\" -H \"Authorization: Bearer sk-test-example-key-123\"
    ```

    Args:
        key (None | str | Unset): Key in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        key=key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    key: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Info Key Fn

     Retrieve information about a key.
    Parameters:
        key: Optional[str] = Query parameter representing the key in the request
        user_api_key_dict: UserAPIKeyAuth = Dependency representing the user's API key
    Returns:
        Dict containing the key and its associated information

    Example Curl:
    ```
    curl -X GET \"http://0.0.0.0:4000/key/info?key=sk-test-example-key-123\" -H \"Authorization: Bearer
    sk-1234\"
    ```

    Example Curl - if no key is passed, it will use the Key Passed in Authorization Header
    ```
    curl -X GET \"http://0.0.0.0:4000/key/info\" -H \"Authorization: Bearer sk-test-example-key-123\"
    ```

    Args:
        key (None | str | Unset): Key in the request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
key=key,

    )).parsed
