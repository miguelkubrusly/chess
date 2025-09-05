from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/stream/event",
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
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    """ Stream incoming events

     Stream the events reaching a lichess user in real time as [ndjson](#section/Introduction/Streaming-
    with-ND-JSON).

    An empty line is sent every 7 seconds for keep alive purposes.

    Each non-empty line is a JSON object containing a `type` field. Possible values are:
    - `gameStart` Start of a game
    - `gameFinish` Completion of a game
    - `challenge` A player sends you a challenge or you challenge someone
    - `challengeCanceled` A player cancels their challenge to you
    - `challengeDeclined` The opponent declines your challenge

    When the stream opens, all current challenges and games are sent.

    Only one global event stream can be active at a time. When the stream opens, the previous one with
    the same access token is closed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    """ Stream incoming events

     Stream the events reaching a lichess user in real time as [ndjson](#section/Introduction/Streaming-
    with-ND-JSON).

    An empty line is sent every 7 seconds for keep alive purposes.

    Each non-empty line is a JSON object containing a `type` field. Possible values are:
    - `gameStart` Start of a game
    - `gameFinish` Completion of a game
    - `challenge` A player sends you a challenge or you challenge someone
    - `challengeCanceled` A player cancels their challenge to you
    - `challengeDeclined` The opponent declines your challenge

    When the stream opens, all current challenges and games are sent.

    Only one global event stream can be active at a time. When the stream opens, the previous one with
    the same access token is closed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

