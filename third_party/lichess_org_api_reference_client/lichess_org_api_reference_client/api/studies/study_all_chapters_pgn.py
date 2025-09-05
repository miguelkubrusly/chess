from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from typing import Union



def _get_kwargs(
    study_id: str,
    *,
    clocks: Union[Unset, bool] = True,
    comments: Union[Unset, bool] = True,
    variations: Union[Unset, bool] = True,
    orientation: Union[Unset, bool] = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["clocks"] = clocks

    params["comments"] = comments

    params["variations"] = variations

    params["orientation"] = orientation


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/study/{study_id}.pgn".format(study_id=study_id,),
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
    study_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    clocks: Union[Unset, bool] = True,
    comments: Union[Unset, bool] = True,
    variations: Union[Unset, bool] = True,
    orientation: Union[Unset, bool] = False,

) -> Response[Any]:
    """ Export all chapters

     Download all chapters of a study in PGN format.

    Args:
        study_id (str):
        clocks (Union[Unset, bool]):  Default: True.
        comments (Union[Unset, bool]):  Default: True.
        variations (Union[Unset, bool]):  Default: True.
        orientation (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        study_id=study_id,
clocks=clocks,
comments=comments,
variations=variations,
orientation=orientation,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    study_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    clocks: Union[Unset, bool] = True,
    comments: Union[Unset, bool] = True,
    variations: Union[Unset, bool] = True,
    orientation: Union[Unset, bool] = False,

) -> Response[Any]:
    """ Export all chapters

     Download all chapters of a study in PGN format.

    Args:
        study_id (str):
        clocks (Union[Unset, bool]):  Default: True.
        comments (Union[Unset, bool]):  Default: True.
        variations (Union[Unset, bool]):  Default: True.
        orientation (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        study_id=study_id,
clocks=clocks,
comments=comments,
variations=variations,
orientation=orientation,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

