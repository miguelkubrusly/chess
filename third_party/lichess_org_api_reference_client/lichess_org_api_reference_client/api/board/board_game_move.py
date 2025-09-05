from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.board_game_move_response_200 import BoardGameMoveResponse200
from ...models.board_game_move_response_400 import BoardGameMoveResponse400
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    game_id: str,
    move: str,
    *,
    offering_draw: Union[Unset, bool] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["offeringDraw"] = offering_draw


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/board/game/{game_id}/move/{move}".format(game_id=game_id,move=move,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[BoardGameMoveResponse200, BoardGameMoveResponse400]]:
    if response.status_code == 200:
        response_200 = BoardGameMoveResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = BoardGameMoveResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[BoardGameMoveResponse200, BoardGameMoveResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_id: str,
    move: str,
    *,
    client: AuthenticatedClient,
    offering_draw: Union[Unset, bool] = UNSET,

) -> Response[Union[BoardGameMoveResponse200, BoardGameMoveResponse400]]:
    """ Make a Board move

     Make a move in a game being played with the Board API.
    The move can also contain a draw offer/agreement.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        move (str):  Example: e2e4.
        offering_draw (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BoardGameMoveResponse200, BoardGameMoveResponse400]]
     """


    kwargs = _get_kwargs(
        game_id=game_id,
move=move,
offering_draw=offering_draw,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    game_id: str,
    move: str,
    *,
    client: AuthenticatedClient,
    offering_draw: Union[Unset, bool] = UNSET,

) -> Optional[Union[BoardGameMoveResponse200, BoardGameMoveResponse400]]:
    """ Make a Board move

     Make a move in a game being played with the Board API.
    The move can also contain a draw offer/agreement.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        move (str):  Example: e2e4.
        offering_draw (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BoardGameMoveResponse200, BoardGameMoveResponse400]
     """


    return sync_detailed(
        game_id=game_id,
move=move,
client=client,
offering_draw=offering_draw,

    ).parsed

async def asyncio_detailed(
    game_id: str,
    move: str,
    *,
    client: AuthenticatedClient,
    offering_draw: Union[Unset, bool] = UNSET,

) -> Response[Union[BoardGameMoveResponse200, BoardGameMoveResponse400]]:
    """ Make a Board move

     Make a move in a game being played with the Board API.
    The move can also contain a draw offer/agreement.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        move (str):  Example: e2e4.
        offering_draw (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BoardGameMoveResponse200, BoardGameMoveResponse400]]
     """


    kwargs = _get_kwargs(
        game_id=game_id,
move=move,
offering_draw=offering_draw,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    game_id: str,
    move: str,
    *,
    client: AuthenticatedClient,
    offering_draw: Union[Unset, bool] = UNSET,

) -> Optional[Union[BoardGameMoveResponse200, BoardGameMoveResponse400]]:
    """ Make a Board move

     Make a move in a game being played with the Board API.
    The move can also contain a draw offer/agreement.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        move (str):  Example: e2e4.
        offering_draw (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BoardGameMoveResponse200, BoardGameMoveResponse400]
     """


    return (await asyncio_detailed(
        game_id=game_id,
move=move,
client=client,
offering_draw=offering_draw,

    )).parsed
