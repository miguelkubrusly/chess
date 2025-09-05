from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_user_activity_response_200_item import ApiUserActivityResponse200Item
from typing import cast



def _get_kwargs(
    username: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/user/{username}/activity".format(username=username,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[list['ApiUserActivityResponse200Item']]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ApiUserActivityResponse200Item.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[list['ApiUserActivityResponse200Item']]:
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

) -> Response[list['ApiUserActivityResponse200Item']]:
    """ Get user activity

     Read data to generate the activity feed of a user.

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ApiUserActivityResponse200Item']]
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

) -> Optional[list['ApiUserActivityResponse200Item']]:
    """ Get user activity

     Read data to generate the activity feed of a user.

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ApiUserActivityResponse200Item']
     """


    return sync_detailed(
        username=username,
client=client,

    ).parsed

async def asyncio_detailed(
    username: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[list['ApiUserActivityResponse200Item']]:
    """ Get user activity

     Read data to generate the activity feed of a user.

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ApiUserActivityResponse200Item']]
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

) -> Optional[list['ApiUserActivityResponse200Item']]:
    """ Get user activity

     Read data to generate the activity feed of a user.

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ApiUserActivityResponse200Item']
     """


    return (await asyncio_detailed(
        username=username,
client=client,

    )).parsed
