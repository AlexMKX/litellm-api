from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_skill_response import DeleteSkillResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    skill_id: str,
    *,
    custom_llm_provider: None | str | Unset = 'anthropic',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_custom_llm_provider: None | str | Unset
    if isinstance(custom_llm_provider, Unset):
        json_custom_llm_provider = UNSET
    else:
        json_custom_llm_provider = custom_llm_provider
    params["custom_llm_provider"] = json_custom_llm_provider


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/skills/{skill_id}".format(skill_id=quote(str(skill_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteSkillResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DeleteSkillResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteSkillResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    skill_id: str,
    *,
    client: AuthenticatedClient,
    custom_llm_provider: None | str | Unset = 'anthropic',

) -> Response[DeleteSkillResponse | HTTPValidationError]:
    r""" Delete Skill

     Delete a skill by ID from Anthropic.

    Requires `?beta=true` query parameter.

    Note: Anthropic does not allow deleting skills with existing versions.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: claude-account-1`
    - Pass model via query: `?model=claude-account-1`
    - Pass model via body: `{\"model\": \"claude-account-1\"}`

    Example usage:
    ```bash
    # Basic usage
    curl -X DELETE \"http://localhost:4000/v1/skills/skill_123?beta=true\"       -H \"Authorization:
    Bearer your-key\"

    # With model-based routing
    curl -X DELETE \"http://localhost:4000/v1/skills/skill_123?beta=true\"       -H \"Authorization:
    Bearer your-key\"       -H \"x-litellm-model: claude-account-1\"
    ```

    Returns: DeleteSkillResponse with type=\"skill_deleted\"

    Args:
        skill_id (str):
        custom_llm_provider (None | str | Unset):  Default: 'anthropic'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSkillResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        skill_id=skill_id,
custom_llm_provider=custom_llm_provider,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    skill_id: str,
    *,
    client: AuthenticatedClient,
    custom_llm_provider: None | str | Unset = 'anthropic',

) -> DeleteSkillResponse | HTTPValidationError | None:
    r""" Delete Skill

     Delete a skill by ID from Anthropic.

    Requires `?beta=true` query parameter.

    Note: Anthropic does not allow deleting skills with existing versions.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: claude-account-1`
    - Pass model via query: `?model=claude-account-1`
    - Pass model via body: `{\"model\": \"claude-account-1\"}`

    Example usage:
    ```bash
    # Basic usage
    curl -X DELETE \"http://localhost:4000/v1/skills/skill_123?beta=true\"       -H \"Authorization:
    Bearer your-key\"

    # With model-based routing
    curl -X DELETE \"http://localhost:4000/v1/skills/skill_123?beta=true\"       -H \"Authorization:
    Bearer your-key\"       -H \"x-litellm-model: claude-account-1\"
    ```

    Returns: DeleteSkillResponse with type=\"skill_deleted\"

    Args:
        skill_id (str):
        custom_llm_provider (None | str | Unset):  Default: 'anthropic'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSkillResponse | HTTPValidationError
     """


    return sync_detailed(
        skill_id=skill_id,
client=client,
custom_llm_provider=custom_llm_provider,

    ).parsed

async def asyncio_detailed(
    skill_id: str,
    *,
    client: AuthenticatedClient,
    custom_llm_provider: None | str | Unset = 'anthropic',

) -> Response[DeleteSkillResponse | HTTPValidationError]:
    r""" Delete Skill

     Delete a skill by ID from Anthropic.

    Requires `?beta=true` query parameter.

    Note: Anthropic does not allow deleting skills with existing versions.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: claude-account-1`
    - Pass model via query: `?model=claude-account-1`
    - Pass model via body: `{\"model\": \"claude-account-1\"}`

    Example usage:
    ```bash
    # Basic usage
    curl -X DELETE \"http://localhost:4000/v1/skills/skill_123?beta=true\"       -H \"Authorization:
    Bearer your-key\"

    # With model-based routing
    curl -X DELETE \"http://localhost:4000/v1/skills/skill_123?beta=true\"       -H \"Authorization:
    Bearer your-key\"       -H \"x-litellm-model: claude-account-1\"
    ```

    Returns: DeleteSkillResponse with type=\"skill_deleted\"

    Args:
        skill_id (str):
        custom_llm_provider (None | str | Unset):  Default: 'anthropic'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSkillResponse | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        skill_id=skill_id,
custom_llm_provider=custom_llm_provider,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    skill_id: str,
    *,
    client: AuthenticatedClient,
    custom_llm_provider: None | str | Unset = 'anthropic',

) -> DeleteSkillResponse | HTTPValidationError | None:
    r""" Delete Skill

     Delete a skill by ID from Anthropic.

    Requires `?beta=true` query parameter.

    Note: Anthropic does not allow deleting skills with existing versions.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: claude-account-1`
    - Pass model via query: `?model=claude-account-1`
    - Pass model via body: `{\"model\": \"claude-account-1\"}`

    Example usage:
    ```bash
    # Basic usage
    curl -X DELETE \"http://localhost:4000/v1/skills/skill_123?beta=true\"       -H \"Authorization:
    Bearer your-key\"

    # With model-based routing
    curl -X DELETE \"http://localhost:4000/v1/skills/skill_123?beta=true\"       -H \"Authorization:
    Bearer your-key\"       -H \"x-litellm-model: claude-account-1\"
    ```

    Returns: DeleteSkillResponse with type=\"skill_deleted\"

    Args:
        skill_id (str):
        custom_llm_provider (None | str | Unset):  Default: 'anthropic'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSkillResponse | HTTPValidationError
     """


    return (await asyncio_detailed(
        skill_id=skill_id,
client=client,
custom_llm_provider=custom_llm_provider,

    )).parsed
