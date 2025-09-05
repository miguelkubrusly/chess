from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_board_seek_body import ApiBoardSeekBody
from ...models.api_board_seek_response_200 import ApiBoardSeekResponse200
from ...models.api_board_seek_response_400 import ApiBoardSeekResponse400
from typing import cast



def _get_kwargs(
    *,
    body: ApiBoardSeekBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/board/seek",
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ApiBoardSeekResponse200, ApiBoardSeekResponse400]]:
    if response.status_code == 200:
        response_200 = ApiBoardSeekResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ApiBoardSeekResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ApiBoardSeekResponse200, ApiBoardSeekResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiBoardSeekBody,

) -> Response[Union[ApiBoardSeekResponse200, ApiBoardSeekResponse400]]:
    """ Create a seek

     Create a public seek, to start a game with a random player.

    ### Real-time seek

    Specify the `time` and `increment` clock values.
    The response is streamed but doesn't contain any information.

    **Keep the connection open to keep the seek active**.

    If the client closes the connection, the seek is canceled. This way, if the client terminates, the
    user won't be paired in a game they wouldn't play.
    When the seek is accepted, or expires, the server closes the connection.

    **Make sure to also have an [Event stream](#operation/apiStreamEvent) open**, to be notified when a
    game starts.
    We recommend opening the [Event stream](#operation/apiStreamEvent) first, then the seek stream. This
    way,
    you won't miss the game event if the seek is accepted immediately.

    ### Correspondence seek

    Specify the `days` per turn value.
    The response is not streamed, it immediately completes with the seek ID. The seek remains active on
    the server until it is joined by someone.

    Args:
        body (ApiBoardSeekBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBoardSeekResponse200, ApiBoardSeekResponse400]]
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
    body: ApiBoardSeekBody,

) -> Optional[Union[ApiBoardSeekResponse200, ApiBoardSeekResponse400]]:
    """ Create a seek

     Create a public seek, to start a game with a random player.

    ### Real-time seek

    Specify the `time` and `increment` clock values.
    The response is streamed but doesn't contain any information.

    **Keep the connection open to keep the seek active**.

    If the client closes the connection, the seek is canceled. This way, if the client terminates, the
    user won't be paired in a game they wouldn't play.
    When the seek is accepted, or expires, the server closes the connection.

    **Make sure to also have an [Event stream](#operation/apiStreamEvent) open**, to be notified when a
    game starts.
    We recommend opening the [Event stream](#operation/apiStreamEvent) first, then the seek stream. This
    way,
    you won't miss the game event if the seek is accepted immediately.

    ### Correspondence seek

    Specify the `days` per turn value.
    The response is not streamed, it immediately completes with the seek ID. The seek remains active on
    the server until it is joined by someone.

    Args:
        body (ApiBoardSeekBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiBoardSeekResponse200, ApiBoardSeekResponse400]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiBoardSeekBody,

) -> Response[Union[ApiBoardSeekResponse200, ApiBoardSeekResponse400]]:
    """ Create a seek

     Create a public seek, to start a game with a random player.

    ### Real-time seek

    Specify the `time` and `increment` clock values.
    The response is streamed but doesn't contain any information.

    **Keep the connection open to keep the seek active**.

    If the client closes the connection, the seek is canceled. This way, if the client terminates, the
    user won't be paired in a game they wouldn't play.
    When the seek is accepted, or expires, the server closes the connection.

    **Make sure to also have an [Event stream](#operation/apiStreamEvent) open**, to be notified when a
    game starts.
    We recommend opening the [Event stream](#operation/apiStreamEvent) first, then the seek stream. This
    way,
    you won't miss the game event if the seek is accepted immediately.

    ### Correspondence seek

    Specify the `days` per turn value.
    The response is not streamed, it immediately completes with the seek ID. The seek remains active on
    the server until it is joined by someone.

    Args:
        body (ApiBoardSeekBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBoardSeekResponse200, ApiBoardSeekResponse400]]
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
    body: ApiBoardSeekBody,

) -> Optional[Union[ApiBoardSeekResponse200, ApiBoardSeekResponse400]]:
    """ Create a seek

     Create a public seek, to start a game with a random player.

    ### Real-time seek

    Specify the `time` and `increment` clock values.
    The response is streamed but doesn't contain any information.

    **Keep the connection open to keep the seek active**.

    If the client closes the connection, the seek is canceled. This way, if the client terminates, the
    user won't be paired in a game they wouldn't play.
    When the seek is accepted, or expires, the server closes the connection.

    **Make sure to also have an [Event stream](#operation/apiStreamEvent) open**, to be notified when a
    game starts.
    We recommend opening the [Event stream](#operation/apiStreamEvent) first, then the seek stream. This
    way,
    you won't miss the game event if the seek is accepted immediately.

    ### Correspondence seek

    Specify the `days` per turn value.
    The response is not streamed, it immediately completes with the seek ID. The seek remains active on
    the server until it is joined by someone.

    Args:
        body (ApiBoardSeekBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiBoardSeekResponse200, ApiBoardSeekResponse400]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
