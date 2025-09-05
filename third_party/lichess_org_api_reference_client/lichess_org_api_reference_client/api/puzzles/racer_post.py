from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.racer_post_response_200 import RacerPostResponse200
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/racer",
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[RacerPostResponse200]:
    if response.status_code == 200:
        response_200 = RacerPostResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[RacerPostResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[RacerPostResponse200]:
    """ Create and join a puzzle race

     Create a new private [puzzle race](https://lichess.org/racer).
    The Lichess user who creates the race must join the race page,
    and manually start the race when enough players have joined.
    - <https://lichess.org/racer>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RacerPostResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> Optional[RacerPostResponse200]:
    """ Create and join a puzzle race

     Create a new private [puzzle race](https://lichess.org/racer).
    The Lichess user who creates the race must join the race page,
    and manually start the race when enough players have joined.
    - <https://lichess.org/racer>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RacerPostResponse200
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[RacerPostResponse200]:
    """ Create and join a puzzle race

     Create a new private [puzzle race](https://lichess.org/racer).
    The Lichess user who creates the race must join the race page,
    and manually start the race when enough players have joined.
    - <https://lichess.org/racer>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RacerPostResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> Optional[RacerPostResponse200]:
    """ Create and join a puzzle race

     Create a new private [puzzle race](https://lichess.org/racer).
    The Lichess user who creates the race must join the race page,
    and manually start the race when enough players have joined.
    - <https://lichess.org/racer>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RacerPostResponse200
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
