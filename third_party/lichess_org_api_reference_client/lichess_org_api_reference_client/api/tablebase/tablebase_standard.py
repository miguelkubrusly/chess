from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.tablebase_standard_response_200 import TablebaseStandardResponse200
from typing import cast



def _get_kwargs(
    *,
    fen: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["fen"] = fen


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/standard",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[TablebaseStandardResponse200]:
    if response.status_code == 200:
        response_200 = TablebaseStandardResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[TablebaseStandardResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fen: str,

) -> Response[TablebaseStandardResponse200]:
    """ Tablebase lookup

     **Endpoint: <https://tablebase.lichess.ovh>**
    Example: `curl http://tablebase.lichess.ovh/standard?fen=4k3/6KP/8/8/8/8/7p/8_w_-_-_0_1`

    Args:
        fen (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TablebaseStandardResponse200]
     """


    kwargs = _get_kwargs(
        fen=fen,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    fen: str,

) -> Optional[TablebaseStandardResponse200]:
    """ Tablebase lookup

     **Endpoint: <https://tablebase.lichess.ovh>**
    Example: `curl http://tablebase.lichess.ovh/standard?fen=4k3/6KP/8/8/8/8/7p/8_w_-_-_0_1`

    Args:
        fen (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TablebaseStandardResponse200
     """


    return sync_detailed(
        client=client,
fen=fen,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fen: str,

) -> Response[TablebaseStandardResponse200]:
    """ Tablebase lookup

     **Endpoint: <https://tablebase.lichess.ovh>**
    Example: `curl http://tablebase.lichess.ovh/standard?fen=4k3/6KP/8/8/8/8/7p/8_w_-_-_0_1`

    Args:
        fen (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TablebaseStandardResponse200]
     """


    kwargs = _get_kwargs(
        fen=fen,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    fen: str,

) -> Optional[TablebaseStandardResponse200]:
    """ Tablebase lookup

     **Endpoint: <https://tablebase.lichess.ovh>**
    Example: `curl http://tablebase.lichess.ovh/standard?fen=4k3/6KP/8/8/8/8/7p/8_w_-_-_0_1`

    Args:
        fen (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TablebaseStandardResponse200
     """


    return (await asyncio_detailed(
        client=client,
fen=fen,

    )).parsed
