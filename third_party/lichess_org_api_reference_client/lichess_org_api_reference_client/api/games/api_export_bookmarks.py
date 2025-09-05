from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_export_bookmarks_sort import ApiExportBookmarksSort
from ...types import UNSET, Unset
from typing import Union



def _get_kwargs(
    *,
    since: Union[Unset, int] = UNSET,
    until: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    moves: Union[Unset, bool] = True,
    pgn_in_json: Union[Unset, bool] = False,
    tags: Union[Unset, bool] = True,
    clocks: Union[Unset, bool] = False,
    evals: Union[Unset, bool] = False,
    accuracy: Union[Unset, bool] = False,
    opening: Union[Unset, bool] = False,
    division: Union[Unset, bool] = False,
    literate: Union[Unset, bool] = False,
    last_fen: Union[Unset, bool] = False,
    sort: Union[Unset, ApiExportBookmarksSort] = ApiExportBookmarksSort.DATEDESC,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["since"] = since

    params["until"] = until

    params["max"] = max_

    params["moves"] = moves

    params["pgnInJson"] = pgn_in_json

    params["tags"] = tags

    params["clocks"] = clocks

    params["evals"] = evals

    params["accuracy"] = accuracy

    params["opening"] = opening

    params["division"] = division

    params["literate"] = literate

    params["lastFen"] = last_fen

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/games/export/bookmarks",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    since: Union[Unset, int] = UNSET,
    until: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    moves: Union[Unset, bool] = True,
    pgn_in_json: Union[Unset, bool] = False,
    tags: Union[Unset, bool] = True,
    clocks: Union[Unset, bool] = False,
    evals: Union[Unset, bool] = False,
    accuracy: Union[Unset, bool] = False,
    opening: Union[Unset, bool] = False,
    division: Union[Unset, bool] = False,
    literate: Union[Unset, bool] = False,
    last_fen: Union[Unset, bool] = False,
    sort: Union[Unset, ApiExportBookmarksSort] = ApiExportBookmarksSort.DATEDESC,

) -> Response[Any]:
    """ Export your bookmarked games

     Download all games bookmarked by you, in PGN or [ndjson](#section/Introduction/Streaming-with-ND-
    JSON) format.
    Games are sorted by reverse chronological order (most recent first).
    We recommend streaming the response, for it can be very long.

    Args:
        since (Union[Unset, int]):
        until (Union[Unset, int]):
        max_ (Union[Unset, int]):
        moves (Union[Unset, bool]):  Default: True.
        pgn_in_json (Union[Unset, bool]):  Default: False.
        tags (Union[Unset, bool]):  Default: True.
        clocks (Union[Unset, bool]):  Default: False.
        evals (Union[Unset, bool]):  Default: False.
        accuracy (Union[Unset, bool]):  Default: False.
        opening (Union[Unset, bool]):  Default: False.
        division (Union[Unset, bool]):  Default: False.
        literate (Union[Unset, bool]):  Default: False.
        last_fen (Union[Unset, bool]):  Default: False.
        sort (Union[Unset, ApiExportBookmarksSort]):  Default: ApiExportBookmarksSort.DATEDESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        since=since,
until=until,
max_=max_,
moves=moves,
pgn_in_json=pgn_in_json,
tags=tags,
clocks=clocks,
evals=evals,
accuracy=accuracy,
opening=opening,
division=division,
literate=literate,
last_fen=last_fen,
sort=sort,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    since: Union[Unset, int] = UNSET,
    until: Union[Unset, int] = UNSET,
    max_: Union[Unset, int] = UNSET,
    moves: Union[Unset, bool] = True,
    pgn_in_json: Union[Unset, bool] = False,
    tags: Union[Unset, bool] = True,
    clocks: Union[Unset, bool] = False,
    evals: Union[Unset, bool] = False,
    accuracy: Union[Unset, bool] = False,
    opening: Union[Unset, bool] = False,
    division: Union[Unset, bool] = False,
    literate: Union[Unset, bool] = False,
    last_fen: Union[Unset, bool] = False,
    sort: Union[Unset, ApiExportBookmarksSort] = ApiExportBookmarksSort.DATEDESC,

) -> Response[Any]:
    """ Export your bookmarked games

     Download all games bookmarked by you, in PGN or [ndjson](#section/Introduction/Streaming-with-ND-
    JSON) format.
    Games are sorted by reverse chronological order (most recent first).
    We recommend streaming the response, for it can be very long.

    Args:
        since (Union[Unset, int]):
        until (Union[Unset, int]):
        max_ (Union[Unset, int]):
        moves (Union[Unset, bool]):  Default: True.
        pgn_in_json (Union[Unset, bool]):  Default: False.
        tags (Union[Unset, bool]):  Default: True.
        clocks (Union[Unset, bool]):  Default: False.
        evals (Union[Unset, bool]):  Default: False.
        accuracy (Union[Unset, bool]):  Default: False.
        opening (Union[Unset, bool]):  Default: False.
        division (Union[Unset, bool]):  Default: False.
        literate (Union[Unset, bool]):  Default: False.
        last_fen (Union[Unset, bool]):  Default: False.
        sort (Union[Unset, ApiExportBookmarksSort]):  Default: ApiExportBookmarksSort.DATEDESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        since=since,
until=until,
max_=max_,
moves=moves,
pgn_in_json=pgn_in_json,
tags=tags,
clocks=clocks,
evals=evals,
accuracy=accuracy,
opening=opening,
division=division,
literate=literate,
last_fen=last_fen,
sort=sort,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

