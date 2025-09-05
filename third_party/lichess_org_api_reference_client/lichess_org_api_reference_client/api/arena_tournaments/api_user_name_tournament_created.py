from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_user_name_tournament_created_status import ApiUserNameTournamentCreatedStatus
from ...types import UNSET, Unset
from typing import Union



def _get_kwargs(
    username: str,
    *,
    nb: Union[Unset, int] = UNSET,
    status: Union[Unset, ApiUserNameTournamentCreatedStatus] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["nb"] = nb

    json_status: Union[Unset, int] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/user/{username}/tournament/created".format(username=username,),
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
    username: str,
    *,
    client: AuthenticatedClient,
    nb: Union[Unset, int] = UNSET,
    status: Union[Unset, ApiUserNameTournamentCreatedStatus] = UNSET,

) -> Response[Any]:
    """ Get tournaments created by a user

     Get all tournaments created by a given user.
    Tournaments are sorted by reverse chronological order of start date (last starting first).
    Tournaments are streamed as [ndjson](#section/Introduction/Streaming-with-ND-JSON).
    The stream is throttled, depending on who is making the request:
      - Anonymous request: 20 tournaments per second
      - [OAuth2 authenticated](#section/Introduction/Authentication) request: 30 tournaments per second
      - Authenticated, downloading your own tournaments: 50 tournaments per second

    Args:
        username (str):
        nb (Union[Unset, int]):
        status (Union[Unset, ApiUserNameTournamentCreatedStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        username=username,
nb=nb,
status=status,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    nb: Union[Unset, int] = UNSET,
    status: Union[Unset, ApiUserNameTournamentCreatedStatus] = UNSET,

) -> Response[Any]:
    """ Get tournaments created by a user

     Get all tournaments created by a given user.
    Tournaments are sorted by reverse chronological order of start date (last starting first).
    Tournaments are streamed as [ndjson](#section/Introduction/Streaming-with-ND-JSON).
    The stream is throttled, depending on who is making the request:
      - Anonymous request: 20 tournaments per second
      - [OAuth2 authenticated](#section/Introduction/Authentication) request: 30 tournaments per second
      - Authenticated, downloading your own tournaments: 50 tournaments per second

    Args:
        username (str):
        nb (Union[Unset, int]):
        status (Union[Unset, ApiUserNameTournamentCreatedStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        username=username,
nb=nb,
status=status,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

