from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_swiss_terminate_response_200 import ApiSwissTerminateResponse200
from ...models.api_swiss_terminate_response_400 import ApiSwissTerminateResponse400
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/swiss/{id}/terminate".format(id=id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ApiSwissTerminateResponse200, ApiSwissTerminateResponse400]]:
    if response.status_code == 200:
        response_200 = ApiSwissTerminateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ApiSwissTerminateResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ApiSwissTerminateResponse200, ApiSwissTerminateResponse400]]:
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

) -> Response[Union[ApiSwissTerminateResponse200, ApiSwissTerminateResponse400]]:
    """ Terminate a Swiss tournament

     Terminate a Swiss tournament

    Args:
        id (str):  Example: W5FrxusN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiSwissTerminateResponse200, ApiSwissTerminateResponse400]]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[ApiSwissTerminateResponse200, ApiSwissTerminateResponse400]]:
    """ Terminate a Swiss tournament

     Terminate a Swiss tournament

    Args:
        id (str):  Example: W5FrxusN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiSwissTerminateResponse200, ApiSwissTerminateResponse400]
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[ApiSwissTerminateResponse200, ApiSwissTerminateResponse400]]:
    """ Terminate a Swiss tournament

     Terminate a Swiss tournament

    Args:
        id (str):  Example: W5FrxusN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiSwissTerminateResponse200, ApiSwissTerminateResponse400]]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[ApiSwissTerminateResponse200, ApiSwissTerminateResponse400]]:
    """ Terminate a Swiss tournament

     Terminate a Swiss tournament

    Args:
        id (str):  Example: W5FrxusN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiSwissTerminateResponse200, ApiSwissTerminateResponse400]
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
