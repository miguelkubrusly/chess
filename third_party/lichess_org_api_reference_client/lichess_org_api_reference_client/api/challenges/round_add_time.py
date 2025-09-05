from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.round_add_time_response_200 import RoundAddTimeResponse200
from typing import cast



def _get_kwargs(
    game_id: str,
    seconds: float,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/round/{game_id}/add-time/{seconds}".format(game_id=game_id,seconds=seconds,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[RoundAddTimeResponse200]:
    if response.status_code == 200:
        response_200 = RoundAddTimeResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[RoundAddTimeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_id: str,
    seconds: float,
    *,
    client: AuthenticatedClient,

) -> Response[RoundAddTimeResponse200]:
    """ Add time to the opponent clock

     Add seconds to the opponent's clock. Can be used to create games with time odds.

    Args:
        game_id (str): ID of the game
        seconds (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RoundAddTimeResponse200]
     """


    kwargs = _get_kwargs(
        game_id=game_id,
seconds=seconds,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    game_id: str,
    seconds: float,
    *,
    client: AuthenticatedClient,

) -> Optional[RoundAddTimeResponse200]:
    """ Add time to the opponent clock

     Add seconds to the opponent's clock. Can be used to create games with time odds.

    Args:
        game_id (str): ID of the game
        seconds (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RoundAddTimeResponse200
     """


    return sync_detailed(
        game_id=game_id,
seconds=seconds,
client=client,

    ).parsed

async def asyncio_detailed(
    game_id: str,
    seconds: float,
    *,
    client: AuthenticatedClient,

) -> Response[RoundAddTimeResponse200]:
    """ Add time to the opponent clock

     Add seconds to the opponent's clock. Can be used to create games with time odds.

    Args:
        game_id (str): ID of the game
        seconds (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RoundAddTimeResponse200]
     """


    kwargs = _get_kwargs(
        game_id=game_id,
seconds=seconds,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    game_id: str,
    seconds: float,
    *,
    client: AuthenticatedClient,

) -> Optional[RoundAddTimeResponse200]:
    """ Add time to the opponent clock

     Add seconds to the opponent's clock. Can be used to create games with time odds.

    Args:
        game_id (str): ID of the game
        seconds (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RoundAddTimeResponse200
     """


    return (await asyncio_detailed(
        game_id=game_id,
seconds=seconds,
client=client,

    )).parsed
