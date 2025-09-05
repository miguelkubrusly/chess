from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from typing import Union



def _get_kwargs(
    team_id: str,
    *,
    full: Union[Unset, bool] = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["full"] = full


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/team/{team_id}/users".format(team_id=team_id,),
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
    client: AuthenticatedClient,
    full: Union[Unset, bool] = False,

) -> Response[Any]:
    """ Get members of a team

     Members are sorted by reverse chronological order of joining the team (most recent first).
    OAuth is only required if the list of members is private.
    Up to 5,000 users are streamed as [ndjson](#section/Introduction/Streaming-with-ND-JSON).

    Args:
        team_id (str):  Example: coders.
        full (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
full=full,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient,
    full: Union[Unset, bool] = False,

) -> Response[Any]:
    """ Get members of a team

     Members are sorted by reverse chronological order of joining the team (most recent first).
    OAuth is only required if the list of members is private.
    Up to 5,000 users are streamed as [ndjson](#section/Introduction/Streaming-with-ND-JSON).

    Args:
        team_id (str):  Example: coders.
        full (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        team_id=team_id,
full=full,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

