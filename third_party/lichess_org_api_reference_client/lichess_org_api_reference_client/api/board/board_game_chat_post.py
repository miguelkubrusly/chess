from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.board_game_chat_post_body import BoardGameChatPostBody
from ...models.board_game_chat_post_response_200 import BoardGameChatPostResponse200
from ...models.board_game_chat_post_response_400 import BoardGameChatPostResponse400
from typing import cast



def _get_kwargs(
    game_id: str,
    *,
    body: BoardGameChatPostBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/board/game/{game_id}/chat".format(game_id=game_id,),
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[BoardGameChatPostResponse200, BoardGameChatPostResponse400]]:
    if response.status_code == 200:
        response_200 = BoardGameChatPostResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = BoardGameChatPostResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[BoardGameChatPostResponse200, BoardGameChatPostResponse400]]:
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
    body: BoardGameChatPostBody,

) -> Response[Union[BoardGameChatPostResponse200, BoardGameChatPostResponse400]]:
    """ Write in the chat

     Post a message to the player or spectator chat, in a game being played with the Board API.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        body (BoardGameChatPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BoardGameChatPostResponse200, BoardGameChatPostResponse400]]
     """


    kwargs = _get_kwargs(
        game_id=game_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    game_id: str,
    *,
    client: AuthenticatedClient,
    body: BoardGameChatPostBody,

) -> Optional[Union[BoardGameChatPostResponse200, BoardGameChatPostResponse400]]:
    """ Write in the chat

     Post a message to the player or spectator chat, in a game being played with the Board API.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        body (BoardGameChatPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BoardGameChatPostResponse200, BoardGameChatPostResponse400]
     """


    return sync_detailed(
        game_id=game_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    game_id: str,
    *,
    client: AuthenticatedClient,
    body: BoardGameChatPostBody,

) -> Response[Union[BoardGameChatPostResponse200, BoardGameChatPostResponse400]]:
    """ Write in the chat

     Post a message to the player or spectator chat, in a game being played with the Board API.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        body (BoardGameChatPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BoardGameChatPostResponse200, BoardGameChatPostResponse400]]
     """


    kwargs = _get_kwargs(
        game_id=game_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    game_id: str,
    *,
    client: AuthenticatedClient,
    body: BoardGameChatPostBody,

) -> Optional[Union[BoardGameChatPostResponse200, BoardGameChatPostResponse400]]:
    """ Write in the chat

     Post a message to the player or spectator chat, in a game being played with the Board API.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        body (BoardGameChatPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BoardGameChatPostResponse200, BoardGameChatPostResponse400]
     """


    return (await asyncio_detailed(
        game_id=game_id,
client=client,
body=body,

    )).parsed
