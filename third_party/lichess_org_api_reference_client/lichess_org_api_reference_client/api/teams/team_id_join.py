from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.team_id_join_body import TeamIdJoinBody
from ...models.team_id_join_response_200 import TeamIdJoinResponse200
from typing import cast



def _get_kwargs(
    team_id: str,
    *,
    body: TeamIdJoinBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/team/{team_id}/join".format(team_id=team_id,),
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[TeamIdJoinResponse200]:
    if response.status_code == 200:
        response_200 = TeamIdJoinResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[TeamIdJoinResponse200]:
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
    body: TeamIdJoinBody,

) -> Response[TeamIdJoinResponse200]:
    """ Join a team

     Join a team.
    If the team requires a password but the `password` field is incorrect,
    then the call fails with `403 Forbidden`.
    Similarly, if the team join policy requires a confirmation but the
    `message` parameter is not given, then the call fails with
    `403 Forbidden`.

    Args:
        team_id (str):  Example: coders.
        body (TeamIdJoinBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamIdJoinResponse200]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    team_id: str,
    *,
    client: AuthenticatedClient,
    body: TeamIdJoinBody,

) -> Optional[TeamIdJoinResponse200]:
    """ Join a team

     Join a team.
    If the team requires a password but the `password` field is incorrect,
    then the call fails with `403 Forbidden`.
    Similarly, if the team join policy requires a confirmation but the
    `message` parameter is not given, then the call fails with
    `403 Forbidden`.

    Args:
        team_id (str):  Example: coders.
        body (TeamIdJoinBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamIdJoinResponse200
     """


    return sync_detailed(
        team_id=team_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient,
    body: TeamIdJoinBody,

) -> Response[TeamIdJoinResponse200]:
    """ Join a team

     Join a team.
    If the team requires a password but the `password` field is incorrect,
    then the call fails with `403 Forbidden`.
    Similarly, if the team join policy requires a confirmation but the
    `message` parameter is not given, then the call fails with
    `403 Forbidden`.

    Args:
        team_id (str):  Example: coders.
        body (TeamIdJoinBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamIdJoinResponse200]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    team_id: str,
    *,
    client: AuthenticatedClient,
    body: TeamIdJoinBody,

) -> Optional[TeamIdJoinResponse200]:
    """ Join a team

     Join a team.
    If the team requires a password but the `password` field is incorrect,
    then the call fails with `403 Forbidden`.
    Similarly, if the team join policy requires a confirmation but the
    `message` parameter is not given, then the call fails with
    `403 Forbidden`.

    Args:
        team_id (str):  Example: coders.
        body (TeamIdJoinBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamIdJoinResponse200
     """


    return (await asyncio_detailed(
        team_id=team_id,
client=client,
body=body,

    )).parsed
