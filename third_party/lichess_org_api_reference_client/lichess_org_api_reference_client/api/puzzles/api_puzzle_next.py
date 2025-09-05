from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_puzzle_next_difficulty import ApiPuzzleNextDifficulty
from ...models.api_puzzle_next_response_200 import ApiPuzzleNextResponse200
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    angle: Union[Unset, str] = UNSET,
    difficulty: Union[Unset, ApiPuzzleNextDifficulty] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["angle"] = angle

    json_difficulty: Union[Unset, str] = UNSET
    if not isinstance(difficulty, Unset):
        json_difficulty = difficulty.value

    params["difficulty"] = json_difficulty


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/puzzle/next",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ApiPuzzleNextResponse200]:
    if response.status_code == 200:
        response_200 = ApiPuzzleNextResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ApiPuzzleNextResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    angle: Union[Unset, str] = UNSET,
    difficulty: Union[Unset, ApiPuzzleNextDifficulty] = UNSET,

) -> Response[ApiPuzzleNextResponse200]:
    """ Get a new puzzle

     Get a random Lichess puzzle in JSON format.

    If authenticated, only returns puzzles that the user has never seen before.

    **DO NOT** use this endpoint to enumerate puzzles for mass download. Instead, download the [full
    public puzzle database](https://database.lichess.org/#puzzles).

    Args:
        angle (Union[Unset, str]):
        difficulty (Union[Unset, ApiPuzzleNextDifficulty]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiPuzzleNextResponse200]
     """


    kwargs = _get_kwargs(
        angle=angle,
difficulty=difficulty,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    angle: Union[Unset, str] = UNSET,
    difficulty: Union[Unset, ApiPuzzleNextDifficulty] = UNSET,

) -> Optional[ApiPuzzleNextResponse200]:
    """ Get a new puzzle

     Get a random Lichess puzzle in JSON format.

    If authenticated, only returns puzzles that the user has never seen before.

    **DO NOT** use this endpoint to enumerate puzzles for mass download. Instead, download the [full
    public puzzle database](https://database.lichess.org/#puzzles).

    Args:
        angle (Union[Unset, str]):
        difficulty (Union[Unset, ApiPuzzleNextDifficulty]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiPuzzleNextResponse200
     """


    return sync_detailed(
        client=client,
angle=angle,
difficulty=difficulty,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    angle: Union[Unset, str] = UNSET,
    difficulty: Union[Unset, ApiPuzzleNextDifficulty] = UNSET,

) -> Response[ApiPuzzleNextResponse200]:
    """ Get a new puzzle

     Get a random Lichess puzzle in JSON format.

    If authenticated, only returns puzzles that the user has never seen before.

    **DO NOT** use this endpoint to enumerate puzzles for mass download. Instead, download the [full
    public puzzle database](https://database.lichess.org/#puzzles).

    Args:
        angle (Union[Unset, str]):
        difficulty (Union[Unset, ApiPuzzleNextDifficulty]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiPuzzleNextResponse200]
     """


    kwargs = _get_kwargs(
        angle=angle,
difficulty=difficulty,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    angle: Union[Unset, str] = UNSET,
    difficulty: Union[Unset, ApiPuzzleNextDifficulty] = UNSET,

) -> Optional[ApiPuzzleNextResponse200]:
    """ Get a new puzzle

     Get a random Lichess puzzle in JSON format.

    If authenticated, only returns puzzles that the user has never seen before.

    **DO NOT** use this endpoint to enumerate puzzles for mass download. Instead, download the [full
    public puzzle database](https://database.lichess.org/#puzzles).

    Args:
        angle (Union[Unset, str]):
        difficulty (Union[Unset, ApiPuzzleNextDifficulty]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiPuzzleNextResponse200
     """


    return (await asyncio_detailed(
        client=client,
angle=angle,
difficulty=difficulty,

    )).parsed
