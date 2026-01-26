from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.register_plugin_request import RegisterPluginRequest
from typing import cast



def _get_kwargs(
    *,
    body: RegisterPluginRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/claude-code/plugins",
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
    body: RegisterPluginRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Register Plugin

     Register a plugin in the LiteLLM marketplace.

    LiteLLM acts as a registry/discovery layer. Plugins are hosted on
    GitHub/GitLab/Bitbucket. Claude Code will clone from the git source
    when users install.

    Parameters:
        - name: Plugin name (kebab-case)
        - source: Git source reference (github or url format)
        - version: Semantic version (optional)
        - description: Plugin description (optional)
        - author: Author information (optional)
        - homepage: Plugin homepage URL (optional)
        - keywords: Search keywords (optional)
        - category: Plugin category (optional)

    Returns:
        Registration status and plugin information.

    Example:
        ```bash
        curl -X POST http://localhost:4000/claude-code/plugins \
          -H \"Authorization: Bearer sk-...\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"name\": \"my-plugin\",
            \"source\": {\"source\": \"github\", \"repo\": \"org/my-plugin\"},
            \"version\": \"1.0.0\",
            \"description\": \"My awesome plugin\"
          }'
        ```

    Args:
        body (RegisterPluginRequest): Request body for registering a plugin in the marketplace.

            LiteLLM acts as a registry/discovery layer. Plugins are hosted on
            GitHub/GitLab/Bitbucket and referenced by their git source.

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
    body: RegisterPluginRequest,

) -> Any | HTTPValidationError | None:
    r""" Register Plugin

     Register a plugin in the LiteLLM marketplace.

    LiteLLM acts as a registry/discovery layer. Plugins are hosted on
    GitHub/GitLab/Bitbucket. Claude Code will clone from the git source
    when users install.

    Parameters:
        - name: Plugin name (kebab-case)
        - source: Git source reference (github or url format)
        - version: Semantic version (optional)
        - description: Plugin description (optional)
        - author: Author information (optional)
        - homepage: Plugin homepage URL (optional)
        - keywords: Search keywords (optional)
        - category: Plugin category (optional)

    Returns:
        Registration status and plugin information.

    Example:
        ```bash
        curl -X POST http://localhost:4000/claude-code/plugins \
          -H \"Authorization: Bearer sk-...\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"name\": \"my-plugin\",
            \"source\": {\"source\": \"github\", \"repo\": \"org/my-plugin\"},
            \"version\": \"1.0.0\",
            \"description\": \"My awesome plugin\"
          }'
        ```

    Args:
        body (RegisterPluginRequest): Request body for registering a plugin in the marketplace.

            LiteLLM acts as a registry/discovery layer. Plugins are hosted on
            GitHub/GitLab/Bitbucket and referenced by their git source.

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
    body: RegisterPluginRequest,

) -> Response[Any | HTTPValidationError]:
    r""" Register Plugin

     Register a plugin in the LiteLLM marketplace.

    LiteLLM acts as a registry/discovery layer. Plugins are hosted on
    GitHub/GitLab/Bitbucket. Claude Code will clone from the git source
    when users install.

    Parameters:
        - name: Plugin name (kebab-case)
        - source: Git source reference (github or url format)
        - version: Semantic version (optional)
        - description: Plugin description (optional)
        - author: Author information (optional)
        - homepage: Plugin homepage URL (optional)
        - keywords: Search keywords (optional)
        - category: Plugin category (optional)

    Returns:
        Registration status and plugin information.

    Example:
        ```bash
        curl -X POST http://localhost:4000/claude-code/plugins \
          -H \"Authorization: Bearer sk-...\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"name\": \"my-plugin\",
            \"source\": {\"source\": \"github\", \"repo\": \"org/my-plugin\"},
            \"version\": \"1.0.0\",
            \"description\": \"My awesome plugin\"
          }'
        ```

    Args:
        body (RegisterPluginRequest): Request body for registering a plugin in the marketplace.

            LiteLLM acts as a registry/discovery layer. Plugins are hosted on
            GitHub/GitLab/Bitbucket and referenced by their git source.

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
    body: RegisterPluginRequest,

) -> Any | HTTPValidationError | None:
    r""" Register Plugin

     Register a plugin in the LiteLLM marketplace.

    LiteLLM acts as a registry/discovery layer. Plugins are hosted on
    GitHub/GitLab/Bitbucket. Claude Code will clone from the git source
    when users install.

    Parameters:
        - name: Plugin name (kebab-case)
        - source: Git source reference (github or url format)
        - version: Semantic version (optional)
        - description: Plugin description (optional)
        - author: Author information (optional)
        - homepage: Plugin homepage URL (optional)
        - keywords: Search keywords (optional)
        - category: Plugin category (optional)

    Returns:
        Registration status and plugin information.

    Example:
        ```bash
        curl -X POST http://localhost:4000/claude-code/plugins \
          -H \"Authorization: Bearer sk-...\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"name\": \"my-plugin\",
            \"source\": {\"source\": \"github\", \"repo\": \"org/my-plugin\"},
            \"version\": \"1.0.0\",
            \"description\": \"My awesome plugin\"
          }'
        ```

    Args:
        body (RegisterPluginRequest): Request body for registering a plugin in the marketplace.

            LiteLLM acts as a registry/discovery layer. Plugins are hosted on
            GitHub/GitLab/Bitbucket and referenced by their git source.

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
