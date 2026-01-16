from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.add_team_callback import AddTeamCallback
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    team_id: str,
    *,
    body: AddTeamCallback,
    litellm_changed_by: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(litellm_changed_by, Unset):
        headers["litellm-changed-by"] = litellm_changed_by



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/team/{team_id}/callback".format(team_id=quote(str(team_id), safe=""),),
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
    team_id: str,
    *,
    client: AuthenticatedClient,
    body: AddTeamCallback,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Add Team Callbacks

     Add a success/failure callback to a team

    Use this if if you want different teams to have different success/failure callbacks

    Parameters:
    - callback_name (Literal[\"langfuse\", \"langsmith\", \"gcs\"], required): The name of the callback
    to add
    - callback_type (Literal[\"success\", \"failure\", \"success_and_failure\"], required): The type of
    callback to add. One of:
        - \"success\": Callback for successful LLM calls
        - \"failure\": Callback for failed LLM calls
        - \"success_and_failure\": Callback for both successful and failed LLM calls
    - callback_vars (StandardCallbackDynamicParams, required): A dictionary of variables to pass to the
    callback
        - langfuse_public_key: The public key for the Langfuse callback
        - langfuse_secret_key: The secret key for the Langfuse callback
        - langfuse_secret: The secret for the Langfuse callback
        - langfuse_host: The host for the Langfuse callback
        - gcs_bucket_name: The name of the GCS bucket
        - gcs_path_service_account: The path to the GCS service account
        - langsmith_api_key: The API key for the Langsmith callback
        - langsmith_project: The project for the Langsmith callback
        - langsmith_base_url: The base URL for the Langsmith callback

    Example curl:
    ```
    curl -X POST 'http:/localhost:4000/team/dbe2f686-a686-4896-864a-4c3924458709/callback'         -H
    'Content-Type: application/json'         -H 'Authorization: Bearer sk-1234'         -d '{
        \"callback_name\": \"langfuse\",
        \"callback_type\": \"success\",
        \"callback_vars\": {\"langfuse_public_key\": \"pk-lf-xxxx1\", \"langfuse_secret_key\": \"sk-
    xxxxx\"}

    }'
    ```

    This means for the team where team_id = dbe2f686-a686-4896-864a-4c3924458709, all LLM calls will be
    logged to langfuse using the public key pk-lf-xxxx1 and the secret key sk-xxxxx

    Args:
        team_id (str):
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (AddTeamCallback):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
body=body,
litellm_changed_by=litellm_changed_by,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    team_id: str,
    *,
    client: AuthenticatedClient,
    body: AddTeamCallback,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Add Team Callbacks

     Add a success/failure callback to a team

    Use this if if you want different teams to have different success/failure callbacks

    Parameters:
    - callback_name (Literal[\"langfuse\", \"langsmith\", \"gcs\"], required): The name of the callback
    to add
    - callback_type (Literal[\"success\", \"failure\", \"success_and_failure\"], required): The type of
    callback to add. One of:
        - \"success\": Callback for successful LLM calls
        - \"failure\": Callback for failed LLM calls
        - \"success_and_failure\": Callback for both successful and failed LLM calls
    - callback_vars (StandardCallbackDynamicParams, required): A dictionary of variables to pass to the
    callback
        - langfuse_public_key: The public key for the Langfuse callback
        - langfuse_secret_key: The secret key for the Langfuse callback
        - langfuse_secret: The secret for the Langfuse callback
        - langfuse_host: The host for the Langfuse callback
        - gcs_bucket_name: The name of the GCS bucket
        - gcs_path_service_account: The path to the GCS service account
        - langsmith_api_key: The API key for the Langsmith callback
        - langsmith_project: The project for the Langsmith callback
        - langsmith_base_url: The base URL for the Langsmith callback

    Example curl:
    ```
    curl -X POST 'http:/localhost:4000/team/dbe2f686-a686-4896-864a-4c3924458709/callback'         -H
    'Content-Type: application/json'         -H 'Authorization: Bearer sk-1234'         -d '{
        \"callback_name\": \"langfuse\",
        \"callback_type\": \"success\",
        \"callback_vars\": {\"langfuse_public_key\": \"pk-lf-xxxx1\", \"langfuse_secret_key\": \"sk-
    xxxxx\"}

    }'
    ```

    This means for the team where team_id = dbe2f686-a686-4896-864a-4c3924458709, all LLM calls will be
    logged to langfuse using the public key pk-lf-xxxx1 and the secret key sk-xxxxx

    Args:
        team_id (str):
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (AddTeamCallback):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        team_id=team_id,
client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    ).parsed

async def asyncio_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient,
    body: AddTeamCallback,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Response[Any | HTTPValidationError]:
    r""" Add Team Callbacks

     Add a success/failure callback to a team

    Use this if if you want different teams to have different success/failure callbacks

    Parameters:
    - callback_name (Literal[\"langfuse\", \"langsmith\", \"gcs\"], required): The name of the callback
    to add
    - callback_type (Literal[\"success\", \"failure\", \"success_and_failure\"], required): The type of
    callback to add. One of:
        - \"success\": Callback for successful LLM calls
        - \"failure\": Callback for failed LLM calls
        - \"success_and_failure\": Callback for both successful and failed LLM calls
    - callback_vars (StandardCallbackDynamicParams, required): A dictionary of variables to pass to the
    callback
        - langfuse_public_key: The public key for the Langfuse callback
        - langfuse_secret_key: The secret key for the Langfuse callback
        - langfuse_secret: The secret for the Langfuse callback
        - langfuse_host: The host for the Langfuse callback
        - gcs_bucket_name: The name of the GCS bucket
        - gcs_path_service_account: The path to the GCS service account
        - langsmith_api_key: The API key for the Langsmith callback
        - langsmith_project: The project for the Langsmith callback
        - langsmith_base_url: The base URL for the Langsmith callback

    Example curl:
    ```
    curl -X POST 'http:/localhost:4000/team/dbe2f686-a686-4896-864a-4c3924458709/callback'         -H
    'Content-Type: application/json'         -H 'Authorization: Bearer sk-1234'         -d '{
        \"callback_name\": \"langfuse\",
        \"callback_type\": \"success\",
        \"callback_vars\": {\"langfuse_public_key\": \"pk-lf-xxxx1\", \"langfuse_secret_key\": \"sk-
    xxxxx\"}

    }'
    ```

    This means for the team where team_id = dbe2f686-a686-4896-864a-4c3924458709, all LLM calls will be
    logged to langfuse using the public key pk-lf-xxxx1 and the secret key sk-xxxxx

    Args:
        team_id (str):
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (AddTeamCallback):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
body=body,
litellm_changed_by=litellm_changed_by,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    team_id: str,
    *,
    client: AuthenticatedClient,
    body: AddTeamCallback,
    litellm_changed_by: None | str | Unset = UNSET,

) -> Any | HTTPValidationError | None:
    r""" Add Team Callbacks

     Add a success/failure callback to a team

    Use this if if you want different teams to have different success/failure callbacks

    Parameters:
    - callback_name (Literal[\"langfuse\", \"langsmith\", \"gcs\"], required): The name of the callback
    to add
    - callback_type (Literal[\"success\", \"failure\", \"success_and_failure\"], required): The type of
    callback to add. One of:
        - \"success\": Callback for successful LLM calls
        - \"failure\": Callback for failed LLM calls
        - \"success_and_failure\": Callback for both successful and failed LLM calls
    - callback_vars (StandardCallbackDynamicParams, required): A dictionary of variables to pass to the
    callback
        - langfuse_public_key: The public key for the Langfuse callback
        - langfuse_secret_key: The secret key for the Langfuse callback
        - langfuse_secret: The secret for the Langfuse callback
        - langfuse_host: The host for the Langfuse callback
        - gcs_bucket_name: The name of the GCS bucket
        - gcs_path_service_account: The path to the GCS service account
        - langsmith_api_key: The API key for the Langsmith callback
        - langsmith_project: The project for the Langsmith callback
        - langsmith_base_url: The base URL for the Langsmith callback

    Example curl:
    ```
    curl -X POST 'http:/localhost:4000/team/dbe2f686-a686-4896-864a-4c3924458709/callback'         -H
    'Content-Type: application/json'         -H 'Authorization: Bearer sk-1234'         -d '{
        \"callback_name\": \"langfuse\",
        \"callback_type\": \"success\",
        \"callback_vars\": {\"langfuse_public_key\": \"pk-lf-xxxx1\", \"langfuse_secret_key\": \"sk-
    xxxxx\"}

    }'
    ```

    This means for the team where team_id = dbe2f686-a686-4896-864a-4c3924458709, all LLM calls will be
    logged to langfuse using the public key pk-lf-xxxx1 and the secret key sk-xxxxx

    Args:
        team_id (str):
        litellm_changed_by (None | str | Unset): The litellm-changed-by header enables tracking of
            actions performed by authorized users on behalf of other users, providing an audit trail
            for accountability
        body (AddTeamCallback):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        team_id=team_id,
client=client,
body=body,
litellm_changed_by=litellm_changed_by,

    )).parsed
