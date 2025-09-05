from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    broadcast_round_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/stream/broadcast/round/{broadcast_round_id}.pgn".format(broadcast_round_id=broadcast_round_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    broadcast_round_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    """ Stream an ongoing broadcast round as PGN

     This streaming endpoint first sends all games of a broadcast round in PGN format.
    Then, it waits for new moves to be played. As soon as it happens, the entire PGN of the game is sent
    to the stream.
    The stream will also send PGNs when games are added to the round.
    This is the best way to get updates about an ongoing round. Streaming means no polling,
    and no pollings means no latency, and minimum impact on the server.

    Args:
        broadcast_round_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        broadcast_round_id=broadcast_round_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    broadcast_round_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    """ Stream an ongoing broadcast round as PGN

     This streaming endpoint first sends all games of a broadcast round in PGN format.
    Then, it waits for new moves to be played. As soon as it happens, the entire PGN of the game is sent
    to the stream.
    The stream will also send PGNs when games are added to the round.
    This is the best way to get updates about an ongoing round. Streaming means no polling,
    and no pollings means no latency, and minimum impact on the server.

    Args:
        broadcast_round_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        broadcast_round_id=broadcast_round_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

