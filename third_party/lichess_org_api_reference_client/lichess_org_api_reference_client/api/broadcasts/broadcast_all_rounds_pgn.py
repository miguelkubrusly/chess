from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    broadcast_tournament_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/broadcast/{broadcast_tournament_id}.pgn".format(broadcast_tournament_id=broadcast_tournament_id,),
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
    broadcast_tournament_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    """ Export all rounds as PGN

     Download all games of all rounds of a broadcast in PGN format.
    If a `study:read` [OAuth token](#tag/OAuth) is provided,
    the private rounds where the user is a contributor will be available.
    You may want to [download only the games of a single round](#operation/broadcastRoundPgn) instead.

    Args:
        broadcast_tournament_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        broadcast_tournament_id=broadcast_tournament_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    broadcast_tournament_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    """ Export all rounds as PGN

     Download all games of all rounds of a broadcast in PGN format.
    If a `study:read` [OAuth token](#tag/OAuth) is provided,
    the private rounds where the user is a contributor will be available.
    You may want to [download only the games of a single round](#operation/broadcastRoundPgn) instead.

    Args:
        broadcast_tournament_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        broadcast_tournament_id=broadcast_tournament_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

