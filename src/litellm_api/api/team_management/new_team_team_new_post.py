from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llm_team_table import LiteLLMTeamTable
from ...models.new_team_request import NewTeamRequest
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: NewTeamRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(litellm_changed_by, Unset):
        headers["litellm-changed-by"] = litellm_changed_by



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/team/new",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | LiteLLMTeamTable | None:
    if response.status_code == 200:
        response_200 = LiteLLMTeamTable.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | LiteLLMTeamTable]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NewTeamRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | LiteLLMTeamTable]:
    r""" New Team

     Allow users to create a new team. Apply user permissions to their team.

    👉 [Detailed Doc on setting team budgets](https://docs.litellm.ai/docs/proxy/team_budgets)


    Parameters:
    - team_alias: Optional[str] - User defined team alias
    - team_id: Optional[str] - The team id of the user. If none passed, we'll generate it.
    - members_with_roles: List[{\"role\": \"admin\" or \"user\", \"user_id\": \"<user-id>\"}] - A list
    of users and their roles in the team. Get user_id when making a new user via `/user/new`.
    - team_member_permissions: Optional[List[str]] - A list of routes that non-admin team members can
    access. example: [\"/key/generate\", \"/key/update\", \"/key/delete\"]
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"extra_info\": \"some info\"}
    - model_rpm_limit: Optional[Dict[str, int]] - The RPM (Requests Per Minute) limit for this team -
    applied across all keys for this team.
    - model_tpm_limit: Optional[Dict[str, int]] - The TPM (Tokens Per Minute) limit for this team -
    applied across all keys for this team.
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - rpm_limit_type: Optional[Literal[\"guaranteed_throughput\", \"best_effort_throughput\"]] - The
    type of RPM limit enforcement. Use \"guaranteed_throughput\" to raise an error if overallocating
    RPM, or \"best_effort_throughput\" for best effort enforcement.
    - tpm_limit_type: Optional[Literal[\"guaranteed_throughput\", \"best_effort_throughput\"]] - The
    type of TPM limit enforcement. Use \"guaranteed_throughput\" to raise an error if overallocating
    TPM, or \"best_effort_throughput\" for best effort enforcement.
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - soft_budget: Optional[float] - The soft budget threshold for the team. If max_budget is set,
    soft_budget must be strictly lower than max_budget. Can be set independently if max_budget is not
    set.
    - budget_duration: Optional[str] - The duration of the budget for the team. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.
    - members: Optional[List] - Control team members via `/team/member/add` and `/team/member/delete`.
    - tags: Optional[List[str]] - Tags for [tracking
    spend](https://litellm.vercel.app/docs/proxy/enterprise#tracking-spend-for-custom-tags) and/or doing
    [tag-based routing](https://litellm.vercel.app/docs/proxy/tag_routing).
    - prompts: Optional[List[str]] - List of prompts that the team is allowed to use.
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
    - team_member_rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for individual team
    members.
    - team_member_tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for individual team
    members.
    - team_member_key_duration: Optional[str] - The duration for a team member's key. e.g. \"1d\",
    \"1w\", \"1mo\"
    - allowed_passthrough_routes: Optional[List[str]] - List of allowed pass through routes for the
    team.
    - allowed_vector_store_indexes: Optional[List[dict]] - List of allowed vector store indexes for the
    key. Example - [{\"index_name\": \"my-index\", \"index_permissions\": [\"write\", \"read\"]}]. If
    specified, the key will only be able to use these specific vector store indexes. Create index, using
    `/v1/indexes` endpoint.
    - secret_manager_settings: Optional[dict] - Secret manager settings for the team.
    [Docs](https://docs.litellm.ai/docs/secret_managers/overview)
    - router_settings: Optional[UpdateRouterConfig] - team-specific router settings. Example -
    {\"model_group_retry_policy\": {\"max_retries\": 5}}. IF null or {} then no router settings.

    Returns:
    - team_id: (str) Unique team id - used for tracking spend across multiple keys for same team id.

    _deprecated_params:
    - admins: list - A list of user_id's for the admin role
    - users: list - A list of user_id's for the user role

    Example Request:
    ```
    curl --location 'http://0.0.0.0:4000/team/new'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
      \"team_alias\": \"my-new-team_2\",
      \"members_with_roles\": [{\"role\": \"admin\", \"user_id\": \"user-1234\"},
        {\"role\": \"user\", \"user_id\": \"user-2434\"}]
    }'

    ```

     ```
    curl --location 'http://0.0.0.0:4000/team/new'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
                \"team_alias\": \"QA Prod Bot\",
                \"max_budget\": 0.000000001,
                \"budget_duration\": \"1d\"
            }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (NewTeamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiteLLMTeamTable]
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
    body: NewTeamRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> HTTPValidationError | LiteLLMTeamTable | None:
    r""" New Team

     Allow users to create a new team. Apply user permissions to their team.

    👉 [Detailed Doc on setting team budgets](https://docs.litellm.ai/docs/proxy/team_budgets)


    Parameters:
    - team_alias: Optional[str] - User defined team alias
    - team_id: Optional[str] - The team id of the user. If none passed, we'll generate it.
    - members_with_roles: List[{\"role\": \"admin\" or \"user\", \"user_id\": \"<user-id>\"}] - A list
    of users and their roles in the team. Get user_id when making a new user via `/user/new`.
    - team_member_permissions: Optional[List[str]] - A list of routes that non-admin team members can
    access. example: [\"/key/generate\", \"/key/update\", \"/key/delete\"]
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"extra_info\": \"some info\"}
    - model_rpm_limit: Optional[Dict[str, int]] - The RPM (Requests Per Minute) limit for this team -
    applied across all keys for this team.
    - model_tpm_limit: Optional[Dict[str, int]] - The TPM (Tokens Per Minute) limit for this team -
    applied across all keys for this team.
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - rpm_limit_type: Optional[Literal[\"guaranteed_throughput\", \"best_effort_throughput\"]] - The
    type of RPM limit enforcement. Use \"guaranteed_throughput\" to raise an error if overallocating
    RPM, or \"best_effort_throughput\" for best effort enforcement.
    - tpm_limit_type: Optional[Literal[\"guaranteed_throughput\", \"best_effort_throughput\"]] - The
    type of TPM limit enforcement. Use \"guaranteed_throughput\" to raise an error if overallocating
    TPM, or \"best_effort_throughput\" for best effort enforcement.
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - soft_budget: Optional[float] - The soft budget threshold for the team. If max_budget is set,
    soft_budget must be strictly lower than max_budget. Can be set independently if max_budget is not
    set.
    - budget_duration: Optional[str] - The duration of the budget for the team. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.
    - members: Optional[List] - Control team members via `/team/member/add` and `/team/member/delete`.
    - tags: Optional[List[str]] - Tags for [tracking
    spend](https://litellm.vercel.app/docs/proxy/enterprise#tracking-spend-for-custom-tags) and/or doing
    [tag-based routing](https://litellm.vercel.app/docs/proxy/tag_routing).
    - prompts: Optional[List[str]] - List of prompts that the team is allowed to use.
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
    - team_member_rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for individual team
    members.
    - team_member_tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for individual team
    members.
    - team_member_key_duration: Optional[str] - The duration for a team member's key. e.g. \"1d\",
    \"1w\", \"1mo\"
    - allowed_passthrough_routes: Optional[List[str]] - List of allowed pass through routes for the
    team.
    - allowed_vector_store_indexes: Optional[List[dict]] - List of allowed vector store indexes for the
    key. Example - [{\"index_name\": \"my-index\", \"index_permissions\": [\"write\", \"read\"]}]. If
    specified, the key will only be able to use these specific vector store indexes. Create index, using
    `/v1/indexes` endpoint.
    - secret_manager_settings: Optional[dict] - Secret manager settings for the team.
    [Docs](https://docs.litellm.ai/docs/secret_managers/overview)
    - router_settings: Optional[UpdateRouterConfig] - team-specific router settings. Example -
    {\"model_group_retry_policy\": {\"max_retries\": 5}}. IF null or {} then no router settings.

    Returns:
    - team_id: (str) Unique team id - used for tracking spend across multiple keys for same team id.

    _deprecated_params:
    - admins: list - A list of user_id's for the admin role
    - users: list - A list of user_id's for the user role

    Example Request:
    ```
    curl --location 'http://0.0.0.0:4000/team/new'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
      \"team_alias\": \"my-new-team_2\",
      \"members_with_roles\": [{\"role\": \"admin\", \"user_id\": \"user-1234\"},
        {\"role\": \"user\", \"user_id\": \"user-2434\"}]
    }'

    ```

     ```
    curl --location 'http://0.0.0.0:4000/team/new'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
                \"team_alias\": \"QA Prod Bot\",
                \"max_budget\": 0.000000001,
                \"budget_duration\": \"1d\"
            }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (NewTeamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiteLLMTeamTable
     """


    return sync_detailed(
        client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewTeamRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[HTTPValidationError | LiteLLMTeamTable]:
    r""" New Team

     Allow users to create a new team. Apply user permissions to their team.

    👉 [Detailed Doc on setting team budgets](https://docs.litellm.ai/docs/proxy/team_budgets)


    Parameters:
    - team_alias: Optional[str] - User defined team alias
    - team_id: Optional[str] - The team id of the user. If none passed, we'll generate it.
    - members_with_roles: List[{\"role\": \"admin\" or \"user\", \"user_id\": \"<user-id>\"}] - A list
    of users and their roles in the team. Get user_id when making a new user via `/user/new`.
    - team_member_permissions: Optional[List[str]] - A list of routes that non-admin team members can
    access. example: [\"/key/generate\", \"/key/update\", \"/key/delete\"]
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"extra_info\": \"some info\"}
    - model_rpm_limit: Optional[Dict[str, int]] - The RPM (Requests Per Minute) limit for this team -
    applied across all keys for this team.
    - model_tpm_limit: Optional[Dict[str, int]] - The TPM (Tokens Per Minute) limit for this team -
    applied across all keys for this team.
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - rpm_limit_type: Optional[Literal[\"guaranteed_throughput\", \"best_effort_throughput\"]] - The
    type of RPM limit enforcement. Use \"guaranteed_throughput\" to raise an error if overallocating
    RPM, or \"best_effort_throughput\" for best effort enforcement.
    - tpm_limit_type: Optional[Literal[\"guaranteed_throughput\", \"best_effort_throughput\"]] - The
    type of TPM limit enforcement. Use \"guaranteed_throughput\" to raise an error if overallocating
    TPM, or \"best_effort_throughput\" for best effort enforcement.
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - soft_budget: Optional[float] - The soft budget threshold for the team. If max_budget is set,
    soft_budget must be strictly lower than max_budget. Can be set independently if max_budget is not
    set.
    - budget_duration: Optional[str] - The duration of the budget for the team. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.
    - members: Optional[List] - Control team members via `/team/member/add` and `/team/member/delete`.
    - tags: Optional[List[str]] - Tags for [tracking
    spend](https://litellm.vercel.app/docs/proxy/enterprise#tracking-spend-for-custom-tags) and/or doing
    [tag-based routing](https://litellm.vercel.app/docs/proxy/tag_routing).
    - prompts: Optional[List[str]] - List of prompts that the team is allowed to use.
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
    - team_member_rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for individual team
    members.
    - team_member_tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for individual team
    members.
    - team_member_key_duration: Optional[str] - The duration for a team member's key. e.g. \"1d\",
    \"1w\", \"1mo\"
    - allowed_passthrough_routes: Optional[List[str]] - List of allowed pass through routes for the
    team.
    - allowed_vector_store_indexes: Optional[List[dict]] - List of allowed vector store indexes for the
    key. Example - [{\"index_name\": \"my-index\", \"index_permissions\": [\"write\", \"read\"]}]. If
    specified, the key will only be able to use these specific vector store indexes. Create index, using
    `/v1/indexes` endpoint.
    - secret_manager_settings: Optional[dict] - Secret manager settings for the team.
    [Docs](https://docs.litellm.ai/docs/secret_managers/overview)
    - router_settings: Optional[UpdateRouterConfig] - team-specific router settings. Example -
    {\"model_group_retry_policy\": {\"max_retries\": 5}}. IF null or {} then no router settings.

    Returns:
    - team_id: (str) Unique team id - used for tracking spend across multiple keys for same team id.

    _deprecated_params:
    - admins: list - A list of user_id's for the admin role
    - users: list - A list of user_id's for the user role

    Example Request:
    ```
    curl --location 'http://0.0.0.0:4000/team/new'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
      \"team_alias\": \"my-new-team_2\",
      \"members_with_roles\": [{\"role\": \"admin\", \"user_id\": \"user-1234\"},
        {\"role\": \"user\", \"user_id\": \"user-2434\"}]
    }'

    ```

     ```
    curl --location 'http://0.0.0.0:4000/team/new'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
                \"team_alias\": \"QA Prod Bot\",
                \"max_budget\": 0.000000001,
                \"budget_duration\": \"1d\"
            }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (NewTeamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiteLLMTeamTable]
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
    body: NewTeamRequest,
    litellm_changed_by: None | str | Unset = UNSET,

) -> HTTPValidationError | LiteLLMTeamTable | None:
    r""" New Team

     Allow users to create a new team. Apply user permissions to their team.

    👉 [Detailed Doc on setting team budgets](https://docs.litellm.ai/docs/proxy/team_budgets)


    Parameters:
    - team_alias: Optional[str] - User defined team alias
    - team_id: Optional[str] - The team id of the user. If none passed, we'll generate it.
    - members_with_roles: List[{\"role\": \"admin\" or \"user\", \"user_id\": \"<user-id>\"}] - A list
    of users and their roles in the team. Get user_id when making a new user via `/user/new`.
    - team_member_permissions: Optional[List[str]] - A list of routes that non-admin team members can
    access. example: [\"/key/generate\", \"/key/update\", \"/key/delete\"]
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"extra_info\": \"some info\"}
    - model_rpm_limit: Optional[Dict[str, int]] - The RPM (Requests Per Minute) limit for this team -
    applied across all keys for this team.
    - model_tpm_limit: Optional[Dict[str, int]] - The TPM (Tokens Per Minute) limit for this team -
    applied across all keys for this team.
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - rpm_limit_type: Optional[Literal[\"guaranteed_throughput\", \"best_effort_throughput\"]] - The
    type of RPM limit enforcement. Use \"guaranteed_throughput\" to raise an error if overallocating
    RPM, or \"best_effort_throughput\" for best effort enforcement.
    - tpm_limit_type: Optional[Literal[\"guaranteed_throughput\", \"best_effort_throughput\"]] - The
    type of TPM limit enforcement. Use \"guaranteed_throughput\" to raise an error if overallocating
    TPM, or \"best_effort_throughput\" for best effort enforcement.
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - soft_budget: Optional[float] - The soft budget threshold for the team. If max_budget is set,
    soft_budget must be strictly lower than max_budget. Can be set independently if max_budget is not
    set.
    - budget_duration: Optional[str] - The duration of the budget for the team. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.
    - members: Optional[List] - Control team members via `/team/member/add` and `/team/member/delete`.
    - tags: Optional[List[str]] - Tags for [tracking
    spend](https://litellm.vercel.app/docs/proxy/enterprise#tracking-spend-for-custom-tags) and/or doing
    [tag-based routing](https://litellm.vercel.app/docs/proxy/tag_routing).
    - prompts: Optional[List[str]] - List of prompts that the team is allowed to use.
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
    - team_member_rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for individual team
    members.
    - team_member_tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for individual team
    members.
    - team_member_key_duration: Optional[str] - The duration for a team member's key. e.g. \"1d\",
    \"1w\", \"1mo\"
    - allowed_passthrough_routes: Optional[List[str]] - List of allowed pass through routes for the
    team.
    - allowed_vector_store_indexes: Optional[List[dict]] - List of allowed vector store indexes for the
    key. Example - [{\"index_name\": \"my-index\", \"index_permissions\": [\"write\", \"read\"]}]. If
    specified, the key will only be able to use these specific vector store indexes. Create index, using
    `/v1/indexes` endpoint.
    - secret_manager_settings: Optional[dict] - Secret manager settings for the team.
    [Docs](https://docs.litellm.ai/docs/secret_managers/overview)
    - router_settings: Optional[UpdateRouterConfig] - team-specific router settings. Example -
    {\"model_group_retry_policy\": {\"max_retries\": 5}}. IF null or {} then no router settings.

    Returns:
    - team_id: (str) Unique team id - used for tracking spend across multiple keys for same team id.

    _deprecated_params:
    - admins: list - A list of user_id's for the admin role
    - users: list - A list of user_id's for the user role

    Example Request:
    ```
    curl --location 'http://0.0.0.0:4000/team/new'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
      \"team_alias\": \"my-new-team_2\",
      \"members_with_roles\": [{\"role\": \"admin\", \"user_id\": \"user-1234\"},
        {\"role\": \"user\", \"user_id\": \"user-2434\"}]
    }'

    ```

     ```
    curl --location 'http://0.0.0.0:4000/team/new'     --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'     --data '{
                \"team_alias\": \"QA Prod Bot\",
                \"max_budget\": 0.000000001,
                \"budget_duration\": \"1d\"
            }'
    ```

    Args:
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (NewTeamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiteLLMTeamTable
     """


    return (await asyncio_detailed(
        client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    )).parsed
