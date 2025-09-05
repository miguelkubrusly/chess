from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.challenge_start_clocks_response_200 import ChallengeStartClocksResponse200
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    game_id: str,
    *,
    token1: str,
    token2: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["token1"] = token1

    params["token2"] = token2


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/challenge/{game_id}/start-clocks".format(game_id=game_id,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ChallengeStartClocksResponse200]:
    if response.status_code == 200:
        response_200 = ChallengeStartClocksResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ChallengeStartClocksResponse200]:
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
    token1: str,
    token2: Union[Unset, str] = UNSET,

) -> Response[ChallengeStartClocksResponse200]:
    """ Start clocks of a game

     Start the clocks of a game immediately, even if a player has not yet made a move.
    Requires the OAuth tokens of both players with `challenge:write` scope.
    If the clocks have already started, the call will have no effect.

    For AI games with only one player, omit the `token2` parameter.

    Args:
        game_id (str): ID of the game
        token1 (str):
        token2 (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChallengeStartClocksResponse200]
     """


    kwargs = _get_kwargs(
        game_id=game_id,
token1=token1,
token2=token2,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    game_id: str,
    *,
    client: AuthenticatedClient,
    token1: str,
    token2: Union[Unset, str] = UNSET,

) -> Optional[ChallengeStartClocksResponse200]:
    """ Start clocks of a game

     Start the clocks of a game immediately, even if a player has not yet made a move.
    Requires the OAuth tokens of both players with `challenge:write` scope.
    If the clocks have already started, the call will have no effect.

    For AI games with only one player, omit the `token2` parameter.

    Args:
        game_id (str): ID of the game
        token1 (str):
        token2 (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChallengeStartClocksResponse200
     """


    return sync_detailed(
        game_id=game_id,
client=client,
token1=token1,
token2=token2,

    ).parsed

async def asyncio_detailed(
    game_id: str,
    *,
    client: AuthenticatedClient,
    token1: str,
    token2: Union[Unset, str] = UNSET,

) -> Response[ChallengeStartClocksResponse200]:
    """ Start clocks of a game

     Start the clocks of a game immediately, even if a player has not yet made a move.
    Requires the OAuth tokens of both players with `challenge:write` scope.
    If the clocks have already started, the call will have no effect.

    For AI games with only one player, omit the `token2` parameter.

    Args:
        game_id (str): ID of the game
        token1 (str):
        token2 (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChallengeStartClocksResponse200]
     """


    kwargs = _get_kwargs(
        game_id=game_id,
token1=token1,
token2=token2,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    game_id: str,
    *,
    client: AuthenticatedClient,
    token1: str,
    token2: Union[Unset, str] = UNSET,

) -> Optional[ChallengeStartClocksResponse200]:
    """ Start clocks of a game

     Start the clocks of a game immediately, even if a player has not yet made a move.
    Requires the OAuth tokens of both players with `challenge:write` scope.
    If the clocks have already started, the call will have no effect.

    For AI games with only one player, omit the `token2` parameter.

    Args:
        game_id (str): ID of the game
        token1 (str):
        token2 (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChallengeStartClocksResponse200
     """


    return (await asyncio_detailed(
        game_id=game_id,
client=client,
token1=token1,
token2=token2,

    )).parsed
