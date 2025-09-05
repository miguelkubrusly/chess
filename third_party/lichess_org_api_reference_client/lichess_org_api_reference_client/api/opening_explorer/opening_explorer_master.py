from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.opening_explorer_master_response_200 import OpeningExplorerMasterResponse200
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    fen: Union[Unset, str] = UNSET,
    play: Union[Unset, str] = '',
    since: Union[Unset, float] = 1952.0,
    until: Union[Unset, float] = UNSET,
    moves: Union[Unset, float] = 12.0,
    top_games: Union[Unset, float] = 15.0,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["fen"] = fen

    params["play"] = play

    params["since"] = since

    params["until"] = until

    params["moves"] = moves

    params["topGames"] = top_games


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/masters",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[OpeningExplorerMasterResponse200]:
    if response.status_code == 200:
        response_200 = OpeningExplorerMasterResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[OpeningExplorerMasterResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fen: Union[Unset, str] = UNSET,
    play: Union[Unset, str] = '',
    since: Union[Unset, float] = 1952.0,
    until: Union[Unset, float] = UNSET,
    moves: Union[Unset, float] = 12.0,
    top_games: Union[Unset, float] = 15.0,

) -> Response[OpeningExplorerMasterResponse200]:
    """ Masters database

     **Endpoint: <https://explorer.lichess.ovh/masters>**

    Example: `curl https://explorer.lichess.ovh/masters?play=d2d4,d7d5,c2c4,c7c6,c4d5`

    Args:
        fen (Union[Unset, str]):
        play (Union[Unset, str]):  Default: ''.
        since (Union[Unset, float]):  Default: 1952.0.
        until (Union[Unset, float]):
        moves (Union[Unset, float]):  Default: 12.0.
        top_games (Union[Unset, float]):  Default: 15.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpeningExplorerMasterResponse200]
     """


    kwargs = _get_kwargs(
        fen=fen,
play=play,
since=since,
until=until,
moves=moves,
top_games=top_games,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    fen: Union[Unset, str] = UNSET,
    play: Union[Unset, str] = '',
    since: Union[Unset, float] = 1952.0,
    until: Union[Unset, float] = UNSET,
    moves: Union[Unset, float] = 12.0,
    top_games: Union[Unset, float] = 15.0,

) -> Optional[OpeningExplorerMasterResponse200]:
    """ Masters database

     **Endpoint: <https://explorer.lichess.ovh/masters>**

    Example: `curl https://explorer.lichess.ovh/masters?play=d2d4,d7d5,c2c4,c7c6,c4d5`

    Args:
        fen (Union[Unset, str]):
        play (Union[Unset, str]):  Default: ''.
        since (Union[Unset, float]):  Default: 1952.0.
        until (Union[Unset, float]):
        moves (Union[Unset, float]):  Default: 12.0.
        top_games (Union[Unset, float]):  Default: 15.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpeningExplorerMasterResponse200
     """


    return sync_detailed(
        client=client,
fen=fen,
play=play,
since=since,
until=until,
moves=moves,
top_games=top_games,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fen: Union[Unset, str] = UNSET,
    play: Union[Unset, str] = '',
    since: Union[Unset, float] = 1952.0,
    until: Union[Unset, float] = UNSET,
    moves: Union[Unset, float] = 12.0,
    top_games: Union[Unset, float] = 15.0,

) -> Response[OpeningExplorerMasterResponse200]:
    """ Masters database

     **Endpoint: <https://explorer.lichess.ovh/masters>**

    Example: `curl https://explorer.lichess.ovh/masters?play=d2d4,d7d5,c2c4,c7c6,c4d5`

    Args:
        fen (Union[Unset, str]):
        play (Union[Unset, str]):  Default: ''.
        since (Union[Unset, float]):  Default: 1952.0.
        until (Union[Unset, float]):
        moves (Union[Unset, float]):  Default: 12.0.
        top_games (Union[Unset, float]):  Default: 15.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpeningExplorerMasterResponse200]
     """


    kwargs = _get_kwargs(
        fen=fen,
play=play,
since=since,
until=until,
moves=moves,
top_games=top_games,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    fen: Union[Unset, str] = UNSET,
    play: Union[Unset, str] = '',
    since: Union[Unset, float] = 1952.0,
    until: Union[Unset, float] = UNSET,
    moves: Union[Unset, float] = 12.0,
    top_games: Union[Unset, float] = 15.0,

) -> Optional[OpeningExplorerMasterResponse200]:
    """ Masters database

     **Endpoint: <https://explorer.lichess.ovh/masters>**

    Example: `curl https://explorer.lichess.ovh/masters?play=d2d4,d7d5,c2c4,c7c6,c4d5`

    Args:
        fen (Union[Unset, str]):
        play (Union[Unset, str]):  Default: ''.
        since (Union[Unset, float]):  Default: 1952.0.
        until (Union[Unset, float]):
        moves (Union[Unset, float]):  Default: 12.0.
        top_games (Union[Unset, float]):  Default: 15.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpeningExplorerMasterResponse200
     """


    return (await asyncio_detailed(
        client=client,
fen=fen,
play=play,
since=since,
until=until,
moves=moves,
top_games=top_games,

    )).parsed
