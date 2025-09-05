from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.team_id_quit_response_200 import TeamIdQuitResponse200
from typing import cast



def _get_kwargs(
    team_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/team/{team_id}/quit".format(team_id=team_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[TeamIdQuitResponse200]:
    if response.status_code == 200:
        response_200 = TeamIdQuitResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[TeamIdQuitResponse200]:
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

) -> Response[TeamIdQuitResponse200]:
    """ Leave a team

     Leave a team.
    - <https://lichess.org/team>

    Args:
        team_id (str):  Example: coders.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamIdQuitResponse200]
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
    client: AuthenticatedClient,

) -> Optional[TeamIdQuitResponse200]:
    """ Leave a team

     Leave a team.
    - <https://lichess.org/team>

    Args:
        team_id (str):  Example: coders.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamIdQuitResponse200
     """


    return sync_detailed(
        team_id=team_id,
client=client,

    ).parsed

async def asyncio_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[TeamIdQuitResponse200]:
    """ Leave a team

     Leave a team.
    - <https://lichess.org/team>

    Args:
        team_id (str):  Example: coders.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamIdQuitResponse200]
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
    client: AuthenticatedClient,

) -> Optional[TeamIdQuitResponse200]:
    """ Leave a team

     Leave a team.
    - <https://lichess.org/team>

    Args:
        team_id (str):  Example: coders.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamIdQuitResponse200
     """


    return (await asyncio_detailed(
        team_id=team_id,
client=client,

    )).parsed
