from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.broadcast_round_reset_response_200 import BroadcastRoundResetResponse200
from typing import cast



def _get_kwargs(
    broadcast_round_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/broadcast/round/{broadcast_round_id}/reset".format(broadcast_round_id=broadcast_round_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[BroadcastRoundResetResponse200]:
    if response.status_code == 200:
        response_200 = BroadcastRoundResetResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[BroadcastRoundResetResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    broadcast_round_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[BroadcastRoundResetResponse200]:
    """ Reset a broadcast round

     Remove any games from the broadcast round and reset it to its initial state.

    Args:
        broadcast_round_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BroadcastRoundResetResponse200]
     """


    kwargs = _get_kwargs(
        broadcast_round_id=broadcast_round_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    broadcast_round_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[BroadcastRoundResetResponse200]:
    """ Reset a broadcast round

     Remove any games from the broadcast round and reset it to its initial state.

    Args:
        broadcast_round_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BroadcastRoundResetResponse200
     """


    return sync_detailed(
        broadcast_round_id=broadcast_round_id,
client=client,

    ).parsed

async def asyncio_detailed(
    broadcast_round_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[BroadcastRoundResetResponse200]:
    """ Reset a broadcast round

     Remove any games from the broadcast round and reset it to its initial state.

    Args:
        broadcast_round_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BroadcastRoundResetResponse200]
     """


    kwargs = _get_kwargs(
        broadcast_round_id=broadcast_round_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    broadcast_round_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[BroadcastRoundResetResponse200]:
    """ Reset a broadcast round

     Remove any games from the broadcast round and reset it to its initial state.

    Args:
        broadcast_round_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BroadcastRoundResetResponse200
     """


    return (await asyncio_detailed(
        broadcast_round_id=broadcast_round_id,
client=client,

    )).parsed
