from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.update_customer_request import UpdateCustomerRequest
from typing import cast



def _get_kwargs(
    *,
    body: UpdateCustomerRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/customer/update",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: UpdateCustomerRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Update End User

     Example curl

    Parameters:
    - user_id: str
    - alias: Optional[str] = None  # human-friendly alias
    - blocked: bool = False  # allow/disallow requests for this end-user
    - max_budget: Optional[float] = None
    - budget_id: Optional[str] = None  # give either a budget_id or max_budget
    - allowed_model_region: Optional[AllowedModelRegion] = (
        None  # require all user requests to use models in this specific region
    )
    - default_model: Optional[str] = (
        None  # if no equivalent model in allowed region - default all requests to this model
    )

    Example curl:
    ```
    curl --location 'http://0.0.0.0:4000/customer/update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"user_id\": \"test-litellm-user-4\",
        \"budget_id\": \"paid_tier\"
    }'

    See below for all params
    ```

    Args:
        body (UpdateCustomerRequest): Update a Customer, use this to update customer budgets etc

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: UpdateCustomerRequest,

) -> Any | HTTPValidationError | None:
    r""" Update End User

     Example curl

    Parameters:
    - user_id: str
    - alias: Optional[str] = None  # human-friendly alias
    - blocked: bool = False  # allow/disallow requests for this end-user
    - max_budget: Optional[float] = None
    - budget_id: Optional[str] = None  # give either a budget_id or max_budget
    - allowed_model_region: Optional[AllowedModelRegion] = (
        None  # require all user requests to use models in this specific region
    )
    - default_model: Optional[str] = (
        None  # if no equivalent model in allowed region - default all requests to this model
    )

    Example curl:
    ```
    curl --location 'http://0.0.0.0:4000/customer/update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"user_id\": \"test-litellm-user-4\",
        \"budget_id\": \"paid_tier\"
    }'

    See below for all params
    ```

    Args:
        body (UpdateCustomerRequest): Update a Customer, use this to update customer budgets etc

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateCustomerRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Update End User

     Example curl

    Parameters:
    - user_id: str
    - alias: Optional[str] = None  # human-friendly alias
    - blocked: bool = False  # allow/disallow requests for this end-user
    - max_budget: Optional[float] = None
    - budget_id: Optional[str] = None  # give either a budget_id or max_budget
    - allowed_model_region: Optional[AllowedModelRegion] = (
        None  # require all user requests to use models in this specific region
    )
    - default_model: Optional[str] = (
        None  # if no equivalent model in allowed region - default all requests to this model
    )

    Example curl:
    ```
    curl --location 'http://0.0.0.0:4000/customer/update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"user_id\": \"test-litellm-user-4\",
        \"budget_id\": \"paid_tier\"
    }'

    See below for all params
    ```

    Args:
        body (UpdateCustomerRequest): Update a Customer, use this to update customer budgets etc

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpdateCustomerRequest,

) -> Any | HTTPValidationError | None:
    r""" Update End User

     Example curl

    Parameters:
    - user_id: str
    - alias: Optional[str] = None  # human-friendly alias
    - blocked: bool = False  # allow/disallow requests for this end-user
    - max_budget: Optional[float] = None
    - budget_id: Optional[str] = None  # give either a budget_id or max_budget
    - allowed_model_region: Optional[AllowedModelRegion] = (
        None  # require all user requests to use models in this specific region
    )
    - default_model: Optional[str] = (
        None  # if no equivalent model in allowed region - default all requests to this model
    )

    Example curl:
    ```
    curl --location 'http://0.0.0.0:4000/customer/update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
        \"user_id\": \"test-litellm-user-4\",
        \"budget_id\": \"paid_tier\"
    }'

    See below for all params
    ```

    Args:
        body (UpdateCustomerRequest): Update a Customer, use this to update customer budgets etc

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
