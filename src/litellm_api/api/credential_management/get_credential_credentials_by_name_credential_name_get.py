from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.credential_item import CredentialItem
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    credential_name: str,
    *,
    model_id: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_model_id: None | str | Unset
    if isinstance(model_id, Unset):
        json_model_id = UNSET
    else:
        json_model_id = model_id
    params["model_id"] = json_model_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/credentials/by_name/{credential_name}".format(credential_name=quote(str(credential_name), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CredentialItem | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CredentialItem.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CredentialItem | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    credential_name: str,
    *,
    client: AuthenticatedClient,
    model_id: None | str | Unset = UNSET,

) -> Response[CredentialItem | HTTPValidationError]:
    """ Get Credential

     [BETA] endpoint. This might change unexpectedly.

    Args:
        credential_name (str): The credential name, percent-decoded; may contain slashes
        model_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialItem | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        credential_name=credential_name,
model_id=model_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    credential_name: str,
    *,
    client: AuthenticatedClient,
    model_id: None | str | Unset = UNSET,

) -> CredentialItem | HTTPValidationError | None:
    """ Get Credential

     [BETA] endpoint. This might change unexpectedly.

    Args:
        credential_name (str): The credential name, percent-decoded; may contain slashes
        model_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialItem | HTTPValidationError
     """


    return sync_detailed(
        credential_name=credential_name,
client=client,
model_id=model_id,

    ).parsed

async def asyncio_detailed(
    credential_name: str,
    *,
    client: AuthenticatedClient,
    model_id: None | str | Unset = UNSET,

) -> Response[CredentialItem | HTTPValidationError]:
    """ Get Credential

     [BETA] endpoint. This might change unexpectedly.

    Args:
        credential_name (str): The credential name, percent-decoded; may contain slashes
        model_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialItem | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        credential_name=credential_name,
model_id=model_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    credential_name: str,
    *,
    client: AuthenticatedClient,
    model_id: None | str | Unset = UNSET,

) -> CredentialItem | HTTPValidationError | None:
    """ Get Credential

     [BETA] endpoint. This might change unexpectedly.

    Args:
        credential_name (str): The credential name, percent-decoded; may contain slashes
        model_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialItem | HTTPValidationError
     """


    return (await asyncio_detailed(
        credential_name=credential_name,
client=client,
model_id=model_id,

    )).parsed
