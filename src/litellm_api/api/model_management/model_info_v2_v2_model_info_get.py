from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    model: None | str | Unset = UNSET,
    user_models_only: bool | None | Unset = False,
    include_team_models: bool | None | Unset = False,
    debug: bool | None | Unset = False,
    page: int | Unset = 1,
    size: int | Unset = 50,
    search: None | str | Unset = UNSET,
    model_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    sort_order: None | str | Unset = 'asc',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_model: None | str | Unset
    if isinstance(model, Unset):
        json_model = UNSET
    else:
        json_model = model
    params["model"] = json_model

    json_user_models_only: bool | None | Unset
    if isinstance(user_models_only, Unset):
        json_user_models_only = UNSET
    else:
        json_user_models_only = user_models_only
    params["user_models_only"] = json_user_models_only

    json_include_team_models: bool | None | Unset
    if isinstance(include_team_models, Unset):
        json_include_team_models = UNSET
    else:
        json_include_team_models = include_team_models
    params["include_team_models"] = json_include_team_models

    json_debug: bool | None | Unset
    if isinstance(debug, Unset):
        json_debug = UNSET
    else:
        json_debug = debug
    params["debug"] = json_debug

    params["page"] = page

    params["size"] = size

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_model_id: None | str | Unset
    if isinstance(model_id, Unset):
        json_model_id = UNSET
    else:
        json_model_id = model_id
    params["modelId"] = json_model_id

    json_team_id: None | str | Unset
    if isinstance(team_id, Unset):
        json_team_id = UNSET
    else:
        json_team_id = team_id
    params["teamId"] = json_team_id

    json_sort_by: None | str | Unset
    if isinstance(sort_by, Unset):
        json_sort_by = UNSET
    else:
        json_sort_by = sort_by
    params["sortBy"] = json_sort_by

    json_sort_order: None | str | Unset
    if isinstance(sort_order, Unset):
        json_sort_order = UNSET
    else:
        json_sort_order = sort_order
    params["sortOrder"] = json_sort_order


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/model/info",
        "params": params,
    }


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
    model: None | str | Unset = UNSET,
    user_models_only: bool | None | Unset = False,
    include_team_models: bool | None | Unset = False,
    debug: bool | None | Unset = False,
    page: int | Unset = 1,
    size: int | Unset = 50,
    search: None | str | Unset = UNSET,
    model_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    sort_order: None | str | Unset = 'asc',

) -> Response[Any | HTTPValidationError]:
    r""" Model Info V2

     Paginated model metadata for proxy deployments (pricing, provider, team access).

    Returns configured router deployments with enriched `model_info` (costs, provider,
    context window, etc.). Sensitive fields such as API keys and api_base are omitted.

    Query parameters:
        model: Filter to a single public `model_name`.
        user_models_only: When true, only return models created by the calling user.
        include_team_models: When true, populate `access_via_team_ids` and `direct_access`
            on each model and filter to deployments the caller can use.
        page / size: Pagination controls (defaults: page=1, size=50).
        search: Case-insensitive partial match on model name or team public name.
        modelId: Return a single deployment by LiteLLM model id.
        teamId: Filter to models with direct access or team membership for this team id.
        sortBy / sortOrder: Sort by model_name, created_at, updated_at, costs, or status.

    Example request:
    ```
    curl -X GET 'http://localhost:4000/v2/model/info?include_team_models=true&page=1&size=50' \
    --header 'Authorization: Bearer sk-1234'
    ```

    Example response:
    ```json
    {
        \"data\": [
            {
                \"model_name\": \"gpt-4\",
                \"litellm_params\": {\"model\": \"openai/gpt-4.1\"},
                \"model_info\": {
                    \"id\": \"abc123\",
                    \"litellm_provider\": \"openai\",
                    \"access_via_team_ids\": [\"team-1\"],
                    \"direct_access\": true
                }
            }
        ],
        \"total_count\": 1,
        \"current_page\": 1,
        \"total_pages\": 1,
        \"size\": 50
    }
    ```

    Args:
        model (None | str | Unset): Specify the model name (optional)
        user_models_only (bool | None | Unset): Only return models added by this user Default:
            False.
        include_team_models (bool | None | Unset): Return all models across all teams user is in.
            Default: False.
        debug (bool | None | Unset):  Default: False.
        page (int | Unset): Page number Default: 1.
        size (int | Unset): Page size Default: 50.
        search (None | str | Unset): Search model names (case-insensitive partial match)
        model_id (None | str | Unset): Search for a specific model by its unique ID
        team_id (None | str | Unset): Filter models by team ID. Returns models with
            direct_access=True or teamId in access_via_team_ids
        sort_by (None | str | Unset): Field to sort by. Options: model_name, created_at,
            updated_at, costs, status
        sort_order (None | str | Unset): Sort order. Options: asc, desc Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        model=model,
user_models_only=user_models_only,
include_team_models=include_team_models,
debug=debug,
page=page,
size=size,
search=search,
model_id=model_id,
team_id=team_id,
sort_by=sort_by,
sort_order=sort_order,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    model: None | str | Unset = UNSET,
    user_models_only: bool | None | Unset = False,
    include_team_models: bool | None | Unset = False,
    debug: bool | None | Unset = False,
    page: int | Unset = 1,
    size: int | Unset = 50,
    search: None | str | Unset = UNSET,
    model_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    sort_order: None | str | Unset = 'asc',

) -> Any | HTTPValidationError | None:
    r""" Model Info V2

     Paginated model metadata for proxy deployments (pricing, provider, team access).

    Returns configured router deployments with enriched `model_info` (costs, provider,
    context window, etc.). Sensitive fields such as API keys and api_base are omitted.

    Query parameters:
        model: Filter to a single public `model_name`.
        user_models_only: When true, only return models created by the calling user.
        include_team_models: When true, populate `access_via_team_ids` and `direct_access`
            on each model and filter to deployments the caller can use.
        page / size: Pagination controls (defaults: page=1, size=50).
        search: Case-insensitive partial match on model name or team public name.
        modelId: Return a single deployment by LiteLLM model id.
        teamId: Filter to models with direct access or team membership for this team id.
        sortBy / sortOrder: Sort by model_name, created_at, updated_at, costs, or status.

    Example request:
    ```
    curl -X GET 'http://localhost:4000/v2/model/info?include_team_models=true&page=1&size=50' \
    --header 'Authorization: Bearer sk-1234'
    ```

    Example response:
    ```json
    {
        \"data\": [
            {
                \"model_name\": \"gpt-4\",
                \"litellm_params\": {\"model\": \"openai/gpt-4.1\"},
                \"model_info\": {
                    \"id\": \"abc123\",
                    \"litellm_provider\": \"openai\",
                    \"access_via_team_ids\": [\"team-1\"],
                    \"direct_access\": true
                }
            }
        ],
        \"total_count\": 1,
        \"current_page\": 1,
        \"total_pages\": 1,
        \"size\": 50
    }
    ```

    Args:
        model (None | str | Unset): Specify the model name (optional)
        user_models_only (bool | None | Unset): Only return models added by this user Default:
            False.
        include_team_models (bool | None | Unset): Return all models across all teams user is in.
            Default: False.
        debug (bool | None | Unset):  Default: False.
        page (int | Unset): Page number Default: 1.
        size (int | Unset): Page size Default: 50.
        search (None | str | Unset): Search model names (case-insensitive partial match)
        model_id (None | str | Unset): Search for a specific model by its unique ID
        team_id (None | str | Unset): Filter models by team ID. Returns models with
            direct_access=True or teamId in access_via_team_ids
        sort_by (None | str | Unset): Field to sort by. Options: model_name, created_at,
            updated_at, costs, status
        sort_order (None | str | Unset): Sort order. Options: asc, desc Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
model=model,
user_models_only=user_models_only,
include_team_models=include_team_models,
debug=debug,
page=page,
size=size,
search=search,
model_id=model_id,
team_id=team_id,
sort_by=sort_by,
sort_order=sort_order,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    model: None | str | Unset = UNSET,
    user_models_only: bool | None | Unset = False,
    include_team_models: bool | None | Unset = False,
    debug: bool | None | Unset = False,
    page: int | Unset = 1,
    size: int | Unset = 50,
    search: None | str | Unset = UNSET,
    model_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    sort_order: None | str | Unset = 'asc',

) -> Response[Any | HTTPValidationError]:
    r""" Model Info V2

     Paginated model metadata for proxy deployments (pricing, provider, team access).

    Returns configured router deployments with enriched `model_info` (costs, provider,
    context window, etc.). Sensitive fields such as API keys and api_base are omitted.

    Query parameters:
        model: Filter to a single public `model_name`.
        user_models_only: When true, only return models created by the calling user.
        include_team_models: When true, populate `access_via_team_ids` and `direct_access`
            on each model and filter to deployments the caller can use.
        page / size: Pagination controls (defaults: page=1, size=50).
        search: Case-insensitive partial match on model name or team public name.
        modelId: Return a single deployment by LiteLLM model id.
        teamId: Filter to models with direct access or team membership for this team id.
        sortBy / sortOrder: Sort by model_name, created_at, updated_at, costs, or status.

    Example request:
    ```
    curl -X GET 'http://localhost:4000/v2/model/info?include_team_models=true&page=1&size=50' \
    --header 'Authorization: Bearer sk-1234'
    ```

    Example response:
    ```json
    {
        \"data\": [
            {
                \"model_name\": \"gpt-4\",
                \"litellm_params\": {\"model\": \"openai/gpt-4.1\"},
                \"model_info\": {
                    \"id\": \"abc123\",
                    \"litellm_provider\": \"openai\",
                    \"access_via_team_ids\": [\"team-1\"],
                    \"direct_access\": true
                }
            }
        ],
        \"total_count\": 1,
        \"current_page\": 1,
        \"total_pages\": 1,
        \"size\": 50
    }
    ```

    Args:
        model (None | str | Unset): Specify the model name (optional)
        user_models_only (bool | None | Unset): Only return models added by this user Default:
            False.
        include_team_models (bool | None | Unset): Return all models across all teams user is in.
            Default: False.
        debug (bool | None | Unset):  Default: False.
        page (int | Unset): Page number Default: 1.
        size (int | Unset): Page size Default: 50.
        search (None | str | Unset): Search model names (case-insensitive partial match)
        model_id (None | str | Unset): Search for a specific model by its unique ID
        team_id (None | str | Unset): Filter models by team ID. Returns models with
            direct_access=True or teamId in access_via_team_ids
        sort_by (None | str | Unset): Field to sort by. Options: model_name, created_at,
            updated_at, costs, status
        sort_order (None | str | Unset): Sort order. Options: asc, desc Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        model=model,
user_models_only=user_models_only,
include_team_models=include_team_models,
debug=debug,
page=page,
size=size,
search=search,
model_id=model_id,
team_id=team_id,
sort_by=sort_by,
sort_order=sort_order,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    model: None | str | Unset = UNSET,
    user_models_only: bool | None | Unset = False,
    include_team_models: bool | None | Unset = False,
    debug: bool | None | Unset = False,
    page: int | Unset = 1,
    size: int | Unset = 50,
    search: None | str | Unset = UNSET,
    model_id: None | str | Unset = UNSET,
    team_id: None | str | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    sort_order: None | str | Unset = 'asc',

) -> Any | HTTPValidationError | None:
    r""" Model Info V2

     Paginated model metadata for proxy deployments (pricing, provider, team access).

    Returns configured router deployments with enriched `model_info` (costs, provider,
    context window, etc.). Sensitive fields such as API keys and api_base are omitted.

    Query parameters:
        model: Filter to a single public `model_name`.
        user_models_only: When true, only return models created by the calling user.
        include_team_models: When true, populate `access_via_team_ids` and `direct_access`
            on each model and filter to deployments the caller can use.
        page / size: Pagination controls (defaults: page=1, size=50).
        search: Case-insensitive partial match on model name or team public name.
        modelId: Return a single deployment by LiteLLM model id.
        teamId: Filter to models with direct access or team membership for this team id.
        sortBy / sortOrder: Sort by model_name, created_at, updated_at, costs, or status.

    Example request:
    ```
    curl -X GET 'http://localhost:4000/v2/model/info?include_team_models=true&page=1&size=50' \
    --header 'Authorization: Bearer sk-1234'
    ```

    Example response:
    ```json
    {
        \"data\": [
            {
                \"model_name\": \"gpt-4\",
                \"litellm_params\": {\"model\": \"openai/gpt-4.1\"},
                \"model_info\": {
                    \"id\": \"abc123\",
                    \"litellm_provider\": \"openai\",
                    \"access_via_team_ids\": [\"team-1\"],
                    \"direct_access\": true
                }
            }
        ],
        \"total_count\": 1,
        \"current_page\": 1,
        \"total_pages\": 1,
        \"size\": 50
    }
    ```

    Args:
        model (None | str | Unset): Specify the model name (optional)
        user_models_only (bool | None | Unset): Only return models added by this user Default:
            False.
        include_team_models (bool | None | Unset): Return all models across all teams user is in.
            Default: False.
        debug (bool | None | Unset):  Default: False.
        page (int | Unset): Page number Default: 1.
        size (int | Unset): Page size Default: 50.
        search (None | str | Unset): Search model names (case-insensitive partial match)
        model_id (None | str | Unset): Search for a specific model by its unique ID
        team_id (None | str | Unset): Filter models by team ID. Returns models with
            direct_access=True or teamId in access_via_team_ids
        sort_by (None | str | Unset): Field to sort by. Options: model_name, created_at,
            updated_at, costs, status
        sort_order (None | str | Unset): Sort order. Options: asc, desc Default: 'asc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
model=model,
user_models_only=user_models_only,
include_team_models=include_team_models,
debug=debug,
page=page,
size=size,
search=search,
model_id=model_id,
team_id=team_id,
sort_by=sort_by,
sort_order=sort_order,

    )).parsed
