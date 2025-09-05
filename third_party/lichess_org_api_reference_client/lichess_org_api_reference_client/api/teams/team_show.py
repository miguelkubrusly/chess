from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.team_show_response_200 import TeamShowResponse200
from typing import cast



def _get_kwargs(
    team_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/team/{team_id}".format(team_id=team_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[TeamShowResponse200]:
    if response.status_code == 200:
        response_200 = TeamShowResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[TeamShowResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[TeamShowResponse200]:
    """ Get a single team

     Public info about a team. Includes the list of publicly visible leaders.

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamShowResponse200]
     """


    kwargs = _get_kwargs(
        team_id=team_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[TeamShowResponse200]:
    """ Get a single team

     Public info about a team. Includes the list of publicly visible leaders.

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamShowResponse200
     """


    return sync_detailed(
        team_id=team_id,
client=client,

    ).parsed

async def asyncio_detailed(
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[TeamShowResponse200]:
    """ Get a single team

     Public info about a team. Includes the list of publicly visible leaders.

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamShowResponse200]
     """


    kwargs = _get_kwargs(
        team_id=team_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[TeamShowResponse200]:
    """ Get a single team

     Public info about a team. Includes the list of publicly visible leaders.

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamShowResponse200
     """


    return (await asyncio_detailed(
        team_id=team_id,
client=client,

    )).parsed
