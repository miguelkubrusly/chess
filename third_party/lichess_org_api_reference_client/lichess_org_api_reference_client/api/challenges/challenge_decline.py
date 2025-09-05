from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.challenge_decline_body import ChallengeDeclineBody
from ...models.challenge_decline_response_200 import ChallengeDeclineResponse200
from ...models.challenge_decline_response_404 import ChallengeDeclineResponse404
from typing import cast



def _get_kwargs(
    challenge_id: str,
    *,
    body: ChallengeDeclineBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/challenge/{challenge_id}/decline".format(challenge_id=challenge_id,),
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ChallengeDeclineResponse200, ChallengeDeclineResponse404]]:
    if response.status_code == 200:
        response_200 = ChallengeDeclineResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = ChallengeDeclineResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ChallengeDeclineResponse200, ChallengeDeclineResponse404]]:
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
    body: ChallengeDeclineBody,

) -> Response[Union[ChallengeDeclineResponse200, ChallengeDeclineResponse404]]:
    """ Decline a challenge

     Decline an incoming challenge.

    Args:
        challenge_id (str):  Example: 5IrD6Gzz.
        body (ChallengeDeclineBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChallengeDeclineResponse200, ChallengeDeclineResponse404]]
     """


    kwargs = _get_kwargs(
        challenge_id=challenge_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    challenge_id: str,
    *,
    client: AuthenticatedClient,
    body: ChallengeDeclineBody,

) -> Optional[Union[ChallengeDeclineResponse200, ChallengeDeclineResponse404]]:
    """ Decline a challenge

     Decline an incoming challenge.

    Args:
        challenge_id (str):  Example: 5IrD6Gzz.
        body (ChallengeDeclineBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChallengeDeclineResponse200, ChallengeDeclineResponse404]
     """


    return sync_detailed(
        challenge_id=challenge_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    challenge_id: str,
    *,
    client: AuthenticatedClient,
    body: ChallengeDeclineBody,

) -> Response[Union[ChallengeDeclineResponse200, ChallengeDeclineResponse404]]:
    """ Decline a challenge

     Decline an incoming challenge.

    Args:
        challenge_id (str):  Example: 5IrD6Gzz.
        body (ChallengeDeclineBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChallengeDeclineResponse200, ChallengeDeclineResponse404]]
     """


    kwargs = _get_kwargs(
        challenge_id=challenge_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    challenge_id: str,
    *,
    client: AuthenticatedClient,
    body: ChallengeDeclineBody,

) -> Optional[Union[ChallengeDeclineResponse200, ChallengeDeclineResponse404]]:
    """ Decline a challenge

     Decline an incoming challenge.

    Args:
        challenge_id (str):  Example: 5IrD6Gzz.
        body (ChallengeDeclineBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChallengeDeclineResponse200, ChallengeDeclineResponse404]
     """


    return (await asyncio_detailed(
        challenge_id=challenge_id,
client=client,
body=body,

    )).parsed
