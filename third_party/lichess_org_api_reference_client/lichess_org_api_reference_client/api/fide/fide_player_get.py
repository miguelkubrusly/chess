from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.fide_player_get_response_200 import FidePlayerGetResponse200
from typing import cast



def _get_kwargs(
    player_id: float,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/fide/player/{player_id}".format(player_id=player_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[FidePlayerGetResponse200]:
    if response.status_code == 200:
        response_200 = FidePlayerGetResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[FidePlayerGetResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    player_id: float,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[FidePlayerGetResponse200]:
    """ Get a FIDE player

     Get information about a FIDE player.

    Args:
        player_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FidePlayerGetResponse200]
     """


    kwargs = _get_kwargs(
        player_id=player_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    player_id: float,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[FidePlayerGetResponse200]:
    """ Get a FIDE player

     Get information about a FIDE player.

    Args:
        player_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FidePlayerGetResponse200
     """


    return sync_detailed(
        player_id=player_id,
client=client,

    ).parsed

async def asyncio_detailed(
    player_id: float,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[FidePlayerGetResponse200]:
    """ Get a FIDE player

     Get information about a FIDE player.

    Args:
        player_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FidePlayerGetResponse200]
     """


    kwargs = _get_kwargs(
        player_id=player_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    player_id: float,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[FidePlayerGetResponse200]:
    """ Get a FIDE player

     Get information about a FIDE player.

    Args:
        player_id (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FidePlayerGetResponse200
     """


    return (await asyncio_detailed(
        player_id=player_id,
client=client,

    )).parsed
