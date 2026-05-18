from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.policy_list_db_response import PolicyListDBResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    version_status: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_version_status: None | str | Unset
    if isinstance(version_status, Unset):
        json_version_status = UNSET
    else:
        json_version_status = version_status
    params["version_status"] = json_version_status


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/policies/list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | PolicyListDBResponse | None:
    if response.status_code == 200:
        response_200 = PolicyListDBResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | PolicyListDBResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    version_status: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | PolicyListDBResponse]:
    r""" List Policies

     List all policies from the database. Optionally filter by version_status.

    Query params:
    - version_status: Optional. One of \"draft\", \"published\", \"production\".
      If omitted, all versions are returned.

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/policies/list\" \
        -H \"Authorization: Bearer <your_api_key>\"
    curl -X GET \"http://localhost:4000/policies/list?version_status=production\" \
        -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"policies\": [
            {
                \"policy_id\": \"123e4567-e89b-12d3-a456-426614174000\",
                \"policy_name\": \"global-baseline\",
                \"version_number\": 1,
                \"version_status\": \"production\",
                \"inherit\": null,
                \"description\": \"Base guardrails for all requests\",
                \"guardrails_add\": [\"pii_masking\"],
                \"guardrails_remove\": [],
                \"condition\": null,
                \"created_at\": \"2024-01-01T00:00:00Z\",
                \"updated_at\": \"2024-01-01T00:00:00Z\"
            }
        ],
        \"total_count\": 1
    }
    ```

    Args:
        version_status (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyListDBResponse]
     """


    kwargs = _get_kwargs(
        version_status=version_status,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    version_status: None | str | Unset = UNSET,

) -> HTTPValidationError | PolicyListDBResponse | None:
    r""" List Policies

     List all policies from the database. Optionally filter by version_status.

    Query params:
    - version_status: Optional. One of \"draft\", \"published\", \"production\".
      If omitted, all versions are returned.

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/policies/list\" \
        -H \"Authorization: Bearer <your_api_key>\"
    curl -X GET \"http://localhost:4000/policies/list?version_status=production\" \
        -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"policies\": [
            {
                \"policy_id\": \"123e4567-e89b-12d3-a456-426614174000\",
                \"policy_name\": \"global-baseline\",
                \"version_number\": 1,
                \"version_status\": \"production\",
                \"inherit\": null,
                \"description\": \"Base guardrails for all requests\",
                \"guardrails_add\": [\"pii_masking\"],
                \"guardrails_remove\": [],
                \"condition\": null,
                \"created_at\": \"2024-01-01T00:00:00Z\",
                \"updated_at\": \"2024-01-01T00:00:00Z\"
            }
        ],
        \"total_count\": 1
    }
    ```

    Args:
        version_status (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyListDBResponse
     """


    return sync_detailed(
        client=client,
version_status=version_status,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    version_status: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | PolicyListDBResponse]:
    r""" List Policies

     List all policies from the database. Optionally filter by version_status.

    Query params:
    - version_status: Optional. One of \"draft\", \"published\", \"production\".
      If omitted, all versions are returned.

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/policies/list\" \
        -H \"Authorization: Bearer <your_api_key>\"
    curl -X GET \"http://localhost:4000/policies/list?version_status=production\" \
        -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"policies\": [
            {
                \"policy_id\": \"123e4567-e89b-12d3-a456-426614174000\",
                \"policy_name\": \"global-baseline\",
                \"version_number\": 1,
                \"version_status\": \"production\",
                \"inherit\": null,
                \"description\": \"Base guardrails for all requests\",
                \"guardrails_add\": [\"pii_masking\"],
                \"guardrails_remove\": [],
                \"condition\": null,
                \"created_at\": \"2024-01-01T00:00:00Z\",
                \"updated_at\": \"2024-01-01T00:00:00Z\"
            }
        ],
        \"total_count\": 1
    }
    ```

    Args:
        version_status (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PolicyListDBResponse]
     """


    kwargs = _get_kwargs(
        version_status=version_status,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    version_status: None | str | Unset = UNSET,

) -> HTTPValidationError | PolicyListDBResponse | None:
    r""" List Policies

     List all policies from the database. Optionally filter by version_status.

    Query params:
    - version_status: Optional. One of \"draft\", \"published\", \"production\".
      If omitted, all versions are returned.

    Example Request:
    ```bash
    curl -X GET \"http://localhost:4000/policies/list\" \
        -H \"Authorization: Bearer <your_api_key>\"
    curl -X GET \"http://localhost:4000/policies/list?version_status=production\" \
        -H \"Authorization: Bearer <your_api_key>\"
    ```

    Example Response:
    ```json
    {
        \"policies\": [
            {
                \"policy_id\": \"123e4567-e89b-12d3-a456-426614174000\",
                \"policy_name\": \"global-baseline\",
                \"version_number\": 1,
                \"version_status\": \"production\",
                \"inherit\": null,
                \"description\": \"Base guardrails for all requests\",
                \"guardrails_add\": [\"pii_masking\"],
                \"guardrails_remove\": [],
                \"condition\": null,
                \"created_at\": \"2024-01-01T00:00:00Z\",
                \"updated_at\": \"2024-01-01T00:00:00Z\"
            }
        ],
        \"total_count\": 1
    }
    ```

    Args:
        version_status (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PolicyListDBResponse
     """


    return (await asyncio_detailed(
        client=client,
version_status=version_status,

    )).parsed
