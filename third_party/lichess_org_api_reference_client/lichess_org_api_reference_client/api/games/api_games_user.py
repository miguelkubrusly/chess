from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_games_user_color import ApiGamesUserColor
from ...models.api_games_user_perf_type import ApiGamesUserPerfType
from ...models.api_games_user_sort import ApiGamesUserSort
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    username: str,
    *,
    since: Union[Unset, int] = UNSET,
    until: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    vs: Union[Unset, str] = UNSET,
    rated: Union[Unset, bool] = UNSET,
    perf_type: Union[Unset, 'ApiGamesUserPerfType'] = UNSET,
    color: Union[Unset, ApiGamesUserColor] = UNSET,
    analysed: Union[Unset, bool] = UNSET,
    moves: Union[Unset, bool] = True,
    pgn_in_json: Union[Unset, bool] = False,
    tags: Union[Unset, bool] = True,
    clocks: Union[Unset, bool] = False,
    evals: Union[Unset, bool] = False,
    accuracy: Union[Unset, bool] = False,
    opening: Union[Unset, bool] = False,
    division: Union[Unset, bool] = False,
    ongoing: Union[Unset, bool] = False,
    finished: Union[Unset, bool] = True,
    literate: Union[Unset, bool] = False,
    last_fen: Union[Unset, bool] = False,
    with_bookmarked: Union[Unset, bool] = False,
    sort: Union[Unset, ApiGamesUserSort] = ApiGamesUserSort.DATEDESC,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["since"] = since

    params["until"] = until

    params["max"] = max_

    params["vs"] = vs

    params["rated"] = rated

    json_perf_type: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(perf_type, Unset):
        json_perf_type = perf_type.to_dict()
    if not isinstance(json_perf_type, Unset):
        params.update(json_perf_type)


    json_color: Union[Unset, str] = UNSET
    if not isinstance(color, Unset):
        json_color = color.value

    params["color"] = json_color

    params["analysed"] = analysed

    params["moves"] = moves

    params["pgnInJson"] = pgn_in_json

    params["tags"] = tags

    params["clocks"] = clocks

    params["evals"] = evals

    params["accuracy"] = accuracy

    params["opening"] = opening

    params["division"] = division

    params["ongoing"] = ongoing

    params["finished"] = finished

    params["literate"] = literate

    params["lastFen"] = last_fen

    params["withBookmarked"] = with_bookmarked

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/games/user/{username}".format(username=username,),
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
    username: str,
    *,
    client: AuthenticatedClient,
    since: Union[Unset, int] = UNSET,
    until: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    vs: Union[Unset, str] = UNSET,
    rated: Union[Unset, bool] = UNSET,
    perf_type: Union[Unset, 'ApiGamesUserPerfType'] = UNSET,
    color: Union[Unset, ApiGamesUserColor] = UNSET,
    analysed: Union[Unset, bool] = UNSET,
    moves: Union[Unset, bool] = True,
    pgn_in_json: Union[Unset, bool] = False,
    tags: Union[Unset, bool] = True,
    clocks: Union[Unset, bool] = False,
    evals: Union[Unset, bool] = False,
    accuracy: Union[Unset, bool] = False,
    opening: Union[Unset, bool] = False,
    division: Union[Unset, bool] = False,
    ongoing: Union[Unset, bool] = False,
    finished: Union[Unset, bool] = True,
    literate: Union[Unset, bool] = False,
    last_fen: Union[Unset, bool] = False,
    with_bookmarked: Union[Unset, bool] = False,
    sort: Union[Unset, ApiGamesUserSort] = ApiGamesUserSort.DATEDESC,

) -> Response[Any]:
    """ Export games of a user

     Download all games of any user in PGN or [ndjson](#section/Introduction/Streaming-with-ND-JSON)
    format.
    Games are sorted by reverse chronological order (most recent first).
    We recommend streaming the response, for it can be very long.
    <https://lichess.org/@/german11> for instance has more than 500,000 games.
    The game stream is throttled, depending on who is making the request:
      - Anonymous request: 20 games per second
      - [OAuth2 authenticated](#section/Introduction/Authentication) request: 30 games per second
      - Authenticated, downloading your own games: 60 games per second

    Args:
        username (str):
        since (Union[Unset, int]):
        until (Union[Unset, int]):
        max_ (Union[Unset, int]):
        vs (Union[Unset, str]):
        rated (Union[Unset, bool]):
        perf_type (Union[Unset, ApiGamesUserPerfType]):
        color (Union[Unset, ApiGamesUserColor]):
        analysed (Union[Unset, bool]):
        moves (Union[Unset, bool]):  Default: True.
        pgn_in_json (Union[Unset, bool]):  Default: False.
        tags (Union[Unset, bool]):  Default: True.
        clocks (Union[Unset, bool]):  Default: False.
        evals (Union[Unset, bool]):  Default: False.
        accuracy (Union[Unset, bool]):  Default: False.
        opening (Union[Unset, bool]):  Default: False.
        division (Union[Unset, bool]):  Default: False.
        ongoing (Union[Unset, bool]):  Default: False.
        finished (Union[Unset, bool]):  Default: True.
        literate (Union[Unset, bool]):  Default: False.
        last_fen (Union[Unset, bool]):  Default: False.
        with_bookmarked (Union[Unset, bool]):  Default: False.
        sort (Union[Unset, ApiGamesUserSort]):  Default: ApiGamesUserSort.DATEDESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        username=username,
since=since,
until=until,
max_=max_,
vs=vs,
rated=rated,
perf_type=perf_type,
color=color,
analysed=analysed,
moves=moves,
pgn_in_json=pgn_in_json,
tags=tags,
clocks=clocks,
evals=evals,
accuracy=accuracy,
opening=opening,
division=division,
ongoing=ongoing,
finished=finished,
literate=literate,
last_fen=last_fen,
with_bookmarked=with_bookmarked,
sort=sort,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    since: Union[Unset, int] = UNSET,
    until: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    vs: Union[Unset, str] = UNSET,
    rated: Union[Unset, bool] = UNSET,
    perf_type: Union[Unset, 'ApiGamesUserPerfType'] = UNSET,
    color: Union[Unset, ApiGamesUserColor] = UNSET,
    analysed: Union[Unset, bool] = UNSET,
    moves: Union[Unset, bool] = True,
    pgn_in_json: Union[Unset, bool] = False,
    tags: Union[Unset, bool] = True,
    clocks: Union[Unset, bool] = False,
    evals: Union[Unset, bool] = False,
    accuracy: Union[Unset, bool] = False,
    opening: Union[Unset, bool] = False,
    division: Union[Unset, bool] = False,
    ongoing: Union[Unset, bool] = False,
    finished: Union[Unset, bool] = True,
    literate: Union[Unset, bool] = False,
    last_fen: Union[Unset, bool] = False,
    with_bookmarked: Union[Unset, bool] = False,
    sort: Union[Unset, ApiGamesUserSort] = ApiGamesUserSort.DATEDESC,

) -> Response[Any]:
    """ Export games of a user

     Download all games of any user in PGN or [ndjson](#section/Introduction/Streaming-with-ND-JSON)
    format.
    Games are sorted by reverse chronological order (most recent first).
    We recommend streaming the response, for it can be very long.
    <https://lichess.org/@/german11> for instance has more than 500,000 games.
    The game stream is throttled, depending on who is making the request:
      - Anonymous request: 20 games per second
      - [OAuth2 authenticated](#section/Introduction/Authentication) request: 30 games per second
      - Authenticated, downloading your own games: 60 games per second

    Args:
        username (str):
        since (Union[Unset, int]):
        until (Union[Unset, int]):
        max_ (Union[Unset, int]):
        vs (Union[Unset, str]):
        rated (Union[Unset, bool]):
        perf_type (Union[Unset, ApiGamesUserPerfType]):
        color (Union[Unset, ApiGamesUserColor]):
        analysed (Union[Unset, bool]):
        moves (Union[Unset, bool]):  Default: True.
        pgn_in_json (Union[Unset, bool]):  Default: False.
        tags (Union[Unset, bool]):  Default: True.
        clocks (Union[Unset, bool]):  Default: False.
        evals (Union[Unset, bool]):  Default: False.
        accuracy (Union[Unset, bool]):  Default: False.
        opening (Union[Unset, bool]):  Default: False.
        division (Union[Unset, bool]):  Default: False.
        ongoing (Union[Unset, bool]):  Default: False.
        finished (Union[Unset, bool]):  Default: True.
        literate (Union[Unset, bool]):  Default: False.
        last_fen (Union[Unset, bool]):  Default: False.
        with_bookmarked (Union[Unset, bool]):  Default: False.
        sort (Union[Unset, ApiGamesUserSort]):  Default: ApiGamesUserSort.DATEDESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        username=username,
since=since,
until=until,
max_=max_,
vs=vs,
rated=rated,
perf_type=perf_type,
color=color,
analysed=analysed,
moves=moves,
pgn_in_json=pgn_in_json,
tags=tags,
clocks=clocks,
evals=evals,
accuracy=accuracy,
opening=opening,
division=division,
ongoing=ongoing,
finished=finished,
literate=literate,
last_fen=last_fen,
with_bookmarked=with_bookmarked,
sort=sort,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

