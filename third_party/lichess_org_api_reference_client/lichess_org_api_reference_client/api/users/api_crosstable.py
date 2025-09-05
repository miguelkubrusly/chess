from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_crosstable_response_200 import ApiCrosstableResponse200
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    user1: str,
    user2: str,
    *,
    matchup: Union[Unset, bool] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["matchup"] = matchup


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/crosstable/{user1}/{user2}".format(user1=user1,user2=user2,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ApiCrosstableResponse200]:
    if response.status_code == 200:
        response_200 = ApiCrosstableResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ApiCrosstableResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user1: str,
    user2: str,
    *,
    client: Union[AuthenticatedClient, Client],
    matchup: Union[Unset, bool] = UNSET,

) -> Response[ApiCrosstableResponse200]:
    """ Get crosstable

     Get total number of games, and current score, of any two users.
    If the `matchup` flag is provided, and the users are currently playing, also gets the current match
    game number and scores.

    Args:
        user1 (str):
        user2 (str):
        matchup (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCrosstableResponse200]
     """


    kwargs = _get_kwargs(
        user1=user1,
user2=user2,
matchup=matchup,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    user1: str,
    user2: str,
    *,
    client: Union[AuthenticatedClient, Client],
    matchup: Union[Unset, bool] = UNSET,

) -> Optional[ApiCrosstableResponse200]:
    """ Get crosstable

     Get total number of games, and current score, of any two users.
    If the `matchup` flag is provided, and the users are currently playing, also gets the current match
    game number and scores.

    Args:
        user1 (str):
        user2 (str):
        matchup (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCrosstableResponse200
     """


    return sync_detailed(
        user1=user1,
user2=user2,
client=client,
matchup=matchup,

    ).parsed

async def asyncio_detailed(
    user1: str,
    user2: str,
    *,
    client: Union[AuthenticatedClient, Client],
    matchup: Union[Unset, bool] = UNSET,

) -> Response[ApiCrosstableResponse200]:
    """ Get crosstable

     Get total number of games, and current score, of any two users.
    If the `matchup` flag is provided, and the users are currently playing, also gets the current match
    game number and scores.

    Args:
        user1 (str):
        user2 (str):
        matchup (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiCrosstableResponse200]
     """


    kwargs = _get_kwargs(
        user1=user1,
user2=user2,
matchup=matchup,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    user1: str,
    user2: str,
    *,
    client: Union[AuthenticatedClient, Client],
    matchup: Union[Unset, bool] = UNSET,

) -> Optional[ApiCrosstableResponse200]:
    """ Get crosstable

     Get total number of games, and current score, of any two users.
    If the `matchup` flag is provided, and the users are currently playing, also gets the current match
    game number and scores.

    Args:
        user1 (str):
        user2 (str):
        matchup (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiCrosstableResponse200
     """


    return (await asyncio_detailed(
        user1=user1,
user2=user2,
client=client,
matchup=matchup,

    )).parsed
