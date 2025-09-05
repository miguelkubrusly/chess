from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.timeline_response_200 import TimelineResponse200
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    since: Union[Unset, int] = UNSET,
    nb: Union[Unset, int] = 15,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["since"] = since

    params["nb"] = nb


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/timeline",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[TimelineResponse200]:
    if response.status_code == 200:
        response_200 = TimelineResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[TimelineResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    since: Union[Unset, int] = UNSET,
    nb: Union[Unset, int] = 15,

) -> Response[TimelineResponse200]:
    """ Get my timeline

     Get the timeline events of the logged in user.

    Args:
        since (Union[Unset, int]):
        nb (Union[Unset, int]):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TimelineResponse200]
     """


    kwargs = _get_kwargs(
        since=since,
nb=nb,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    since: Union[Unset, int] = UNSET,
    nb: Union[Unset, int] = 15,

) -> Optional[TimelineResponse200]:
    """ Get my timeline

     Get the timeline events of the logged in user.

    Args:
        since (Union[Unset, int]):
        nb (Union[Unset, int]):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TimelineResponse200
     """


    return sync_detailed(
        client=client,
since=since,
nb=nb,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    since: Union[Unset, int] = UNSET,
    nb: Union[Unset, int] = 15,

) -> Response[TimelineResponse200]:
    """ Get my timeline

     Get the timeline events of the logged in user.

    Args:
        since (Union[Unset, int]):
        nb (Union[Unset, int]):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TimelineResponse200]
     """


    kwargs = _get_kwargs(
        since=since,
nb=nb,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    since: Union[Unset, int] = UNSET,
    nb: Union[Unset, int] = 15,

) -> Optional[TimelineResponse200]:
    """ Get my timeline

     Get the timeline events of the logged in user.

    Args:
        since (Union[Unset, int]):
        nb (Union[Unset, int]):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TimelineResponse200
     """


    return (await asyncio_detailed(
        client=client,
since=since,
nb=nb,

    )).parsed
