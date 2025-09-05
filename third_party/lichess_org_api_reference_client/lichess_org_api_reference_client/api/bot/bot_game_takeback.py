from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bot_game_takeback_response_200 import BotGameTakebackResponse200
from ...models.bot_game_takeback_response_400 import BotGameTakebackResponse400
from typing import cast
from typing import cast, Union
from typing import Literal, cast



def _get_kwargs(
    game_id: str,
    accept: Union[Literal['yes'], bool],

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/bot/game/{game_id}/takeback/{accept}".format(game_id=game_id,accept=accept,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[BotGameTakebackResponse200, BotGameTakebackResponse400]]:
    if response.status_code == 200:
        response_200 = BotGameTakebackResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = BotGameTakebackResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[BotGameTakebackResponse200, BotGameTakebackResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_id: str,
    accept: Union[Literal['yes'], bool],
    *,
    client: AuthenticatedClient,

) -> Response[Union[BotGameTakebackResponse200, BotGameTakebackResponse400]]:
    """ Handle takeback offers

     Create/accept/decline takebacks with the Bot API.
    - `yes`: Propose a takeback, or accept the opponent's takeback offer.
    - `no`: Decline a takeback offer from the opponent.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        accept (Union[Literal['yes'], bool]):  Example: yes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BotGameTakebackResponse200, BotGameTakebackResponse400]]
     """


    kwargs = _get_kwargs(
        game_id=game_id,
accept=accept,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    game_id: str,
    accept: Union[Literal['yes'], bool],
    *,
    client: AuthenticatedClient,

) -> Optional[Union[BotGameTakebackResponse200, BotGameTakebackResponse400]]:
    """ Handle takeback offers

     Create/accept/decline takebacks with the Bot API.
    - `yes`: Propose a takeback, or accept the opponent's takeback offer.
    - `no`: Decline a takeback offer from the opponent.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        accept (Union[Literal['yes'], bool]):  Example: yes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BotGameTakebackResponse200, BotGameTakebackResponse400]
     """


    return sync_detailed(
        game_id=game_id,
accept=accept,
client=client,

    ).parsed

async def asyncio_detailed(
    game_id: str,
    accept: Union[Literal['yes'], bool],
    *,
    client: AuthenticatedClient,

) -> Response[Union[BotGameTakebackResponse200, BotGameTakebackResponse400]]:
    """ Handle takeback offers

     Create/accept/decline takebacks with the Bot API.
    - `yes`: Propose a takeback, or accept the opponent's takeback offer.
    - `no`: Decline a takeback offer from the opponent.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        accept (Union[Literal['yes'], bool]):  Example: yes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BotGameTakebackResponse200, BotGameTakebackResponse400]]
     """


    kwargs = _get_kwargs(
        game_id=game_id,
accept=accept,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    game_id: str,
    accept: Union[Literal['yes'], bool],
    *,
    client: AuthenticatedClient,

) -> Optional[Union[BotGameTakebackResponse200, BotGameTakebackResponse400]]:
    """ Handle takeback offers

     Create/accept/decline takebacks with the Bot API.
    - `yes`: Propose a takeback, or accept the opponent's takeback offer.
    - `no`: Decline a takeback offer from the opponent.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        accept (Union[Literal['yes'], bool]):  Example: yes.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BotGameTakebackResponse200, BotGameTakebackResponse400]
     """


    return (await asyncio_detailed(
        game_id=game_id,
accept=accept,
client=client,

    )).parsed
