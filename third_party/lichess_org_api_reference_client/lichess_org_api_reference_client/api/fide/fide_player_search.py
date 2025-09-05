from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.fide_player_search_response_200_item import FidePlayerSearchResponse200Item
from typing import cast



def _get_kwargs(
    *,
    q: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["q"] = q


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/fide/player",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[list['FidePlayerSearchResponse200Item']]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = FidePlayerSearchResponse200Item.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[list['FidePlayerSearchResponse200Item']]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    q: str,

) -> Response[list['FidePlayerSearchResponse200Item']]:
    """ Search FIDE players

     List of FIDE players search results for a query.

    Args:
        q (str):  Example: Erigaisi Arjun.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['FidePlayerSearchResponse200Item']]
     """


    kwargs = _get_kwargs(
        q=q,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    q: str,

) -> Optional[list['FidePlayerSearchResponse200Item']]:
    """ Search FIDE players

     List of FIDE players search results for a query.

    Args:
        q (str):  Example: Erigaisi Arjun.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['FidePlayerSearchResponse200Item']
     """


    return sync_detailed(
        client=client,
q=q,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    q: str,

) -> Response[list['FidePlayerSearchResponse200Item']]:
    """ Search FIDE players

     List of FIDE players search results for a query.

    Args:
        q (str):  Example: Erigaisi Arjun.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['FidePlayerSearchResponse200Item']]
     """


    kwargs = _get_kwargs(
        q=q,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    q: str,

) -> Optional[list['FidePlayerSearchResponse200Item']]:
    """ Search FIDE players

     List of FIDE players search results for a query.

    Args:
        q (str):  Example: Erigaisi Arjun.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['FidePlayerSearchResponse200Item']
     """


    return (await asyncio_detailed(
        client=client,
q=q,

    )).parsed
