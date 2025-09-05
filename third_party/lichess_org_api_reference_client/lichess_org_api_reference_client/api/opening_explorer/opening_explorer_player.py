from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.opening_explorer_player_color import OpeningExplorerPlayerColor
from ...models.opening_explorer_player_modes_item import OpeningExplorerPlayerModesItem
from ...models.opening_explorer_player_speeds_item import OpeningExplorerPlayerSpeedsItem
from ...models.opening_explorer_player_variant import OpeningExplorerPlayerVariant
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    player: str,
    color: OpeningExplorerPlayerColor,
    variant: Union[Unset, OpeningExplorerPlayerVariant] = OpeningExplorerPlayerVariant.STANDARD,
    fen: Union[Unset, str] = UNSET,
    play: Union[Unset, str] = '',
    speeds: Union[Unset, list[OpeningExplorerPlayerSpeedsItem]] = UNSET,
    modes: Union[Unset, list[OpeningExplorerPlayerModesItem]] = UNSET,
    since: Union[Unset, str] = '1952-01',
    until: Union[Unset, str] = '3000-12',
    moves: Union[Unset, float] = UNSET,
    recent_games: Union[Unset, float] = 8.0,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["player"] = player

    json_color = color.value
    params["color"] = json_color

    json_variant: Union[Unset, str] = UNSET
    if not isinstance(variant, Unset):
        json_variant = variant.value

    params["variant"] = json_variant

    params["fen"] = fen

    params["play"] = play

    json_speeds: Union[Unset, list[str]] = UNSET
    if not isinstance(speeds, Unset):
        json_speeds = []
        for speeds_item_data in speeds:
            speeds_item = speeds_item_data.value
            json_speeds.append(speeds_item)


    params["speeds"] = json_speeds

    json_modes: Union[Unset, list[str]] = UNSET
    if not isinstance(modes, Unset):
        json_modes = []
        for modes_item_data in modes:
            modes_item = modes_item_data.value
            json_modes.append(modes_item)


    params["modes"] = json_modes

    params["since"] = since

    params["until"] = until

    params["moves"] = moves

    params["recentGames"] = recent_games


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/player",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    player: str,
    color: OpeningExplorerPlayerColor,
    variant: Union[Unset, OpeningExplorerPlayerVariant] = OpeningExplorerPlayerVariant.STANDARD,
    fen: Union[Unset, str] = UNSET,
    play: Union[Unset, str] = '',
    speeds: Union[Unset, list[OpeningExplorerPlayerSpeedsItem]] = UNSET,
    modes: Union[Unset, list[OpeningExplorerPlayerModesItem]] = UNSET,
    since: Union[Unset, str] = '1952-01',
    until: Union[Unset, str] = '3000-12',
    moves: Union[Unset, float] = UNSET,
    recent_games: Union[Unset, float] = 8.0,

) -> Response[Any]:
    """ Player games

     **Endpoint: <https://explorer.lichess.ovh/player>**

    Games of a Lichess player.

    Responds with a stream of [newline delimited JSON](#section/Introduction/Streaming-with-ND-JSON).
    Will start indexing
    on demand, immediately respond with the current results, and stream
    more updates until indexing is complete. The stream is throttled
    and deduplicated. Empty lines may be sent to avoid timeouts.

    Will index new games at most once per minute, and revisit previously
    ongoing games at most once every day.

    Example: `curl
    https://explorer.lichess.ovh/player?player=revoof&color=white&play=d2d4,d7d5&recentGames=1`

    Args:
        player (str):
        color (OpeningExplorerPlayerColor):
        variant (Union[Unset, OpeningExplorerPlayerVariant]):  Default:
            OpeningExplorerPlayerVariant.STANDARD. Example: standard.
        fen (Union[Unset, str]):
        play (Union[Unset, str]):  Default: ''.
        speeds (Union[Unset, list[OpeningExplorerPlayerSpeedsItem]]):
        modes (Union[Unset, list[OpeningExplorerPlayerModesItem]]):
        since (Union[Unset, str]):  Default: '1952-01'.
        until (Union[Unset, str]):  Default: '3000-12'.
        moves (Union[Unset, float]):
        recent_games (Union[Unset, float]):  Default: 8.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        player=player,
color=color,
variant=variant,
fen=fen,
play=play,
speeds=speeds,
modes=modes,
since=since,
until=until,
moves=moves,
recent_games=recent_games,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    player: str,
    color: OpeningExplorerPlayerColor,
    variant: Union[Unset, OpeningExplorerPlayerVariant] = OpeningExplorerPlayerVariant.STANDARD,
    fen: Union[Unset, str] = UNSET,
    play: Union[Unset, str] = '',
    speeds: Union[Unset, list[OpeningExplorerPlayerSpeedsItem]] = UNSET,
    modes: Union[Unset, list[OpeningExplorerPlayerModesItem]] = UNSET,
    since: Union[Unset, str] = '1952-01',
    until: Union[Unset, str] = '3000-12',
    moves: Union[Unset, float] = UNSET,
    recent_games: Union[Unset, float] = 8.0,

) -> Response[Any]:
    """ Player games

     **Endpoint: <https://explorer.lichess.ovh/player>**

    Games of a Lichess player.

    Responds with a stream of [newline delimited JSON](#section/Introduction/Streaming-with-ND-JSON).
    Will start indexing
    on demand, immediately respond with the current results, and stream
    more updates until indexing is complete. The stream is throttled
    and deduplicated. Empty lines may be sent to avoid timeouts.

    Will index new games at most once per minute, and revisit previously
    ongoing games at most once every day.

    Example: `curl
    https://explorer.lichess.ovh/player?player=revoof&color=white&play=d2d4,d7d5&recentGames=1`

    Args:
        player (str):
        color (OpeningExplorerPlayerColor):
        variant (Union[Unset, OpeningExplorerPlayerVariant]):  Default:
            OpeningExplorerPlayerVariant.STANDARD. Example: standard.
        fen (Union[Unset, str]):
        play (Union[Unset, str]):  Default: ''.
        speeds (Union[Unset, list[OpeningExplorerPlayerSpeedsItem]]):
        modes (Union[Unset, list[OpeningExplorerPlayerModesItem]]):
        since (Union[Unset, str]):  Default: '1952-01'.
        until (Union[Unset, str]):  Default: '3000-12'.
        moves (Union[Unset, float]):
        recent_games (Union[Unset, float]):  Default: 8.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        player=player,
color=color,
variant=variant,
fen=fen,
play=play,
speeds=speeds,
modes=modes,
since=since,
until=until,
moves=moves,
recent_games=recent_games,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

