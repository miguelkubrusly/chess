from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.challenge_cancel_response_200 import ChallengeCancelResponse200
from ...models.challenge_cancel_response_404 import ChallengeCancelResponse404
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    challenge_id: str,
    *,
    opponent_token: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["opponentToken"] = opponent_token


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/challenge/{challenge_id}/cancel".format(challenge_id=challenge_id,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ChallengeCancelResponse200, ChallengeCancelResponse404]]:
    if response.status_code == 200:
        response_200 = ChallengeCancelResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = ChallengeCancelResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ChallengeCancelResponse200, ChallengeCancelResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    challenge_id: str,
    *,
    client: AuthenticatedClient,
    opponent_token: Union[Unset, str] = UNSET,

) -> Response[Union[ChallengeCancelResponse200, ChallengeCancelResponse404]]:
    """ Cancel a challenge

     Cancel a challenge you sent, or aborts the game if the challenge was accepted, but the game was not
    yet played.
    Note that the ID of a game is the same as the ID of the challenge that created it.
    Works for user challenges and open challenges alike.

    Args:
        challenge_id (str):  Example: 5IrD6Gzz.
        opponent_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChallengeCancelResponse200, ChallengeCancelResponse404]]
     """


    kwargs = _get_kwargs(
        challenge_id=challenge_id,
opponent_token=opponent_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    challenge_id: str,
    *,
    client: AuthenticatedClient,
    opponent_token: Union[Unset, str] = UNSET,

) -> Optional[Union[ChallengeCancelResponse200, ChallengeCancelResponse404]]:
    """ Cancel a challenge

     Cancel a challenge you sent, or aborts the game if the challenge was accepted, but the game was not
    yet played.
    Note that the ID of a game is the same as the ID of the challenge that created it.
    Works for user challenges and open challenges alike.

    Args:
        challenge_id (str):  Example: 5IrD6Gzz.
        opponent_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChallengeCancelResponse200, ChallengeCancelResponse404]
     """


    return sync_detailed(
        challenge_id=challenge_id,
client=client,
opponent_token=opponent_token,

    ).parsed

async def asyncio_detailed(
    challenge_id: str,
    *,
    client: AuthenticatedClient,
    opponent_token: Union[Unset, str] = UNSET,

) -> Response[Union[ChallengeCancelResponse200, ChallengeCancelResponse404]]:
    """ Cancel a challenge

     Cancel a challenge you sent, or aborts the game if the challenge was accepted, but the game was not
    yet played.
    Note that the ID of a game is the same as the ID of the challenge that created it.
    Works for user challenges and open challenges alike.

    Args:
        challenge_id (str):  Example: 5IrD6Gzz.
        opponent_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChallengeCancelResponse200, ChallengeCancelResponse404]]
     """


    kwargs = _get_kwargs(
        challenge_id=challenge_id,
opponent_token=opponent_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    challenge_id: str,
    *,
    client: AuthenticatedClient,
    opponent_token: Union[Unset, str] = UNSET,

) -> Optional[Union[ChallengeCancelResponse200, ChallengeCancelResponse404]]:
    """ Cancel a challenge

     Cancel a challenge you sent, or aborts the game if the challenge was accepted, but the game was not
    yet played.
    Note that the ID of a game is the same as the ID of the challenge that created it.
    Works for user challenges and open challenges alike.

    Args:
        challenge_id (str):  Example: 5IrD6Gzz.
        opponent_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChallengeCancelResponse200, ChallengeCancelResponse404]
     """


    return (await asyncio_detailed(
        challenge_id=challenge_id,
client=client,
opponent_token=opponent_token,

    )).parsed
