from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.broadcast_tour_get_response_200 import BroadcastTourGetResponse200
from typing import cast



def _get_kwargs(
    broadcast_tournament_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/broadcast/{broadcast_tournament_id}".format(broadcast_tournament_id=broadcast_tournament_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[BroadcastTourGetResponse200]:
    if response.status_code == 200:
        response_200 = BroadcastTourGetResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[BroadcastTourGetResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    broadcast_tournament_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[BroadcastTourGetResponse200]:
    """ Get a broadcast tournament

     Get information about a broadcast tournament.

    Args:
        broadcast_tournament_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BroadcastTourGetResponse200]
     """


    kwargs = _get_kwargs(
        broadcast_tournament_id=broadcast_tournament_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    broadcast_tournament_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[BroadcastTourGetResponse200]:
    """ Get a broadcast tournament

     Get information about a broadcast tournament.

    Args:
        broadcast_tournament_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BroadcastTourGetResponse200
     """


    return sync_detailed(
        broadcast_tournament_id=broadcast_tournament_id,
client=client,

    ).parsed

async def asyncio_detailed(
    broadcast_tournament_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[BroadcastTourGetResponse200]:
    """ Get a broadcast tournament

     Get information about a broadcast tournament.

    Args:
        broadcast_tournament_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BroadcastTourGetResponse200]
     """


    kwargs = _get_kwargs(
        broadcast_tournament_id=broadcast_tournament_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    broadcast_tournament_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[BroadcastTourGetResponse200]:
    """ Get a broadcast tournament

     Get information about a broadcast tournament.

    Args:
        broadcast_tournament_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BroadcastTourGetResponse200
     """


    return (await asyncio_detailed(
        broadcast_tournament_id=broadcast_tournament_id,
client=client,

    )).parsed
