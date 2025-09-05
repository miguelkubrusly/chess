from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.racer_get_response_200 import RacerGetResponse200
from ...models.racer_get_response_404 import RacerGetResponse404
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/racer/{id}".format(id=id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[RacerGetResponse200, RacerGetResponse404]]:
    if response.status_code == 200:
        response_200 = RacerGetResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = RacerGetResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[RacerGetResponse200, RacerGetResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[RacerGetResponse200, RacerGetResponse404]]:
    """ Get puzzle race results

     Get the results of a [puzzle race](https://lichess.org/racer).
    Returns information about players, puzzles, and the current status of the race.
    - <https://lichess.org/racer>

    Note that Lichess puzzle races are not persisted, and are only available
    for 30 minutes. After that delay, they are permanently deleted.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RacerGetResponse200, RacerGetResponse404]]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[RacerGetResponse200, RacerGetResponse404]]:
    """ Get puzzle race results

     Get the results of a [puzzle race](https://lichess.org/racer).
    Returns information about players, puzzles, and the current status of the race.
    - <https://lichess.org/racer>

    Note that Lichess puzzle races are not persisted, and are only available
    for 30 minutes. After that delay, they are permanently deleted.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RacerGetResponse200, RacerGetResponse404]
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[RacerGetResponse200, RacerGetResponse404]]:
    """ Get puzzle race results

     Get the results of a [puzzle race](https://lichess.org/racer).
    Returns information about players, puzzles, and the current status of the race.
    - <https://lichess.org/racer>

    Note that Lichess puzzle races are not persisted, and are only available
    for 30 minutes. After that delay, they are permanently deleted.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RacerGetResponse200, RacerGetResponse404]]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[RacerGetResponse200, RacerGetResponse404]]:
    """ Get puzzle race results

     Get the results of a [puzzle race](https://lichess.org/racer).
    Returns information about players, puzzles, and the current status of the race.
    - <https://lichess.org/racer>

    Note that Lichess puzzle races are not persisted, and are only available
    for 30 minutes. After that delay, they are permanently deleted.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RacerGetResponse200, RacerGetResponse404]
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
