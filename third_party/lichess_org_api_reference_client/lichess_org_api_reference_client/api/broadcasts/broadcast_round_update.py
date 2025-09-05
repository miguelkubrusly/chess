from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.broadcast_round_update_body import BroadcastRoundUpdateBody
from ...models.broadcast_round_update_response_200 import BroadcastRoundUpdateResponse200
from ...models.broadcast_round_update_response_400 import BroadcastRoundUpdateResponse400
from typing import cast



def _get_kwargs(
    broadcast_round_id: str,
    *,
    body: BroadcastRoundUpdateBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/broadcast/round/{broadcast_round_id}/edit".format(broadcast_round_id=broadcast_round_id,),
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[BroadcastRoundUpdateResponse200, BroadcastRoundUpdateResponse400]]:
    if response.status_code == 200:
        response_200 = BroadcastRoundUpdateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = BroadcastRoundUpdateResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[BroadcastRoundUpdateResponse200, BroadcastRoundUpdateResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    broadcast_round_id: str,
    *,
    client: AuthenticatedClient,
    body: BroadcastRoundUpdateBody,

) -> Response[Union[BroadcastRoundUpdateResponse200, BroadcastRoundUpdateResponse400]]:
    """ Update a broadcast round

     Update information about a broadcast round.
    This endpoint accepts the same form data as the web form.
    All fields must be populated with data. Missing fields will override the broadcast with empty data.
    For instance, if you omit `startDate`, then any pre-existing start date will be removed.

    Args:
        broadcast_round_id (str):
        body (BroadcastRoundUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BroadcastRoundUpdateResponse200, BroadcastRoundUpdateResponse400]]
     """


    kwargs = _get_kwargs(
        broadcast_round_id=broadcast_round_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    broadcast_round_id: str,
    *,
    client: AuthenticatedClient,
    body: BroadcastRoundUpdateBody,

) -> Optional[Union[BroadcastRoundUpdateResponse200, BroadcastRoundUpdateResponse400]]:
    """ Update a broadcast round

     Update information about a broadcast round.
    This endpoint accepts the same form data as the web form.
    All fields must be populated with data. Missing fields will override the broadcast with empty data.
    For instance, if you omit `startDate`, then any pre-existing start date will be removed.

    Args:
        broadcast_round_id (str):
        body (BroadcastRoundUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BroadcastRoundUpdateResponse200, BroadcastRoundUpdateResponse400]
     """


    return sync_detailed(
        broadcast_round_id=broadcast_round_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    broadcast_round_id: str,
    *,
    client: AuthenticatedClient,
    body: BroadcastRoundUpdateBody,

) -> Response[Union[BroadcastRoundUpdateResponse200, BroadcastRoundUpdateResponse400]]:
    """ Update a broadcast round

     Update information about a broadcast round.
    This endpoint accepts the same form data as the web form.
    All fields must be populated with data. Missing fields will override the broadcast with empty data.
    For instance, if you omit `startDate`, then any pre-existing start date will be removed.

    Args:
        broadcast_round_id (str):
        body (BroadcastRoundUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BroadcastRoundUpdateResponse200, BroadcastRoundUpdateResponse400]]
     """


    kwargs = _get_kwargs(
        broadcast_round_id=broadcast_round_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    broadcast_round_id: str,
    *,
    client: AuthenticatedClient,
    body: BroadcastRoundUpdateBody,

) -> Optional[Union[BroadcastRoundUpdateResponse200, BroadcastRoundUpdateResponse400]]:
    """ Update a broadcast round

     Update information about a broadcast round.
    This endpoint accepts the same form data as the web form.
    All fields must be populated with data. Missing fields will override the broadcast with empty data.
    For instance, if you omit `startDate`, then any pre-existing start date will be removed.

    Args:
        broadcast_round_id (str):
        body (BroadcastRoundUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BroadcastRoundUpdateResponse200, BroadcastRoundUpdateResponse400]
     """


    return (await asyncio_detailed(
        broadcast_round_id=broadcast_round_id,
client=client,
body=body,

    )).parsed
