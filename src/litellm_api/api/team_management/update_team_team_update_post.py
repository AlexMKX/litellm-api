from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.update_team_request import UpdateTeamRequest
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UpdateTeamRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(litellm_changed_by, Unset):
        headers["litellm-changed-by"] = litellm_changed_by



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/team/update",
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
    body: UpdateTeamRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Update Team

     Use `/team/member_add` AND `/team/member/delete` to add/remove new team members

    You can now update team budget / rate limits via /team/update

    Parameters:
    - team_id: str - The team id of the user. Required param.
    - team_alias: Optional[str] - User defined team alias
    - team_member_permissions: Optional[List[str]] - A list of routes that non-admin team members can
    access. example: [\"/key/generate\", \"/key/update\", \"/key/delete\"]
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"team\": \"core-infra\", \"app\": \"app2\", \"email\": \"ishaan@berri.ai\" }
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - soft_budget: Optional[float] - The soft budget threshold for the team. If max_budget is set
    (either in the request or existing), soft_budget must be strictly lower than max_budget. Can be set
    independently if max_budget is not set.
    - budget_duration: Optional[str] - The duration of the budget for the team. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - prompts: Optional[List[str]] - List of prompts that the team is allowed to use.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.
    - tags: Optional[List[str]] - Tags for [tracking
    spend](https://litellm.vercel.app/docs/proxy/enterprise#tracking-spend-for-custom-tags) and/or doing
    [tag-based routing](https://litellm.vercel.app/docs/proxy/tag_routing).
    - organization_id: Optional[str] - The organization id of the team. Default is None. Create via
    `/organization/new`.
    - model_aliases: Optional[dict] - Model aliases for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/team_based_routing#create-team-with-model-alias)
    - guardrails: Optional[List[str]] - Guardrails for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/guardrails)
    - policies: Optional[List[str]] - Policies for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/guardrails/guardrail_policies)
    - disable_global_guardrails: Optional[bool] - Whether to disable global guardrails for the key.
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - team-specific object permission.
    Example - {\"vector_stores\": [\"vector_store_1\", \"vector_store_2\"], \"agents\": [\"agent_1\",
    \"agent_2\"], \"agent_access_groups\": [\"dev_group\"]}. IF null or {} then no object permission.
    - team_member_budget: Optional[float] - The maximum budget allocated to an individual team member.
    - team_member_budget_duration: Optional[str] - The duration of the budget for the team member. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - team_member_rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for individual team
    members.
    - team_member_tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for individual team
    members.
    - team_member_key_duration: Optional[str] - The duration for a team member's key. e.g. \"1d\",
    \"1w\", \"1mo\"
    - allowed_passthrough_routes: Optional[List[str]] - List of allowed pass through routes for the
    team.
    - model_rpm_limit: Optional[Dict[str, int]] - The RPM (Requests Per Minute) limit per model for this
    team. Example: {\"gpt-4\": 100, \"gpt-3.5-turbo\": 200}
    - model_tpm_limit: Optional[Dict[str, int]] - The TPM (Tokens Per Minute) limit per model for this
    team. Example: {\"gpt-4\": 10000, \"gpt-3.5-turbo\": 20000}
    Example - update team TPM Limit
    - allowed_vector_store_indexes: Optional[List[dict]] - List of allowed vector store indexes for the
    key. Example - [{\"index_name\": \"my-index\", \"index_permissions\": [\"write\", \"read\"]}]. If
    specified, the key will only be able to use these specific vector store indexes. Create index, using
    `/v1/indexes` endpoint.
    - secret_manager_settings: Optional[dict] - Secret manager settings for the team.
    [Docs](https://docs.litellm.ai/docs/secret_managers/overview)
    - router_settings: Optional[UpdateRouterConfig] - team-specific router settings. Example -
    {\"model_group_retry_policy\": {\"max_retries\": 5}}. IF null or {} then no router settings.
    - access_group_ids: Optional[List[str]] - List of access group IDs to associate with the team.
    Access groups define which models the team can access. Example - [\"access_group_1\",
    \"access_group_2\"].

    ```
    curl --location 'http://0.0.0.0:4000/team/update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data-raw '{
        \"team_id\": \"8d916b1c-510d-4894-a334-1c16a93344f5\",
        \"tpm_limit\": 100
    }'
    ```

    Example - Update Team `max_budget` budget
    ```
    curl --location 'http://0.0.0.0:4000/team/update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data-raw '{
        \"team_id\": \"8d916b1c-510d-4894-a334-1c16a93344f5\",
        \"max_budget\": 10
    }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (UpdateTeamRequest): UpdateTeamRequest, used by /team/update when you need to update
            a team

            team_id: str
            team_alias: Optional[str] = None
            organization_id: Optional[str] = None
            metadata: Optional[dict] = None
            tpm_limit: Optional[int] = None
            rpm_limit: Optional[int] = None
            max_budget: Optional[float] = None
            models: Optional[list] = None
            blocked: Optional[bool] = None
            budget_duration: Optional[str] = None
            guardrails: Optional[List[str]] = None
            policies: Optional[List[str]] = None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        body=body,
litellm_changed_by=litellm_changed_by,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: UpdateTeamRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Update Team

     Use `/team/member_add` AND `/team/member/delete` to add/remove new team members

    You can now update team budget / rate limits via /team/update

    Parameters:
    - team_id: str - The team id of the user. Required param.
    - team_alias: Optional[str] - User defined team alias
    - team_member_permissions: Optional[List[str]] - A list of routes that non-admin team members can
    access. example: [\"/key/generate\", \"/key/update\", \"/key/delete\"]
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"team\": \"core-infra\", \"app\": \"app2\", \"email\": \"ishaan@berri.ai\" }
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - soft_budget: Optional[float] - The soft budget threshold for the team. If max_budget is set
    (either in the request or existing), soft_budget must be strictly lower than max_budget. Can be set
    independently if max_budget is not set.
    - budget_duration: Optional[str] - The duration of the budget for the team. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - prompts: Optional[List[str]] - List of prompts that the team is allowed to use.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.
    - tags: Optional[List[str]] - Tags for [tracking
    spend](https://litellm.vercel.app/docs/proxy/enterprise#tracking-spend-for-custom-tags) and/or doing
    [tag-based routing](https://litellm.vercel.app/docs/proxy/tag_routing).
    - organization_id: Optional[str] - The organization id of the team. Default is None. Create via
    `/organization/new`.
    - model_aliases: Optional[dict] - Model aliases for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/team_based_routing#create-team-with-model-alias)
    - guardrails: Optional[List[str]] - Guardrails for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/guardrails)
    - policies: Optional[List[str]] - Policies for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/guardrails/guardrail_policies)
    - disable_global_guardrails: Optional[bool] - Whether to disable global guardrails for the key.
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - team-specific object permission.
    Example - {\"vector_stores\": [\"vector_store_1\", \"vector_store_2\"], \"agents\": [\"agent_1\",
    \"agent_2\"], \"agent_access_groups\": [\"dev_group\"]}. IF null or {} then no object permission.
    - team_member_budget: Optional[float] - The maximum budget allocated to an individual team member.
    - team_member_budget_duration: Optional[str] - The duration of the budget for the team member. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - team_member_rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for individual team
    members.
    - team_member_tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for individual team
    members.
    - team_member_key_duration: Optional[str] - The duration for a team member's key. e.g. \"1d\",
    \"1w\", \"1mo\"
    - allowed_passthrough_routes: Optional[List[str]] - List of allowed pass through routes for the
    team.
    - model_rpm_limit: Optional[Dict[str, int]] - The RPM (Requests Per Minute) limit per model for this
    team. Example: {\"gpt-4\": 100, \"gpt-3.5-turbo\": 200}
    - model_tpm_limit: Optional[Dict[str, int]] - The TPM (Tokens Per Minute) limit per model for this
    team. Example: {\"gpt-4\": 10000, \"gpt-3.5-turbo\": 20000}
    Example - update team TPM Limit
    - allowed_vector_store_indexes: Optional[List[dict]] - List of allowed vector store indexes for the
    key. Example - [{\"index_name\": \"my-index\", \"index_permissions\": [\"write\", \"read\"]}]. If
    specified, the key will only be able to use these specific vector store indexes. Create index, using
    `/v1/indexes` endpoint.
    - secret_manager_settings: Optional[dict] - Secret manager settings for the team.
    [Docs](https://docs.litellm.ai/docs/secret_managers/overview)
    - router_settings: Optional[UpdateRouterConfig] - team-specific router settings. Example -
    {\"model_group_retry_policy\": {\"max_retries\": 5}}. IF null or {} then no router settings.
    - access_group_ids: Optional[List[str]] - List of access group IDs to associate with the team.
    Access groups define which models the team can access. Example - [\"access_group_1\",
    \"access_group_2\"].

    ```
    curl --location 'http://0.0.0.0:4000/team/update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data-raw '{
        \"team_id\": \"8d916b1c-510d-4894-a334-1c16a93344f5\",
        \"tpm_limit\": 100
    }'
    ```

    Example - Update Team `max_budget` budget
    ```
    curl --location 'http://0.0.0.0:4000/team/update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data-raw '{
        \"team_id\": \"8d916b1c-510d-4894-a334-1c16a93344f5\",
        \"max_budget\": 10
    }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (UpdateTeamRequest): UpdateTeamRequest, used by /team/update when you need to update
            a team

            team_id: str
            team_alias: Optional[str] = None
            organization_id: Optional[str] = None
            metadata: Optional[dict] = None
            tpm_limit: Optional[int] = None
            rpm_limit: Optional[int] = None
            max_budget: Optional[float] = None
            models: Optional[list] = None
            blocked: Optional[bool] = None
            budget_duration: Optional[str] = None
            guardrails: Optional[List[str]] = None
            policies: Optional[List[str]] = None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateTeamRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Update Team

     Use `/team/member_add` AND `/team/member/delete` to add/remove new team members

    You can now update team budget / rate limits via /team/update

    Parameters:
    - team_id: str - The team id of the user. Required param.
    - team_alias: Optional[str] - User defined team alias
    - team_member_permissions: Optional[List[str]] - A list of routes that non-admin team members can
    access. example: [\"/key/generate\", \"/key/update\", \"/key/delete\"]
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"team\": \"core-infra\", \"app\": \"app2\", \"email\": \"ishaan@berri.ai\" }
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - soft_budget: Optional[float] - The soft budget threshold for the team. If max_budget is set
    (either in the request or existing), soft_budget must be strictly lower than max_budget. Can be set
    independently if max_budget is not set.
    - budget_duration: Optional[str] - The duration of the budget for the team. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - prompts: Optional[List[str]] - List of prompts that the team is allowed to use.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.
    - tags: Optional[List[str]] - Tags for [tracking
    spend](https://litellm.vercel.app/docs/proxy/enterprise#tracking-spend-for-custom-tags) and/or doing
    [tag-based routing](https://litellm.vercel.app/docs/proxy/tag_routing).
    - organization_id: Optional[str] - The organization id of the team. Default is None. Create via
    `/organization/new`.
    - model_aliases: Optional[dict] - Model aliases for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/team_based_routing#create-team-with-model-alias)
    - guardrails: Optional[List[str]] - Guardrails for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/guardrails)
    - policies: Optional[List[str]] - Policies for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/guardrails/guardrail_policies)
    - disable_global_guardrails: Optional[bool] - Whether to disable global guardrails for the key.
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - team-specific object permission.
    Example - {\"vector_stores\": [\"vector_store_1\", \"vector_store_2\"], \"agents\": [\"agent_1\",
    \"agent_2\"], \"agent_access_groups\": [\"dev_group\"]}. IF null or {} then no object permission.
    - team_member_budget: Optional[float] - The maximum budget allocated to an individual team member.
    - team_member_budget_duration: Optional[str] - The duration of the budget for the team member. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - team_member_rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for individual team
    members.
    - team_member_tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for individual team
    members.
    - team_member_key_duration: Optional[str] - The duration for a team member's key. e.g. \"1d\",
    \"1w\", \"1mo\"
    - allowed_passthrough_routes: Optional[List[str]] - List of allowed pass through routes for the
    team.
    - model_rpm_limit: Optional[Dict[str, int]] - The RPM (Requests Per Minute) limit per model for this
    team. Example: {\"gpt-4\": 100, \"gpt-3.5-turbo\": 200}
    - model_tpm_limit: Optional[Dict[str, int]] - The TPM (Tokens Per Minute) limit per model for this
    team. Example: {\"gpt-4\": 10000, \"gpt-3.5-turbo\": 20000}
    Example - update team TPM Limit
    - allowed_vector_store_indexes: Optional[List[dict]] - List of allowed vector store indexes for the
    key. Example - [{\"index_name\": \"my-index\", \"index_permissions\": [\"write\", \"read\"]}]. If
    specified, the key will only be able to use these specific vector store indexes. Create index, using
    `/v1/indexes` endpoint.
    - secret_manager_settings: Optional[dict] - Secret manager settings for the team.
    [Docs](https://docs.litellm.ai/docs/secret_managers/overview)
    - router_settings: Optional[UpdateRouterConfig] - team-specific router settings. Example -
    {\"model_group_retry_policy\": {\"max_retries\": 5}}. IF null or {} then no router settings.
    - access_group_ids: Optional[List[str]] - List of access group IDs to associate with the team.
    Access groups define which models the team can access. Example - [\"access_group_1\",
    \"access_group_2\"].

    ```
    curl --location 'http://0.0.0.0:4000/team/update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data-raw '{
        \"team_id\": \"8d916b1c-510d-4894-a334-1c16a93344f5\",
        \"tpm_limit\": 100
    }'
    ```

    Example - Update Team `max_budget` budget
    ```
    curl --location 'http://0.0.0.0:4000/team/update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data-raw '{
        \"team_id\": \"8d916b1c-510d-4894-a334-1c16a93344f5\",
        \"max_budget\": 10
    }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (UpdateTeamRequest): UpdateTeamRequest, used by /team/update when you need to update
            a team

            team_id: str
            team_alias: Optional[str] = None
            organization_id: Optional[str] = None
            metadata: Optional[dict] = None
            tpm_limit: Optional[int] = None
            rpm_limit: Optional[int] = None
            max_budget: Optional[float] = None
            models: Optional[list] = None
            blocked: Optional[bool] = None
            budget_duration: Optional[str] = None
            guardrails: Optional[List[str]] = None
            policies: Optional[List[str]] = None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        body=body,
litellm_changed_by=litellm_changed_by,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpdateTeamRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Update Team

     Use `/team/member_add` AND `/team/member/delete` to add/remove new team members

    You can now update team budget / rate limits via /team/update

    Parameters:
    - team_id: str - The team id of the user. Required param.
    - team_alias: Optional[str] - User defined team alias
    - team_member_permissions: Optional[List[str]] - A list of routes that non-admin team members can
    access. example: [\"/key/generate\", \"/key/update\", \"/key/delete\"]
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"team\": \"core-infra\", \"app\": \"app2\", \"email\": \"ishaan@berri.ai\" }
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - soft_budget: Optional[float] - The soft budget threshold for the team. If max_budget is set
    (either in the request or existing), soft_budget must be strictly lower than max_budget. Can be set
    independently if max_budget is not set.
    - budget_duration: Optional[str] - The duration of the budget for the team. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - prompts: Optional[List[str]] - List of prompts that the team is allowed to use.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.
    - tags: Optional[List[str]] - Tags for [tracking
    spend](https://litellm.vercel.app/docs/proxy/enterprise#tracking-spend-for-custom-tags) and/or doing
    [tag-based routing](https://litellm.vercel.app/docs/proxy/tag_routing).
    - organization_id: Optional[str] - The organization id of the team. Default is None. Create via
    `/organization/new`.
    - model_aliases: Optional[dict] - Model aliases for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/team_based_routing#create-team-with-model-alias)
    - guardrails: Optional[List[str]] - Guardrails for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/guardrails)
    - policies: Optional[List[str]] - Policies for the team.
    [Docs](https://docs.litellm.ai/docs/proxy/guardrails/guardrail_policies)
    - disable_global_guardrails: Optional[bool] - Whether to disable global guardrails for the key.
    - object_permission: Optional[LiteLLM_ObjectPermissionBase] - team-specific object permission.
    Example - {\"vector_stores\": [\"vector_store_1\", \"vector_store_2\"], \"agents\": [\"agent_1\",
    \"agent_2\"], \"agent_access_groups\": [\"dev_group\"]}. IF null or {} then no object permission.
    - team_member_budget: Optional[float] - The maximum budget allocated to an individual team member.
    - team_member_budget_duration: Optional[str] - The duration of the budget for the team member. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - team_member_rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for individual team
    members.
    - team_member_tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for individual team
    members.
    - team_member_key_duration: Optional[str] - The duration for a team member's key. e.g. \"1d\",
    \"1w\", \"1mo\"
    - allowed_passthrough_routes: Optional[List[str]] - List of allowed pass through routes for the
    team.
    - model_rpm_limit: Optional[Dict[str, int]] - The RPM (Requests Per Minute) limit per model for this
    team. Example: {\"gpt-4\": 100, \"gpt-3.5-turbo\": 200}
    - model_tpm_limit: Optional[Dict[str, int]] - The TPM (Tokens Per Minute) limit per model for this
    team. Example: {\"gpt-4\": 10000, \"gpt-3.5-turbo\": 20000}
    Example - update team TPM Limit
    - allowed_vector_store_indexes: Optional[List[dict]] - List of allowed vector store indexes for the
    key. Example - [{\"index_name\": \"my-index\", \"index_permissions\": [\"write\", \"read\"]}]. If
    specified, the key will only be able to use these specific vector store indexes. Create index, using
    `/v1/indexes` endpoint.
    - secret_manager_settings: Optional[dict] - Secret manager settings for the team.
    [Docs](https://docs.litellm.ai/docs/secret_managers/overview)
    - router_settings: Optional[UpdateRouterConfig] - team-specific router settings. Example -
    {\"model_group_retry_policy\": {\"max_retries\": 5}}. IF null or {} then no router settings.
    - access_group_ids: Optional[List[str]] - List of access group IDs to associate with the team.
    Access groups define which models the team can access. Example - [\"access_group_1\",
    \"access_group_2\"].

    ```
    curl --location 'http://0.0.0.0:4000/team/update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data-raw '{
        \"team_id\": \"8d916b1c-510d-4894-a334-1c16a93344f5\",
        \"tpm_limit\": 100
    }'
    ```

    Example - Update Team `max_budget` budget
    ```
    curl --location 'http://0.0.0.0:4000/team/update'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data-raw '{
        \"team_id\": \"8d916b1c-510d-4894-a334-1c16a93344f5\",
        \"max_budget\": 10
    }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (UpdateTeamRequest): UpdateTeamRequest, used by /team/update when you need to update
            a team

            team_id: str
            team_alias: Optional[str] = None
            organization_id: Optional[str] = None
            metadata: Optional[dict] = None
            tpm_limit: Optional[int] = None
            rpm_limit: Optional[int] = None
            max_budget: Optional[float] = None
            models: Optional[list] = None
            blocked: Optional[bool] = None
            budget_duration: Optional[str] = None
            guardrails: Optional[List[str]] = None
            policies: Optional[List[str]] = None

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    )).parsed
