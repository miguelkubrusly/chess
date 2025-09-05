from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_external_engine_acquire_body import ApiExternalEngineAcquireBody
from ...models.api_external_engine_acquire_response_200 import ApiExternalEngineAcquireResponse200
from typing import cast



def _get_kwargs(
    *,
    body: ApiExternalEngineAcquireBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/external-engine/work",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ApiExternalEngineAcquireResponse200]]:
    if response.status_code == 200:
        response_200 = ApiExternalEngineAcquireResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ApiExternalEngineAcquireResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiExternalEngineAcquireBody,

) -> Response[Union[Any, ApiExternalEngineAcquireResponse200]]:
    """ Acquire analysis request

     **Endpoint: `https://engine.lichess.ovh/api/external-engine/work`**
    Wait for an analysis requests to any of the external engines that
    have been registered with the given `secret`.
    Uses long polling.
    After acquiring a request, the provider should immediately
    [start streaming the results](#tag/External-engine/operation/apiExternalEngineSubmit).

    Args:
        body (ApiExternalEngineAcquireBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiExternalEngineAcquireResponse200]]
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
    client: Union[AuthenticatedClient, Client],
    body: ApiExternalEngineAcquireBody,

) -> Optional[Union[Any, ApiExternalEngineAcquireResponse200]]:
    """ Acquire analysis request

     **Endpoint: `https://engine.lichess.ovh/api/external-engine/work`**
    Wait for an analysis requests to any of the external engines that
    have been registered with the given `secret`.
    Uses long polling.
    After acquiring a request, the provider should immediately
    [start streaming the results](#tag/External-engine/operation/apiExternalEngineSubmit).

    Args:
        body (ApiExternalEngineAcquireBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiExternalEngineAcquireResponse200]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApiExternalEngineAcquireBody,

) -> Response[Union[Any, ApiExternalEngineAcquireResponse200]]:
    """ Acquire analysis request

     **Endpoint: `https://engine.lichess.ovh/api/external-engine/work`**
    Wait for an analysis requests to any of the external engines that
    have been registered with the given `secret`.
    Uses long polling.
    After acquiring a request, the provider should immediately
    [start streaming the results](#tag/External-engine/operation/apiExternalEngineSubmit).

    Args:
        body (ApiExternalEngineAcquireBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiExternalEngineAcquireResponse200]]
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
    client: Union[AuthenticatedClient, Client],
    body: ApiExternalEngineAcquireBody,

) -> Optional[Union[Any, ApiExternalEngineAcquireResponse200]]:
    """ Acquire analysis request

     **Endpoint: `https://engine.lichess.ovh/api/external-engine/work`**
    Wait for an analysis requests to any of the external engines that
    have been registered with the given `secret`.
    Uses long polling.
    After acquiring a request, the provider should immediately
    [start streaming the results](#tag/External-engine/operation/apiExternalEngineSubmit).

    Args:
        body (ApiExternalEngineAcquireBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiExternalEngineAcquireResponse200]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
