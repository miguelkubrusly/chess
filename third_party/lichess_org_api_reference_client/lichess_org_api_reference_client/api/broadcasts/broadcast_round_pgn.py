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
        "url": "/api/broadcast/round/{broadcast_round_id}.pgn".format(broadcast_round_id=broadcast_round_id,),
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
    """ Export one round as PGN

     Download all games of a single round of a broadcast tournament in PGN format.
    You *could* poll this endpoint to get updates about a tournament, but it would be slow,
    and very inefficient.
    Instead, consider [streaming the tournament](#operation/broadcastStreamRoundPgn) to get
    a new PGN every time a game is updated, in real-time.

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
    """ Export one round as PGN

     Download all games of a single round of a broadcast tournament in PGN format.
    You *could* poll this endpoint to get updates about a tournament, but it would be slow,
    and very inefficient.
    Instead, consider [streaming the tournament](#operation/broadcastStreamRoundPgn) to get
    a new PGN every time a game is updated, in real-time.

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

