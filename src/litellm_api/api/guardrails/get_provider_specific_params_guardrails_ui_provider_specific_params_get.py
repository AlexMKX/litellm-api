from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/guardrails/ui/provider_specific_params",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    r""" Get Provider Specific Params

     Get provider-specific parameters for different guardrail types.

    Returns a dictionary mapping guardrail providers to their specific parameters,
    including parameter names, descriptions, and whether they are required.

    Example Response:
    ```json
    {
        \"bedrock\": {
            \"guardrailIdentifier\": {
                \"description\": \"The ID of your guardrail on Bedrock\",
                \"required\": true,
                \"type\": null
            },
            \"guardrailVersion\": {
                \"description\": \"The version of your Bedrock guardrail (e.g., DRAFT or version
    number)\",
                \"required\": true,
                \"type\": null
            }
        },
        \"azure_content_safety_text_moderation\": {
            \"api_key\": {
                \"description\": \"API key for the Azure Content Safety Text Moderation guardrail\",
                \"required\": false,
                \"type\": null
            },
            \"optional_params\": {
                \"description\": \"Optional parameters for the Azure Content Safety Text Moderation
    guardrail\",
                \"required\": true,
                \"type\": \"nested\",
                \"fields\": {
                    \"severity_threshold\": {
                        \"description\": \"Severity threshold for the Azure Content Safety Text
    Moderation guardrail across all categories\",
                        \"required\": false,
                        \"type\": null
                    },
                    \"categories\": {
                        \"description\": \"Categories to scan for the Azure Content Safety Text
    Moderation guardrail\",
                        \"required\": false,
                        \"type\": \"multiselect\",
                        \"options\": [\"Hate\", \"SelfHarm\", \"Sexual\", \"Violence\"],
                        \"default_value\": None
                    }
                }
            }
        }
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    r""" Get Provider Specific Params

     Get provider-specific parameters for different guardrail types.

    Returns a dictionary mapping guardrail providers to their specific parameters,
    including parameter names, descriptions, and whether they are required.

    Example Response:
    ```json
    {
        \"bedrock\": {
            \"guardrailIdentifier\": {
                \"description\": \"The ID of your guardrail on Bedrock\",
                \"required\": true,
                \"type\": null
            },
            \"guardrailVersion\": {
                \"description\": \"The version of your Bedrock guardrail (e.g., DRAFT or version
    number)\",
                \"required\": true,
                \"type\": null
            }
        },
        \"azure_content_safety_text_moderation\": {
            \"api_key\": {
                \"description\": \"API key for the Azure Content Safety Text Moderation guardrail\",
                \"required\": false,
                \"type\": null
            },
            \"optional_params\": {
                \"description\": \"Optional parameters for the Azure Content Safety Text Moderation
    guardrail\",
                \"required\": true,
                \"type\": \"nested\",
                \"fields\": {
                    \"severity_threshold\": {
                        \"description\": \"Severity threshold for the Azure Content Safety Text
    Moderation guardrail across all categories\",
                        \"required\": false,
                        \"type\": null
                    },
                    \"categories\": {
                        \"description\": \"Categories to scan for the Azure Content Safety Text
    Moderation guardrail\",
                        \"required\": false,
                        \"type\": \"multiselect\",
                        \"options\": [\"Hate\", \"SelfHarm\", \"Sexual\", \"Violence\"],
                        \"default_value\": None
                    }
                }
            }
        }
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

