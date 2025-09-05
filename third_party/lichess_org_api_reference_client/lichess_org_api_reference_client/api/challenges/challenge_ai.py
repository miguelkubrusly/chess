from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.challenge_ai_body import ChallengeAiBody
from ...models.challenge_ai_response_201 import ChallengeAiResponse201
from ...models.challenge_ai_response_400 import ChallengeAiResponse400
from typing import cast



def _get_kwargs(
    *,
    body: ChallengeAiBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/challenge/ai",
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ChallengeAiResponse201, ChallengeAiResponse400]]:
    if response.status_code == 201:
        response_201 = ChallengeAiResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = ChallengeAiResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ChallengeAiResponse201, ChallengeAiResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ChallengeAiBody,

) -> Response[Union[ChallengeAiResponse201, ChallengeAiResponse400]]:
    """ Challenge the AI

     Start a game with Lichess AI.
    You will be notified on the [event stream](#operation/apiStreamEvent) that a new game has started.

    Args:
        body (ChallengeAiBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChallengeAiResponse201, ChallengeAiResponse400]]
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
    client: AuthenticatedClient,
    body: ChallengeAiBody,

) -> Optional[Union[ChallengeAiResponse201, ChallengeAiResponse400]]:
    """ Challenge the AI

     Start a game with Lichess AI.
    You will be notified on the [event stream](#operation/apiStreamEvent) that a new game has started.

    Args:
        body (ChallengeAiBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChallengeAiResponse201, ChallengeAiResponse400]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ChallengeAiBody,

) -> Response[Union[ChallengeAiResponse201, ChallengeAiResponse400]]:
    """ Challenge the AI

     Start a game with Lichess AI.
    You will be notified on the [event stream](#operation/apiStreamEvent) that a new game has started.

    Args:
        body (ChallengeAiBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChallengeAiResponse201, ChallengeAiResponse400]]
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
    client: AuthenticatedClient,
    body: ChallengeAiBody,

) -> Optional[Union[ChallengeAiResponse201, ChallengeAiResponse400]]:
    """ Challenge the AI

     Start a game with Lichess AI.
    You will be notified on the [event stream](#operation/apiStreamEvent) that a new game has started.

    Args:
        body (ChallengeAiBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChallengeAiResponse201, ChallengeAiResponse400]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
