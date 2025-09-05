from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from typing import Union



def _get_kwargs(
    username: str,
    *,
    nb: Union[Unset, int] = UNSET,
    performance: Union[Unset, bool] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["nb"] = nb

    params["performance"] = performance


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/user/{username}/tournament/played".format(username=username,),
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
    username: str,
    *,
    client: AuthenticatedClient,
    nb: Union[Unset, int] = UNSET,
    performance: Union[Unset, bool] = UNSET,

) -> Response[Any]:
    """ Get tournaments played by a user

     Get all tournaments played by a given user.
    Tournaments are sorted by reverse chronological order of start date (last played first).
    Tournaments are streamed as [ndjson](#section/Introduction/Streaming-with-ND-JSON).
    The stream is throttled, depending on who is making the request:
      - Anonymous request: 20 tournaments per second
      - [OAuth2 authenticated](#section/Introduction/Authentication) request: 30 tournaments per second
      - Authenticated, downloading your own tournaments: 50 tournaments per second

    Args:
        username (str):
        nb (Union[Unset, int]):
        performance (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        username=username,
nb=nb,
performance=performance,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    nb: Union[Unset, int] = UNSET,
    performance: Union[Unset, bool] = UNSET,

) -> Response[Any]:
    """ Get tournaments played by a user

     Get all tournaments played by a given user.
    Tournaments are sorted by reverse chronological order of start date (last played first).
    Tournaments are streamed as [ndjson](#section/Introduction/Streaming-with-ND-JSON).
    The stream is throttled, depending on who is making the request:
      - Anonymous request: 20 tournaments per second
      - [OAuth2 authenticated](#section/Introduction/Authentication) request: 30 tournaments per second
      - Authenticated, downloading your own tournaments: 50 tournaments per second

    Args:
        username (str):
        nb (Union[Unset, int]):
        performance (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        username=username,
nb=nb,
performance=performance,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

