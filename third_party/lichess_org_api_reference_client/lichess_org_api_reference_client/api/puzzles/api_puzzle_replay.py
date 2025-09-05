from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_puzzle_replay_response_200 import ApiPuzzleReplayResponse200
from ...models.api_puzzle_replay_response_404 import ApiPuzzleReplayResponse404
from typing import cast



def _get_kwargs(
    days: float,
    theme: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/puzzle/replay/{days}/{theme}".format(days=days,theme=theme,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ApiPuzzleReplayResponse200, ApiPuzzleReplayResponse404]]:
    if response.status_code == 200:
        response_200 = ApiPuzzleReplayResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = ApiPuzzleReplayResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ApiPuzzleReplayResponse200, ApiPuzzleReplayResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    days: float,
    theme: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[ApiPuzzleReplayResponse200, ApiPuzzleReplayResponse404]]:
    """ Get puzzles to replay

     Gets the puzzle IDs of remaining puzzles to re-attempt in JSON format.

    Args:
        days (float):
        theme (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiPuzzleReplayResponse200, ApiPuzzleReplayResponse404]]
     """


    kwargs = _get_kwargs(
        days=days,
theme=theme,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    days: float,
    theme: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[ApiPuzzleReplayResponse200, ApiPuzzleReplayResponse404]]:
    """ Get puzzles to replay

     Gets the puzzle IDs of remaining puzzles to re-attempt in JSON format.

    Args:
        days (float):
        theme (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiPuzzleReplayResponse200, ApiPuzzleReplayResponse404]
     """


    return sync_detailed(
        days=days,
theme=theme,
client=client,

    ).parsed

async def asyncio_detailed(
    days: float,
    theme: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[ApiPuzzleReplayResponse200, ApiPuzzleReplayResponse404]]:
    """ Get puzzles to replay

     Gets the puzzle IDs of remaining puzzles to re-attempt in JSON format.

    Args:
        days (float):
        theme (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiPuzzleReplayResponse200, ApiPuzzleReplayResponse404]]
     """


    kwargs = _get_kwargs(
        days=days,
theme=theme,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    days: float,
    theme: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[ApiPuzzleReplayResponse200, ApiPuzzleReplayResponse404]]:
    """ Get puzzles to replay

     Gets the puzzle IDs of remaining puzzles to re-attempt in JSON format.

    Args:
        days (float):
        theme (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiPuzzleReplayResponse200, ApiPuzzleReplayResponse404]
     """


    return (await asyncio_detailed(
        days=days,
theme=theme,
client=client,

    )).parsed
