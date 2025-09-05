from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.game_import_body import GameImportBody
from ...models.game_import_response_200 import GameImportResponse200
from typing import cast



def _get_kwargs(
    *,
    body: GameImportBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/import",
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[GameImportResponse200]:
    if response.status_code == 200:
        response_200 = GameImportResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[GameImportResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GameImportBody,

) -> Response[GameImportResponse200]:
    """ Import one game

     Import a game from PGN. See <https://lichess.org/paste>.
    Rate limiting: 200 games per hour for OAuth requests, 100 games per hour for anonymous requests.
    To broadcast ongoing games, consider [pushing to a broadcast instead](#operation/broadcastPush).
    To analyse a position or a line, just construct an analysis board URL (most standard tags supported
    if URL-encoded):
    [https://lichess.org/analysis/pgn/e4_e5_Nf3_Nc6_Bc4_Bc5_Bxf7+](https://lichess.org/analysis/pgn/e4_e
    5_Nf3_Nc6_Bc4_Bc5_Bxf7+)

    Args:
        body (GameImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameImportResponse200]
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
    body: GameImportBody,

) -> Optional[GameImportResponse200]:
    """ Import one game

     Import a game from PGN. See <https://lichess.org/paste>.
    Rate limiting: 200 games per hour for OAuth requests, 100 games per hour for anonymous requests.
    To broadcast ongoing games, consider [pushing to a broadcast instead](#operation/broadcastPush).
    To analyse a position or a line, just construct an analysis board URL (most standard tags supported
    if URL-encoded):
    [https://lichess.org/analysis/pgn/e4_e5_Nf3_Nc6_Bc4_Bc5_Bxf7+](https://lichess.org/analysis/pgn/e4_e
    5_Nf3_Nc6_Bc4_Bc5_Bxf7+)

    Args:
        body (GameImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameImportResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GameImportBody,

) -> Response[GameImportResponse200]:
    """ Import one game

     Import a game from PGN. See <https://lichess.org/paste>.
    Rate limiting: 200 games per hour for OAuth requests, 100 games per hour for anonymous requests.
    To broadcast ongoing games, consider [pushing to a broadcast instead](#operation/broadcastPush).
    To analyse a position or a line, just construct an analysis board URL (most standard tags supported
    if URL-encoded):
    [https://lichess.org/analysis/pgn/e4_e5_Nf3_Nc6_Bc4_Bc5_Bxf7+](https://lichess.org/analysis/pgn/e4_e
    5_Nf3_Nc6_Bc4_Bc5_Bxf7+)

    Args:
        body (GameImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameImportResponse200]
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
    body: GameImportBody,

) -> Optional[GameImportResponse200]:
    """ Import one game

     Import a game from PGN. See <https://lichess.org/paste>.
    Rate limiting: 200 games per hour for OAuth requests, 100 games per hour for anonymous requests.
    To broadcast ongoing games, consider [pushing to a broadcast instead](#operation/broadcastPush).
    To analyse a position or a line, just construct an analysis board URL (most standard tags supported
    if URL-encoded):
    [https://lichess.org/analysis/pgn/e4_e5_Nf3_Nc6_Bc4_Bc5_Bxf7+](https://lichess.org/analysis/pgn/e4_e
    5_Nf3_Nc6_Bc4_Bc5_Bxf7+)

    Args:
        body (GameImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameImportResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
