from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.team_requests_response_200_item import TeamRequestsResponse200Item
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    team_id: str,
    *,
    declined: Union[Unset, bool] = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["declined"] = declined


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/team/{team_id}/requests".format(team_id=team_id,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[list['TeamRequestsResponse200Item']]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = TeamRequestsResponse200Item.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[list['TeamRequestsResponse200Item']]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient,
    declined: Union[Unset, bool] = False,

) -> Response[list['TeamRequestsResponse200Item']]:
    """ Get join requests

     Get pending join requests of your team

    Args:
        team_id (str):
        declined (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['TeamRequestsResponse200Item']]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
declined=declined,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    team_id: str,
    *,
    client: AuthenticatedClient,
    declined: Union[Unset, bool] = False,

) -> Optional[list['TeamRequestsResponse200Item']]:
    """ Get join requests

     Get pending join requests of your team

    Args:
        team_id (str):
        declined (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['TeamRequestsResponse200Item']
     """


    return sync_detailed(
        team_id=team_id,
client=client,
declined=declined,

    ).parsed

async def asyncio_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient,
    declined: Union[Unset, bool] = False,

) -> Response[list['TeamRequestsResponse200Item']]:
    """ Get join requests

     Get pending join requests of your team

    Args:
        team_id (str):
        declined (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['TeamRequestsResponse200Item']]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
declined=declined,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    team_id: str,
    *,
    client: AuthenticatedClient,
    declined: Union[Unset, bool] = False,

) -> Optional[list['TeamRequestsResponse200Item']]:
    """ Get join requests

     Get pending join requests of your team

    Args:
        team_id (str):
        declined (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['TeamRequestsResponse200Item']
     """


    return (await asyncio_detailed(
        team_id=team_id,
client=client,
declined=declined,

    )).parsed
