from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.team_of_username_response_200_item import TeamOfUsernameResponse200Item
from typing import cast



def _get_kwargs(
    username: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/team/of/{username}".format(username=username,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[list['TeamOfUsernameResponse200Item']]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = TeamOfUsernameResponse200Item.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[list['TeamOfUsernameResponse200Item']]:
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

) -> Response[list['TeamOfUsernameResponse200Item']]:
    """ Teams of a player

     All the teams a player is a member of.

    Args:
        username (str):  Example: thibault.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['TeamOfUsernameResponse200Item']]
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
    client: Union[AuthenticatedClient, Client],

) -> Optional[list['TeamOfUsernameResponse200Item']]:
    """ Teams of a player

     All the teams a player is a member of.

    Args:
        username (str):  Example: thibault.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['TeamOfUsernameResponse200Item']
     """


    return sync_detailed(
        username=username,
client=client,

    ).parsed

async def asyncio_detailed(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[list['TeamOfUsernameResponse200Item']]:
    """ Teams of a player

     All the teams a player is a member of.

    Args:
        username (str):  Example: thibault.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['TeamOfUsernameResponse200Item']]
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
    client: Union[AuthenticatedClient, Client],

) -> Optional[list['TeamOfUsernameResponse200Item']]:
    """ Teams of a player

     All the teams a player is a member of.

    Args:
        username (str):  Example: thibault.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['TeamOfUsernameResponse200Item']
     """


    return (await asyncio_detailed(
        username=username,
client=client,

    )).parsed
