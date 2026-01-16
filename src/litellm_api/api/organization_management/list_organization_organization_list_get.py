from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llm_organization_table_with_members import LiteLLMOrganizationTableWithMembers
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    org_id: None | str | Unset = UNSET,
    org_alias: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_org_id: None | str | Unset
    if isinstance(org_id, Unset):
        json_org_id = UNSET
    else:
        json_org_id = org_id
    params["org_id"] = json_org_id

    json_org_alias: None | str | Unset
    if isinstance(org_alias, Unset):
        json_org_alias = UNSET
    else:
        json_org_alias = org_alias
    params["org_alias"] = json_org_alias


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/organization/list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | list[LiteLLMOrganizationTableWithMembers] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = LiteLLMOrganizationTableWithMembers.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | list[LiteLLMOrganizationTableWithMembers]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    org_id: None | str | Unset = UNSET,
    org_alias: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | list[LiteLLMOrganizationTableWithMembers]]:
    """ List Organization

     Get a list of organizations with optional filtering.

    Parameters:
        org_id: Optional[str]
            Filter organizations by exact organization_id match
        org_alias: Optional[str]
            Filter organizations by partial organization_alias match (case-insensitive)

    Example:
    ```
    curl --location --request GET 'http://0.0.0.0:4000/organization/list?org_alias=my-org'
    --header 'Authorization: Bearer sk-1234'
    ```

    Example with org_id:
    ```
    curl --location --request GET
    'http://0.0.0.0:4000/organization/list?org_id=123e4567-e89b-12d3-a456-426614174000'         --header
    'Authorization: Bearer sk-1234'
    ```

    Args:
        org_id (None | str | Unset): Filter organizations by exact organization_id match
        org_alias (None | str | Unset): Filter organizations by partial organization_alias match.
            Supports case-insensitive search.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LiteLLMOrganizationTableWithMembers]]
     """


    kwargs = _get_kwargs(
        org_id=org_id,
org_alias=org_alias,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    org_id: None | str | Unset = UNSET,
    org_alias: None | str | Unset = UNSET,

) -> HTTPValidationError | list[LiteLLMOrganizationTableWithMembers] | None:
    """ List Organization

     Get a list of organizations with optional filtering.

    Parameters:
        org_id: Optional[str]
            Filter organizations by exact organization_id match
        org_alias: Optional[str]
            Filter organizations by partial organization_alias match (case-insensitive)

    Example:
    ```
    curl --location --request GET 'http://0.0.0.0:4000/organization/list?org_alias=my-org'
    --header 'Authorization: Bearer sk-1234'
    ```

    Example with org_id:
    ```
    curl --location --request GET
    'http://0.0.0.0:4000/organization/list?org_id=123e4567-e89b-12d3-a456-426614174000'         --header
    'Authorization: Bearer sk-1234'
    ```

    Args:
        org_id (None | str | Unset): Filter organizations by exact organization_id match
        org_alias (None | str | Unset): Filter organizations by partial organization_alias match.
            Supports case-insensitive search.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LiteLLMOrganizationTableWithMembers]
     """


    return sync_detailed(
        client=client,
org_id=org_id,
org_alias=org_alias,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    org_id: None | str | Unset = UNSET,
    org_alias: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | list[LiteLLMOrganizationTableWithMembers]]:
    """ List Organization

     Get a list of organizations with optional filtering.

    Parameters:
        org_id: Optional[str]
            Filter organizations by exact organization_id match
        org_alias: Optional[str]
            Filter organizations by partial organization_alias match (case-insensitive)

    Example:
    ```
    curl --location --request GET 'http://0.0.0.0:4000/organization/list?org_alias=my-org'
    --header 'Authorization: Bearer sk-1234'
    ```

    Example with org_id:
    ```
    curl --location --request GET
    'http://0.0.0.0:4000/organization/list?org_id=123e4567-e89b-12d3-a456-426614174000'         --header
    'Authorization: Bearer sk-1234'
    ```

    Args:
        org_id (None | str | Unset): Filter organizations by exact organization_id match
        org_alias (None | str | Unset): Filter organizations by partial organization_alias match.
            Supports case-insensitive search.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LiteLLMOrganizationTableWithMembers]]
     """


    kwargs = _get_kwargs(
        org_id=org_id,
org_alias=org_alias,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    org_id: None | str | Unset = UNSET,
    org_alias: None | str | Unset = UNSET,

) -> HTTPValidationError | list[LiteLLMOrganizationTableWithMembers] | None:
    """ List Organization

     Get a list of organizations with optional filtering.

    Parameters:
        org_id: Optional[str]
            Filter organizations by exact organization_id match
        org_alias: Optional[str]
            Filter organizations by partial organization_alias match (case-insensitive)

    Example:
    ```
    curl --location --request GET 'http://0.0.0.0:4000/organization/list?org_alias=my-org'
    --header 'Authorization: Bearer sk-1234'
    ```

    Example with org_id:
    ```
    curl --location --request GET
    'http://0.0.0.0:4000/organization/list?org_id=123e4567-e89b-12d3-a456-426614174000'         --header
    'Authorization: Bearer sk-1234'
    ```

    Args:
        org_id (None | str | Unset): Filter organizations by exact organization_id match
        org_alias (None | str | Unset): Filter organizations by partial organization_alias match.
            Supports case-insensitive search.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LiteLLMOrganizationTableWithMembers]
     """


    return (await asyncio_detailed(
        client=client,
org_id=org_id,
org_alias=org_alias,

    )).parsed
