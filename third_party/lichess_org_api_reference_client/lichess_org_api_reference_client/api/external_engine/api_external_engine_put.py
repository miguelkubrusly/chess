from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_external_engine_put_body import ApiExternalEnginePutBody
from ...models.api_external_engine_put_response_200 import ApiExternalEnginePutResponse200
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: ApiExternalEnginePutBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/external-engine/{id}".format(id=id,),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ApiExternalEnginePutResponse200]:
    if response.status_code == 200:
        response_200 = ApiExternalEnginePutResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ApiExternalEnginePutResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiExternalEnginePutBody,

) -> Response[ApiExternalEnginePutResponse200]:
    """ Update external engine

     Updates the properties of an external engine.

    Args:
        id (str):
        body (ApiExternalEnginePutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiExternalEnginePutResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiExternalEnginePutBody,

) -> Optional[ApiExternalEnginePutResponse200]:
    """ Update external engine

     Updates the properties of an external engine.

    Args:
        id (str):
        body (ApiExternalEnginePutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiExternalEnginePutResponse200
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiExternalEnginePutBody,

) -> Response[ApiExternalEnginePutResponse200]:
    """ Update external engine

     Updates the properties of an external engine.

    Args:
        id (str):
        body (ApiExternalEnginePutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiExternalEnginePutResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiExternalEnginePutBody,

) -> Optional[ApiExternalEnginePutResponse200]:
    """ Update external engine

     Updates the properties of an external engine.

    Args:
        id (str):
        body (ApiExternalEnginePutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiExternalEnginePutResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
