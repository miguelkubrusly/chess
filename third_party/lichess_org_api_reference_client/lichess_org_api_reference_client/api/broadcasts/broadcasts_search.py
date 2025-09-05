from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.broadcasts_search_response_200 import BroadcastsSearchResponse200
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    page: Union[Unset, int] = 1,
    q: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["q"] = q


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/broadcast/search",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[BroadcastsSearchResponse200]:
    if response.status_code == 200:
        response_200 = BroadcastsSearchResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[BroadcastsSearchResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    q: Union[Unset, str] = UNSET,

) -> Response[BroadcastsSearchResponse200]:
    """ Search broadcasts

     Search across recent official broadcasts.

    Args:
        page (Union[Unset, int]):  Default: 1.
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BroadcastsSearchResponse200]
     """


    kwargs = _get_kwargs(
        page=page,
q=q,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    q: Union[Unset, str] = UNSET,

) -> Optional[BroadcastsSearchResponse200]:
    """ Search broadcasts

     Search across recent official broadcasts.

    Args:
        page (Union[Unset, int]):  Default: 1.
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BroadcastsSearchResponse200
     """


    return sync_detailed(
        client=client,
page=page,
q=q,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    q: Union[Unset, str] = UNSET,

) -> Response[BroadcastsSearchResponse200]:
    """ Search broadcasts

     Search across recent official broadcasts.

    Args:
        page (Union[Unset, int]):  Default: 1.
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BroadcastsSearchResponse200]
     """


    kwargs = _get_kwargs(
        page=page,
q=q,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    q: Union[Unset, str] = UNSET,

) -> Optional[BroadcastsSearchResponse200]:
    """ Search broadcasts

     Search across recent official broadcasts.

    Args:
        page (Union[Unset, int]):  Default: 1.
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BroadcastsSearchResponse200
     """


    return (await asyncio_detailed(
        client=client,
page=page,
q=q,

    )).parsed
