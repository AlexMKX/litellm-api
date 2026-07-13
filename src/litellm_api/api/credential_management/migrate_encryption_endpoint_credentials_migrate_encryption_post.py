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
    dry_run: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["dry_run"] = dry_run


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/credentials/migrate-encryption",
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
    dry_run: bool | Unset = False,

) -> Response[Any | HTTPValidationError]:
    """ Migrate Encryption Endpoint

     Re-encrypt all at-rest credentials into the AES-256-GCM (``v2:gcm:``) format.

    Admin only. Requires ``general_settings.encryption_algorithm: aes-256-gcm``.
    Idempotent and resumable — re-running skips already-migrated values. Pass
    ``dry_run=true`` for a non-mutating scan (equivalent to ``--check``).

    Args:
        dry_run (bool | Unset): If true, scan and report without writing any changes. Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        dry_run=dry_run,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    dry_run: bool | Unset = False,

) -> Any | HTTPValidationError | None:
    """ Migrate Encryption Endpoint

     Re-encrypt all at-rest credentials into the AES-256-GCM (``v2:gcm:``) format.

    Admin only. Requires ``general_settings.encryption_algorithm: aes-256-gcm``.
    Idempotent and resumable — re-running skips already-migrated values. Pass
    ``dry_run=true`` for a non-mutating scan (equivalent to ``--check``).

    Args:
        dry_run (bool | Unset): If true, scan and report without writing any changes. Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
dry_run=dry_run,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    dry_run: bool | Unset = False,

) -> Response[Any | HTTPValidationError]:
    """ Migrate Encryption Endpoint

     Re-encrypt all at-rest credentials into the AES-256-GCM (``v2:gcm:``) format.

    Admin only. Requires ``general_settings.encryption_algorithm: aes-256-gcm``.
    Idempotent and resumable — re-running skips already-migrated values. Pass
    ``dry_run=true`` for a non-mutating scan (equivalent to ``--check``).

    Args:
        dry_run (bool | Unset): If true, scan and report without writing any changes. Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        dry_run=dry_run,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    dry_run: bool | Unset = False,

) -> Any | HTTPValidationError | None:
    """ Migrate Encryption Endpoint

     Re-encrypt all at-rest credentials into the AES-256-GCM (``v2:gcm:``) format.

    Admin only. Requires ``general_settings.encryption_algorithm: aes-256-gcm``.
    Idempotent and resumable — re-running skips already-migrated values. Pass
    ``dry_run=true`` for a non-mutating scan (equivalent to ``--check``).

    Args:
        dry_run (bool | Unset): If true, scan and report without writing any changes. Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
dry_run=dry_run,

    )).parsed
