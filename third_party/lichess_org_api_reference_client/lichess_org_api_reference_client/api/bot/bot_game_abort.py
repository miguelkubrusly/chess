from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bot_game_abort_response_200 import BotGameAbortResponse200
from ...models.bot_game_abort_response_400 import BotGameAbortResponse400
from typing import cast



def _get_kwargs(
    game_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/bot/game/{game_id}/abort".format(game_id=game_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[BotGameAbortResponse200, BotGameAbortResponse400]]:
    if response.status_code == 200:
        response_200 = BotGameAbortResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = BotGameAbortResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[BotGameAbortResponse200, BotGameAbortResponse400]]:
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

) -> Response[Union[BotGameAbortResponse200, BotGameAbortResponse400]]:
    """ Abort a game

     Abort a game being played with the Bot API.

    Args:
        game_id (str):  Example: 5IrD6Gzz.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BotGameAbortResponse200, BotGameAbortResponse400]]
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

) -> Optional[Union[BotGameAbortResponse200, BotGameAbortResponse400]]:
    """ Abort a game

     Abort a game being played with the Bot API.

    Args:
        game_id (str):  Example: 5IrD6Gzz.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BotGameAbortResponse200, BotGameAbortResponse400]
     """


    return sync_detailed(
        game_id=game_id,
client=client,

    ).parsed

async def asyncio_detailed(
    game_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[BotGameAbortResponse200, BotGameAbortResponse400]]:
    """ Abort a game

     Abort a game being played with the Bot API.

    Args:
        game_id (str):  Example: 5IrD6Gzz.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BotGameAbortResponse200, BotGameAbortResponse400]]
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

) -> Optional[Union[BotGameAbortResponse200, BotGameAbortResponse400]]:
    """ Abort a game

     Abort a game being played with the Bot API.

    Args:
        game_id (str):  Example: 5IrD6Gzz.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BotGameAbortResponse200, BotGameAbortResponse400]
     """


    return (await asyncio_detailed(
        game_id=game_id,
client=client,

    )).parsed
