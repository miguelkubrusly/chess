from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_users_status_response_200_item import ApiUsersStatusResponse200Item
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    ids: str,
    with_signal: Union[Unset, bool] = UNSET,
    with_game_ids: Union[Unset, bool] = UNSET,
    with_game_metas: Union[Unset, bool] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["ids"] = ids

    params["withSignal"] = with_signal

    params["withGameIds"] = with_game_ids

    params["withGameMetas"] = with_game_metas


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/users/status",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[list['ApiUsersStatusResponse200Item']]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ApiUsersStatusResponse200Item.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[list['ApiUsersStatusResponse200Item']]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ids: str,
    with_signal: Union[Unset, bool] = UNSET,
    with_game_ids: Union[Unset, bool] = UNSET,
    with_game_metas: Union[Unset, bool] = UNSET,

) -> Response[list['ApiUsersStatusResponse200Item']]:
    """ Get real-time users status

     Read the `online`, `playing` and `streaming` flags of several users.
    This API is very fast and cheap on lichess side.
    So you can call it quite often (like once every 5 seconds).
    Use it to track players and know when they're connected on lichess and playing games.

    Args:
        ids (str):
        with_signal (Union[Unset, bool]):
        with_game_ids (Union[Unset, bool]):
        with_game_metas (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ApiUsersStatusResponse200Item']]
     """


    kwargs = _get_kwargs(
        ids=ids,
with_signal=with_signal,
with_game_ids=with_game_ids,
with_game_metas=with_game_metas,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    ids: str,
    with_signal: Union[Unset, bool] = UNSET,
    with_game_ids: Union[Unset, bool] = UNSET,
    with_game_metas: Union[Unset, bool] = UNSET,

) -> Optional[list['ApiUsersStatusResponse200Item']]:
    """ Get real-time users status

     Read the `online`, `playing` and `streaming` flags of several users.
    This API is very fast and cheap on lichess side.
    So you can call it quite often (like once every 5 seconds).
    Use it to track players and know when they're connected on lichess and playing games.

    Args:
        ids (str):
        with_signal (Union[Unset, bool]):
        with_game_ids (Union[Unset, bool]):
        with_game_metas (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ApiUsersStatusResponse200Item']
     """


    return sync_detailed(
        client=client,
ids=ids,
with_signal=with_signal,
with_game_ids=with_game_ids,
with_game_metas=with_game_metas,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ids: str,
    with_signal: Union[Unset, bool] = UNSET,
    with_game_ids: Union[Unset, bool] = UNSET,
    with_game_metas: Union[Unset, bool] = UNSET,

) -> Response[list['ApiUsersStatusResponse200Item']]:
    """ Get real-time users status

     Read the `online`, `playing` and `streaming` flags of several users.
    This API is very fast and cheap on lichess side.
    So you can call it quite often (like once every 5 seconds).
    Use it to track players and know when they're connected on lichess and playing games.

    Args:
        ids (str):
        with_signal (Union[Unset, bool]):
        with_game_ids (Union[Unset, bool]):
        with_game_metas (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ApiUsersStatusResponse200Item']]
     """


    kwargs = _get_kwargs(
        ids=ids,
with_signal=with_signal,
with_game_ids=with_game_ids,
with_game_metas=with_game_metas,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    ids: str,
    with_signal: Union[Unset, bool] = UNSET,
    with_game_ids: Union[Unset, bool] = UNSET,
    with_game_metas: Union[Unset, bool] = UNSET,

) -> Optional[list['ApiUsersStatusResponse200Item']]:
    """ Get real-time users status

     Read the `online`, `playing` and `streaming` flags of several users.
    This API is very fast and cheap on lichess side.
    So you can call it quite often (like once every 5 seconds).
    Use it to track players and know when they're connected on lichess and playing games.

    Args:
        ids (str):
        with_signal (Union[Unset, bool]):
        with_game_ids (Union[Unset, bool]):
        with_game_metas (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ApiUsersStatusResponse200Item']
     """


    return (await asyncio_detailed(
        client=client,
ids=ids,
with_signal=with_signal,
with_game_ids=with_game_ids,
with_game_metas=with_game_metas,

    )).parsed
