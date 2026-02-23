from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llm_project_table import LiteLLMProjectTable
from ...models.update_project_request import UpdateProjectRequest
from typing import cast



def _get_kwargs(
    *,
    body: UpdateProjectRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/project/update",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | LiteLLMProjectTable | None:
    if response.status_code == 200:
        response_200 = LiteLLMProjectTable.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | LiteLLMProjectTable]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateProjectRequest,

) -> Response[HTTPValidationError | LiteLLMProjectTable]:
    r""" Update Project

     Update a project

    Parameters:
    - project_id: *str* - The project id to update. Required.
    - project_alias: *Optional[str]* - Updated name for the project
    - description: *Optional[str]* - Updated description for the project
    - team_id: *Optional[str]* - Updated team_id for the project
    - metadata: *Optional[dict]* - Updated metadata for project
    - models: *Optional[list]* - Updated list of models for the project
    - blocked: *Optional[bool]* - Updated blocked status
    - max_budget: *Optional[float]* - Updated max budget
    - tpm_limit: *Optional[int]* - Updated tpm limit
    - rpm_limit: *Optional[int]* - Updated rpm limit
    - model_rpm_limit: *Optional[dict]* - Updated RPM limits per model
    - model_tpm_limit: *Optional[dict]* - Updated TPM limits per model
    - budget_duration: *Optional[str]* - Updated budget duration
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - Updated object permission

    Example:
    ```bash
    curl --location 'http://0.0.0.0:4000/project/update' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_id\": \"project-123\",
        \"description\": \"Updated flight search system with enhanced capabilities\",
        \"max_budget\": 200,
        \"model_rpm_limit\": {
            \"gpt-4\": 2000,
            \"gpt-3.5-turbo\": 10000
        },
        \"metadata\": {
            \"use_case_id\": \"SNOW-12345\",
            \"status\": \"active\"
        }
    }'
    ```

    Args:
        body (UpdateProjectRequest): Request model for POST /project/update

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiteLLMProjectTable]
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
    body: UpdateProjectRequest,

) -> HTTPValidationError | LiteLLMProjectTable | None:
    r""" Update Project

     Update a project

    Parameters:
    - project_id: *str* - The project id to update. Required.
    - project_alias: *Optional[str]* - Updated name for the project
    - description: *Optional[str]* - Updated description for the project
    - team_id: *Optional[str]* - Updated team_id for the project
    - metadata: *Optional[dict]* - Updated metadata for project
    - models: *Optional[list]* - Updated list of models for the project
    - blocked: *Optional[bool]* - Updated blocked status
    - max_budget: *Optional[float]* - Updated max budget
    - tpm_limit: *Optional[int]* - Updated tpm limit
    - rpm_limit: *Optional[int]* - Updated rpm limit
    - model_rpm_limit: *Optional[dict]* - Updated RPM limits per model
    - model_tpm_limit: *Optional[dict]* - Updated TPM limits per model
    - budget_duration: *Optional[str]* - Updated budget duration
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - Updated object permission

    Example:
    ```bash
    curl --location 'http://0.0.0.0:4000/project/update' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_id\": \"project-123\",
        \"description\": \"Updated flight search system with enhanced capabilities\",
        \"max_budget\": 200,
        \"model_rpm_limit\": {
            \"gpt-4\": 2000,
            \"gpt-3.5-turbo\": 10000
        },
        \"metadata\": {
            \"use_case_id\": \"SNOW-12345\",
            \"status\": \"active\"
        }
    }'
    ```

    Args:
        body (UpdateProjectRequest): Request model for POST /project/update

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiteLLMProjectTable
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateProjectRequest,

) -> Response[HTTPValidationError | LiteLLMProjectTable]:
    r""" Update Project

     Update a project

    Parameters:
    - project_id: *str* - The project id to update. Required.
    - project_alias: *Optional[str]* - Updated name for the project
    - description: *Optional[str]* - Updated description for the project
    - team_id: *Optional[str]* - Updated team_id for the project
    - metadata: *Optional[dict]* - Updated metadata for project
    - models: *Optional[list]* - Updated list of models for the project
    - blocked: *Optional[bool]* - Updated blocked status
    - max_budget: *Optional[float]* - Updated max budget
    - tpm_limit: *Optional[int]* - Updated tpm limit
    - rpm_limit: *Optional[int]* - Updated rpm limit
    - model_rpm_limit: *Optional[dict]* - Updated RPM limits per model
    - model_tpm_limit: *Optional[dict]* - Updated TPM limits per model
    - budget_duration: *Optional[str]* - Updated budget duration
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - Updated object permission

    Example:
    ```bash
    curl --location 'http://0.0.0.0:4000/project/update' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_id\": \"project-123\",
        \"description\": \"Updated flight search system with enhanced capabilities\",
        \"max_budget\": 200,
        \"model_rpm_limit\": {
            \"gpt-4\": 2000,
            \"gpt-3.5-turbo\": 10000
        },
        \"metadata\": {
            \"use_case_id\": \"SNOW-12345\",
            \"status\": \"active\"
        }
    }'
    ```

    Args:
        body (UpdateProjectRequest): Request model for POST /project/update

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiteLLMProjectTable]
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
    body: UpdateProjectRequest,

) -> HTTPValidationError | LiteLLMProjectTable | None:
    r""" Update Project

     Update a project

    Parameters:
    - project_id: *str* - The project id to update. Required.
    - project_alias: *Optional[str]* - Updated name for the project
    - description: *Optional[str]* - Updated description for the project
    - team_id: *Optional[str]* - Updated team_id for the project
    - metadata: *Optional[dict]* - Updated metadata for project
    - models: *Optional[list]* - Updated list of models for the project
    - blocked: *Optional[bool]* - Updated blocked status
    - max_budget: *Optional[float]* - Updated max budget
    - tpm_limit: *Optional[int]* - Updated tpm limit
    - rpm_limit: *Optional[int]* - Updated rpm limit
    - model_rpm_limit: *Optional[dict]* - Updated RPM limits per model
    - model_tpm_limit: *Optional[dict]* - Updated TPM limits per model
    - budget_duration: *Optional[str]* - Updated budget duration
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - Updated object permission

    Example:
    ```bash
    curl --location 'http://0.0.0.0:4000/project/update' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        \"project_id\": \"project-123\",
        \"description\": \"Updated flight search system with enhanced capabilities\",
        \"max_budget\": 200,
        \"model_rpm_limit\": {
            \"gpt-4\": 2000,
            \"gpt-3.5-turbo\": 10000
        },
        \"metadata\": {
            \"use_case_id\": \"SNOW-12345\",
            \"status\": \"active\"
        }
    }'
    ```

    Args:
        body (UpdateProjectRequest): Request model for POST /project/update

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiteLLMProjectTable
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
