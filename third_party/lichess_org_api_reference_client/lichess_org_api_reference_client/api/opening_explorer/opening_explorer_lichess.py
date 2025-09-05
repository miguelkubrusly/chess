from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.opening_explorer_lichess_ratings_item import OpeningExplorerLichessRatingsItem
from ...models.opening_explorer_lichess_response_200 import OpeningExplorerLichessResponse200
from ...models.opening_explorer_lichess_speeds_item import OpeningExplorerLichessSpeedsItem
from ...models.opening_explorer_lichess_variant import OpeningExplorerLichessVariant
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    variant: Union[Unset, OpeningExplorerLichessVariant] = OpeningExplorerLichessVariant.STANDARD,
    fen: Union[Unset, str] = UNSET,
    play: Union[Unset, str] = '',
    speeds: Union[Unset, list[OpeningExplorerLichessSpeedsItem]] = UNSET,
    ratings: Union[Unset, list[OpeningExplorerLichessRatingsItem]] = UNSET,
    since: Union[Unset, str] = '1952-01',
    until: Union[Unset, str] = '3000-12',
    moves: Union[Unset, float] = 12.0,
    top_games: Union[Unset, float] = 4.0,
    recent_games: Union[Unset, float] = 4.0,
    history: Union[Unset, bool] = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

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

    json_ratings: Union[Unset, list[int]] = UNSET
    if not isinstance(ratings, Unset):
        json_ratings = []
        for ratings_item_data in ratings:
            ratings_item = ratings_item_data.value
            json_ratings.append(ratings_item)


    params["ratings"] = json_ratings

    params["since"] = since

    params["until"] = until

    params["moves"] = moves

    params["topGames"] = top_games

    params["recentGames"] = recent_games

    params["history"] = history


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/lichess",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[OpeningExplorerLichessResponse200]:
    if response.status_code == 200:
        response_200 = OpeningExplorerLichessResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[OpeningExplorerLichessResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    variant: Union[Unset, OpeningExplorerLichessVariant] = OpeningExplorerLichessVariant.STANDARD,
    fen: Union[Unset, str] = UNSET,
    play: Union[Unset, str] = '',
    speeds: Union[Unset, list[OpeningExplorerLichessSpeedsItem]] = UNSET,
    ratings: Union[Unset, list[OpeningExplorerLichessRatingsItem]] = UNSET,
    since: Union[Unset, str] = '1952-01',
    until: Union[Unset, str] = '3000-12',
    moves: Union[Unset, float] = 12.0,
    top_games: Union[Unset, float] = 4.0,
    recent_games: Union[Unset, float] = 4.0,
    history: Union[Unset, bool] = False,

) -> Response[OpeningExplorerLichessResponse200]:
    """ Lichess games

     **Endpoint: <https://explorer.lichess.ovh/lichess>**

    Games sampled from all Lichess players.

    Example: `curl https://explorer.lichess.ovh/lichess?variant=standard&speeds=blitz,rapid,classical&ra
    tings=2200,2500&fen=rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR%20w%20KQkq%20-%200%201`

    Args:
        variant (Union[Unset, OpeningExplorerLichessVariant]):  Default:
            OpeningExplorerLichessVariant.STANDARD. Example: standard.
        fen (Union[Unset, str]):
        play (Union[Unset, str]):  Default: ''.
        speeds (Union[Unset, list[OpeningExplorerLichessSpeedsItem]]):
        ratings (Union[Unset, list[OpeningExplorerLichessRatingsItem]]):
        since (Union[Unset, str]):  Default: '1952-01'.
        until (Union[Unset, str]):  Default: '3000-12'.
        moves (Union[Unset, float]):  Default: 12.0.
        top_games (Union[Unset, float]):  Default: 4.0.
        recent_games (Union[Unset, float]):  Default: 4.0.
        history (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpeningExplorerLichessResponse200]
     """


    kwargs = _get_kwargs(
        variant=variant,
fen=fen,
play=play,
speeds=speeds,
ratings=ratings,
since=since,
until=until,
moves=moves,
top_games=top_games,
recent_games=recent_games,
history=history,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    variant: Union[Unset, OpeningExplorerLichessVariant] = OpeningExplorerLichessVariant.STANDARD,
    fen: Union[Unset, str] = UNSET,
    play: Union[Unset, str] = '',
    speeds: Union[Unset, list[OpeningExplorerLichessSpeedsItem]] = UNSET,
    ratings: Union[Unset, list[OpeningExplorerLichessRatingsItem]] = UNSET,
    since: Union[Unset, str] = '1952-01',
    until: Union[Unset, str] = '3000-12',
    moves: Union[Unset, float] = 12.0,
    top_games: Union[Unset, float] = 4.0,
    recent_games: Union[Unset, float] = 4.0,
    history: Union[Unset, bool] = False,

) -> Optional[OpeningExplorerLichessResponse200]:
    """ Lichess games

     **Endpoint: <https://explorer.lichess.ovh/lichess>**

    Games sampled from all Lichess players.

    Example: `curl https://explorer.lichess.ovh/lichess?variant=standard&speeds=blitz,rapid,classical&ra
    tings=2200,2500&fen=rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR%20w%20KQkq%20-%200%201`

    Args:
        variant (Union[Unset, OpeningExplorerLichessVariant]):  Default:
            OpeningExplorerLichessVariant.STANDARD. Example: standard.
        fen (Union[Unset, str]):
        play (Union[Unset, str]):  Default: ''.
        speeds (Union[Unset, list[OpeningExplorerLichessSpeedsItem]]):
        ratings (Union[Unset, list[OpeningExplorerLichessRatingsItem]]):
        since (Union[Unset, str]):  Default: '1952-01'.
        until (Union[Unset, str]):  Default: '3000-12'.
        moves (Union[Unset, float]):  Default: 12.0.
        top_games (Union[Unset, float]):  Default: 4.0.
        recent_games (Union[Unset, float]):  Default: 4.0.
        history (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpeningExplorerLichessResponse200
     """


    return sync_detailed(
        client=client,
variant=variant,
fen=fen,
play=play,
speeds=speeds,
ratings=ratings,
since=since,
until=until,
moves=moves,
top_games=top_games,
recent_games=recent_games,
history=history,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    variant: Union[Unset, OpeningExplorerLichessVariant] = OpeningExplorerLichessVariant.STANDARD,
    fen: Union[Unset, str] = UNSET,
    play: Union[Unset, str] = '',
    speeds: Union[Unset, list[OpeningExplorerLichessSpeedsItem]] = UNSET,
    ratings: Union[Unset, list[OpeningExplorerLichessRatingsItem]] = UNSET,
    since: Union[Unset, str] = '1952-01',
    until: Union[Unset, str] = '3000-12',
    moves: Union[Unset, float] = 12.0,
    top_games: Union[Unset, float] = 4.0,
    recent_games: Union[Unset, float] = 4.0,
    history: Union[Unset, bool] = False,

) -> Response[OpeningExplorerLichessResponse200]:
    """ Lichess games

     **Endpoint: <https://explorer.lichess.ovh/lichess>**

    Games sampled from all Lichess players.

    Example: `curl https://explorer.lichess.ovh/lichess?variant=standard&speeds=blitz,rapid,classical&ra
    tings=2200,2500&fen=rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR%20w%20KQkq%20-%200%201`

    Args:
        variant (Union[Unset, OpeningExplorerLichessVariant]):  Default:
            OpeningExplorerLichessVariant.STANDARD. Example: standard.
        fen (Union[Unset, str]):
        play (Union[Unset, str]):  Default: ''.
        speeds (Union[Unset, list[OpeningExplorerLichessSpeedsItem]]):
        ratings (Union[Unset, list[OpeningExplorerLichessRatingsItem]]):
        since (Union[Unset, str]):  Default: '1952-01'.
        until (Union[Unset, str]):  Default: '3000-12'.
        moves (Union[Unset, float]):  Default: 12.0.
        top_games (Union[Unset, float]):  Default: 4.0.
        recent_games (Union[Unset, float]):  Default: 4.0.
        history (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpeningExplorerLichessResponse200]
     """


    kwargs = _get_kwargs(
        variant=variant,
fen=fen,
play=play,
speeds=speeds,
ratings=ratings,
since=since,
until=until,
moves=moves,
top_games=top_games,
recent_games=recent_games,
history=history,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    variant: Union[Unset, OpeningExplorerLichessVariant] = OpeningExplorerLichessVariant.STANDARD,
    fen: Union[Unset, str] = UNSET,
    play: Union[Unset, str] = '',
    speeds: Union[Unset, list[OpeningExplorerLichessSpeedsItem]] = UNSET,
    ratings: Union[Unset, list[OpeningExplorerLichessRatingsItem]] = UNSET,
    since: Union[Unset, str] = '1952-01',
    until: Union[Unset, str] = '3000-12',
    moves: Union[Unset, float] = 12.0,
    top_games: Union[Unset, float] = 4.0,
    recent_games: Union[Unset, float] = 4.0,
    history: Union[Unset, bool] = False,

) -> Optional[OpeningExplorerLichessResponse200]:
    """ Lichess games

     **Endpoint: <https://explorer.lichess.ovh/lichess>**

    Games sampled from all Lichess players.

    Example: `curl https://explorer.lichess.ovh/lichess?variant=standard&speeds=blitz,rapid,classical&ra
    tings=2200,2500&fen=rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR%20w%20KQkq%20-%200%201`

    Args:
        variant (Union[Unset, OpeningExplorerLichessVariant]):  Default:
            OpeningExplorerLichessVariant.STANDARD. Example: standard.
        fen (Union[Unset, str]):
        play (Union[Unset, str]):  Default: ''.
        speeds (Union[Unset, list[OpeningExplorerLichessSpeedsItem]]):
        ratings (Union[Unset, list[OpeningExplorerLichessRatingsItem]]):
        since (Union[Unset, str]):  Default: '1952-01'.
        until (Union[Unset, str]):  Default: '3000-12'.
        moves (Union[Unset, float]):  Default: 12.0.
        top_games (Union[Unset, float]):  Default: 4.0.
        recent_games (Union[Unset, float]):  Default: 4.0.
        history (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpeningExplorerLichessResponse200
     """


    return (await asyncio_detailed(
        client=client,
variant=variant,
fen=fen,
play=play,
speeds=speeds,
ratings=ratings,
since=since,
until=until,
moves=moves,
top_games=top_games,
recent_games=recent_games,
history=history,

    )).parsed
