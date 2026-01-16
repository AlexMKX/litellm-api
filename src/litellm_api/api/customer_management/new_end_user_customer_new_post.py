from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.new_customer_request import NewCustomerRequest
from typing import cast



def _get_kwargs(
    *,
    body: NewCustomerRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/customer/new",
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
    body: NewCustomerRequest,

) -> Response[Any | HTTPValidationError]:
    r""" New End User

     Allow creating a new Customer


    Parameters:
    - user_id: str - The unique identifier for the user.
    - alias: Optional[str] - A human-friendly alias for the user.
    - blocked: bool - Flag to allow or disallow requests for this end-user. Default is False.
    - max_budget: Optional[float] - The maximum budget allocated to the user. Either 'max_budget' or
    'budget_id' should be provided, not both.
    - budget_id: Optional[str] - The identifier for an existing budget allocated to the user. Either
    'max_budget' or 'budget_id' should be provided, not both.
    - allowed_model_region: Optional[Union[Literal[\"eu\"], Literal[\"us\"]]] - Require all user
    requests to use models in this specific region.
    - default_model: Optional[str] - If no equivalent model in the allowed region, default all requests
    to this model.
    - metadata: Optional[dict] = Metadata for customer, store information for customer. Example metadata
    = {\"data_training_opt_out\": True}
    - budget_duration: Optional[str] - Budget is reset at the end of specified duration. If not set,
    budget is never reset. You can set duration as seconds (\"30s\"), minutes (\"30m\"), hours
    (\"30h\"), days (\"30d\").
    - tpm_limit: Optional[int] - [Not Implemented Yet] Specify tpm limit for a given customer (Tokens
    per minute)
    - rpm_limit: Optional[int] - [Not Implemented Yet] Specify rpm limit for a given customer (Requests
    per minute)
    - model_max_budget: Optional[dict] - [Not Implemented Yet] Specify max budget for a given model.
    Example: {\"openai/gpt-4o-mini\": {\"max_budget\": 100.0, \"budget_duration\": \"1d\"}}
    - max_parallel_requests: Optional[int] - [Not Implemented Yet] Specify max parallel requests for a
    given customer.
    - soft_budget: Optional[float] - [Not Implemented Yet] Get alerts when customer crosses given
    budget, doesn't block requests.
    - spend: Optional[float] - Specify initial spend for a given customer.
    - budget_reset_at: Optional[str] - Specify the date and time when the budget should be reset.


    - Allow specifying allowed regions
    - Allow specifying default model

    Example curl:
    ```
    curl --location 'http://0.0.0.0:4000/customer/new'         --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'         --data '{
            \"user_id\" : \"ishaan-jaff-3\",
            \"allowed_region\": \"eu\",
            \"budget_id\": \"free_tier\",
            \"default_model\": \"azure/gpt-3.5-turbo-eu\" <- all calls from this user, use this model?
        }'

        # return end-user object
    ```

    NOTE: This used to be called `/end_user/new`, we will still be maintaining compatibility for
    /end_user/XXX for these endpoints

    Args:
        body (NewCustomerRequest): Create a new customer, allocate a budget to them

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
    body: NewCustomerRequest,

) -> Any | HTTPValidationError | None:
    r""" New End User

     Allow creating a new Customer


    Parameters:
    - user_id: str - The unique identifier for the user.
    - alias: Optional[str] - A human-friendly alias for the user.
    - blocked: bool - Flag to allow or disallow requests for this end-user. Default is False.
    - max_budget: Optional[float] - The maximum budget allocated to the user. Either 'max_budget' or
    'budget_id' should be provided, not both.
    - budget_id: Optional[str] - The identifier for an existing budget allocated to the user. Either
    'max_budget' or 'budget_id' should be provided, not both.
    - allowed_model_region: Optional[Union[Literal[\"eu\"], Literal[\"us\"]]] - Require all user
    requests to use models in this specific region.
    - default_model: Optional[str] - If no equivalent model in the allowed region, default all requests
    to this model.
    - metadata: Optional[dict] = Metadata for customer, store information for customer. Example metadata
    = {\"data_training_opt_out\": True}
    - budget_duration: Optional[str] - Budget is reset at the end of specified duration. If not set,
    budget is never reset. You can set duration as seconds (\"30s\"), minutes (\"30m\"), hours
    (\"30h\"), days (\"30d\").
    - tpm_limit: Optional[int] - [Not Implemented Yet] Specify tpm limit for a given customer (Tokens
    per minute)
    - rpm_limit: Optional[int] - [Not Implemented Yet] Specify rpm limit for a given customer (Requests
    per minute)
    - model_max_budget: Optional[dict] - [Not Implemented Yet] Specify max budget for a given model.
    Example: {\"openai/gpt-4o-mini\": {\"max_budget\": 100.0, \"budget_duration\": \"1d\"}}
    - max_parallel_requests: Optional[int] - [Not Implemented Yet] Specify max parallel requests for a
    given customer.
    - soft_budget: Optional[float] - [Not Implemented Yet] Get alerts when customer crosses given
    budget, doesn't block requests.
    - spend: Optional[float] - Specify initial spend for a given customer.
    - budget_reset_at: Optional[str] - Specify the date and time when the budget should be reset.


    - Allow specifying allowed regions
    - Allow specifying default model

    Example curl:
    ```
    curl --location 'http://0.0.0.0:4000/customer/new'         --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'         --data '{
            \"user_id\" : \"ishaan-jaff-3\",
            \"allowed_region\": \"eu\",
            \"budget_id\": \"free_tier\",
            \"default_model\": \"azure/gpt-3.5-turbo-eu\" <- all calls from this user, use this model?
        }'

        # return end-user object
    ```

    NOTE: This used to be called `/end_user/new`, we will still be maintaining compatibility for
    /end_user/XXX for these endpoints

    Args:
        body (NewCustomerRequest): Create a new customer, allocate a budget to them

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
    body: NewCustomerRequest,

) -> Response[Any | HTTPValidationError]:
    r""" New End User

     Allow creating a new Customer


    Parameters:
    - user_id: str - The unique identifier for the user.
    - alias: Optional[str] - A human-friendly alias for the user.
    - blocked: bool - Flag to allow or disallow requests for this end-user. Default is False.
    - max_budget: Optional[float] - The maximum budget allocated to the user. Either 'max_budget' or
    'budget_id' should be provided, not both.
    - budget_id: Optional[str] - The identifier for an existing budget allocated to the user. Either
    'max_budget' or 'budget_id' should be provided, not both.
    - allowed_model_region: Optional[Union[Literal[\"eu\"], Literal[\"us\"]]] - Require all user
    requests to use models in this specific region.
    - default_model: Optional[str] - If no equivalent model in the allowed region, default all requests
    to this model.
    - metadata: Optional[dict] = Metadata for customer, store information for customer. Example metadata
    = {\"data_training_opt_out\": True}
    - budget_duration: Optional[str] - Budget is reset at the end of specified duration. If not set,
    budget is never reset. You can set duration as seconds (\"30s\"), minutes (\"30m\"), hours
    (\"30h\"), days (\"30d\").
    - tpm_limit: Optional[int] - [Not Implemented Yet] Specify tpm limit for a given customer (Tokens
    per minute)
    - rpm_limit: Optional[int] - [Not Implemented Yet] Specify rpm limit for a given customer (Requests
    per minute)
    - model_max_budget: Optional[dict] - [Not Implemented Yet] Specify max budget for a given model.
    Example: {\"openai/gpt-4o-mini\": {\"max_budget\": 100.0, \"budget_duration\": \"1d\"}}
    - max_parallel_requests: Optional[int] - [Not Implemented Yet] Specify max parallel requests for a
    given customer.
    - soft_budget: Optional[float] - [Not Implemented Yet] Get alerts when customer crosses given
    budget, doesn't block requests.
    - spend: Optional[float] - Specify initial spend for a given customer.
    - budget_reset_at: Optional[str] - Specify the date and time when the budget should be reset.


    - Allow specifying allowed regions
    - Allow specifying default model

    Example curl:
    ```
    curl --location 'http://0.0.0.0:4000/customer/new'         --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'         --data '{
            \"user_id\" : \"ishaan-jaff-3\",
            \"allowed_region\": \"eu\",
            \"budget_id\": \"free_tier\",
            \"default_model\": \"azure/gpt-3.5-turbo-eu\" <- all calls from this user, use this model?
        }'

        # return end-user object
    ```

    NOTE: This used to be called `/end_user/new`, we will still be maintaining compatibility for
    /end_user/XXX for these endpoints

    Args:
        body (NewCustomerRequest): Create a new customer, allocate a budget to them

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
    body: NewCustomerRequest,

) -> Any | HTTPValidationError | None:
    r""" New End User

     Allow creating a new Customer


    Parameters:
    - user_id: str - The unique identifier for the user.
    - alias: Optional[str] - A human-friendly alias for the user.
    - blocked: bool - Flag to allow or disallow requests for this end-user. Default is False.
    - max_budget: Optional[float] - The maximum budget allocated to the user. Either 'max_budget' or
    'budget_id' should be provided, not both.
    - budget_id: Optional[str] - The identifier for an existing budget allocated to the user. Either
    'max_budget' or 'budget_id' should be provided, not both.
    - allowed_model_region: Optional[Union[Literal[\"eu\"], Literal[\"us\"]]] - Require all user
    requests to use models in this specific region.
    - default_model: Optional[str] - If no equivalent model in the allowed region, default all requests
    to this model.
    - metadata: Optional[dict] = Metadata for customer, store information for customer. Example metadata
    = {\"data_training_opt_out\": True}
    - budget_duration: Optional[str] - Budget is reset at the end of specified duration. If not set,
    budget is never reset. You can set duration as seconds (\"30s\"), minutes (\"30m\"), hours
    (\"30h\"), days (\"30d\").
    - tpm_limit: Optional[int] - [Not Implemented Yet] Specify tpm limit for a given customer (Tokens
    per minute)
    - rpm_limit: Optional[int] - [Not Implemented Yet] Specify rpm limit for a given customer (Requests
    per minute)
    - model_max_budget: Optional[dict] - [Not Implemented Yet] Specify max budget for a given model.
    Example: {\"openai/gpt-4o-mini\": {\"max_budget\": 100.0, \"budget_duration\": \"1d\"}}
    - max_parallel_requests: Optional[int] - [Not Implemented Yet] Specify max parallel requests for a
    given customer.
    - soft_budget: Optional[float] - [Not Implemented Yet] Get alerts when customer crosses given
    budget, doesn't block requests.
    - spend: Optional[float] - Specify initial spend for a given customer.
    - budget_reset_at: Optional[str] - Specify the date and time when the budget should be reset.


    - Allow specifying allowed regions
    - Allow specifying default model

    Example curl:
    ```
    curl --location 'http://0.0.0.0:4000/customer/new'         --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'         --data '{
            \"user_id\" : \"ishaan-jaff-3\",
            \"allowed_region\": \"eu\",
            \"budget_id\": \"free_tier\",
            \"default_model\": \"azure/gpt-3.5-turbo-eu\" <- all calls from this user, use this model?
        }'

        # return end-user object
    ```

    NOTE: This used to be called `/end_user/new`, we will still be maintaining compatibility for
    /end_user/XXX for these endpoints

    Args:
        body (NewCustomerRequest): Create a new customer, allocate a budget to them

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
