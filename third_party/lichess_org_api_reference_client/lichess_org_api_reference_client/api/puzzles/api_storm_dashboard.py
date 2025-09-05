from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_storm_dashboard_response_200 import ApiStormDashboardResponse200
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    username: str,
    *,
    days: Union[Unset, int] = 30,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["days"] = days


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/storm/dashboard/{username}".format(username=username,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ApiStormDashboardResponse200]:
    if response.status_code == 200:
        response_200 = ApiStormDashboardResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ApiStormDashboardResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    days: Union[Unset, int] = 30,

) -> Response[ApiStormDashboardResponse200]:
    """ Get the storm dashboard of a player

     Download the [storm dashboard](https://lichess.org/storm/dashboard/mrbasso) of any player as JSON.
    Contains the aggregated highscores, and the history of storm runs aggregated by days.
    Use `?days=0` if you only care about the highscores.

    Args:
        username (str):
        days (Union[Unset, int]):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiStormDashboardResponse200]
     """


    kwargs = _get_kwargs(
        username=username,
days=days,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    days: Union[Unset, int] = 30,

) -> Optional[ApiStormDashboardResponse200]:
    """ Get the storm dashboard of a player

     Download the [storm dashboard](https://lichess.org/storm/dashboard/mrbasso) of any player as JSON.
    Contains the aggregated highscores, and the history of storm runs aggregated by days.
    Use `?days=0` if you only care about the highscores.

    Args:
        username (str):
        days (Union[Unset, int]):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiStormDashboardResponse200
     """


    return sync_detailed(
        username=username,
client=client,
days=days,

    ).parsed

async def asyncio_detailed(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    days: Union[Unset, int] = 30,

) -> Response[ApiStormDashboardResponse200]:
    """ Get the storm dashboard of a player

     Download the [storm dashboard](https://lichess.org/storm/dashboard/mrbasso) of any player as JSON.
    Contains the aggregated highscores, and the history of storm runs aggregated by days.
    Use `?days=0` if you only care about the highscores.

    Args:
        username (str):
        days (Union[Unset, int]):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiStormDashboardResponse200]
     """


    kwargs = _get_kwargs(
        username=username,
days=days,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    days: Union[Unset, int] = 30,

) -> Optional[ApiStormDashboardResponse200]:
    """ Get the storm dashboard of a player

     Download the [storm dashboard](https://lichess.org/storm/dashboard/mrbasso) of any player as JSON.
    Contains the aggregated highscores, and the history of storm runs aggregated by days.
    Use `?days=0` if you only care about the highscores.

    Args:
        username (str):
        days (Union[Unset, int]):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiStormDashboardResponse200
     """


    return (await asyncio_detailed(
        username=username,
client=client,
days=days,

    )).parsed
