from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.challenge_open_body import ChallengeOpenBody
from ...models.challenge_open_response_200 import ChallengeOpenResponse200
from ...models.challenge_open_response_400 import ChallengeOpenResponse400
from typing import cast



def _get_kwargs(
    *,
    body: ChallengeOpenBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/challenge/open",
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ChallengeOpenResponse200, ChallengeOpenResponse400]]:
    if response.status_code == 200:
        response_200 = ChallengeOpenResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ChallengeOpenResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ChallengeOpenResponse200, ChallengeOpenResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChallengeOpenBody,

) -> Response[Union[ChallengeOpenResponse200, ChallengeOpenResponse400]]:
    """ Open-ended challenge

     Create a challenge that any 2 players can join.
    Share the URL of the challenge. the first 2 players to click it will be paired for a game.
    The response body also contains `whiteUrl` and `blackUrl`.
    You can control which color each player gets by giving them these URLs,
    instead of the main challenge URL.
    Open challenges expire after 24h.
    If the challenge creation is [authenticated with OAuth2](#section/Introduction/Authentication),
    then you can use the [challenge cancel endpoint](#operation/challengeCancel) to cancel it.
    To directly pair 2 known players, use [this endpoint](#operation/bulkPairingList) instead.

    Args:
        body (ChallengeOpenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChallengeOpenResponse200, ChallengeOpenResponse400]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChallengeOpenBody,

) -> Optional[Union[ChallengeOpenResponse200, ChallengeOpenResponse400]]:
    """ Open-ended challenge

     Create a challenge that any 2 players can join.
    Share the URL of the challenge. the first 2 players to click it will be paired for a game.
    The response body also contains `whiteUrl` and `blackUrl`.
    You can control which color each player gets by giving them these URLs,
    instead of the main challenge URL.
    Open challenges expire after 24h.
    If the challenge creation is [authenticated with OAuth2](#section/Introduction/Authentication),
    then you can use the [challenge cancel endpoint](#operation/challengeCancel) to cancel it.
    To directly pair 2 known players, use [this endpoint](#operation/bulkPairingList) instead.

    Args:
        body (ChallengeOpenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChallengeOpenResponse200, ChallengeOpenResponse400]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChallengeOpenBody,

) -> Response[Union[ChallengeOpenResponse200, ChallengeOpenResponse400]]:
    """ Open-ended challenge

     Create a challenge that any 2 players can join.
    Share the URL of the challenge. the first 2 players to click it will be paired for a game.
    The response body also contains `whiteUrl` and `blackUrl`.
    You can control which color each player gets by giving them these URLs,
    instead of the main challenge URL.
    Open challenges expire after 24h.
    If the challenge creation is [authenticated with OAuth2](#section/Introduction/Authentication),
    then you can use the [challenge cancel endpoint](#operation/challengeCancel) to cancel it.
    To directly pair 2 known players, use [this endpoint](#operation/bulkPairingList) instead.

    Args:
        body (ChallengeOpenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChallengeOpenResponse200, ChallengeOpenResponse400]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChallengeOpenBody,

) -> Optional[Union[ChallengeOpenResponse200, ChallengeOpenResponse400]]:
    """ Open-ended challenge

     Create a challenge that any 2 players can join.
    Share the URL of the challenge. the first 2 players to click it will be paired for a game.
    The response body also contains `whiteUrl` and `blackUrl`.
    You can control which color each player gets by giving them these URLs,
    instead of the main challenge URL.
    Open challenges expire after 24h.
    If the challenge creation is [authenticated with OAuth2](#section/Introduction/Authentication),
    then you can use the [challenge cancel endpoint](#operation/challengeCancel) to cancel it.
    To directly pair 2 known players, use [this endpoint](#operation/bulkPairingList) instead.

    Args:
        body (ChallengeOpenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChallengeOpenResponse200, ChallengeOpenResponse400]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
