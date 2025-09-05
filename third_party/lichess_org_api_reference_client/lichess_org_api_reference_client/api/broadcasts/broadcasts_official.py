from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from typing import Union



def _get_kwargs(
    *,
    nb: Union[Unset, int] = 20,
    html: Union[Unset, bool] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["nb"] = nb

    params["html"] = html


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/broadcast",
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
    *,
    client: Union[AuthenticatedClient, Client],
    nb: Union[Unset, int] = 20,
    html: Union[Unset, bool] = UNSET,

) -> Response[Any]:
    """ Get official broadcasts

     Returns ongoing official broadcasts sorted by tier.
    After that, returns finished broadcasts sorted by most recent sync time.
    Broadcasts are streamed as [ndjson](#section/Introduction/Streaming-with-ND-JSON).

    Args:
        nb (Union[Unset, int]):  Default: 20.
        html (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        nb=nb,
html=html,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    nb: Union[Unset, int] = 20,
    html: Union[Unset, bool] = UNSET,

) -> Response[Any]:
    """ Get official broadcasts

     Returns ongoing official broadcasts sorted by tier.
    After that, returns finished broadcasts sorted by most recent sync time.
    Broadcasts are streamed as [ndjson](#section/Introduction/Streaming-with-ND-JSON).

    Args:
        nb (Union[Unset, int]):  Default: 20.
        html (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        nb=nb,
html=html,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

