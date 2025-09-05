from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_tournament_join_body import ApiTournamentJoinBody
from ...models.api_tournament_join_response_200 import ApiTournamentJoinResponse200
from ...models.api_tournament_join_response_400 import ApiTournamentJoinResponse400
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: ApiTournamentJoinBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/tournament/{id}/join".format(id=id,),
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ApiTournamentJoinResponse200, ApiTournamentJoinResponse400]]:
    if response.status_code == 200:
        response_200 = ApiTournamentJoinResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ApiTournamentJoinResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ApiTournamentJoinResponse200, ApiTournamentJoinResponse400]]:
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
    body: ApiTournamentJoinBody,

) -> Response[Union[ApiTournamentJoinResponse200, ApiTournamentJoinResponse400]]:
    """ Join an Arena tournament

     Join an Arena tournament, possibly with a password and/or a team.
    Also unpauses if you had previously [paused](#operation/apiTournamentWithdraw) the tournament.

    Args:
        id (str):  Example: hL7vMrFQ.
        body (ApiTournamentJoinBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiTournamentJoinResponse200, ApiTournamentJoinResponse400]]
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
    body: ApiTournamentJoinBody,

) -> Optional[Union[ApiTournamentJoinResponse200, ApiTournamentJoinResponse400]]:
    """ Join an Arena tournament

     Join an Arena tournament, possibly with a password and/or a team.
    Also unpauses if you had previously [paused](#operation/apiTournamentWithdraw) the tournament.

    Args:
        id (str):  Example: hL7vMrFQ.
        body (ApiTournamentJoinBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiTournamentJoinResponse200, ApiTournamentJoinResponse400]
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
    body: ApiTournamentJoinBody,

) -> Response[Union[ApiTournamentJoinResponse200, ApiTournamentJoinResponse400]]:
    """ Join an Arena tournament

     Join an Arena tournament, possibly with a password and/or a team.
    Also unpauses if you had previously [paused](#operation/apiTournamentWithdraw) the tournament.

    Args:
        id (str):  Example: hL7vMrFQ.
        body (ApiTournamentJoinBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiTournamentJoinResponse200, ApiTournamentJoinResponse400]]
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
    body: ApiTournamentJoinBody,

) -> Optional[Union[ApiTournamentJoinResponse200, ApiTournamentJoinResponse400]]:
    """ Join an Arena tournament

     Join an Arena tournament, possibly with a password and/or a team.
    Also unpauses if you had previously [paused](#operation/apiTournamentWithdraw) the tournament.

    Args:
        id (str):  Example: hL7vMrFQ.
        body (ApiTournamentJoinBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiTournamentJoinResponse200, ApiTournamentJoinResponse400]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
