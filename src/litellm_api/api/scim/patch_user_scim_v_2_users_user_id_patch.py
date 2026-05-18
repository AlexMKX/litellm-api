from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.scim_patch_op import SCIMPatchOp
from ...models.scim_user import SCIMUser
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    user_id: str,
    *,
    body: SCIMPatchOp,
    feature: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_feature: None | str | Unset
    if isinstance(feature, Unset):
        json_feature = UNSET
    else:
        json_feature = feature
    params["feature"] = json_feature


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/scim/v2/Users/{user_id}".format(user_id=quote(str(user_id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | SCIMUser | None:
    if response.status_code == 200:
        response_200 = SCIMUser.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | SCIMUser]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: SCIMPatchOp,
    feature: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | SCIMUser]:
    """ Patch User

     Patch a user according to SCIM v2 protocol

    Args:
        user_id (str):
        feature (None | str | Unset):
        body (SCIMPatchOp):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SCIMUser]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
body=body,
feature=feature,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: SCIMPatchOp,
    feature: None | str | Unset = UNSET,

) -> HTTPValidationError | SCIMUser | None:
    """ Patch User

     Patch a user according to SCIM v2 protocol

    Args:
        user_id (str):
        feature (None | str | Unset):
        body (SCIMPatchOp):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SCIMUser
     """


    return sync_detailed(
        user_id=user_id,
client=client,
body=body,
feature=feature,

    ).parsed

async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: SCIMPatchOp,
    feature: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | SCIMUser]:
    """ Patch User

     Patch a user according to SCIM v2 protocol

    Args:
        user_id (str):
        feature (None | str | Unset):
        body (SCIMPatchOp):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SCIMUser]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
body=body,
feature=feature,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: SCIMPatchOp,
    feature: None | str | Unset = UNSET,

) -> HTTPValidationError | SCIMUser | None:
    """ Patch User

     Patch a user according to SCIM v2 protocol

    Args:
        user_id (str):
        feature (None | str | Unset):
        body (SCIMPatchOp):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SCIMUser
     """


    return (await asyncio_detailed(
        user_id=user_id,
client=client,
body=body,
feature=feature,

    )).parsed
