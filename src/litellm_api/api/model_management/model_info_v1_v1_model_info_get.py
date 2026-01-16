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
    litellm_model_id: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_litellm_model_id: None | str | Unset
    if isinstance(litellm_model_id, Unset):
        json_litellm_model_id = UNSET
    else:
        json_litellm_model_id = litellm_model_id
    params["litellm_model_id"] = json_litellm_model_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/model/info",
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
    litellm_model_id: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Model Info V1

     Provides more info about each model in /models, including config.yaml descriptions (except api key
    and api base)

    Parameters:
        litellm_model_id: Optional[str] = None (this is the value of `x-litellm-model-id` returned in
    response headers)

        - When litellm_model_id is passed, it will return the info for that specific model
        - When litellm_model_id is not passed, it will return the info for all models

    Returns:
        Returns a dictionary containing information about each model.

    Example Response:
    ```json
    {
        \"data\": [
                    {
                        \"model_name\": \"fake-openai-endpoint\",
                        \"litellm_params\": {
                            \"api_base\": \"https://exampleopenaiendpoint-production.up.railway.app/\",
                            \"model\": \"openai/fake\"
                        },
                        \"model_info\": {
                            \"id\":
    \"112f74fab24a7a5245d2ced3536dd8f5f9192c57ee6e332af0f0512e08bed5af\",
                            \"db_model\": false
                        }
                    }
                ]
    }

    ```

    Args:
        litellm_model_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        litellm_model_id=litellm_model_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    litellm_model_id: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Model Info V1

     Provides more info about each model in /models, including config.yaml descriptions (except api key
    and api base)

    Parameters:
        litellm_model_id: Optional[str] = None (this is the value of `x-litellm-model-id` returned in
    response headers)

        - When litellm_model_id is passed, it will return the info for that specific model
        - When litellm_model_id is not passed, it will return the info for all models

    Returns:
        Returns a dictionary containing information about each model.

    Example Response:
    ```json
    {
        \"data\": [
                    {
                        \"model_name\": \"fake-openai-endpoint\",
                        \"litellm_params\": {
                            \"api_base\": \"https://exampleopenaiendpoint-production.up.railway.app/\",
                            \"model\": \"openai/fake\"
                        },
                        \"model_info\": {
                            \"id\":
    \"112f74fab24a7a5245d2ced3536dd8f5f9192c57ee6e332af0f0512e08bed5af\",
                            \"db_model\": false
                        }
                    }
                ]
    }

    ```

    Args:
        litellm_model_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        client=client,
litellm_model_id=litellm_model_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    litellm_model_id: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Model Info V1

     Provides more info about each model in /models, including config.yaml descriptions (except api key
    and api base)

    Parameters:
        litellm_model_id: Optional[str] = None (this is the value of `x-litellm-model-id` returned in
    response headers)

        - When litellm_model_id is passed, it will return the info for that specific model
        - When litellm_model_id is not passed, it will return the info for all models

    Returns:
        Returns a dictionary containing information about each model.

    Example Response:
    ```json
    {
        \"data\": [
                    {
                        \"model_name\": \"fake-openai-endpoint\",
                        \"litellm_params\": {
                            \"api_base\": \"https://exampleopenaiendpoint-production.up.railway.app/\",
                            \"model\": \"openai/fake\"
                        },
                        \"model_info\": {
                            \"id\":
    \"112f74fab24a7a5245d2ced3536dd8f5f9192c57ee6e332af0f0512e08bed5af\",
                            \"db_model\": false
                        }
                    }
                ]
    }

    ```

    Args:
        litellm_model_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        litellm_model_id=litellm_model_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    litellm_model_id: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Model Info V1

     Provides more info about each model in /models, including config.yaml descriptions (except api key
    and api base)

    Parameters:
        litellm_model_id: Optional[str] = None (this is the value of `x-litellm-model-id` returned in
    response headers)

        - When litellm_model_id is passed, it will return the info for that specific model
        - When litellm_model_id is not passed, it will return the info for all models

    Returns:
        Returns a dictionary containing information about each model.

    Example Response:
    ```json
    {
        \"data\": [
                    {
                        \"model_name\": \"fake-openai-endpoint\",
                        \"litellm_params\": {
                            \"api_base\": \"https://exampleopenaiendpoint-production.up.railway.app/\",
                            \"model\": \"openai/fake\"
                        },
                        \"model_info\": {
                            \"id\":
    \"112f74fab24a7a5245d2ced3536dd8f5f9192c57ee6e332af0f0512e08bed5af\",
                            \"db_model\": false
                        }
                    }
                ]
    }

    ```

    Args:
        litellm_model_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        client=client,
litellm_model_id=litellm_model_id,

    )).parsed
