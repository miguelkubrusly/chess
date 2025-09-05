from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.challenge_accept_color import ChallengeAcceptColor
from ...models.challenge_accept_response_200 import ChallengeAcceptResponse200
from ...models.challenge_accept_response_404 import ChallengeAcceptResponse404
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    challenge_id: str,
    *,
    color: Union[Unset, ChallengeAcceptColor] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_color: Union[Unset, str] = UNSET
    if not isinstance(color, Unset):
        json_color = color.value

    params["color"] = json_color


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/challenge/{challenge_id}/accept".format(challenge_id=challenge_id,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ChallengeAcceptResponse200, ChallengeAcceptResponse404]]:
    if response.status_code == 200:
        response_200 = ChallengeAcceptResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = ChallengeAcceptResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ChallengeAcceptResponse200, ChallengeAcceptResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    challenge_id: str,
    *,
    client: AuthenticatedClient,
    color: Union[Unset, ChallengeAcceptColor] = UNSET,

) -> Response[Union[ChallengeAcceptResponse200, ChallengeAcceptResponse404]]:
    """ Accept a challenge

     Accept an incoming challenge.
    You should receive a `gameStart` event on the [incoming events stream](#operation/apiStreamEvent).

    Args:
        challenge_id (str):  Example: 5IrD6Gzz.
        color (Union[Unset, ChallengeAcceptColor]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChallengeAcceptResponse200, ChallengeAcceptResponse404]]
     """


    kwargs = _get_kwargs(
        challenge_id=challenge_id,
color=color,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    challenge_id: str,
    *,
    client: AuthenticatedClient,
    color: Union[Unset, ChallengeAcceptColor] = UNSET,

) -> Optional[Union[ChallengeAcceptResponse200, ChallengeAcceptResponse404]]:
    """ Accept a challenge

     Accept an incoming challenge.
    You should receive a `gameStart` event on the [incoming events stream](#operation/apiStreamEvent).

    Args:
        challenge_id (str):  Example: 5IrD6Gzz.
        color (Union[Unset, ChallengeAcceptColor]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChallengeAcceptResponse200, ChallengeAcceptResponse404]
     """


    return sync_detailed(
        challenge_id=challenge_id,
client=client,
color=color,

    ).parsed

async def asyncio_detailed(
    challenge_id: str,
    *,
    client: AuthenticatedClient,
    color: Union[Unset, ChallengeAcceptColor] = UNSET,

) -> Response[Union[ChallengeAcceptResponse200, ChallengeAcceptResponse404]]:
    """ Accept a challenge

     Accept an incoming challenge.
    You should receive a `gameStart` event on the [incoming events stream](#operation/apiStreamEvent).

    Args:
        challenge_id (str):  Example: 5IrD6Gzz.
        color (Union[Unset, ChallengeAcceptColor]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChallengeAcceptResponse200, ChallengeAcceptResponse404]]
     """


    kwargs = _get_kwargs(
        challenge_id=challenge_id,
color=color,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    challenge_id: str,
    *,
    client: AuthenticatedClient,
    color: Union[Unset, ChallengeAcceptColor] = UNSET,

) -> Optional[Union[ChallengeAcceptResponse200, ChallengeAcceptResponse404]]:
    """ Accept a challenge

     Accept an incoming challenge.
    You should receive a `gameStart` event on the [incoming events stream](#operation/apiStreamEvent).

    Args:
        challenge_id (str):  Example: 5IrD6Gzz.
        color (Union[Unset, ChallengeAcceptColor]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChallengeAcceptResponse200, ChallengeAcceptResponse404]
     """


    return (await asyncio_detailed(
        challenge_id=challenge_id,
client=client,
color=color,

    )).parsed
