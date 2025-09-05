from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bot_game_stream_response_404 import BotGameStreamResponse404
from typing import cast



def _get_kwargs(
    game_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/bot/game/stream/{game_id}".format(game_id=game_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[BotGameStreamResponse404]:
    if response.status_code == 404:
        response_404 = BotGameStreamResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[BotGameStreamResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[BotGameStreamResponse404]:
    r""" Stream Bot game state

     Stream the state of a game being played with the Bot API, as
    [ndjson](#section/Introduction/Streaming-with-ND-JSON).
    Use this endpoint to get updates about the game in real-time, with a single request.
    Each line is a JSON object containing a `type` field. Possible values are:
    - `gameFull` Full game data. All values are immutable, except for the `state` field.
    - `gameState` Current state of the game. Immutable values not included.
    - `chatLine` Chat message sent by a user (or the bot itself) in the `room` \"player\" or
    \"spectator\".
    - `opponentGone` Whether the opponent has left the game, and how long before you can claim a win or
    draw.
    The first line is always of type `gameFull`.

    Args:
        game_id (str):  Example: 5IrD6Gzz.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotGameStreamResponse404]
     """


    kwargs = _get_kwargs(
        game_id=game_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    game_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[BotGameStreamResponse404]:
    r""" Stream Bot game state

     Stream the state of a game being played with the Bot API, as
    [ndjson](#section/Introduction/Streaming-with-ND-JSON).
    Use this endpoint to get updates about the game in real-time, with a single request.
    Each line is a JSON object containing a `type` field. Possible values are:
    - `gameFull` Full game data. All values are immutable, except for the `state` field.
    - `gameState` Current state of the game. Immutable values not included.
    - `chatLine` Chat message sent by a user (or the bot itself) in the `room` \"player\" or
    \"spectator\".
    - `opponentGone` Whether the opponent has left the game, and how long before you can claim a win or
    draw.
    The first line is always of type `gameFull`.

    Args:
        game_id (str):  Example: 5IrD6Gzz.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotGameStreamResponse404
     """


    return sync_detailed(
        game_id=game_id,
client=client,

    ).parsed

async def asyncio_detailed(
    game_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[BotGameStreamResponse404]:
    r""" Stream Bot game state

     Stream the state of a game being played with the Bot API, as
    [ndjson](#section/Introduction/Streaming-with-ND-JSON).
    Use this endpoint to get updates about the game in real-time, with a single request.
    Each line is a JSON object containing a `type` field. Possible values are:
    - `gameFull` Full game data. All values are immutable, except for the `state` field.
    - `gameState` Current state of the game. Immutable values not included.
    - `chatLine` Chat message sent by a user (or the bot itself) in the `room` \"player\" or
    \"spectator\".
    - `opponentGone` Whether the opponent has left the game, and how long before you can claim a win or
    draw.
    The first line is always of type `gameFull`.

    Args:
        game_id (str):  Example: 5IrD6Gzz.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotGameStreamResponse404]
     """


    kwargs = _get_kwargs(
        game_id=game_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    game_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[BotGameStreamResponse404]:
    r""" Stream Bot game state

     Stream the state of a game being played with the Bot API, as
    [ndjson](#section/Introduction/Streaming-with-ND-JSON).
    Use this endpoint to get updates about the game in real-time, with a single request.
    Each line is a JSON object containing a `type` field. Possible values are:
    - `gameFull` Full game data. All values are immutable, except for the `state` field.
    - `gameState` Current state of the game. Immutable values not included.
    - `chatLine` Chat message sent by a user (or the bot itself) in the `room` \"player\" or
    \"spectator\".
    - `opponentGone` Whether the opponent has left the game, and how long before you can claim a win or
    draw.
    The first line is always of type `gameFull`.

    Args:
        game_id (str):  Example: 5IrD6Gzz.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotGameStreamResponse404
     """


    return (await asyncio_detailed(
        game_id=game_id,
client=client,

    )).parsed
