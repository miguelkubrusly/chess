from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.unblock_user_response_200 import UnblockUserResponse200
from typing import cast



def _get_kwargs(
    username: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/rel/unblock/{username}".format(username=username,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[UnblockUserResponse200]:
    if response.status_code == 200:
        response_200 = UnblockUserResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[UnblockUserResponse200]:
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

) -> Response[UnblockUserResponse200]:
    """ Unblock a player

     Unblock a player, removing them from your list of blocked Lichess users.

    Args:
        username (str):  Example: thibault.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnblockUserResponse200]
     """


    kwargs = _get_kwargs(
        username=username,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    username: str,
    *,
    client: AuthenticatedClient,

) -> Optional[UnblockUserResponse200]:
    """ Unblock a player

     Unblock a player, removing them from your list of blocked Lichess users.

    Args:
        username (str):  Example: thibault.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnblockUserResponse200
     """


    return sync_detailed(
        username=username,
client=client,

    ).parsed

async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,

) -> Response[UnblockUserResponse200]:
    """ Unblock a player

     Unblock a player, removing them from your list of blocked Lichess users.

    Args:
        username (str):  Example: thibault.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UnblockUserResponse200]
     """


    kwargs = _get_kwargs(
        username=username,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,

) -> Optional[UnblockUserResponse200]:
    """ Unblock a player

     Unblock a player, removing them from your list of blocked Lichess users.

    Args:
        username (str):  Example: thibault.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UnblockUserResponse200
     """


    return (await asyncio_detailed(
        username=username,
client=client,

    )).parsed
