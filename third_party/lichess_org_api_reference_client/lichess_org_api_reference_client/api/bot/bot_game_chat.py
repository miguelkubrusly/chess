from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bot_game_chat_body import BotGameChatBody
from ...models.bot_game_chat_response_200 import BotGameChatResponse200
from ...models.bot_game_chat_response_400 import BotGameChatResponse400
from typing import cast



def _get_kwargs(
    game_id: str,
    *,
    body: BotGameChatBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/bot/game/{game_id}/chat".format(game_id=game_id,),
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[BotGameChatResponse200, BotGameChatResponse400]]:
    if response.status_code == 200:
        response_200 = BotGameChatResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = BotGameChatResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[BotGameChatResponse200, BotGameChatResponse400]]:
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
    body: BotGameChatBody,

) -> Response[Union[BotGameChatResponse200, BotGameChatResponse400]]:
    """ Write in the chat

     Post a message to the player or spectator chat, in a game being played with the Bot API.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        body (BotGameChatBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BotGameChatResponse200, BotGameChatResponse400]]
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
    body: BotGameChatBody,

) -> Optional[Union[BotGameChatResponse200, BotGameChatResponse400]]:
    """ Write in the chat

     Post a message to the player or spectator chat, in a game being played with the Bot API.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        body (BotGameChatBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BotGameChatResponse200, BotGameChatResponse400]
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
    body: BotGameChatBody,

) -> Response[Union[BotGameChatResponse200, BotGameChatResponse400]]:
    """ Write in the chat

     Post a message to the player or spectator chat, in a game being played with the Bot API.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        body (BotGameChatBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BotGameChatResponse200, BotGameChatResponse400]]
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
    body: BotGameChatBody,

) -> Optional[Union[BotGameChatResponse200, BotGameChatResponse400]]:
    """ Write in the chat

     Post a message to the player or spectator chat, in a game being played with the Bot API.

    Args:
        game_id (str):  Example: 5IrD6Gzz.
        body (BotGameChatBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BotGameChatResponse200, BotGameChatResponse400]
     """


    return (await asyncio_detailed(
        game_id=game_id,
client=client,
body=body,

    )).parsed
