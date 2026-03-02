from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.new_project_request import NewProjectRequest
from ...models.new_project_response import NewProjectResponse
from typing import cast



def _get_kwargs(
    *,
    body: NewProjectRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/project/new",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | NewProjectResponse | None:
    if response.status_code == 200:
        response_200 = NewProjectResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | NewProjectResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NewProjectRequest,

) -> Response[HTTPValidationError | NewProjectResponse]:
    r""" New Project

     Create a new project. Projects sit between teams and keys in the hierarchy.

    Only admins or team admins can create projects.

    # Parameters

    - project_alias: *Optional[str]* - The name of the project.
    - description: *Optional[str]* - Description of the project's purpose and use case.
    - team_id: *str* - The team id that this project belongs to. Required.
    - models: *List* - The models the project has access to.
    - budget_id: *Optional[str]* - The id for a budget (tpm/rpm/max budget) for the project.
    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - max_budget: *Optional[float]* - Max budget for project
    - tpm_limit: *Optional[int]* - Max tpm limit for project
    - rpm_limit: *Optional[int]* - Max rpm limit for project
    - max_parallel_requests: *Optional[int]* - Max parallel requests for project
    - soft_budget: *Optional[float]* - Get a slack alert when this soft budget is reached. Don't block
    requests.
    - model_max_budget: *Optional[dict]* - Max budget for a specific model. Example: {\"gpt-4\": 100.0,
    \"gpt-3.5-turbo\": 50.0}
    - model_rpm_limit: *Optional[dict]* - RPM limits per model. Example: {\"gpt-4\": 1000,
    \"gpt-3.5-turbo\": 5000}
    - model_tpm_limit: *Optional[dict]* - TPM limits per model. Example: {\"gpt-4\": 50000,
    \"gpt-3.5-turbo\": 100000}
    - budget_duration: *Optional[str]* - Frequency of reseting project budget
    - metadata: *Optional[dict]* - Metadata for project, store information for project. Example metadata
    - {\"use_case_id\": \"SNOW-12345\", \"responsible_ai_id\": \"RAI-67890\"}
    - tags: *Optional[list]* - Tags for the project. Example: [\"production\", \"api\"]
    - blocked: *bool* - Flag indicating if the project is blocked or not - will stop all calls from keys
    with this project_id.
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - project-specific object permission.
    Example - {\"vector_stores\": [\"vector_store_1\", \"vector_store_2\"]}. IF null or {} then no
    object permission.

    Example 1: Create new project **without** a budget_id, with model-specific limits

    ```bash
    curl --location 'http://0.0.0.0:4000/project/new' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_alias\": \"flight-search-assistant\",
        \"description\": \"AI-powered flight search and booking assistant\",
        \"team_id\": \"team-123\",
        \"models\": [\"gpt-4\", \"gpt-3.5-turbo\"],
        \"max_budget\": 100,
        \"model_rpm_limit\": {
            \"gpt-4\": 1000,
            \"gpt-3.5-turbo\": 5000
        },
        \"model_tpm_limit\": {
            \"gpt-4\": 50000,
            \"gpt-3.5-turbo\": 100000
        },
        \"metadata\": {
            \"use_case_id\": \"SNOW-12345\",
            \"responsible_ai_id\": \"RAI-67890\"
        }
    }'
    ```

    Example 2: Create new project **with** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/project/new' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_alias\": \"hotel-recommendations\",
        \"description\": \"Personalized hotel recommendation engine\",
        \"team_id\": \"team-123\",
        \"models\": [\"claude-3-sonnet\"],
        \"budget_id\": \"428eeaa8-f3ac-4e85-a8fb-7dc8d7aa8689\",
        \"metadata\": {
            \"use_case_id\": \"SNOW-54321\"
        }
    }'
    ```

    Args:
        body (NewProjectRequest): Request model for POST /project/new

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NewProjectResponse]
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
    body: NewProjectRequest,

) -> HTTPValidationError | NewProjectResponse | None:
    r""" New Project

     Create a new project. Projects sit between teams and keys in the hierarchy.

    Only admins or team admins can create projects.

    # Parameters

    - project_alias: *Optional[str]* - The name of the project.
    - description: *Optional[str]* - Description of the project's purpose and use case.
    - team_id: *str* - The team id that this project belongs to. Required.
    - models: *List* - The models the project has access to.
    - budget_id: *Optional[str]* - The id for a budget (tpm/rpm/max budget) for the project.
    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - max_budget: *Optional[float]* - Max budget for project
    - tpm_limit: *Optional[int]* - Max tpm limit for project
    - rpm_limit: *Optional[int]* - Max rpm limit for project
    - max_parallel_requests: *Optional[int]* - Max parallel requests for project
    - soft_budget: *Optional[float]* - Get a slack alert when this soft budget is reached. Don't block
    requests.
    - model_max_budget: *Optional[dict]* - Max budget for a specific model. Example: {\"gpt-4\": 100.0,
    \"gpt-3.5-turbo\": 50.0}
    - model_rpm_limit: *Optional[dict]* - RPM limits per model. Example: {\"gpt-4\": 1000,
    \"gpt-3.5-turbo\": 5000}
    - model_tpm_limit: *Optional[dict]* - TPM limits per model. Example: {\"gpt-4\": 50000,
    \"gpt-3.5-turbo\": 100000}
    - budget_duration: *Optional[str]* - Frequency of reseting project budget
    - metadata: *Optional[dict]* - Metadata for project, store information for project. Example metadata
    - {\"use_case_id\": \"SNOW-12345\", \"responsible_ai_id\": \"RAI-67890\"}
    - tags: *Optional[list]* - Tags for the project. Example: [\"production\", \"api\"]
    - blocked: *bool* - Flag indicating if the project is blocked or not - will stop all calls from keys
    with this project_id.
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - project-specific object permission.
    Example - {\"vector_stores\": [\"vector_store_1\", \"vector_store_2\"]}. IF null or {} then no
    object permission.

    Example 1: Create new project **without** a budget_id, with model-specific limits

    ```bash
    curl --location 'http://0.0.0.0:4000/project/new' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_alias\": \"flight-search-assistant\",
        \"description\": \"AI-powered flight search and booking assistant\",
        \"team_id\": \"team-123\",
        \"models\": [\"gpt-4\", \"gpt-3.5-turbo\"],
        \"max_budget\": 100,
        \"model_rpm_limit\": {
            \"gpt-4\": 1000,
            \"gpt-3.5-turbo\": 5000
        },
        \"model_tpm_limit\": {
            \"gpt-4\": 50000,
            \"gpt-3.5-turbo\": 100000
        },
        \"metadata\": {
            \"use_case_id\": \"SNOW-12345\",
            \"responsible_ai_id\": \"RAI-67890\"
        }
    }'
    ```

    Example 2: Create new project **with** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/project/new' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_alias\": \"hotel-recommendations\",
        \"description\": \"Personalized hotel recommendation engine\",
        \"team_id\": \"team-123\",
        \"models\": [\"claude-3-sonnet\"],
        \"budget_id\": \"428eeaa8-f3ac-4e85-a8fb-7dc8d7aa8689\",
        \"metadata\": {
            \"use_case_id\": \"SNOW-54321\"
        }
    }'
    ```

    Args:
        body (NewProjectRequest): Request model for POST /project/new

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NewProjectResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewProjectRequest,

) -> Response[HTTPValidationError | NewProjectResponse]:
    r""" New Project

     Create a new project. Projects sit between teams and keys in the hierarchy.

    Only admins or team admins can create projects.

    # Parameters

    - project_alias: *Optional[str]* - The name of the project.
    - description: *Optional[str]* - Description of the project's purpose and use case.
    - team_id: *str* - The team id that this project belongs to. Required.
    - models: *List* - The models the project has access to.
    - budget_id: *Optional[str]* - The id for a budget (tpm/rpm/max budget) for the project.
    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - max_budget: *Optional[float]* - Max budget for project
    - tpm_limit: *Optional[int]* - Max tpm limit for project
    - rpm_limit: *Optional[int]* - Max rpm limit for project
    - max_parallel_requests: *Optional[int]* - Max parallel requests for project
    - soft_budget: *Optional[float]* - Get a slack alert when this soft budget is reached. Don't block
    requests.
    - model_max_budget: *Optional[dict]* - Max budget for a specific model. Example: {\"gpt-4\": 100.0,
    \"gpt-3.5-turbo\": 50.0}
    - model_rpm_limit: *Optional[dict]* - RPM limits per model. Example: {\"gpt-4\": 1000,
    \"gpt-3.5-turbo\": 5000}
    - model_tpm_limit: *Optional[dict]* - TPM limits per model. Example: {\"gpt-4\": 50000,
    \"gpt-3.5-turbo\": 100000}
    - budget_duration: *Optional[str]* - Frequency of reseting project budget
    - metadata: *Optional[dict]* - Metadata for project, store information for project. Example metadata
    - {\"use_case_id\": \"SNOW-12345\", \"responsible_ai_id\": \"RAI-67890\"}
    - tags: *Optional[list]* - Tags for the project. Example: [\"production\", \"api\"]
    - blocked: *bool* - Flag indicating if the project is blocked or not - will stop all calls from keys
    with this project_id.
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - project-specific object permission.
    Example - {\"vector_stores\": [\"vector_store_1\", \"vector_store_2\"]}. IF null or {} then no
    object permission.

    Example 1: Create new project **without** a budget_id, with model-specific limits

    ```bash
    curl --location 'http://0.0.0.0:4000/project/new' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_alias\": \"flight-search-assistant\",
        \"description\": \"AI-powered flight search and booking assistant\",
        \"team_id\": \"team-123\",
        \"models\": [\"gpt-4\", \"gpt-3.5-turbo\"],
        \"max_budget\": 100,
        \"model_rpm_limit\": {
            \"gpt-4\": 1000,
            \"gpt-3.5-turbo\": 5000
        },
        \"model_tpm_limit\": {
            \"gpt-4\": 50000,
            \"gpt-3.5-turbo\": 100000
        },
        \"metadata\": {
            \"use_case_id\": \"SNOW-12345\",
            \"responsible_ai_id\": \"RAI-67890\"
        }
    }'
    ```

    Example 2: Create new project **with** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/project/new' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_alias\": \"hotel-recommendations\",
        \"description\": \"Personalized hotel recommendation engine\",
        \"team_id\": \"team-123\",
        \"models\": [\"claude-3-sonnet\"],
        \"budget_id\": \"428eeaa8-f3ac-4e85-a8fb-7dc8d7aa8689\",
        \"metadata\": {
            \"use_case_id\": \"SNOW-54321\"
        }
    }'
    ```

    Args:
        body (NewProjectRequest): Request model for POST /project/new

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NewProjectResponse]
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
    body: NewProjectRequest,

) -> HTTPValidationError | NewProjectResponse | None:
    r""" New Project

     Create a new project. Projects sit between teams and keys in the hierarchy.

    Only admins or team admins can create projects.

    # Parameters

    - project_alias: *Optional[str]* - The name of the project.
    - description: *Optional[str]* - Description of the project's purpose and use case.
    - team_id: *str* - The team id that this project belongs to. Required.
    - models: *List* - The models the project has access to.
    - budget_id: *Optional[str]* - The id for a budget (tpm/rpm/max budget) for the project.
    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - max_budget: *Optional[float]* - Max budget for project
    - tpm_limit: *Optional[int]* - Max tpm limit for project
    - rpm_limit: *Optional[int]* - Max rpm limit for project
    - max_parallel_requests: *Optional[int]* - Max parallel requests for project
    - soft_budget: *Optional[float]* - Get a slack alert when this soft budget is reached. Don't block
    requests.
    - model_max_budget: *Optional[dict]* - Max budget for a specific model. Example: {\"gpt-4\": 100.0,
    \"gpt-3.5-turbo\": 50.0}
    - model_rpm_limit: *Optional[dict]* - RPM limits per model. Example: {\"gpt-4\": 1000,
    \"gpt-3.5-turbo\": 5000}
    - model_tpm_limit: *Optional[dict]* - TPM limits per model. Example: {\"gpt-4\": 50000,
    \"gpt-3.5-turbo\": 100000}
    - budget_duration: *Optional[str]* - Frequency of reseting project budget
    - metadata: *Optional[dict]* - Metadata for project, store information for project. Example metadata
    - {\"use_case_id\": \"SNOW-12345\", \"responsible_ai_id\": \"RAI-67890\"}
    - tags: *Optional[list]* - Tags for the project. Example: [\"production\", \"api\"]
    - blocked: *bool* - Flag indicating if the project is blocked or not - will stop all calls from keys
    with this project_id.
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - project-specific object permission.
    Example - {\"vector_stores\": [\"vector_store_1\", \"vector_store_2\"]}. IF null or {} then no
    object permission.

    Example 1: Create new project **without** a budget_id, with model-specific limits

    ```bash
    curl --location 'http://0.0.0.0:4000/project/new' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_alias\": \"flight-search-assistant\",
        \"description\": \"AI-powered flight search and booking assistant\",
        \"team_id\": \"team-123\",
        \"models\": [\"gpt-4\", \"gpt-3.5-turbo\"],
        \"max_budget\": 100,
        \"model_rpm_limit\": {
            \"gpt-4\": 1000,
            \"gpt-3.5-turbo\": 5000
        },
        \"model_tpm_limit\": {
            \"gpt-4\": 50000,
            \"gpt-3.5-turbo\": 100000
        },
        \"metadata\": {
            \"use_case_id\": \"SNOW-12345\",
            \"responsible_ai_id\": \"RAI-67890\"
        }
    }'
    ```

    Example 2: Create new project **with** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/project/new' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_alias\": \"hotel-recommendations\",
        \"description\": \"Personalized hotel recommendation engine\",
        \"team_id\": \"team-123\",
        \"models\": [\"claude-3-sonnet\"],
        \"budget_id\": \"428eeaa8-f3ac-4e85-a8fb-7dc8d7aa8689\",
        \"metadata\": {
            \"use_case_id\": \"SNOW-54321\"
        }
    }'
    ```

    Args:
        body (NewProjectRequest): Request model for POST /project/new

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NewProjectResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
