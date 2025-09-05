from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.game_pgn_response_200 import GamePgnResponse200
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    game_id: str,
    *,
    moves: Union[Unset, bool] = True,
    pgn_in_json: Union[Unset, bool] = False,
    tags: Union[Unset, bool] = True,
    clocks: Union[Unset, bool] = True,
    evals: Union[Unset, bool] = True,
    accuracy: Union[Unset, bool] = False,
    opening: Union[Unset, bool] = True,
    division: Union[Unset, bool] = True,
    literate: Union[Unset, bool] = False,
    with_bookmarked: Union[Unset, bool] = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["moves"] = moves

    params["pgnInJson"] = pgn_in_json

    params["tags"] = tags

    params["clocks"] = clocks

    params["evals"] = evals

    params["accuracy"] = accuracy

    params["opening"] = opening

    params["division"] = division

    params["literate"] = literate

    params["withBookmarked"] = with_bookmarked


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/game/export/{game_id}".format(game_id=game_id,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[GamePgnResponse200]:
    if response.status_code == 200:
        response_200 = GamePgnResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[GamePgnResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    moves: Union[Unset, bool] = True,
    pgn_in_json: Union[Unset, bool] = False,
    tags: Union[Unset, bool] = True,
    clocks: Union[Unset, bool] = True,
    evals: Union[Unset, bool] = True,
    accuracy: Union[Unset, bool] = False,
    opening: Union[Unset, bool] = True,
    division: Union[Unset, bool] = True,
    literate: Union[Unset, bool] = False,
    with_bookmarked: Union[Unset, bool] = False,

) -> Response[GamePgnResponse200]:
    """ Export one game

     Download one game in either PGN or JSON format.
    Ongoing games are delayed by a few seconds ranging from 3 to 60 depending on the time control, as to
    prevent cheat bots from using this API.

    Args:
        game_id (str):
        moves (Union[Unset, bool]):  Default: True.
        pgn_in_json (Union[Unset, bool]):  Default: False.
        tags (Union[Unset, bool]):  Default: True.
        clocks (Union[Unset, bool]):  Default: True.
        evals (Union[Unset, bool]):  Default: True.
        accuracy (Union[Unset, bool]):  Default: False.
        opening (Union[Unset, bool]):  Default: True.
        division (Union[Unset, bool]):  Default: True.
        literate (Union[Unset, bool]):  Default: False.
        with_bookmarked (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GamePgnResponse200]
     """


    kwargs = _get_kwargs(
        game_id=game_id,
moves=moves,
pgn_in_json=pgn_in_json,
tags=tags,
clocks=clocks,
evals=evals,
accuracy=accuracy,
opening=opening,
division=division,
literate=literate,
with_bookmarked=with_bookmarked,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    game_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    moves: Union[Unset, bool] = True,
    pgn_in_json: Union[Unset, bool] = False,
    tags: Union[Unset, bool] = True,
    clocks: Union[Unset, bool] = True,
    evals: Union[Unset, bool] = True,
    accuracy: Union[Unset, bool] = False,
    opening: Union[Unset, bool] = True,
    division: Union[Unset, bool] = True,
    literate: Union[Unset, bool] = False,
    with_bookmarked: Union[Unset, bool] = False,

) -> Optional[GamePgnResponse200]:
    """ Export one game

     Download one game in either PGN or JSON format.
    Ongoing games are delayed by a few seconds ranging from 3 to 60 depending on the time control, as to
    prevent cheat bots from using this API.

    Args:
        game_id (str):
        moves (Union[Unset, bool]):  Default: True.
        pgn_in_json (Union[Unset, bool]):  Default: False.
        tags (Union[Unset, bool]):  Default: True.
        clocks (Union[Unset, bool]):  Default: True.
        evals (Union[Unset, bool]):  Default: True.
        accuracy (Union[Unset, bool]):  Default: False.
        opening (Union[Unset, bool]):  Default: True.
        division (Union[Unset, bool]):  Default: True.
        literate (Union[Unset, bool]):  Default: False.
        with_bookmarked (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GamePgnResponse200
     """


    return sync_detailed(
        game_id=game_id,
client=client,
moves=moves,
pgn_in_json=pgn_in_json,
tags=tags,
clocks=clocks,
evals=evals,
accuracy=accuracy,
opening=opening,
division=division,
literate=literate,
with_bookmarked=with_bookmarked,

    ).parsed

async def asyncio_detailed(
    game_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    moves: Union[Unset, bool] = True,
    pgn_in_json: Union[Unset, bool] = False,
    tags: Union[Unset, bool] = True,
    clocks: Union[Unset, bool] = True,
    evals: Union[Unset, bool] = True,
    accuracy: Union[Unset, bool] = False,
    opening: Union[Unset, bool] = True,
    division: Union[Unset, bool] = True,
    literate: Union[Unset, bool] = False,
    with_bookmarked: Union[Unset, bool] = False,

) -> Response[GamePgnResponse200]:
    """ Export one game

     Download one game in either PGN or JSON format.
    Ongoing games are delayed by a few seconds ranging from 3 to 60 depending on the time control, as to
    prevent cheat bots from using this API.

    Args:
        game_id (str):
        moves (Union[Unset, bool]):  Default: True.
        pgn_in_json (Union[Unset, bool]):  Default: False.
        tags (Union[Unset, bool]):  Default: True.
        clocks (Union[Unset, bool]):  Default: True.
        evals (Union[Unset, bool]):  Default: True.
        accuracy (Union[Unset, bool]):  Default: False.
        opening (Union[Unset, bool]):  Default: True.
        division (Union[Unset, bool]):  Default: True.
        literate (Union[Unset, bool]):  Default: False.
        with_bookmarked (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GamePgnResponse200]
     """


    kwargs = _get_kwargs(
        game_id=game_id,
moves=moves,
pgn_in_json=pgn_in_json,
tags=tags,
clocks=clocks,
evals=evals,
accuracy=accuracy,
opening=opening,
division=division,
literate=literate,
with_bookmarked=with_bookmarked,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    game_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    moves: Union[Unset, bool] = True,
    pgn_in_json: Union[Unset, bool] = False,
    tags: Union[Unset, bool] = True,
    clocks: Union[Unset, bool] = True,
    evals: Union[Unset, bool] = True,
    accuracy: Union[Unset, bool] = False,
    opening: Union[Unset, bool] = True,
    division: Union[Unset, bool] = True,
    literate: Union[Unset, bool] = False,
    with_bookmarked: Union[Unset, bool] = False,

) -> Optional[GamePgnResponse200]:
    """ Export one game

     Download one game in either PGN or JSON format.
    Ongoing games are delayed by a few seconds ranging from 3 to 60 depending on the time control, as to
    prevent cheat bots from using this API.

    Args:
        game_id (str):
        moves (Union[Unset, bool]):  Default: True.
        pgn_in_json (Union[Unset, bool]):  Default: False.
        tags (Union[Unset, bool]):  Default: True.
        clocks (Union[Unset, bool]):  Default: True.
        evals (Union[Unset, bool]):  Default: True.
        accuracy (Union[Unset, bool]):  Default: False.
        opening (Union[Unset, bool]):  Default: True.
        division (Union[Unset, bool]):  Default: True.
        literate (Union[Unset, bool]):  Default: False.
        with_bookmarked (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GamePgnResponse200
     """


    return (await asyncio_detailed(
        game_id=game_id,
client=client,
moves=moves,
pgn_in_json=pgn_in_json,
tags=tags,
clocks=clocks,
evals=evals,
accuracy=accuracy,
opening=opening,
division=division,
literate=literate,
with_bookmarked=with_bookmarked,

    )).parsed
