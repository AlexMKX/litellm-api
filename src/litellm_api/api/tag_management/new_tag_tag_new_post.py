from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.tag_new_request import TagNewRequest
from typing import cast



def _get_kwargs(
    *,
    body: TagNewRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tag/new",
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
    body: TagNewRequest,

) -> Response[Any | HTTPValidationError]:
    """ New Tag

     Create a new tag.

    Parameters:
    - name: str - The name of the tag
    - description: Optional[str] - Description of what this tag represents
    - models: List[str] - List of either 'model_id' or 'model_name' allowed for this tag
    - budget_id: Optional[str] - The id for a budget (tpm/rpm/max budget) for the tag

    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - max_budget: Optional[float] - Max budget for tag
    - tpm_limit: Optional[int] - Max tpm limit for tag
    - rpm_limit: Optional[int] - Max rpm limit for tag
    - max_parallel_requests: Optional[int] - Max parallel requests for tag
    - soft_budget: Optional[float] - Get a slack alert when this soft budget is reached
    - model_max_budget: Optional[dict] - Max budget for a specific model
    - budget_duration: Optional[str] - Frequency of resetting tag budget

    Args:
        body (TagNewRequest):

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
    body: TagNewRequest,

) -> Any | HTTPValidationError | None:
    """ New Tag

     Create a new tag.

    Parameters:
    - name: str - The name of the tag
    - description: Optional[str] - Description of what this tag represents
    - models: List[str] - List of either 'model_id' or 'model_name' allowed for this tag
    - budget_id: Optional[str] - The id for a budget (tpm/rpm/max budget) for the tag

    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - max_budget: Optional[float] - Max budget for tag
    - tpm_limit: Optional[int] - Max tpm limit for tag
    - rpm_limit: Optional[int] - Max rpm limit for tag
    - max_parallel_requests: Optional[int] - Max parallel requests for tag
    - soft_budget: Optional[float] - Get a slack alert when this soft budget is reached
    - model_max_budget: Optional[dict] - Max budget for a specific model
    - budget_duration: Optional[str] - Frequency of resetting tag budget

    Args:
        body (TagNewRequest):

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
    body: TagNewRequest,

) -> Response[Any | HTTPValidationError]:
    """ New Tag

     Create a new tag.

    Parameters:
    - name: str - The name of the tag
    - description: Optional[str] - Description of what this tag represents
    - models: List[str] - List of either 'model_id' or 'model_name' allowed for this tag
    - budget_id: Optional[str] - The id for a budget (tpm/rpm/max budget) for the tag

    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - max_budget: Optional[float] - Max budget for tag
    - tpm_limit: Optional[int] - Max tpm limit for tag
    - rpm_limit: Optional[int] - Max rpm limit for tag
    - max_parallel_requests: Optional[int] - Max parallel requests for tag
    - soft_budget: Optional[float] - Get a slack alert when this soft budget is reached
    - model_max_budget: Optional[dict] - Max budget for a specific model
    - budget_duration: Optional[str] - Frequency of resetting tag budget

    Args:
        body (TagNewRequest):

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
    body: TagNewRequest,

) -> Any | HTTPValidationError | None:
    """ New Tag

     Create a new tag.

    Parameters:
    - name: str - The name of the tag
    - description: Optional[str] - Description of what this tag represents
    - models: List[str] - List of either 'model_id' or 'model_name' allowed for this tag
    - budget_id: Optional[str] - The id for a budget (tpm/rpm/max budget) for the tag

    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - max_budget: Optional[float] - Max budget for tag
    - tpm_limit: Optional[int] - Max tpm limit for tag
    - rpm_limit: Optional[int] - Max rpm limit for tag
    - max_parallel_requests: Optional[int] - Max parallel requests for tag
    - soft_budget: Optional[float] - Get a slack alert when this soft budget is reached
    - model_max_budget: Optional[dict] - Max budget for a specific model
    - budget_duration: Optional[str] - Frequency of resetting tag budget

    Args:
        body (TagNewRequest):

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
