from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_tournament_team_battle_post_body import ApiTournamentTeamBattlePostBody
from ...models.api_tournament_team_battle_post_response_200 import ApiTournamentTeamBattlePostResponse200
from ...models.api_tournament_team_battle_post_response_400 import ApiTournamentTeamBattlePostResponse400
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: ApiTournamentTeamBattlePostBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/tournament/team-battle/{id}".format(id=id,),
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ApiTournamentTeamBattlePostResponse200, ApiTournamentTeamBattlePostResponse400]]:
    if response.status_code == 200:
        response_200 = ApiTournamentTeamBattlePostResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ApiTournamentTeamBattlePostResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ApiTournamentTeamBattlePostResponse200, ApiTournamentTeamBattlePostResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiTournamentTeamBattlePostBody,

) -> Response[Union[ApiTournamentTeamBattlePostResponse200, ApiTournamentTeamBattlePostResponse400]]:
    """ Update a team battle

     Set the teams and number of leaders of a team battle.
    To update the other attributes of a team battle, use the [tournament update
    endpoint](#operation/apiTournamentUpdate).

    Args:
        id (str):
        body (ApiTournamentTeamBattlePostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiTournamentTeamBattlePostResponse200, ApiTournamentTeamBattlePostResponse400]]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiTournamentTeamBattlePostBody,

) -> Optional[Union[ApiTournamentTeamBattlePostResponse200, ApiTournamentTeamBattlePostResponse400]]:
    """ Update a team battle

     Set the teams and number of leaders of a team battle.
    To update the other attributes of a team battle, use the [tournament update
    endpoint](#operation/apiTournamentUpdate).

    Args:
        id (str):
        body (ApiTournamentTeamBattlePostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiTournamentTeamBattlePostResponse200, ApiTournamentTeamBattlePostResponse400]
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiTournamentTeamBattlePostBody,

) -> Response[Union[ApiTournamentTeamBattlePostResponse200, ApiTournamentTeamBattlePostResponse400]]:
    """ Update a team battle

     Set the teams and number of leaders of a team battle.
    To update the other attributes of a team battle, use the [tournament update
    endpoint](#operation/apiTournamentUpdate).

    Args:
        id (str):
        body (ApiTournamentTeamBattlePostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiTournamentTeamBattlePostResponse200, ApiTournamentTeamBattlePostResponse400]]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ApiTournamentTeamBattlePostBody,

) -> Optional[Union[ApiTournamentTeamBattlePostResponse200, ApiTournamentTeamBattlePostResponse400]]:
    """ Update a team battle

     Set the teams and number of leaders of a team battle.
    To update the other attributes of a team battle, use the [tournament update
    endpoint](#operation/apiTournamentUpdate).

    Args:
        id (str):
        body (ApiTournamentTeamBattlePostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiTournamentTeamBattlePostResponse200, ApiTournamentTeamBattlePostResponse400]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
