from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.challenge_show_response_200 import ChallengeShowResponse200
from typing import cast



def _get_kwargs(
    challenge_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/challenge/{challenge_id}/show".format(challenge_id=challenge_id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ChallengeShowResponse200]:
    if response.status_code == 200:
        response_200 = ChallengeShowResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ChallengeShowResponse200]:
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

) -> Response[ChallengeShowResponse200]:
    """ Show one challenge

     Get details about a challenge, even if it has been recently accepted, canceled or declined.

    Args:
        challenge_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChallengeShowResponse200]
     """


    kwargs = _get_kwargs(
        challenge_id=challenge_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    challenge_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[ChallengeShowResponse200]:
    """ Show one challenge

     Get details about a challenge, even if it has been recently accepted, canceled or declined.

    Args:
        challenge_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChallengeShowResponse200
     """


    return sync_detailed(
        challenge_id=challenge_id,
client=client,

    ).parsed

async def asyncio_detailed(
    challenge_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[ChallengeShowResponse200]:
    """ Show one challenge

     Get details about a challenge, even if it has been recently accepted, canceled or declined.

    Args:
        challenge_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChallengeShowResponse200]
     """


    kwargs = _get_kwargs(
        challenge_id=challenge_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    challenge_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[ChallengeShowResponse200]:
    """ Show one challenge

     Get details about a challenge, even if it has been recently accepted, canceled or declined.

    Args:
        challenge_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChallengeShowResponse200
     """


    return (await asyncio_detailed(
        challenge_id=challenge_id,
client=client,

    )).parsed
