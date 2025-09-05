from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.broadcasts_by_user_response_200 import BroadcastsByUserResponse200
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    username: str,
    *,
    page: Union[Unset, float] = 1.0,
    html: Union[Unset, bool] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["html"] = html


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/broadcast/by/{username}".format(username=username,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[BroadcastsByUserResponse200]:
    if response.status_code == 200:
        response_200 = BroadcastsByUserResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[BroadcastsByUserResponse200]:
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
    page: Union[Unset, float] = 1.0,
    html: Union[Unset, bool] = UNSET,

) -> Response[BroadcastsByUserResponse200]:
    """ Get broadcasts created by a user

     Get all incoming, ongoing, and finished official broadcasts.
    The broadcasts are sorted by created date, most recent first.

    Args:
        username (str):
        page (Union[Unset, float]):  Default: 1.0. Example: 1.
        html (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BroadcastsByUserResponse200]
     """


    kwargs = _get_kwargs(
        username=username,
page=page,
html=html,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = 1.0,
    html: Union[Unset, bool] = UNSET,

) -> Optional[BroadcastsByUserResponse200]:
    """ Get broadcasts created by a user

     Get all incoming, ongoing, and finished official broadcasts.
    The broadcasts are sorted by created date, most recent first.

    Args:
        username (str):
        page (Union[Unset, float]):  Default: 1.0. Example: 1.
        html (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BroadcastsByUserResponse200
     """


    return sync_detailed(
        username=username,
client=client,
page=page,
html=html,

    ).parsed

async def asyncio_detailed(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = 1.0,
    html: Union[Unset, bool] = UNSET,

) -> Response[BroadcastsByUserResponse200]:
    """ Get broadcasts created by a user

     Get all incoming, ongoing, and finished official broadcasts.
    The broadcasts are sorted by created date, most recent first.

    Args:
        username (str):
        page (Union[Unset, float]):  Default: 1.0. Example: 1.
        html (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BroadcastsByUserResponse200]
     """


    kwargs = _get_kwargs(
        username=username,
page=page,
html=html,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, float] = 1.0,
    html: Union[Unset, bool] = UNSET,

) -> Optional[BroadcastsByUserResponse200]:
    """ Get broadcasts created by a user

     Get all incoming, ongoing, and finished official broadcasts.
    The broadcasts are sorted by created date, most recent first.

    Args:
        username (str):
        page (Union[Unset, float]):  Default: 1.0. Example: 1.
        html (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BroadcastsByUserResponse200
     """


    return (await asyncio_detailed(
        username=username,
client=client,
page=page,
html=html,

    )).parsed
