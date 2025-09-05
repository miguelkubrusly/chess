from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.team_id_pm_all_body import TeamIdPmAllBody
from ...models.team_id_pm_all_response_200 import TeamIdPmAllResponse200
from ...models.team_id_pm_all_response_400 import TeamIdPmAllResponse400
from typing import cast



def _get_kwargs(
    team_id: str,
    *,
    body: TeamIdPmAllBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/team/{team_id}/pm-all".format(team_id=team_id,),
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[TeamIdPmAllResponse200, TeamIdPmAllResponse400]]:
    if response.status_code == 200:
        response_200 = TeamIdPmAllResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = TeamIdPmAllResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[TeamIdPmAllResponse200, TeamIdPmAllResponse400]]:
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
    body: TeamIdPmAllBody,

) -> Response[Union[TeamIdPmAllResponse200, TeamIdPmAllResponse400]]:
    r""" Message all members

     Send a private message to all members of a team.
    You must be a team leader with the \"Messages\" permission.

    Args:
        team_id (str):  Example: coders.
        body (TeamIdPmAllBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TeamIdPmAllResponse200, TeamIdPmAllResponse400]]
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
    body: TeamIdPmAllBody,

) -> Optional[Union[TeamIdPmAllResponse200, TeamIdPmAllResponse400]]:
    r""" Message all members

     Send a private message to all members of a team.
    You must be a team leader with the \"Messages\" permission.

    Args:
        team_id (str):  Example: coders.
        body (TeamIdPmAllBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TeamIdPmAllResponse200, TeamIdPmAllResponse400]
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
    body: TeamIdPmAllBody,

) -> Response[Union[TeamIdPmAllResponse200, TeamIdPmAllResponse400]]:
    r""" Message all members

     Send a private message to all members of a team.
    You must be a team leader with the \"Messages\" permission.

    Args:
        team_id (str):  Example: coders.
        body (TeamIdPmAllBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TeamIdPmAllResponse200, TeamIdPmAllResponse400]]
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
    body: TeamIdPmAllBody,

) -> Optional[Union[TeamIdPmAllResponse200, TeamIdPmAllResponse400]]:
    r""" Message all members

     Send a private message to all members of a team.
    You must be a team leader with the \"Messages\" permission.

    Args:
        team_id (str):  Example: coders.
        body (TeamIdPmAllBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TeamIdPmAllResponse200, TeamIdPmAllResponse400]
     """


    return (await asyncio_detailed(
        team_id=team_id,
client=client,
body=body,

    )).parsed
