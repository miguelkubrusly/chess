from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_team_arena_status import ApiTeamArenaStatus
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    team_id: str,
    *,
    max_: Union[Unset, int] = 100,
    status: Union[Unset, 'ApiTeamArenaStatus'] = UNSET,
    created_by: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["max"] = max_

    json_status: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(status, Unset):
        json_status = status.to_dict()
    if not isinstance(json_status, Unset):
        params.update(json_status)


    params["createdBy"] = created_by

    params["name"] = name


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/team/{team_id}/arena".format(team_id=team_id,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    max_: Union[Unset, int] = 100,
    status: Union[Unset, 'ApiTeamArenaStatus'] = UNSET,
    created_by: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,

) -> Response[Any]:
    """ Get team Arena tournaments

     Get all Arena tournaments relevant to a team.
    Tournaments are sorted by reverse chronological order of start date (last starting first).
    Tournaments are streamed as [ndjson](#section/Introduction/Streaming-with-ND-JSON).

    Args:
        team_id (str):
        max_ (Union[Unset, int]):  Default: 100.
        status (Union[Unset, ApiTeamArenaStatus]):
        created_by (Union[Unset, str]):
        name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
max_=max_,
status=status,
created_by=created_by,
name=name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    team_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    max_: Union[Unset, int] = 100,
    status: Union[Unset, 'ApiTeamArenaStatus'] = UNSET,
    created_by: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,

) -> Response[Any]:
    """ Get team Arena tournaments

     Get all Arena tournaments relevant to a team.
    Tournaments are sorted by reverse chronological order of start date (last starting first).
    Tournaments are streamed as [ndjson](#section/Introduction/Streaming-with-ND-JSON).

    Args:
        team_id (str):
        max_ (Union[Unset, int]):  Default: 100.
        status (Union[Unset, ApiTeamArenaStatus]):
        created_by (Union[Unset, str]):
        name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
max_=max_,
status=status,
created_by=created_by,
name=name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

