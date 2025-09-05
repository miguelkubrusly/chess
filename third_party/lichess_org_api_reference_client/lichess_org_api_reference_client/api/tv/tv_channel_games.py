from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from typing import Union



def _get_kwargs(
    channel: str,
    *,
    nb: Union[Unset, float] = 10.0,
    moves: Union[Unset, bool] = True,
    pgn_in_json: Union[Unset, bool] = False,
    tags: Union[Unset, bool] = True,
    clocks: Union[Unset, bool] = False,
    opening: Union[Unset, bool] = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["nb"] = nb

    params["moves"] = moves

    params["pgnInJson"] = pgn_in_json

    params["tags"] = tags

    params["clocks"] = clocks

    params["opening"] = opening


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tv/{channel}".format(channel=channel,),
        "params": params,
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
    channel: str,
    *,
    client: Union[AuthenticatedClient, Client],
    nb: Union[Unset, float] = 10.0,
    moves: Union[Unset, bool] = True,
    pgn_in_json: Union[Unset, bool] = False,
    tags: Union[Unset, bool] = True,
    clocks: Union[Unset, bool] = False,
    opening: Union[Unset, bool] = False,

) -> Response[Any]:
    """ Get best ongoing games of a TV channel

     Get a list of ongoing games for a given TV channel. Similar to
    [lichess.org/games](https://lichess.org/games).
    Available in PGN or [ndjson](#section/Introduction/Streaming-with-ND-JSON) format, depending on the
    request `Accept` header.

    Args:
        channel (str):
        nb (Union[Unset, float]):  Default: 10.0.
        moves (Union[Unset, bool]):  Default: True.
        pgn_in_json (Union[Unset, bool]):  Default: False.
        tags (Union[Unset, bool]):  Default: True.
        clocks (Union[Unset, bool]):  Default: False.
        opening (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        channel=channel,
nb=nb,
moves=moves,
pgn_in_json=pgn_in_json,
tags=tags,
clocks=clocks,
opening=opening,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    channel: str,
    *,
    client: Union[AuthenticatedClient, Client],
    nb: Union[Unset, float] = 10.0,
    moves: Union[Unset, bool] = True,
    pgn_in_json: Union[Unset, bool] = False,
    tags: Union[Unset, bool] = True,
    clocks: Union[Unset, bool] = False,
    opening: Union[Unset, bool] = False,

) -> Response[Any]:
    """ Get best ongoing games of a TV channel

     Get a list of ongoing games for a given TV channel. Similar to
    [lichess.org/games](https://lichess.org/games).
    Available in PGN or [ndjson](#section/Introduction/Streaming-with-ND-JSON) format, depending on the
    request `Accept` header.

    Args:
        channel (str):
        nb (Union[Unset, float]):  Default: 10.0.
        moves (Union[Unset, bool]):  Default: True.
        pgn_in_json (Union[Unset, bool]):  Default: False.
        tags (Union[Unset, bool]):  Default: True.
        clocks (Union[Unset, bool]):  Default: False.
        opening (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        channel=channel,
nb=nb,
moves=moves,
pgn_in_json=pgn_in_json,
tags=tags,
clocks=clocks,
opening=opening,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

