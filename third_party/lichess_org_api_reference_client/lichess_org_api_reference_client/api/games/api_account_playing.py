from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_account_playing_response_200 import ApiAccountPlayingResponse200
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    nb: Union[Unset, int] = 9,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["nb"] = nb


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/account/playing",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ApiAccountPlayingResponse200]:
    if response.status_code == 200:
        response_200 = ApiAccountPlayingResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ApiAccountPlayingResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    nb: Union[Unset, int] = 9,

) -> Response[ApiAccountPlayingResponse200]:
    """ Get my ongoing games

     Get the ongoing games of the current user.
    Real-time and correspondence games are included.
    The most urgent games are listed first.

    Args:
        nb (Union[Unset, int]):  Default: 9.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAccountPlayingResponse200]
     """


    kwargs = _get_kwargs(
        nb=nb,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    nb: Union[Unset, int] = 9,

) -> Optional[ApiAccountPlayingResponse200]:
    """ Get my ongoing games

     Get the ongoing games of the current user.
    Real-time and correspondence games are included.
    The most urgent games are listed first.

    Args:
        nb (Union[Unset, int]):  Default: 9.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAccountPlayingResponse200
     """


    return sync_detailed(
        client=client,
nb=nb,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    nb: Union[Unset, int] = 9,

) -> Response[ApiAccountPlayingResponse200]:
    """ Get my ongoing games

     Get the ongoing games of the current user.
    Real-time and correspondence games are included.
    The most urgent games are listed first.

    Args:
        nb (Union[Unset, int]):  Default: 9.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiAccountPlayingResponse200]
     """


    kwargs = _get_kwargs(
        nb=nb,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    nb: Union[Unset, int] = 9,

) -> Optional[ApiAccountPlayingResponse200]:
    """ Get my ongoing games

     Get the ongoing games of the current user.
    Real-time and correspondence games are included.
    The most urgent games are listed first.

    Args:
        nb (Union[Unset, int]):  Default: 9.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiAccountPlayingResponse200
     """


    return (await asyncio_detailed(
        client=client,
nb=nb,

    )).parsed
