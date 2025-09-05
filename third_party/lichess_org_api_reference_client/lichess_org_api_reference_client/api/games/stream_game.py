from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.stream_game_response_429 import StreamGameResponse429
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/stream/game/{id}".format(id=id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[StreamGameResponse429]:
    if response.status_code == 429:
        response_429 = StreamGameResponse429.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[StreamGameResponse429]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[StreamGameResponse429]:
    """ Stream moves of a game

     Stream positions and moves of any ongoing game, in [ndjson](#section/Introduction/Streaming-with-ND-
    JSON).
    A description of the game is sent as a first message.
    Then a message is sent each time a move is played.
    Finally, a description of the game is sent when it finishes, and the stream is closed.
    Ongoing games are delayed by a few seconds ranging from 3 to 60 depending on the time control, as to
    prevent cheat bots from using this API.
    No more than 8 game streams can be opened at the same time from the same IP address.

    Args:
        id (str):  Example: LuGQwhBb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StreamGameResponse429]
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
    client: Union[AuthenticatedClient, Client],

) -> Optional[StreamGameResponse429]:
    """ Stream moves of a game

     Stream positions and moves of any ongoing game, in [ndjson](#section/Introduction/Streaming-with-ND-
    JSON).
    A description of the game is sent as a first message.
    Then a message is sent each time a move is played.
    Finally, a description of the game is sent when it finishes, and the stream is closed.
    Ongoing games are delayed by a few seconds ranging from 3 to 60 depending on the time control, as to
    prevent cheat bots from using this API.
    No more than 8 game streams can be opened at the same time from the same IP address.

    Args:
        id (str):  Example: LuGQwhBb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StreamGameResponse429
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[StreamGameResponse429]:
    """ Stream moves of a game

     Stream positions and moves of any ongoing game, in [ndjson](#section/Introduction/Streaming-with-ND-
    JSON).
    A description of the game is sent as a first message.
    Then a message is sent each time a move is played.
    Finally, a description of the game is sent when it finishes, and the stream is closed.
    Ongoing games are delayed by a few seconds ranging from 3 to 60 depending on the time control, as to
    prevent cheat bots from using this API.
    No more than 8 game streams can be opened at the same time from the same IP address.

    Args:
        id (str):  Example: LuGQwhBb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StreamGameResponse429]
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
    client: Union[AuthenticatedClient, Client],

) -> Optional[StreamGameResponse429]:
    """ Stream moves of a game

     Stream positions and moves of any ongoing game, in [ndjson](#section/Introduction/Streaming-with-ND-
    JSON).
    A description of the game is sent as a first message.
    Then a message is sent each time a move is played.
    Finally, a description of the game is sent when it finishes, and the stream is closed.
    Ongoing games are delayed by a few seconds ranging from 3 to 60 depending on the time control, as to
    prevent cheat bots from using this API.
    No more than 8 game streams can be opened at the same time from the same IP address.

    Args:
        id (str):  Example: LuGQwhBb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StreamGameResponse429
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
