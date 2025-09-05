from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.player_top_nb_perf_type_perf_type import PlayerTopNbPerfTypePerfType
from ...models.player_top_nb_perf_type_response_200 import PlayerTopNbPerfTypeResponse200
from typing import cast



def _get_kwargs(
    nb: int,
    perf_type: PlayerTopNbPerfTypePerfType,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/player/top/{nb}/{perf_type}".format(nb=nb,perf_type=perf_type,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PlayerTopNbPerfTypeResponse200]:
    if response.status_code == 200:
        response_200 = PlayerTopNbPerfTypeResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PlayerTopNbPerfTypeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    nb: int,
    perf_type: PlayerTopNbPerfTypePerfType,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[PlayerTopNbPerfTypeResponse200]:
    """ Get one leaderboard

     Get the leaderboard for a single speed or variant (a.k.a. `perfType`).
    There is no leaderboard for correspondence or puzzles.
    See <https://lichess.org/player/top/200/bullet>.

    Args:
        nb (int):  Example: 100.
        perf_type (PlayerTopNbPerfTypePerfType):  Example: bullet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlayerTopNbPerfTypeResponse200]
     """


    kwargs = _get_kwargs(
        nb=nb,
perf_type=perf_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    nb: int,
    perf_type: PlayerTopNbPerfTypePerfType,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[PlayerTopNbPerfTypeResponse200]:
    """ Get one leaderboard

     Get the leaderboard for a single speed or variant (a.k.a. `perfType`).
    There is no leaderboard for correspondence or puzzles.
    See <https://lichess.org/player/top/200/bullet>.

    Args:
        nb (int):  Example: 100.
        perf_type (PlayerTopNbPerfTypePerfType):  Example: bullet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlayerTopNbPerfTypeResponse200
     """


    return sync_detailed(
        nb=nb,
perf_type=perf_type,
client=client,

    ).parsed

async def asyncio_detailed(
    nb: int,
    perf_type: PlayerTopNbPerfTypePerfType,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[PlayerTopNbPerfTypeResponse200]:
    """ Get one leaderboard

     Get the leaderboard for a single speed or variant (a.k.a. `perfType`).
    There is no leaderboard for correspondence or puzzles.
    See <https://lichess.org/player/top/200/bullet>.

    Args:
        nb (int):  Example: 100.
        perf_type (PlayerTopNbPerfTypePerfType):  Example: bullet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlayerTopNbPerfTypeResponse200]
     """


    kwargs = _get_kwargs(
        nb=nb,
perf_type=perf_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    nb: int,
    perf_type: PlayerTopNbPerfTypePerfType,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[PlayerTopNbPerfTypeResponse200]:
    """ Get one leaderboard

     Get the leaderboard for a single speed or variant (a.k.a. `perfType`).
    There is no leaderboard for correspondence or puzzles.
    See <https://lichess.org/player/top/200/bullet>.

    Args:
        nb (int):  Example: 100.
        perf_type (PlayerTopNbPerfTypePerfType):  Example: bullet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlayerTopNbPerfTypeResponse200
     """


    return (await asyncio_detailed(
        nb=nb,
perf_type=perf_type,
client=client,

    )).parsed
