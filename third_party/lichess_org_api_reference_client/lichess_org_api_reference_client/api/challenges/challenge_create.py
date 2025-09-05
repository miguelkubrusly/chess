from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.challenge_create_body import ChallengeCreateBody
from ...models.challenge_create_response_200 import ChallengeCreateResponse200
from ...models.challenge_create_response_400 import ChallengeCreateResponse400
from typing import cast



def _get_kwargs(
    username: str,
    *,
    body: ChallengeCreateBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/challenge/{username}".format(username=username,),
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ChallengeCreateResponse200, ChallengeCreateResponse400]]:
    if response.status_code == 200:
        response_200 = ChallengeCreateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ChallengeCreateResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ChallengeCreateResponse200, ChallengeCreateResponse400]]:
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
    body: ChallengeCreateBody,

) -> Response[Union[ChallengeCreateResponse200, ChallengeCreateResponse400]]:
    """ Create a challenge

     Challenge someone to play. The targeted player can choose to accept or decline.
    If the challenge is accepted, you will be notified on the [event stream](#operation/apiStreamEvent)
    that a new game has started. The game ID will be the same as the challenge ID.
    Challenges for realtime games (not correspondence) expire after 20s if not accepted.
    To prevent that, use the `keepAliveStream` flag described below.

    Args:
        username (str):  Example: LeelaChess.
        body (ChallengeCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChallengeCreateResponse200, ChallengeCreateResponse400]]
     """


    kwargs = _get_kwargs(
        username=username,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    username: str,
    *,
    client: AuthenticatedClient,
    body: ChallengeCreateBody,

) -> Optional[Union[ChallengeCreateResponse200, ChallengeCreateResponse400]]:
    """ Create a challenge

     Challenge someone to play. The targeted player can choose to accept or decline.
    If the challenge is accepted, you will be notified on the [event stream](#operation/apiStreamEvent)
    that a new game has started. The game ID will be the same as the challenge ID.
    Challenges for realtime games (not correspondence) expire after 20s if not accepted.
    To prevent that, use the `keepAliveStream` flag described below.

    Args:
        username (str):  Example: LeelaChess.
        body (ChallengeCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChallengeCreateResponse200, ChallengeCreateResponse400]
     """


    return sync_detailed(
        username=username,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    body: ChallengeCreateBody,

) -> Response[Union[ChallengeCreateResponse200, ChallengeCreateResponse400]]:
    """ Create a challenge

     Challenge someone to play. The targeted player can choose to accept or decline.
    If the challenge is accepted, you will be notified on the [event stream](#operation/apiStreamEvent)
    that a new game has started. The game ID will be the same as the challenge ID.
    Challenges for realtime games (not correspondence) expire after 20s if not accepted.
    To prevent that, use the `keepAliveStream` flag described below.

    Args:
        username (str):  Example: LeelaChess.
        body (ChallengeCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChallengeCreateResponse200, ChallengeCreateResponse400]]
     """


    kwargs = _get_kwargs(
        username=username,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
    body: ChallengeCreateBody,

) -> Optional[Union[ChallengeCreateResponse200, ChallengeCreateResponse400]]:
    """ Create a challenge

     Challenge someone to play. The targeted player can choose to accept or decline.
    If the challenge is accepted, you will be notified on the [event stream](#operation/apiStreamEvent)
    that a new game has started. The game ID will be the same as the challenge ID.
    Challenges for realtime games (not correspondence) expire after 20s if not accepted.
    To prevent that, use the `keepAliveStream` flag described below.

    Args:
        username (str):  Example: LeelaChess.
        body (ChallengeCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChallengeCreateResponse200, ChallengeCreateResponse400]
     """


    return (await asyncio_detailed(
        username=username,
client=client,
body=body,

    )).parsed
