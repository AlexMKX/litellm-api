from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.skill import Skill
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
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
        "method": "post",
        "url": "/v1/skills",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | Skill | None:
    if response.status_code == 200:
        response_200 = Skill.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | Skill]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    custom_llm_provider: None | str | Unset = 'anthropic',

) -> Response[HTTPValidationError | Skill]:
    r""" Create Skill

     Create a new skill on Anthropic.

    Requires `?beta=true` query parameter.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: claude-account-1`
    - Pass model via query: `?model=claude-account-1`
    - Pass model via form field: `model=claude-account-1`

    Example usage:
    ```bash
    # Basic usage
    curl -X POST \"http://localhost:4000/v1/skills?beta=true\"       -H \"Content-Type: multipart/form-
    data\"       -H \"Authorization: Bearer your-key\"       -F \"display_title=My Skill\"       -F
    \"files[]=@skill.zip\"

    # With model-based routing
    curl -X POST \"http://localhost:4000/v1/skills?beta=true\"       -H \"Content-Type: multipart/form-
    data\"       -H \"Authorization: Bearer your-key\"       -H \"x-litellm-model: claude-account-1\"
    -F \"display_title=My Skill\"       -F \"files[]=@skill.zip\"
    ```

    Returns: Skill object with id, display_title, etc.

    Args:
        custom_llm_provider (None | str | Unset):  Default: 'anthropic'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Skill]
     """


    kwargs = _get_kwargs(
        custom_llm_provider=custom_llm_provider,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    custom_llm_provider: None | str | Unset = 'anthropic',

) -> HTTPValidationError | Skill | None:
    r""" Create Skill

     Create a new skill on Anthropic.

    Requires `?beta=true` query parameter.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: claude-account-1`
    - Pass model via query: `?model=claude-account-1`
    - Pass model via form field: `model=claude-account-1`

    Example usage:
    ```bash
    # Basic usage
    curl -X POST \"http://localhost:4000/v1/skills?beta=true\"       -H \"Content-Type: multipart/form-
    data\"       -H \"Authorization: Bearer your-key\"       -F \"display_title=My Skill\"       -F
    \"files[]=@skill.zip\"

    # With model-based routing
    curl -X POST \"http://localhost:4000/v1/skills?beta=true\"       -H \"Content-Type: multipart/form-
    data\"       -H \"Authorization: Bearer your-key\"       -H \"x-litellm-model: claude-account-1\"
    -F \"display_title=My Skill\"       -F \"files[]=@skill.zip\"
    ```

    Returns: Skill object with id, display_title, etc.

    Args:
        custom_llm_provider (None | str | Unset):  Default: 'anthropic'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Skill
     """


    return sync_detailed(
        client=client,
custom_llm_provider=custom_llm_provider,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    custom_llm_provider: None | str | Unset = 'anthropic',

) -> Response[HTTPValidationError | Skill]:
    r""" Create Skill

     Create a new skill on Anthropic.

    Requires `?beta=true` query parameter.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: claude-account-1`
    - Pass model via query: `?model=claude-account-1`
    - Pass model via form field: `model=claude-account-1`

    Example usage:
    ```bash
    # Basic usage
    curl -X POST \"http://localhost:4000/v1/skills?beta=true\"       -H \"Content-Type: multipart/form-
    data\"       -H \"Authorization: Bearer your-key\"       -F \"display_title=My Skill\"       -F
    \"files[]=@skill.zip\"

    # With model-based routing
    curl -X POST \"http://localhost:4000/v1/skills?beta=true\"       -H \"Content-Type: multipart/form-
    data\"       -H \"Authorization: Bearer your-key\"       -H \"x-litellm-model: claude-account-1\"
    -F \"display_title=My Skill\"       -F \"files[]=@skill.zip\"
    ```

    Returns: Skill object with id, display_title, etc.

    Args:
        custom_llm_provider (None | str | Unset):  Default: 'anthropic'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Skill]
     """


    kwargs = _get_kwargs(
        custom_llm_provider=custom_llm_provider,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    custom_llm_provider: None | str | Unset = 'anthropic',

) -> HTTPValidationError | Skill | None:
    r""" Create Skill

     Create a new skill on Anthropic.

    Requires `?beta=true` query parameter.

    Model-based routing (for multi-account support):
    - Pass model via header: `x-litellm-model: claude-account-1`
    - Pass model via query: `?model=claude-account-1`
    - Pass model via form field: `model=claude-account-1`

    Example usage:
    ```bash
    # Basic usage
    curl -X POST \"http://localhost:4000/v1/skills?beta=true\"       -H \"Content-Type: multipart/form-
    data\"       -H \"Authorization: Bearer your-key\"       -F \"display_title=My Skill\"       -F
    \"files[]=@skill.zip\"

    # With model-based routing
    curl -X POST \"http://localhost:4000/v1/skills?beta=true\"       -H \"Content-Type: multipart/form-
    data\"       -H \"Authorization: Bearer your-key\"       -H \"x-litellm-model: claude-account-1\"
    -F \"display_title=My Skill\"       -F \"files[]=@skill.zip\"
    ```

    Returns: Skill object with id, display_title, etc.

    Args:
        custom_llm_provider (None | str | Unset):  Default: 'anthropic'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Skill
     """


    return (await asyncio_detailed(
        client=client,
custom_llm_provider=custom_llm_provider,

    )).parsed
