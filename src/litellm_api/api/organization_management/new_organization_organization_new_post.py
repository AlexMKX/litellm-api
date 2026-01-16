from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.new_organization_request import NewOrganizationRequest
from ...models.new_organization_response import NewOrganizationResponse
from typing import cast



def _get_kwargs(
    *,
    body: NewOrganizationRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/organization/new",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | NewOrganizationResponse | None:
    if response.status_code == 200:
        response_200 = NewOrganizationResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | NewOrganizationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NewOrganizationRequest,

) -> Response[HTTPValidationError | NewOrganizationResponse]:
    r""" New Organization

     Allow orgs to own teams

    Set org level budgets + model access.

    Only admins can create orgs.

    # Parameters

    - organization_alias: *str* - The name of the organization.
    - models: *List* - The models the organization has access to.
    - budget_id: *Optional[str]* - The id for a budget (tpm/rpm/max budget) for the organization.
    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - max_budget: *Optional[float]* - Max budget for org
    - tpm_limit: *Optional[int]* - Max tpm limit for org
    - rpm_limit: *Optional[int]* - Max rpm limit for org
    - model_rpm_limit: *Optional[Dict[str, int]]* - The RPM (Requests Per Minute) limit per model for
    this organization.
    - model_tpm_limit: *Optional[Dict[str, int]]* - The TPM (Tokens Per Minute) limit per model for this
    organization.
    - max_parallel_requests: *Optional[int]* - [Not Implemented Yet] Max parallel requests for org
    - soft_budget: *Optional[float]* - [Not Implemented Yet] Get a slack alert when this soft budget is
    reached. Don't block requests.
    - model_max_budget: *Optional[dict]* - Max budget for a specific model
    - budget_duration: *Optional[str]* - Frequency of reseting org budget
    - metadata: *Optional[dict]* - Metadata for organization, store information for organization.
    Example metadata - {\"extra_info\": \"some info\"}
    - blocked: *bool* - Flag indicating if the org is blocked or not - will stop all calls from keys
    with this org_id.
    - tags: *Optional[List[str]]* - Tags for [tracking
    spend](https://litellm.vercel.app/docs/proxy/enterprise#tracking-spend-for-custom-tags) and/or doing
    [tag-based routing](https://litellm.vercel.app/docs/proxy/tag_routing).
    - organization_id: *Optional[str]* - The organization id of the team. Default is None. Create via
    `/organization/new`.
    - model_aliases: Optional[dict] - Model aliases for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/team_based_routing#create-team-with-model-alias)
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - organization-specific object
    permission. Example - {\"vector_stores\": [\"vector_store_1\", \"vector_store_2\"]}. IF null or {}
    then no object permission.
    Case 1: Create new org **without** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"max_budget\": 100
    }'


    ```

    Case 2: Create new org **with** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"budget_id\": \"428eeaa8-f3ac-4e85-a8fb-7dc8d7aa8689\"
    }'
    ```

    Args:
        body (NewOrganizationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NewOrganizationResponse]
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
    body: NewOrganizationRequest,

) -> HTTPValidationError | NewOrganizationResponse | None:
    r""" New Organization

     Allow orgs to own teams

    Set org level budgets + model access.

    Only admins can create orgs.

    # Parameters

    - organization_alias: *str* - The name of the organization.
    - models: *List* - The models the organization has access to.
    - budget_id: *Optional[str]* - The id for a budget (tpm/rpm/max budget) for the organization.
    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - max_budget: *Optional[float]* - Max budget for org
    - tpm_limit: *Optional[int]* - Max tpm limit for org
    - rpm_limit: *Optional[int]* - Max rpm limit for org
    - model_rpm_limit: *Optional[Dict[str, int]]* - The RPM (Requests Per Minute) limit per model for
    this organization.
    - model_tpm_limit: *Optional[Dict[str, int]]* - The TPM (Tokens Per Minute) limit per model for this
    organization.
    - max_parallel_requests: *Optional[int]* - [Not Implemented Yet] Max parallel requests for org
    - soft_budget: *Optional[float]* - [Not Implemented Yet] Get a slack alert when this soft budget is
    reached. Don't block requests.
    - model_max_budget: *Optional[dict]* - Max budget for a specific model
    - budget_duration: *Optional[str]* - Frequency of reseting org budget
    - metadata: *Optional[dict]* - Metadata for organization, store information for organization.
    Example metadata - {\"extra_info\": \"some info\"}
    - blocked: *bool* - Flag indicating if the org is blocked or not - will stop all calls from keys
    with this org_id.
    - tags: *Optional[List[str]]* - Tags for [tracking
    spend](https://litellm.vercel.app/docs/proxy/enterprise#tracking-spend-for-custom-tags) and/or doing
    [tag-based routing](https://litellm.vercel.app/docs/proxy/tag_routing).
    - organization_id: *Optional[str]* - The organization id of the team. Default is None. Create via
    `/organization/new`.
    - model_aliases: Optional[dict] - Model aliases for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/team_based_routing#create-team-with-model-alias)
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - organization-specific object
    permission. Example - {\"vector_stores\": [\"vector_store_1\", \"vector_store_2\"]}. IF null or {}
    then no object permission.
    Case 1: Create new org **without** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"max_budget\": 100
    }'


    ```

    Case 2: Create new org **with** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"budget_id\": \"428eeaa8-f3ac-4e85-a8fb-7dc8d7aa8689\"
    }'
    ```

    Args:
        body (NewOrganizationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NewOrganizationResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewOrganizationRequest,

) -> Response[HTTPValidationError | NewOrganizationResponse]:
    r""" New Organization

     Allow orgs to own teams

    Set org level budgets + model access.

    Only admins can create orgs.

    # Parameters

    - organization_alias: *str* - The name of the organization.
    - models: *List* - The models the organization has access to.
    - budget_id: *Optional[str]* - The id for a budget (tpm/rpm/max budget) for the organization.
    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - max_budget: *Optional[float]* - Max budget for org
    - tpm_limit: *Optional[int]* - Max tpm limit for org
    - rpm_limit: *Optional[int]* - Max rpm limit for org
    - model_rpm_limit: *Optional[Dict[str, int]]* - The RPM (Requests Per Minute) limit per model for
    this organization.
    - model_tpm_limit: *Optional[Dict[str, int]]* - The TPM (Tokens Per Minute) limit per model for this
    organization.
    - max_parallel_requests: *Optional[int]* - [Not Implemented Yet] Max parallel requests for org
    - soft_budget: *Optional[float]* - [Not Implemented Yet] Get a slack alert when this soft budget is
    reached. Don't block requests.
    - model_max_budget: *Optional[dict]* - Max budget for a specific model
    - budget_duration: *Optional[str]* - Frequency of reseting org budget
    - metadata: *Optional[dict]* - Metadata for organization, store information for organization.
    Example metadata - {\"extra_info\": \"some info\"}
    - blocked: *bool* - Flag indicating if the org is blocked or not - will stop all calls from keys
    with this org_id.
    - tags: *Optional[List[str]]* - Tags for [tracking
    spend](https://litellm.vercel.app/docs/proxy/enterprise#tracking-spend-for-custom-tags) and/or doing
    [tag-based routing](https://litellm.vercel.app/docs/proxy/tag_routing).
    - organization_id: *Optional[str]* - The organization id of the team. Default is None. Create via
    `/organization/new`.
    - model_aliases: Optional[dict] - Model aliases for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/team_based_routing#create-team-with-model-alias)
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - organization-specific object
    permission. Example - {\"vector_stores\": [\"vector_store_1\", \"vector_store_2\"]}. IF null or {}
    then no object permission.
    Case 1: Create new org **without** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"max_budget\": 100
    }'


    ```

    Case 2: Create new org **with** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"budget_id\": \"428eeaa8-f3ac-4e85-a8fb-7dc8d7aa8689\"
    }'
    ```

    Args:
        body (NewOrganizationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NewOrganizationResponse]
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
    body: NewOrganizationRequest,

) -> HTTPValidationError | NewOrganizationResponse | None:
    r""" New Organization

     Allow orgs to own teams

    Set org level budgets + model access.

    Only admins can create orgs.

    # Parameters

    - organization_alias: *str* - The name of the organization.
    - models: *List* - The models the organization has access to.
    - budget_id: *Optional[str]* - The id for a budget (tpm/rpm/max budget) for the organization.
    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - max_budget: *Optional[float]* - Max budget for org
    - tpm_limit: *Optional[int]* - Max tpm limit for org
    - rpm_limit: *Optional[int]* - Max rpm limit for org
    - model_rpm_limit: *Optional[Dict[str, int]]* - The RPM (Requests Per Minute) limit per model for
    this organization.
    - model_tpm_limit: *Optional[Dict[str, int]]* - The TPM (Tokens Per Minute) limit per model for this
    organization.
    - max_parallel_requests: *Optional[int]* - [Not Implemented Yet] Max parallel requests for org
    - soft_budget: *Optional[float]* - [Not Implemented Yet] Get a slack alert when this soft budget is
    reached. Don't block requests.
    - model_max_budget: *Optional[dict]* - Max budget for a specific model
    - budget_duration: *Optional[str]* - Frequency of reseting org budget
    - metadata: *Optional[dict]* - Metadata for organization, store information for organization.
    Example metadata - {\"extra_info\": \"some info\"}
    - blocked: *bool* - Flag indicating if the org is blocked or not - will stop all calls from keys
    with this org_id.
    - tags: *Optional[List[str]]* - Tags for [tracking
    spend](https://litellm.vercel.app/docs/proxy/enterprise#tracking-spend-for-custom-tags) and/or doing
    [tag-based routing](https://litellm.vercel.app/docs/proxy/tag_routing).
    - organization_id: *Optional[str]* - The organization id of the team. Default is None. Create via
    `/organization/new`.
    - model_aliases: Optional[dict] - Model aliases for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/team_based_routing#create-team-with-model-alias)
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - organization-specific object
    permission. Example - {\"vector_stores\": [\"vector_store_1\", \"vector_store_2\"]}. IF null or {}
    then no object permission.
    Case 1: Create new org **without** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"max_budget\": 100
    }'


    ```

    Case 2: Create new org **with** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"budget_id\": \"428eeaa8-f3ac-4e85-a8fb-7dc8d7aa8689\"
    }'
    ```

    Args:
        body (NewOrganizationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NewOrganizationResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
