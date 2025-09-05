from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.team_request_accept_response_200 import TeamRequestAcceptResponse200
from typing import cast



def _get_kwargs(
    team_id: str,
    user_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/team/{team_id}/request/{user_id}/accept".format(team_id=team_id,user_id=user_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[TeamRequestAcceptResponse200]:
    if response.status_code == 200:
        response_200 = TeamRequestAcceptResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[TeamRequestAcceptResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[TeamRequestAcceptResponse200]:
    """ Accept join request

     Accept someone's request to join your team

    Args:
        team_id (str):  Example: coders.
        user_id (str):  Example: neio.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamRequestAcceptResponse200]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
user_id=user_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    team_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[TeamRequestAcceptResponse200]:
    """ Accept join request

     Accept someone's request to join your team

    Args:
        team_id (str):  Example: coders.
        user_id (str):  Example: neio.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamRequestAcceptResponse200
     """


    return sync_detailed(
        team_id=team_id,
user_id=user_id,
client=client,

    ).parsed

async def asyncio_detailed(
    team_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[TeamRequestAcceptResponse200]:
    """ Accept join request

     Accept someone's request to join your team

    Args:
        team_id (str):  Example: coders.
        user_id (str):  Example: neio.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamRequestAcceptResponse200]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
user_id=user_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    team_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[TeamRequestAcceptResponse200]:
    """ Accept join request

     Accept someone's request to join your team

    Args:
        team_id (str):  Example: coders.
        user_id (str):  Example: neio.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamRequestAcceptResponse200
     """


    return (await asyncio_detailed(
        team_id=team_id,
user_id=user_id,
client=client,

    )).parsed
