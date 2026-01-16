from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.list_skills_response import ListSkillsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    limit: int | None | Unset = 10,
    after_id: None | str | Unset = UNSET,
    before_id: None | str | Unset = UNSET,
    custom_llm_provider: None | str | Unset = 'anthropic',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_after_id: None | str | Unset
    if isinstance(after_id, Unset):
        json_after_id = UNSET
    else:
        json_after_id = after_id
    params["after_id"] = json_after_id

    json_before_id: None | str | Unset
    if isinstance(before_id, Unset):
        json_before_id = UNSET
    else:
        json_before_id = before_id
    params["before_id"] = json_before_id

    json_custom_llm_provider: None | str | Unset
    if isinstance(custom_llm_provider, Unset):
        json_custom_llm_provider = UNSET
    else:
        json_custom_llm_provider = custom_llm_provider
    params["custom_llm_provider"] = json_custom_llm_provider


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/skills",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | ListSkillsResponse | None:
    if response.status_code == 200:
        response_200 = ListSkillsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | ListSkillsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = 10,
    after_id: None | str | Unset = UNSET,
    before_id: None | str | Unset = UNSET,
    custom_llm_provider: None | str | Unset = 'anthropic',

) -> Response[HTTPValidationError | ListSkillsResponse]:
    r""" List Skills

     List skills on Anthropic.

    Requires `?beta=true` query parameter.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: claude-account-1`
    - Pass model via query: `?model=claude-account-1`
    - Pass model via body: `{\"model\": \"claude-account-1\"}`

    Example usage:
    ```bash
    # Basic usage
    curl \"http://localhost:4000/v1/skills?beta=true&limit=10\"       -H \"Authorization: Bearer your-
    key\"

    # With model-based routing
    curl \"http://localhost:4000/v1/skills?beta=true&limit=10\"       -H \"Authorization: Bearer your-
    key\"       -H \"x-litellm-model: claude-account-1\"
    ```

    Returns: ListSkillsResponse with list of skills

    Args:
        limit (int | None | Unset):  Default: 10.
        after_id (None | str | Unset):
        before_id (None | str | Unset):
        custom_llm_provider (None | str | Unset):  Default: 'anthropic'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListSkillsResponse]
     """


    kwargs = _get_kwargs(
        limit=limit,
after_id=after_id,
before_id=before_id,
custom_llm_provider=custom_llm_provider,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = 10,
    after_id: None | str | Unset = UNSET,
    before_id: None | str | Unset = UNSET,
    custom_llm_provider: None | str | Unset = 'anthropic',

) -> HTTPValidationError | ListSkillsResponse | None:
    r""" List Skills

     List skills on Anthropic.

    Requires `?beta=true` query parameter.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: claude-account-1`
    - Pass model via query: `?model=claude-account-1`
    - Pass model via body: `{\"model\": \"claude-account-1\"}`

    Example usage:
    ```bash
    # Basic usage
    curl \"http://localhost:4000/v1/skills?beta=true&limit=10\"       -H \"Authorization: Bearer your-
    key\"

    # With model-based routing
    curl \"http://localhost:4000/v1/skills?beta=true&limit=10\"       -H \"Authorization: Bearer your-
    key\"       -H \"x-litellm-model: claude-account-1\"
    ```

    Returns: ListSkillsResponse with list of skills

    Args:
        limit (int | None | Unset):  Default: 10.
        after_id (None | str | Unset):
        before_id (None | str | Unset):
        custom_llm_provider (None | str | Unset):  Default: 'anthropic'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListSkillsResponse
     """


    return sync_detailed(
        client=client,
limit=limit,
after_id=after_id,
before_id=before_id,
custom_llm_provider=custom_llm_provider,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = 10,
    after_id: None | str | Unset = UNSET,
    before_id: None | str | Unset = UNSET,
    custom_llm_provider: None | str | Unset = 'anthropic',

) -> Response[HTTPValidationError | ListSkillsResponse]:
    r""" List Skills

     List skills on Anthropic.

    Requires `?beta=true` query parameter.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: claude-account-1`
    - Pass model via query: `?model=claude-account-1`
    - Pass model via body: `{\"model\": \"claude-account-1\"}`

    Example usage:
    ```bash
    # Basic usage
    curl \"http://localhost:4000/v1/skills?beta=true&limit=10\"       -H \"Authorization: Bearer your-
    key\"

    # With model-based routing
    curl \"http://localhost:4000/v1/skills?beta=true&limit=10\"       -H \"Authorization: Bearer your-
    key\"       -H \"x-litellm-model: claude-account-1\"
    ```

    Returns: ListSkillsResponse with list of skills

    Args:
        limit (int | None | Unset):  Default: 10.
        after_id (None | str | Unset):
        before_id (None | str | Unset):
        custom_llm_provider (None | str | Unset):  Default: 'anthropic'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListSkillsResponse]
     """


    kwargs = _get_kwargs(
        limit=limit,
after_id=after_id,
before_id=before_id,
custom_llm_provider=custom_llm_provider,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = 10,
    after_id: None | str | Unset = UNSET,
    before_id: None | str | Unset = UNSET,
    custom_llm_provider: None | str | Unset = 'anthropic',

) -> HTTPValidationError | ListSkillsResponse | None:
    r""" List Skills

     List skills on Anthropic.

    Requires `?beta=true` query parameter.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: claude-account-1`
    - Pass model via query: `?model=claude-account-1`
    - Pass model via body: `{\"model\": \"claude-account-1\"}`

    Example usage:
    ```bash
    # Basic usage
    curl \"http://localhost:4000/v1/skills?beta=true&limit=10\"       -H \"Authorization: Bearer your-
    key\"

    # With model-based routing
    curl \"http://localhost:4000/v1/skills?beta=true&limit=10\"       -H \"Authorization: Bearer your-
    key\"       -H \"x-litellm-model: claude-account-1\"
    ```

    Returns: ListSkillsResponse with list of skills

    Args:
        limit (int | None | Unset):  Default: 10.
        after_id (None | str | Unset):
        before_id (None | str | Unset):
        custom_llm_provider (None | str | Unset):  Default: 'anthropic'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListSkillsResponse
     """


    return (await asyncio_detailed(
        client=client,
limit=limit,
after_id=after_id,
before_id=before_id,
custom_llm_provider=custom_llm_provider,

    )).parsed
