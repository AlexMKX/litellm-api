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
    model_group: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_model_group: None | str | Unset
    if isinstance(model_group, Unset):
        json_model_group = UNSET
    else:
        json_model_group = model_group
    params["model_group"] = json_model_group


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/model_group/info",
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
    model_group: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Model Group Info

     Get information about all the deployments on litellm proxy, including config.yaml descriptions
    (except api key and api base)

    - /model_group/info returns all model groups. End users of proxy should use /model_group/info since
    those models will be used for /chat/completions, /embeddings, etc.
    - /model_group/info?model_group=rerank-english-v3.0 returns all model groups for a specific model
    group (`model_name` in config.yaml)



    Example Request (All Models):
    ```shell
    curl -X 'GET'     'http://localhost:4000/model_group/info'     -H 'accept: application/json'     -H
    'x-api-key: sk-1234'
    ```

    Example Request (Specific Model Group):
    ```shell
    curl -X 'GET'     'http://localhost:4000/model_group/info?model_group=rerank-english-v3.0'     -H
    'accept: application/json'     -H 'Authorization: Bearer sk-1234'
    ```

    Example Request (Specific Wildcard Model Group): (e.g. `model_name: openai/*` on config.yaml)
    ```shell
    curl -X 'GET'     'http://localhost:4000/model_group/info?model_group=openai/tts-1'
    -H 'accept: application/json'     -H 'Authorization: Bearersk-1234'
    ```

    Learn how to use and set wildcard models [here](https://docs.litellm.ai/docs/wildcard_routing)

    Example Response:
    ```json
        {
            \"data\": [
                {
                \"model_group\": \"rerank-english-v3.0\",
                \"providers\": [
                    \"cohere\"
                ],
                \"max_input_tokens\": null,
                \"max_output_tokens\": null,
                \"input_cost_per_token\": 0.0,
                \"output_cost_per_token\": 0.0,
                \"mode\": null,
                \"tpm\": null,
                \"rpm\": null,
                \"supports_parallel_function_calling\": false,
                \"supports_vision\": false,
                \"supports_function_calling\": false,
                \"supported_openai_params\": [
                    \"stream\",
                    \"temperature\",
                    \"max_tokens\",
                    \"logit_bias\",
                    \"top_p\",
                    \"frequency_penalty\",
                    \"presence_penalty\",
                    \"stop\",
                    \"n\",
                    \"extra_headers\"
                ]
                },
                {
                \"model_group\": \"gpt-3.5-turbo\",
                \"providers\": [
                    \"openai\"
                ],
                \"max_input_tokens\": 16385.0,
                \"max_output_tokens\": 4096.0,
                \"input_cost_per_token\": 1.5e-06,
                \"output_cost_per_token\": 2e-06,
                \"mode\": \"chat\",
                \"tpm\": null,
                \"rpm\": null,
                \"supports_parallel_function_calling\": false,
                \"supports_vision\": false,
                \"supports_function_calling\": true,
                \"supported_openai_params\": [
                    \"frequency_penalty\",
                    \"logit_bias\",
                    \"logprobs\",
                    \"top_logprobs\",
                    \"max_tokens\",
                    \"max_completion_tokens\",
                    \"n\",
                    \"presence_penalty\",
                    \"seed\",
                    \"stop\",
                    \"stream\",
                    \"stream_options\",
                    \"temperature\",
                    \"top_p\",
                    \"tools\",
                    \"tool_choice\",
                    \"function_call\",
                    \"functions\",
                    \"max_retries\",
                    \"extra_headers\",
                    \"parallel_tool_calls\",
                    \"response_format\"
                ]
                },
                {
                \"model_group\": \"llava-hf\",
                \"providers\": [
                    \"openai\"
                ],
                \"max_input_tokens\": null,
                \"max_output_tokens\": null,
                \"input_cost_per_token\": 0.0,
                \"output_cost_per_token\": 0.0,
                \"mode\": null,
                \"tpm\": null,
                \"rpm\": null,
                \"supports_parallel_function_calling\": false,
                \"supports_vision\": true,
                \"supports_function_calling\": false,
                \"supported_openai_params\": [
                    \"frequency_penalty\",
                    \"logit_bias\",
                    \"logprobs\",
                    \"top_logprobs\",
                    \"max_tokens\",
                    \"max_completion_tokens\",
                    \"n\",
                    \"presence_penalty\",
                    \"seed\",
                    \"stop\",
                    \"stream\",
                    \"stream_options\",
                    \"temperature\",
                    \"top_p\",
                    \"tools\",
                    \"tool_choice\",
                    \"function_call\",
                    \"functions\",
                    \"max_retries\",
                    \"extra_headers\",
                    \"parallel_tool_calls\",
                    \"response_format\"
                ]
                }
            ]
            }
    ```

    Args:
        model_group (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        model_group=model_group,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    model_group: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Model Group Info

     Get information about all the deployments on litellm proxy, including config.yaml descriptions
    (except api key and api base)

    - /model_group/info returns all model groups. End users of proxy should use /model_group/info since
    those models will be used for /chat/completions, /embeddings, etc.
    - /model_group/info?model_group=rerank-english-v3.0 returns all model groups for a specific model
    group (`model_name` in config.yaml)



    Example Request (All Models):
    ```shell
    curl -X 'GET'     'http://localhost:4000/model_group/info'     -H 'accept: application/json'     -H
    'x-api-key: sk-1234'
    ```

    Example Request (Specific Model Group):
    ```shell
    curl -X 'GET'     'http://localhost:4000/model_group/info?model_group=rerank-english-v3.0'     -H
    'accept: application/json'     -H 'Authorization: Bearer sk-1234'
    ```

    Example Request (Specific Wildcard Model Group): (e.g. `model_name: openai/*` on config.yaml)
    ```shell
    curl -X 'GET'     'http://localhost:4000/model_group/info?model_group=openai/tts-1'
    -H 'accept: application/json'     -H 'Authorization: Bearersk-1234'
    ```

    Learn how to use and set wildcard models [here](https://docs.litellm.ai/docs/wildcard_routing)

    Example Response:
    ```json
        {
            \"data\": [
                {
                \"model_group\": \"rerank-english-v3.0\",
                \"providers\": [
                    \"cohere\"
                ],
                \"max_input_tokens\": null,
                \"max_output_tokens\": null,
                \"input_cost_per_token\": 0.0,
                \"output_cost_per_token\": 0.0,
                \"mode\": null,
                \"tpm\": null,
                \"rpm\": null,
                \"supports_parallel_function_calling\": false,
                \"supports_vision\": false,
                \"supports_function_calling\": false,
                \"supported_openai_params\": [
                    \"stream\",
                    \"temperature\",
                    \"max_tokens\",
                    \"logit_bias\",
                    \"top_p\",
                    \"frequency_penalty\",
                    \"presence_penalty\",
                    \"stop\",
                    \"n\",
                    \"extra_headers\"
                ]
                },
                {
                \"model_group\": \"gpt-3.5-turbo\",
                \"providers\": [
                    \"openai\"
                ],
                \"max_input_tokens\": 16385.0,
                \"max_output_tokens\": 4096.0,
                \"input_cost_per_token\": 1.5e-06,
                \"output_cost_per_token\": 2e-06,
                \"mode\": \"chat\",
                \"tpm\": null,
                \"rpm\": null,
                \"supports_parallel_function_calling\": false,
                \"supports_vision\": false,
                \"supports_function_calling\": true,
                \"supported_openai_params\": [
                    \"frequency_penalty\",
                    \"logit_bias\",
                    \"logprobs\",
                    \"top_logprobs\",
                    \"max_tokens\",
                    \"max_completion_tokens\",
                    \"n\",
                    \"presence_penalty\",
                    \"seed\",
                    \"stop\",
                    \"stream\",
                    \"stream_options\",
                    \"temperature\",
                    \"top_p\",
                    \"tools\",
                    \"tool_choice\",
                    \"function_call\",
                    \"functions\",
                    \"max_retries\",
                    \"extra_headers\",
                    \"parallel_tool_calls\",
                    \"response_format\"
                ]
                },
                {
                \"model_group\": \"llava-hf\",
                \"providers\": [
                    \"openai\"
                ],
                \"max_input_tokens\": null,
                \"max_output_tokens\": null,
                \"input_cost_per_token\": 0.0,
                \"output_cost_per_token\": 0.0,
                \"mode\": null,
                \"tpm\": null,
                \"rpm\": null,
                \"supports_parallel_function_calling\": false,
                \"supports_vision\": true,
                \"supports_function_calling\": false,
                \"supported_openai_params\": [
                    \"frequency_penalty\",
                    \"logit_bias\",
                    \"logprobs\",
                    \"top_logprobs\",
                    \"max_tokens\",
                    \"max_completion_tokens\",
                    \"n\",
                    \"presence_penalty\",
                    \"seed\",
                    \"stop\",
                    \"stream\",
                    \"stream_options\",
                    \"temperature\",
                    \"top_p\",
                    \"tools\",
                    \"tool_choice\",
                    \"function_call\",
                    \"functions\",
                    \"max_retries\",
                    \"extra_headers\",
                    \"parallel_tool_calls\",
                    \"response_format\"
                ]
                }
            ]
            }
    ```

    Args:
        model_group (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
model_group=model_group,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    model_group: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Model Group Info

     Get information about all the deployments on litellm proxy, including config.yaml descriptions
    (except api key and api base)

    - /model_group/info returns all model groups. End users of proxy should use /model_group/info since
    those models will be used for /chat/completions, /embeddings, etc.
    - /model_group/info?model_group=rerank-english-v3.0 returns all model groups for a specific model
    group (`model_name` in config.yaml)



    Example Request (All Models):
    ```shell
    curl -X 'GET'     'http://localhost:4000/model_group/info'     -H 'accept: application/json'     -H
    'x-api-key: sk-1234'
    ```

    Example Request (Specific Model Group):
    ```shell
    curl -X 'GET'     'http://localhost:4000/model_group/info?model_group=rerank-english-v3.0'     -H
    'accept: application/json'     -H 'Authorization: Bearer sk-1234'
    ```

    Example Request (Specific Wildcard Model Group): (e.g. `model_name: openai/*` on config.yaml)
    ```shell
    curl -X 'GET'     'http://localhost:4000/model_group/info?model_group=openai/tts-1'
    -H 'accept: application/json'     -H 'Authorization: Bearersk-1234'
    ```

    Learn how to use and set wildcard models [here](https://docs.litellm.ai/docs/wildcard_routing)

    Example Response:
    ```json
        {
            \"data\": [
                {
                \"model_group\": \"rerank-english-v3.0\",
                \"providers\": [
                    \"cohere\"
                ],
                \"max_input_tokens\": null,
                \"max_output_tokens\": null,
                \"input_cost_per_token\": 0.0,
                \"output_cost_per_token\": 0.0,
                \"mode\": null,
                \"tpm\": null,
                \"rpm\": null,
                \"supports_parallel_function_calling\": false,
                \"supports_vision\": false,
                \"supports_function_calling\": false,
                \"supported_openai_params\": [
                    \"stream\",
                    \"temperature\",
                    \"max_tokens\",
                    \"logit_bias\",
                    \"top_p\",
                    \"frequency_penalty\",
                    \"presence_penalty\",
                    \"stop\",
                    \"n\",
                    \"extra_headers\"
                ]
                },
                {
                \"model_group\": \"gpt-3.5-turbo\",
                \"providers\": [
                    \"openai\"
                ],
                \"max_input_tokens\": 16385.0,
                \"max_output_tokens\": 4096.0,
                \"input_cost_per_token\": 1.5e-06,
                \"output_cost_per_token\": 2e-06,
                \"mode\": \"chat\",
                \"tpm\": null,
                \"rpm\": null,
                \"supports_parallel_function_calling\": false,
                \"supports_vision\": false,
                \"supports_function_calling\": true,
                \"supported_openai_params\": [
                    \"frequency_penalty\",
                    \"logit_bias\",
                    \"logprobs\",
                    \"top_logprobs\",
                    \"max_tokens\",
                    \"max_completion_tokens\",
                    \"n\",
                    \"presence_penalty\",
                    \"seed\",
                    \"stop\",
                    \"stream\",
                    \"stream_options\",
                    \"temperature\",
                    \"top_p\",
                    \"tools\",
                    \"tool_choice\",
                    \"function_call\",
                    \"functions\",
                    \"max_retries\",
                    \"extra_headers\",
                    \"parallel_tool_calls\",
                    \"response_format\"
                ]
                },
                {
                \"model_group\": \"llava-hf\",
                \"providers\": [
                    \"openai\"
                ],
                \"max_input_tokens\": null,
                \"max_output_tokens\": null,
                \"input_cost_per_token\": 0.0,
                \"output_cost_per_token\": 0.0,
                \"mode\": null,
                \"tpm\": null,
                \"rpm\": null,
                \"supports_parallel_function_calling\": false,
                \"supports_vision\": true,
                \"supports_function_calling\": false,
                \"supported_openai_params\": [
                    \"frequency_penalty\",
                    \"logit_bias\",
                    \"logprobs\",
                    \"top_logprobs\",
                    \"max_tokens\",
                    \"max_completion_tokens\",
                    \"n\",
                    \"presence_penalty\",
                    \"seed\",
                    \"stop\",
                    \"stream\",
                    \"stream_options\",
                    \"temperature\",
                    \"top_p\",
                    \"tools\",
                    \"tool_choice\",
                    \"function_call\",
                    \"functions\",
                    \"max_retries\",
                    \"extra_headers\",
                    \"parallel_tool_calls\",
                    \"response_format\"
                ]
                }
            ]
            }
    ```

    Args:
        model_group (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        model_group=model_group,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    model_group: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Model Group Info

     Get information about all the deployments on litellm proxy, including config.yaml descriptions
    (except api key and api base)

    - /model_group/info returns all model groups. End users of proxy should use /model_group/info since
    those models will be used for /chat/completions, /embeddings, etc.
    - /model_group/info?model_group=rerank-english-v3.0 returns all model groups for a specific model
    group (`model_name` in config.yaml)



    Example Request (All Models):
    ```shell
    curl -X 'GET'     'http://localhost:4000/model_group/info'     -H 'accept: application/json'     -H
    'x-api-key: sk-1234'
    ```

    Example Request (Specific Model Group):
    ```shell
    curl -X 'GET'     'http://localhost:4000/model_group/info?model_group=rerank-english-v3.0'     -H
    'accept: application/json'     -H 'Authorization: Bearer sk-1234'
    ```

    Example Request (Specific Wildcard Model Group): (e.g. `model_name: openai/*` on config.yaml)
    ```shell
    curl -X 'GET'     'http://localhost:4000/model_group/info?model_group=openai/tts-1'
    -H 'accept: application/json'     -H 'Authorization: Bearersk-1234'
    ```

    Learn how to use and set wildcard models [here](https://docs.litellm.ai/docs/wildcard_routing)

    Example Response:
    ```json
        {
            \"data\": [
                {
                \"model_group\": \"rerank-english-v3.0\",
                \"providers\": [
                    \"cohere\"
                ],
                \"max_input_tokens\": null,
                \"max_output_tokens\": null,
                \"input_cost_per_token\": 0.0,
                \"output_cost_per_token\": 0.0,
                \"mode\": null,
                \"tpm\": null,
                \"rpm\": null,
                \"supports_parallel_function_calling\": false,
                \"supports_vision\": false,
                \"supports_function_calling\": false,
                \"supported_openai_params\": [
                    \"stream\",
                    \"temperature\",
                    \"max_tokens\",
                    \"logit_bias\",
                    \"top_p\",
                    \"frequency_penalty\",
                    \"presence_penalty\",
                    \"stop\",
                    \"n\",
                    \"extra_headers\"
                ]
                },
                {
                \"model_group\": \"gpt-3.5-turbo\",
                \"providers\": [
                    \"openai\"
                ],
                \"max_input_tokens\": 16385.0,
                \"max_output_tokens\": 4096.0,
                \"input_cost_per_token\": 1.5e-06,
                \"output_cost_per_token\": 2e-06,
                \"mode\": \"chat\",
                \"tpm\": null,
                \"rpm\": null,
                \"supports_parallel_function_calling\": false,
                \"supports_vision\": false,
                \"supports_function_calling\": true,
                \"supported_openai_params\": [
                    \"frequency_penalty\",
                    \"logit_bias\",
                    \"logprobs\",
                    \"top_logprobs\",
                    \"max_tokens\",
                    \"max_completion_tokens\",
                    \"n\",
                    \"presence_penalty\",
                    \"seed\",
                    \"stop\",
                    \"stream\",
                    \"stream_options\",
                    \"temperature\",
                    \"top_p\",
                    \"tools\",
                    \"tool_choice\",
                    \"function_call\",
                    \"functions\",
                    \"max_retries\",
                    \"extra_headers\",
                    \"parallel_tool_calls\",
                    \"response_format\"
                ]
                },
                {
                \"model_group\": \"llava-hf\",
                \"providers\": [
                    \"openai\"
                ],
                \"max_input_tokens\": null,
                \"max_output_tokens\": null,
                \"input_cost_per_token\": 0.0,
                \"output_cost_per_token\": 0.0,
                \"mode\": null,
                \"tpm\": null,
                \"rpm\": null,
                \"supports_parallel_function_calling\": false,
                \"supports_vision\": true,
                \"supports_function_calling\": false,
                \"supported_openai_params\": [
                    \"frequency_penalty\",
                    \"logit_bias\",
                    \"logprobs\",
                    \"top_logprobs\",
                    \"max_tokens\",
                    \"max_completion_tokens\",
                    \"n\",
                    \"presence_penalty\",
                    \"seed\",
                    \"stop\",
                    \"stream\",
                    \"stream_options\",
                    \"temperature\",
                    \"top_p\",
                    \"tools\",
                    \"tool_choice\",
                    \"function_call\",
                    \"functions\",
                    \"max_retries\",
                    \"extra_headers\",
                    \"parallel_tool_calls\",
                    \"response_format\"
                ]
                }
            ]
            }
    ```

    Args:
        model_group (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
model_group=model_group,

    )).parsed
