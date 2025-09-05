from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_external_engine_create_body import ApiExternalEngineCreateBody
from ...models.api_external_engine_create_response_200 import ApiExternalEngineCreateResponse200
from typing import cast



def _get_kwargs(
    *,
    body: ApiExternalEngineCreateBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/external-engine",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ApiExternalEngineCreateResponse200]:
    if response.status_code == 200:
        response_200 = ApiExternalEngineCreateResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ApiExternalEngineCreateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiExternalEngineCreateBody,

) -> Response[ApiExternalEngineCreateResponse200]:
    """ Create external engine

     Registers a new external engine for the user. It can then be selected
    and used on the analysis board.
    After registering, the provider should start waiting for analyis requests.

    Args:
        body (ApiExternalEngineCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiExternalEngineCreateResponse200]
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
    body: ApiExternalEngineCreateBody,

) -> Optional[ApiExternalEngineCreateResponse200]:
    """ Create external engine

     Registers a new external engine for the user. It can then be selected
    and used on the analysis board.
    After registering, the provider should start waiting for analyis requests.

    Args:
        body (ApiExternalEngineCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiExternalEngineCreateResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiExternalEngineCreateBody,

) -> Response[ApiExternalEngineCreateResponse200]:
    """ Create external engine

     Registers a new external engine for the user. It can then be selected
    and used on the analysis board.
    After registering, the provider should start waiting for analyis requests.

    Args:
        body (ApiExternalEngineCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiExternalEngineCreateResponse200]
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
    body: ApiExternalEngineCreateBody,

) -> Optional[ApiExternalEngineCreateResponse200]:
    """ Create external engine

     Registers a new external engine for the user. It can then be selected
    and used on the analysis board.
    After registering, the provider should start waiting for analyis requests.

    Args:
        body (ApiExternalEngineCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiExternalEngineCreateResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
